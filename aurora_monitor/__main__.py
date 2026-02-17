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
import time
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

    comment_targets = []

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
                    # Track for comment extraction
                    comment_targets.append({
                        "subreddit": post["subreddit"],
                        "post_id": post["id"],
                        "title": post.get("title", ""),
                    })

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

    # Fetch comments for newly matched posts
    if comment_targets:
        print(f"Fetching comments for {len(comment_targets)} matched posts...")
        for target in comment_targets:
            comments = fetcher.fetch_post_comments(target["subreddit"], target["post_id"])
            for comment in comments:
                if is_seen(state, comment["id"], kind="comment"):
                    continue
                comment_matches = matcher.find_matches([comment])
                for match in comment_matches:
                    match["parent_title"] = target["title"]
                    if match["routing"] == "auto_comment":
                        stats["matches"] += 1
                        if not dry_run and not github_api.check_existing_comment(
                            match["issue"], comment["id"], repo=repo
                        ):
                            formatted = format_issue_comment(match)
                            github_api.post_issue_comment(
                                match["issue"], formatted, repo=repo, dry_run=dry_run
                            )
                        elif dry_run:
                            print(f"  [COMMENT MATCH] #{match['issue']} <- reply by u/{comment['author']}")
                        all_matches.append(match)
                    elif match["routing"] == "triage":
                        stats["triage_items"] += 1
                        all_matches.append(match)
                    else:
                        stats["skipped"] += 1

                    if match.get("cross_references"):
                        stats["cross_references"] += len(match["cross_references"])

                mark_seen(state, comment["id"], kind="comment",
                          timestamp=comment.get("created_utc"))
            stats["comments_scanned"] += len(comments)

    # Weekly digest check
    if digest_gen.should_post_digest():
        print("Sunday — generating weekly digest...")
        digest = digest_gen.generate_digest(all_matches, stats)
        title = digest_gen.digest_title()
        success, _ = github_api.post_discussion(title, digest, category_id, repo=repo, dry_run=dry_run)

    # Save state
    state["last_run"] = datetime.now(tz=timezone.utc).isoformat()
    if not dry_run:
        save_state(STATE_PATH, state)
        print(f"State saved. Processed {stats['posts_scanned']} posts.")
    else:
        print(f"\n[DRY RUN] Would save state. Processed {stats['posts_scanned']} posts.")

    _print_summary(stats)


def run_backfill(config, dry_run=False):
    """Backfill mode: two-pass — match posts, then fetch comments for triage+ posts."""
    state = load_state(STATE_PATH)
    repo = config["github"]["repo"]
    category_id = config["github"]["discussion_category_id"]
    cross_ref_targets = config["github"].get("cross_ref_targets", {})
    triage_threshold = config["matching"]["thresholds"]["low"]

    issues = load_unverified_issues(repo)
    matcher = Matcher(config)
    matcher.issues = issues

    fetcher = RedditFetcher(config)
    digest_gen = DigestGenerator()

    all_matches = []
    comment_targets = []  # posts scoring >= triage threshold
    stats = {
        "posts_scanned": 0,
        "comments_scanned": 0,
        "matches": 0,
        "triage_items": 0,
        "cross_references": 0,
        "skipped": 0,
    }

    # PASS 1: Score all posts against issues
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
                    # Track posts above triage threshold for comment extraction
                    if match["score"] >= triage_threshold:
                        comment_targets.append({
                            "subreddit": post["subreddit"],
                            "post_id": post["id"],
                            "title": post.get("title", ""),
                        })
                else:
                    stats["skipped"] += 1

                if match.get("cross_references"):
                    stats["cross_references"] += len(match["cross_references"])

            # Seed state with all seen posts
            mark_seen(state, post["id"], kind="post", timestamp=post.get("created_utc"))

    # PASS 2: Fetch comments for posts that scored above triage threshold
    if comment_targets:
        # Deduplicate targets (a post may match multiple issues)
        seen_targets = set()
        unique_targets = []
        for t in comment_targets:
            if t["post_id"] not in seen_targets:
                seen_targets.add(t["post_id"])
                unique_targets.append(t)

        print(f"\nPass 2: Fetching comments for {len(unique_targets)} matched posts...")
        consecutive_failures = 0
        for i, target in enumerate(unique_targets):
            try:
                comments = fetcher.fetch_post_comments(target["subreddit"], target["post_id"])
                consecutive_failures = 0
            except Exception as e:
                consecutive_failures += 1
                print(f"  Warning: Failed to fetch comments for {target['post_id']}: {e}")
                if consecutive_failures >= 3:
                    cooldown = 60 * consecutive_failures
                    print(f"  {consecutive_failures} consecutive failures — cooling down {cooldown}s...")
                    time.sleep(cooldown)
                continue
            for comment in comments:
                if is_seen(state, comment["id"], kind="comment"):
                    continue
                # Match comment independently against all issues
                comment_matches = matcher.find_matches([comment])
                for match in comment_matches:
                    if match["routing"] in ("auto_comment", "triage"):
                        # Attach parent post title for formatting
                        match["parent_title"] = target["title"]
                        if match["routing"] == "auto_comment":
                            stats["matches"] += 1
                        else:
                            stats["triage_items"] += 1
                        all_matches.append(match)
                    else:
                        stats["skipped"] += 1

                    if match.get("cross_references"):
                        stats["cross_references"] += len(match["cross_references"])

                mark_seen(state, comment["id"], kind="comment",
                          timestamp=comment.get("created_utc"))
            stats["comments_scanned"] += len(comments)

            if (i + 1) % 50 == 0:
                print(f"  Processed {i + 1}/{len(unique_targets)} posts' comments...")

        print(f"  Scanned {stats['comments_scanned']} comments total")

    # PASS 3: Generate multi-tier outputs
    print("Generating multi-tier backfill report...")
    outputs = digest_gen.generate_outputs(all_matches, stats)

    if dry_run:
        _print_dry_run_outputs(outputs, cross_ref_targets)
    else:
        _post_backfill_outputs(outputs, category_id, repo, cross_ref_targets)
        state["backfill_complete"] = True
        state["last_run"] = datetime.now(tz=timezone.utc).isoformat()
        save_state(STATE_PATH, state)
        print("Backfill complete. State saved.")

    _print_summary(stats)


def _post_backfill_outputs(outputs, category_id, repo, cross_ref_targets):
    """Post multi-tier backfill outputs to GitHub."""
    rate_delay = 1.5  # seconds between API calls

    # 1. Post summary dashboard discussion
    title = f"[Reddit Monitor] Backfill Report — {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')}"
    success, discussion_id = github_api.post_discussion(
        title, outputs["summary_body"], category_id, repo=repo
    )
    if not success:
        print("ERROR: Failed to create summary discussion. Aborting.")
        return

    # 2. Post matched items as batched comments on each unverified issue
    issue_comments = outputs["issue_comments"]
    if issue_comments:
        print(f"Posting matched items to {len(issue_comments)} issues...")
        for issue_num, comments in issue_comments.items():
            if isinstance(comments, list):
                for comment in comments:
                    github_api.post_issue_comment(issue_num, comment, repo=repo)
                    time.sleep(rate_delay)
            else:
                github_api.post_issue_comment(issue_num, comments, repo=repo)
                time.sleep(rate_delay)

    # 3. Post triage items as paginated discussion comments
    triage_comments = outputs["triage_comments"]
    if triage_comments and discussion_id:
        print(f"Posting {len(triage_comments)} triage comment pages...")
        for comment in triage_comments:
            github_api.post_discussion_comment(discussion_id, comment, repo=repo)
            time.sleep(rate_delay)

    # 4. Post cross-references on sibling monitor issues
    cross_ref_comments = outputs["cross_ref_comments"]
    if cross_ref_comments:
        print("Posting cross-references to sibling issues...")
        for ref_type, comments in cross_ref_comments.items():
            target_issue = cross_ref_targets.get(ref_type)
            if not target_issue:
                print(f"  Warning: No target issue configured for {ref_type} cross-refs")
                continue
            for comment in comments:
                github_api.post_issue_comment(target_issue, comment, repo=repo)
                time.sleep(rate_delay)


def _print_dry_run_outputs(outputs, cross_ref_targets):
    """Print dry-run summary of multi-tier outputs."""
    print("\n[DRY RUN] Multi-tier backfill outputs:")
    print(f"  Summary body: {len(outputs['summary_body'])} chars")

    issue_comments = outputs["issue_comments"]
    total_issue_comments = sum(
        len(c) if isinstance(c, list) else 1
        for c in issue_comments.values()
    )
    print(f"  Issue comments: {total_issue_comments} comments across {len(issue_comments)} issues")

    triage_comments = outputs["triage_comments"]
    print(f"  Triage comments: {len(triage_comments)} pages")

    cross_ref_comments = outputs["cross_ref_comments"]
    for ref_type, comments in cross_ref_comments.items():
        target = cross_ref_targets.get(ref_type, "?")
        print(f"  Cross-refs ({ref_type}): {len(comments)} comments -> #{target}")

    # Show summary body preview
    print("\n[DRY RUN] Summary preview:")
    print(outputs["summary_body"][:2000])


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
