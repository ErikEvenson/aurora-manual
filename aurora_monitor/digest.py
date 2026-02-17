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

    def generate_outputs(self, matches, stats, new_content=None):
        """Generate multi-tier output for routing data to natural destinations.

        Returns dict with:
            summary_body: str — dashboard discussion body (<65K)
            issue_comments: dict[int, str|list[str]] — batched per issue (<10K each)
            triage_comments: list[str] — paginated task-list comments (<65K each)
            cross_ref_comments: dict[str, list[str]] — grouped by type (<65K each)
            new_content_comments: list[str] — paginated new content opportunity comments
        """
        matched = [m for m in matches if m["routing"] == "auto_comment"]
        triaged = [m for m in matches if m["routing"] == "triage"]
        cross_refs = [m for m in matches if m.get("cross_references")]

        return {
            "summary_body": self._generate_summary(
                matched, triaged, cross_refs, stats, new_content=new_content
            ),
            "issue_comments": self._generate_issue_comments(matched),
            "triage_comments": self._generate_triage_comments(triaged),
            "cross_ref_comments": self._generate_cross_ref_comments(cross_refs),
            "new_content_comments": self._generate_new_content_comments(new_content),
        }

    def _generate_summary(self, matched, triaged, cross_refs, stats, new_content=None):
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

        # New content opportunities
        if new_content:
            sections.append(self._new_content_summary(new_content))

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
        post_count = sum(1 for m in items if m.get("content_type", "post") == "post")
        comment_count = sum(1 for m in items if m.get("content_type") == "comment")
        count_parts = []
        if post_count:
            count_parts.append(f"{post_count} post{'s' if post_count != 1 else ''}")
        if comment_count:
            count_parts.append(f"{comment_count} comment{'s' if comment_count != 1 else ''}")
        count_label = ", ".join(count_parts) if count_parts else f"{len(items)} items"

        lines = [
            f"### Reddit Community References ({count_label})\n",
            "Content from r/aurora4x and r/aurora that may help verify this issue.\n",
        ]
        for m in items:
            confidence = "High" if m["score"] >= 80 else "Medium"
            dt = _format_date(m.get("created_utc"))
            permalink = f"https://www.reddit.com{m['permalink']}"
            quote = _truncate(m.get("quote", ""), 120)

            if m.get("content_type") == "comment" and m.get("parent_post_id"):
                parent_url = f"https://www.reddit.com/r/{m.get('subreddit', 'aurora4x')}/comments/{m['parent_post_id']}/"
                lines.append(
                    f"- **{confidence}** ({m['score']:.0f}/100) — "
                    f"Reply to [{m.get('parent_title') or 'post'}]({parent_url}) by "
                    f"[u/{m['author']}]({permalink}) ({dt}): \"{quote}\""
                )
            else:
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

    def _new_content_summary(self, new_content):
        """Generate New Content Opportunities section for the summary."""
        lines = [f"## New Content Opportunities\n"]
        lines.append(
            f"{len(new_content)} potential content gaps detected "
            f"from unmatched community posts.\n"
        )
        rows = [
            "| Score | Chapter | Post |",
            "|-------|---------|------|",
        ]
        for opp in new_content[:20]:  # Cap at 20 in summary
            chapters = opp.get("chapters", [])
            ch_str = ", ".join(
                f"Section {ch[0]}" for ch in chapters[:2]
            ) if chapters else "General"
            title = _truncate(opp.get("title", ""), 50)
            rows.append(f"| {opp['score']} | {ch_str} | {title} |")
        lines.append("\n".join(rows))
        return "\n".join(lines)

    def _generate_new_content_comments(self, new_content):
        """Paginate new content opportunities into discussion comments."""
        if not new_content:
            return []

        items_per_page = 50
        comments = []
        for page_start in range(0, len(new_content), items_per_page):
            page = new_content[page_start:page_start + items_per_page]
            page_num = page_start // items_per_page + 1
            total_pages = (len(new_content) + items_per_page - 1) // items_per_page

            lines = [
                f"## New Content Opportunities (Page {page_num}/{total_pages})\n",
            ]
            for opp in page:
                permalink = f"https://www.reddit.com{opp['permalink']}"
                chapters = opp.get("chapters", [])
                ch_str = ", ".join(
                    f"Section {ch[0]}: {ch[1]}" for ch in chapters[:2]
                ) if chapters else "General"
                signals = ", ".join(opp.get("signals", [])[:3])
                lines.append(
                    f"- **{opp['score']}/100** — "
                    f"[{_truncate(opp.get('title', ''), 60)}]({permalink}) "
                    f"by u/{opp.get('author', '?')} — {ch_str}"
                )
                if signals:
                    lines.append(f"  Signals: {signals}")

            comment = "\n".join(lines)
            if len(comment) > MAX_DISCUSSION_BODY_LENGTH:
                comment = comment[:MAX_DISCUSSION_BODY_LENGTH - 50] + "\n\n*[Truncated]*"
            comments.append(comment)

        return comments

    def _stats_section(self, stats):
        """Generate the Statistics section."""
        lines = [
            "## Statistics\n",
            f"- Posts scanned: {stats.get('posts_scanned', 0)}",
            f"- Comments scanned: {stats.get('comments_scanned', 0)}",
            f"- Matches: {stats.get('matches', 0)}",
            f"- Triage items: {stats.get('triage_items', 0)}",
            f"- Cross-references: {stats.get('cross_references', 0)}",
            f"- Skipped (not relevant): {stats.get('skipped', 0)}",
        ]
        if stats.get('new_content', 0) > 0:
            lines.append(f"- New content opportunities: {stats['new_content']}")
        return "\n".join(lines)

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
