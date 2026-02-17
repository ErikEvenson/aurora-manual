"""New content detection for community source monitors.

Identifies Reddit posts that represent content opportunities — mechanics
discussions the manual doesn't yet cover. Separate from Matcher, which
matches against existing unverified issues.
"""

import re
from datetime import datetime, timezone


class NewContentDetector:
    """Detect new content opportunities from unmatched community posts."""

    def __init__(self, config):
        self.nc_config = config["new_content"]
        self.matching_config = config.get("matching", {})
        self.known_authors = self.matching_config.get("known_authors", {})
        self.aurora_terms = self.matching_config.get("keywords", {}).get("aurora_terms", [])
        self.evidence_keywords = self.nc_config.get("evidence_keywords", [])
        self.chapter_keywords = self.nc_config.get("chapter_keywords", {})
        self.min_score = self.nc_config.get("min_score", 40)

    def _get_text(self, post):
        """Extract searchable text from a post."""
        title = post.get("title", "")
        selftext = post.get("selftext", "")
        body = post.get("body", "")
        return f"{title} {selftext} {body}".strip()

    def score_new_content(self, post):
        """Score a post for new content value.

        Returns dict with 'score' (0-100) and 'signals' list.
        """
        text = self._get_text(post).lower()
        score = 0
        signals = []

        # Evidence keywords: +8 each, max 24
        evidence_hits = []
        for kw in self.evidence_keywords:
            if kw.lower() in text:
                evidence_hits.append(kw)
        evidence_bonus = min(len(evidence_hits) * 8, 24)
        if evidence_bonus > 0:
            score += evidence_bonus
            signals.append(f"evidence: {', '.join(evidence_hits[:3])}")

        # Known author bonus (reuse existing config)
        author = post.get("author", "")
        if author in self.known_authors:
            author_bonus = self.known_authors[author].get("bonus", 0)
            score += author_bonus
            signals.append(f"known author: {author}")

        # Keyword density (Aurora keywords / word count)
        words = text.split()
        word_count = len(words) if words else 1
        aurora_hits = sum(1 for term in self.aurora_terms if term.lower() in text)
        density = aurora_hits / word_count
        if density > 0.03:
            score += 10
            signals.append("high keyword density")
        elif density > 0.015:
            score += 5
            signals.append("medium keyword density")

        # Cross-references: forum +10, youtube +5
        raw_text = self._get_text(post)
        if re.search(r'https?://aurora2\.pentarch\.org\S*', raw_text):
            score += 10
            signals.append("forum cross-reference")
        if re.search(r'https?://(?:www\.)?(?:youtube\.com|youtu\.be)\S*', raw_text):
            score += 5
            signals.append("youtube cross-reference")

        # Text length bonus
        text_length = len(self._get_text(post))
        if text_length > 500:
            score += 10
            signals.append("detailed post (>500 chars)")
        elif text_length > 200:
            score += 5
            signals.append("substantial post (>200 chars)")

        # Question penalty: posts phrased as questions -5
        title = post.get("title", "")
        if (title.strip().endswith("?")
                or title.lower().startswith(("how ", "why ", "what ", "can ",
                                             "does ", "is ", "do ", "should "))):
            score -= 5
            signals.append("question format (-5)")

        # Cap at 100
        score = max(0, min(score, 100))

        return {"score": score, "signals": signals}

    def map_to_chapters(self, post):
        """Map a post to manual chapters via keyword matching.

        Requires >=2 keywords from a chapter to match.
        Returns [(chapter_num, chapter_name, confidence)] sorted by confidence desc.
        """
        text = self._get_text(post).lower()
        results = []

        for chapter_num, chapter_info in self.chapter_keywords.items():
            chapter_num = int(chapter_num)
            name = chapter_info["name"]
            keywords = chapter_info["keywords"]

            hits = sum(1 for kw in keywords if kw.lower() in text)
            if hits >= 2:
                confidence = min(hits / len(keywords), 1.0)
                results.append((chapter_num, name, round(confidence, 2)))

        results.sort(key=lambda x: x[2], reverse=True)
        return results

    def assess_unmatched(self, match_results, posts_by_id):
        """Main entry point: assess unmatched posts for new content value.

        Args:
            match_results: list of match result dicts from Matcher.find_matches()
            posts_by_id: dict mapping post_id -> raw post dict

        Returns:
            list of opportunity dicts, sorted by score descending.
        """
        if not match_results and not posts_by_id:
            return []

        # Filter to unmatched posts (routing="ignore" or triage with no issue)
        unmatched_ids = set()
        for result in match_results:
            routing = result.get("routing", "ignore")
            if routing == "ignore":
                unmatched_ids.add(result["post_id"])
            elif routing == "triage" and not result.get("issue"):
                unmatched_ids.add(result["post_id"])

        opportunities = []
        for post_id in unmatched_ids:
            post = posts_by_id.get(post_id)
            if not post:
                continue

            scoring = self.score_new_content(post)
            chapters = self.map_to_chapters(post)

            # Extract quote
            text = self._get_text(post)
            quote = text[:200] + "..." if len(text) > 200 else text

            opportunities.append({
                "post_id": post_id,
                "score": scoring["score"],
                "signals": scoring["signals"],
                "chapters": chapters,
                "title": post.get("title", ""),
                "author": post.get("author", ""),
                "permalink": post.get("permalink", ""),
                "subreddit": post.get("subreddit", ""),
                "created_utc": post.get("created_utc"),
                "quote": quote,
            })

        opportunities.sort(key=lambda x: x["score"], reverse=True)
        return opportunities

    def format_issue_title(self, opportunity):
        """Format a GitHub issue title for a new content opportunity.

        e.g. "New content: [Section 12] missile laser warhead mechanics"
        """
        chapters = opportunity.get("chapters", [])
        if chapters:
            ch_num = chapters[0][0]
            prefix = f"New content: [Section {ch_num}]"
        else:
            prefix = "New content:"

        post_title = opportunity.get("title", "untitled")
        title = f"{prefix} {post_title}"

        if len(title) > 128:
            title = title[:125] + "..."
        return title

    def format_issue_body(self, opportunity):
        """Format a GitHub issue body for a new content opportunity."""
        permalink = f"https://www.reddit.com{opportunity['permalink']}"
        author = opportunity.get("author", "unknown")
        subreddit = opportunity.get("subreddit", "aurora4x")
        score = opportunity.get("score", 0)
        quote = opportunity.get("quote", "")
        signals = opportunity.get("signals", [])
        chapters = opportunity.get("chapters", [])
        created_utc = opportunity.get("created_utc")

        date_str = "N/A"
        if created_utc:
            date_str = datetime.fromtimestamp(
                created_utc, tz=timezone.utc
            ).strftime("%Y-%m-%d")

        sections = []
        sections.append("## Reddit Source\n")
        sections.append(
            f"**Post:** [{opportunity.get('title', '')}]({permalink})\n"
            f"**Author:** u/{author} (r/{subreddit})\n"
            f"**Date:** {date_str}\n"
            f"**Score:** {score}/100\n"
        )

        if quote:
            sections.append(f"> {quote}\n")

        if chapters:
            sections.append("## Suggested Chapters\n")
            for ch_num, ch_name, confidence in chapters:
                sections.append(
                    f"- **Section {ch_num}: {ch_name}** "
                    f"(confidence: {confidence:.0%})"
                )
            sections.append("")

        if signals:
            sections.append("## Detected Signals\n")
            for signal in signals:
                sections.append(f"- {signal}")
            sections.append("")

        sections.append(
            "---\n"
            "*Detected by [aurora-monitor]"
            "(https://github.com/ErikEvenson/aurora-manual/tree/main/aurora_monitor) "
            "— new content detector*"
        )

        return "\n".join(sections)
