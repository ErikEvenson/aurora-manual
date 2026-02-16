"""Aurora Monitor — community source monitor entry point.

Usage:
    python -m aurora_monitor --mode steady-state
    python -m aurora_monitor --mode backfill [--dry-run]
    python -m aurora_monitor --mode dry-run
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

import yaml

from aurora_monitor.sources.reddit import RedditFetcher
from aurora_monitor.matcher import Matcher
from aurora_monitor.state import load_state, save_state, is_seen, mark_seen
from aurora_monitor.digest import DigestGenerator
from aurora_monitor import github_api


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.yaml")
STATE_PATH = os.path.join(BASE_DIR, "state", "reddit.json")


def load_config():
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def load_unverified_issues(repo):
    """Fetch open issues labeled 'unverified' via gh CLI."""
    result = subprocess.run(
        ["gh", "issue", "list", "--repo", repo, "--label", "unverified",
         "--state", "open", "--json", "number,title,body", "--limit", "500"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"Warning: Could not fetch issues: {result.stderr}")
        return []
    return json.loads(result.stdout)


def format_issue_comment(match):
    """Format a GitHub issue comment for a matched Reddit post."""
    confidence = "High" if match["score"] >= 80 else "Medium"
    permalink = f"https://www.reddit.com{match['permalink']}"
    return (
        f"### Reddit Community Reference\n\n"
        f"**Confidence:** {confidence} ({match['score']:.0f}/100)\n"
        f"**Source:** [r/{match['subreddit']} — u/{match['author']}]({permalink})\n"
        f"**Post:** {match['title']}\n"
        f"**Date:** {datetime.fromtimestamp(match['created_utc'], tz=timezone.utc).strftime('%Y-%m-%d')}\n\n"
        f"> {match.get('quote', '')}\n\n"
        f"---\n"
        f"*Detected by [aurora-monitor](https://github.com/ErikEvenson/aurora-manual/tree/main/aurora_monitor) "
        f"— Reddit community source monitor*"
    )


def run_steady_state(config, dry_run=False):
    """Daily steady-state mode: fetch new, dedup, match, route, comment."""
    state = load_state(STATE_PATH)
    if not state["backfill_complete"]:
        print("ERROR: No backfill completed. Run backfill mode first.")
        print("Trigger manually: Actions > reddit-monitor > Run workflow > backfill")
        sys.exit(1)

    repo = config["github"]["repo"]
    category_id = config["github"]["discussion_category_id"]

    # Load issues for matching
    issues = load_unverified_issues(repo)
    matcher = Matcher(config)
    matcher.issues = issues

    fetcher = RedditFetcher(config)
    digest_gen = DigestGenerator()

    all_matches = []
    stats = {
        "posts_scanned": 0,
        "comments_scanned": 0,
        "matches": 0,
        "triage_items": 0,
        "cross_references": 0,
        "skipped": 0,
    }

    for sub in config["reddit"]["subreddits"]:
        print(f"Fetching r/{sub}...")
        posts, _ = fetcher.fetch_new_posts(sub)

        for post in posts:
            stats["posts_scanned"] += 1
            if is_seen(state, post["id"], kind="post"):
                stats["skipped"] += 1
                continue

            # Match against issues
            matches = matcher.find_matches([post])
            for match in matches:
                if match["routing"] == "auto_comment":
                    stats["matches"] += 1
                    # Check for duplicate comment
                    if not dry_run and not github_api.check_existing_comment(
                        match["issue"], post["id"], repo=repo
                    ):
                        comment = format_issue_comment(match)
                        github_api.post_issue_comment(
                            match["issue"], comment, repo=repo, dry_run=dry_run
                        )
                    elif dry_run:
                        print(f"  [MATCH] #{match['issue']} <- r/{sub}/u/{post['author']}: {post['title']}")
                    all_matches.append(match)

                elif match["routing"] == "triage":
                    stats["triage_items"] += 1
                    all_matches.append(match)
                    if dry_run:
                        print(f"  [TRIAGE] r/{sub}/u/{post['author']}: {post['title']}")

                else:
                    stats["skipped"] += 1

                if match.get("cross_references"):
                    stats["cross_references"] += len(match["cross_references"])

            mark_seen(state, post["id"], kind="post", timestamp=post.get("created_utc"))

    # Weekly digest check
    if digest_gen.should_post_digest():
        print("Sunday — generating weekly digest...")
        digest = digest_gen.generate_digest(all_matches, stats)
        title = digest_gen.digest_title()
        github_api.post_discussion(title, digest, category_id, repo=repo, dry_run=dry_run)

    # Save state
    state["last_run"] = datetime.now(tz=timezone.utc).isoformat()
    if not dry_run:
        save_state(STATE_PATH, state)
        print(f"State saved. Processed {stats['posts_scanned']} posts.")
    else:
        print(f"\n[DRY RUN] Would save state. Processed {stats['posts_scanned']} posts.")

    _print_summary(stats)


def run_backfill(config, dry_run=False):
    """Backfill mode: paginate history, match, generate report, seed state."""
    state = load_state(STATE_PATH)
    repo = config["github"]["repo"]
    category_id = config["github"]["discussion_category_id"]

    issues = load_unverified_issues(repo)
    matcher = Matcher(config)
    matcher.issues = issues

    fetcher = RedditFetcher(config)
    digest_gen = DigestGenerator()

    all_matches = []
    stats = {
        "posts_scanned": 0,
        "comments_scanned": 0,
        "matches": 0,
        "triage_items": 0,
        "cross_references": 0,
        "skipped": 0,
    }

    for sub in config["reddit"]["subreddits"]:
        print(f"Backfilling r/{sub}...")
        posts = fetcher.backfill(sub)
        print(f"  Fetched {len(posts)} posts")

        for post in posts:
            stats["posts_scanned"] += 1
            matches = matcher.find_matches([post])
            for match in matches:
                if match["routing"] in ("auto_comment", "triage"):
                    if match["routing"] == "auto_comment":
                        stats["matches"] += 1
                    else:
                        stats["triage_items"] += 1
                    all_matches.append(match)
                else:
                    stats["skipped"] += 1

                if match.get("cross_references"):
                    stats["cross_references"] += len(match["cross_references"])

            # Seed state with all seen posts (backfill never comments)
            mark_seen(state, post["id"], kind="post", timestamp=post.get("created_utc"))

    # Generate backfill report
    print("Generating backfill report...")
    report = _generate_backfill_report(all_matches, stats, digest_gen)

    if dry_run:
        print("\n[DRY RUN] Backfill report:")
        print(report[:2000])
        print(f"\n[DRY RUN] Would post as discussion and mark backfill complete.")
    else:
        title = f"[Reddit Monitor] Backfill Report — {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')}"
        github_api.post_discussion(title, report, category_id, repo=repo)
        state["backfill_complete"] = True
        state["last_run"] = datetime.now(tz=timezone.utc).isoformat()
        save_state(STATE_PATH, state)
        print("Backfill complete. State saved.")

    _print_summary(stats)


def _generate_backfill_report(matches, stats, digest_gen):
    """Generate a one-time backfill report discussion body."""
    digest = digest_gen.generate_digest(matches, stats)
    header = (
        "# Reddit Monitor — Historical Backfill Report\n\n"
        "This report was generated by scanning the full reachable history of "
        "r/aurora4x and r/aurora. **No automatic issue comments were posted.** "
        "All matches below require human review before action.\n\n"
        "To act on a match: manually comment on the relevant issue with the "
        "Reddit permalink and your assessment.\n\n"
        "---\n\n"
    )
    return header + digest


def _print_summary(stats):
    """Print a summary of the run."""
    print("\n--- Summary ---")
    for key, value in stats.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")


def main():
    parser = argparse.ArgumentParser(description="Aurora community source monitor")
    parser.add_argument(
        "--mode",
        choices=["steady-state", "backfill", "dry-run"],
        default="steady-state",
        help="Run mode (default: steady-state)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Process but don't post or save state",
    )
    args = parser.parse_args()

    config = load_config()

    dry_run = args.dry_run or args.mode == "dry-run"

    if args.mode == "backfill":
        run_backfill(config, dry_run=dry_run)
    else:
        run_steady_state(config, dry_run=dry_run)


if __name__ == "__main__":
    main()
