"""Shared markdown digest generator for community source monitors."""

from datetime import date, datetime, timezone


class DigestGenerator:
    """Generate weekly markdown digests of matched and triaged content."""

    def generate_digest(self, matches, stats):
        """Generate a complete markdown digest from match results and stats."""
        matched = [m for m in matches if m["routing"] == "auto_comment"]
        triaged = [m for m in matches if m["routing"] == "triage"]
        cross_refs = [m for m in matches if m.get("cross_references")]

        sections = []

        # Matched section
        sections.append(self._matched_section(matched))

        # Triage section
        sections.append(self._triage_section(triaged))

        # Cross-references section
        sections.append(self._cross_ref_section(cross_refs))

        # Statistics section
        sections.append(self._stats_section(stats))

        return "\n\n".join(sections)

    def _matched_section(self, matched):
        """Generate the Matched section."""
        count = len(matched)
        header = f"## Matched ({count} items)\n\nPosts matching open unverified issues. Auto-commented on the relevant issues."

        if not matched:
            return header + "\n\nNo matches this period."

        rows = ["| Issue | Subreddit | Author | Date | Quote | Confidence |",
                "|-------|-----------|--------|------|-------|------------|"]
        for m in matched:
            dt = _format_date(m.get("created_utc"))
            confidence = "High" if m["score"] >= 80 else "Medium"
            quote = _truncate(m.get("quote", ""), 80)
            rows.append(
                f"| #{m['issue']} | r/{m['subreddit']} | u/{m['author']} "
                f"| {dt} | \"{quote}\" | {confidence} |"
            )
        return header + "\n\n" + "\n".join(rows)

    def _triage_section(self, triaged):
        """Generate the Triage section."""
        count = len(triaged)
        header = f"## Triage ({count} items)\n\nRelevant posts not matching any open issue. Requires human review."

        if not triaged:
            return header + "\n\nNo triage items this period."

        rows = ["| Subreddit | Author | Date | Title | Quote |",
                "|-----------|--------|------|-------|-------|"]
        for m in triaged:
            dt = _format_date(m.get("created_utc"))
            title = _truncate(m.get("title", ""), 60)
            quote = _truncate(m.get("quote", ""), 80)
            rows.append(
                f"| r/{m['subreddit']} | u/{m['author']} | {dt} "
                f"| [{title}](https://www.reddit.com{m['permalink']}) | \"{quote}\" |"
            )
        return header + "\n\n" + "\n".join(rows)

    def _cross_ref_section(self, cross_refs):
        """Generate the Cross-References section."""
        count = sum(len(m.get("cross_references", [])) for m in cross_refs)
        header = f"## Cross-References ({count} items)\n\nPosts containing links to Aurora Forums or YouTube videos flagged for other monitors."

        if not cross_refs:
            return header + "\n\nNo cross-references this period."

        rows = ["| Link Type | Subreddit | Author | URL |",
                "|-----------|-----------|--------|-----|"]
        for m in cross_refs:
            for ref in m.get("cross_references", []):
                link_type = ref["type"].capitalize()
                rows.append(
                    f"| {link_type} | r/{m['subreddit']} | u/{m['author']} "
                    f"| {ref['url']} |"
                )
        return header + "\n\n" + "\n".join(rows)

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
    """Truncate text with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."
