"""Shared markdown digest generator for community source monitors."""

from collections import defaultdict
from datetime import date, datetime, timezone


MAX_ISSUE_COMMENT_LENGTH = 10000
MAX_DISCUSSION_BODY_LENGTH = 65000
TRIAGE_ITEMS_PER_COMMENT = 300
CROSS_REFS_PER_COMMENT = 60


class DigestGenerator:
    """Generate weekly markdown digests of matched and triaged content."""

    def generate_digest(self, matches, stats):
        """Generate a complete markdown digest from match results and stats.

        Backward-compatible wrapper — delegates to generate_outputs().
        """
        outputs = self.generate_outputs(matches, stats)
        return outputs["summary_body"]

    def generate_outputs(self, matches, stats):
        """Generate multi-tier output for routing data to natural destinations.

        Returns dict with:
            summary_body: str — dashboard discussion body (<65K)
            issue_comments: dict[int, str|list[str]] — batched per issue (<10K each)
            triage_comments: list[str] — paginated task-list comments (<65K each)
            cross_ref_comments: dict[str, list[str]] — grouped by type (<65K each)
        """
        matched = [m for m in matches if m["routing"] == "auto_comment"]
        triaged = [m for m in matches if m["routing"] == "triage"]
        cross_refs = [m for m in matches if m.get("cross_references")]

        return {
            "summary_body": self._generate_summary(matched, triaged, cross_refs, stats),
            "issue_comments": self._generate_issue_comments(matched),
            "triage_comments": self._generate_triage_comments(triaged),
            "cross_ref_comments": self._generate_cross_ref_comments(cross_refs),
        }

    def _generate_summary(self, matched, triaged, cross_refs, stats):
        """Generate dashboard discussion body with overview table and stats."""
        sections = []

        # Header
        sections.append(
            "# Reddit Monitor — Backfill Report\n\n"
            "Dashboard for Reddit community source monitoring results.\n"
        )

        # Issue overview table (matched items grouped by issue)
        if matched:
            by_issue = defaultdict(list)
            for m in matched:
                by_issue[m["issue"]].append(m)

            sections.append("## Issue Matches\n")
            rows = [
                "| Issue | Posts | Confidence | Top Quote |",
                "|-------|-------|------------|-----------|",
            ]
            for issue_num in sorted(by_issue.keys()):
                items = by_issue[issue_num]
                high_count = sum(1 for m in items if m["score"] >= 80)
                confidence = f"{high_count} high" if high_count else "medium"
                top = max(items, key=lambda m: m["score"])
                quote = _truncate(top.get("quote", ""), 60)
                rows.append(f"| #{issue_num} | {len(items)} | {confidence} | \"{quote}\" |")
            sections.append("\n".join(rows))
        else:
            sections.append("## Issue Matches\n\nNo matches.")

        # Triage summary
        sections.append(
            f"## Triage\n\n{len(triaged)} items requiring human review. "
            f"See discussion comments below for full task lists."
        )

        # Cross-ref summary
        xref_count = sum(len(m.get("cross_references", [])) for m in cross_refs)
        sections.append(
            f"## Cross-References\n\n{xref_count} links to Aurora Forums / YouTube. "
            f"Posted as comments on sibling monitor issues."
        )

        # Statistics
        sections.append(self._stats_section(stats))

        body = "\n\n".join(sections)
        if len(body) > MAX_DISCUSSION_BODY_LENGTH:
            body = body[:MAX_DISCUSSION_BODY_LENGTH - 50] + "\n\n*[Truncated]*"
        return body

    def _generate_issue_comments(self, matched):
        """Group matched items by issue, format batched comment per issue.

        Returns dict[int, str|list[str]]. If a single issue has too many
        matches to fit in 10K, the value is a list of chunked strings.
        """
        if not matched:
            return {}

        by_issue = defaultdict(list)
        for m in matched:
            by_issue[m["issue"]].append(m)

        result = {}
        for issue_num in sorted(by_issue.keys()):
            items = by_issue[issue_num]
            comment = self._format_issue_batch(items, issue_num)
            if len(comment) <= MAX_ISSUE_COMMENT_LENGTH:
                result[issue_num] = comment
            else:
                # Chunk into multiple comments
                result[issue_num] = self._chunk_issue_comments(items, issue_num)
        return result

    def _format_issue_batch(self, items, issue_num):
        """Format a batch of matched items as a single issue comment."""
        lines = [
            f"### Reddit Community References ({len(items)} posts)\n",
            "Posts from r/aurora4x and r/aurora that may help verify this issue.\n",
        ]
        for m in items:
            confidence = "High" if m["score"] >= 80 else "Medium"
            dt = _format_date(m.get("created_utc"))
            permalink = f"https://www.reddit.com{m['permalink']}"
            quote = _truncate(m.get("quote", ""), 120)
            lines.append(
                f"- **{confidence}** ({m['score']:.0f}/100) — "
                f"[u/{m['author']}]({permalink}) ({dt}): \"{quote}\""
            )
        lines.append(
            "\n---\n*Detected by "
            "[aurora-monitor](https://github.com/ErikEvenson/aurora-manual/tree/main/aurora_monitor)*"
        )
        return "\n".join(lines)

    def _chunk_issue_comments(self, items, issue_num):
        """Split large issue match lists into multiple comments under 10K."""
        comments = []
        chunk = []
        chunk_num = 1
        for m in items:
            chunk.append(m)
            trial = self._format_issue_batch(chunk, issue_num)
            if len(trial) > MAX_ISSUE_COMMENT_LENGTH - 200:  # headroom
                # Back out last item, emit chunk
                chunk.pop()
                if chunk:
                    comments.append(self._format_issue_batch(chunk, issue_num))
                chunk = [m]
                chunk_num += 1
        if chunk:
            comments.append(self._format_issue_batch(chunk, issue_num))
        return comments

    def _generate_triage_comments(self, triaged):
        """Paginate triage items into task-list comments (<65K each)."""
        if not triaged:
            return []

        comments = []
        for page_start in range(0, len(triaged), TRIAGE_ITEMS_PER_COMMENT):
            page = triaged[page_start:page_start + TRIAGE_ITEMS_PER_COMMENT]
            page_num = page_start // TRIAGE_ITEMS_PER_COMMENT + 1
            total_pages = (len(triaged) + TRIAGE_ITEMS_PER_COMMENT - 1) // TRIAGE_ITEMS_PER_COMMENT

            lines = [
                f"## Triage Items (Page {page_num}/{total_pages})\n",
            ]
            for m in page:
                dt = _format_date(m.get("created_utc"))
                title = _truncate(m.get("title", ""), 60)
                permalink = f"https://www.reddit.com{m['permalink']}"
                quote = _truncate(m.get("quote", ""), 80)
                lines.append(
                    f"- [ ] **[{title}]({permalink})** — "
                    f"u/{m['author']} ({dt}) — \"{quote}\""
                )

            comment = "\n".join(lines)
            if len(comment) > MAX_DISCUSSION_BODY_LENGTH:
                comment = comment[:MAX_DISCUSSION_BODY_LENGTH - 50] + "\n\n*[Truncated]*"
            comments.append(comment)

        return comments

    def _generate_cross_ref_comments(self, cross_refs):
        """Group cross-references by type, chunk into comments.

        Returns dict[str, list[str]] where keys are "forum", "youtube", etc.
        """
        if not cross_refs:
            return {}

        by_type = defaultdict(list)
        for m in cross_refs:
            for ref in m.get("cross_references", []):
                by_type[ref["type"]].append({
                    "url": ref["url"],
                    "subreddit": m["subreddit"],
                    "author": m["author"],
                    "title": m.get("title", ""),
                    "permalink": m.get("permalink", ""),
                    "created_utc": m.get("created_utc"),
                })

        result = {}
        for ref_type, items in sorted(by_type.items()):
            comments = []
            for page_start in range(0, len(items), CROSS_REFS_PER_COMMENT):
                page = items[page_start:page_start + CROSS_REFS_PER_COMMENT]
                page_num = page_start // CROSS_REFS_PER_COMMENT + 1
                total_pages = (len(items) + CROSS_REFS_PER_COMMENT - 1) // CROSS_REFS_PER_COMMENT

                lines = [
                    f"## {ref_type.capitalize()} Cross-References "
                    f"(Page {page_num}/{total_pages})\n",
                    f"Links found in Reddit posts pointing to {ref_type} content.\n",
                ]
                for item in page:
                    dt = _format_date(item.get("created_utc"))
                    lines.append(
                        f"- {item['url']} — "
                        f"via [u/{item['author']}](https://www.reddit.com{item['permalink']}) ({dt})"
                    )

                comment = "\n".join(lines)
                if len(comment) > MAX_DISCUSSION_BODY_LENGTH:
                    comment = comment[:MAX_DISCUSSION_BODY_LENGTH - 50] + "\n\n*[Truncated]*"
                comments.append(comment)

            result[ref_type] = comments

        return result

    def _stats_section(self, stats):
        """Generate the Statistics section."""
        return (
            "## Statistics\n\n"
            f"- Posts scanned: {stats.get('posts_scanned', 0)}\n"
            f"- Comments scanned: {stats.get('comments_scanned', 0)}\n"
            f"- Matches: {stats.get('matches', 0)}\n"
            f"- Triage items: {stats.get('triage_items', 0)}\n"
            f"- Cross-references: {stats.get('cross_references', 0)}\n"
            f"- Skipped (not relevant): {stats.get('skipped', 0)}"
        )

    def should_post_digest(self, today=None):
        """Return True if today is Sunday (digest day)."""
        if today is None:
            today = date.today()
        return today.weekday() == 6  # Sunday

    def digest_title(self, today=None):
        """Generate the digest discussion title."""
        if today is None:
            today = date.today()
        return f"[Reddit Monitor] Week of {today.isoformat()}"


def _format_date(timestamp):
    """Format a Unix timestamp as YYYY-MM-DD."""
    if not timestamp:
        return "N/A"
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y-%m-%d")


def _truncate(text, max_length):
    """Truncate text with ellipsis. Sanitizes for markdown table safety."""
    # Collapse newlines and escape pipes for table compatibility
    text = text.replace('\n', ' ').replace('\r', ' ').replace('|', '\\|')
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."
