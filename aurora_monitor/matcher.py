"""Shared keyword + fuzzy matching engine for community source monitors."""

import re
from thefuzz import fuzz


class Matcher:
    """Match community content against open unverified GitHub issues."""

    def __init__(self, config):
        self.config = config["matching"]
        self.thresholds = self.config["thresholds"]
        self.known_authors = self.config.get("known_authors", {})
        self.multi_match_penalty = self.config.get("multi_match_penalty", 10)
        self.keywords = self.config.get("keywords", {})
        self.issues = []

    def score_match(self, post, issue):
        """Score how well a post or comment matches an issue. Returns 0-100+."""
        if "body" in post and "selftext" not in post:
            post_text = post.get("body", "").lower()
        else:
            post_text = f"{post.get('title', '')} {post.get('selftext', '')}".lower()
        issue_text = f"{issue['title']} {issue.get('body', '')}".lower()

        # Fuzzy match score (0-100)
        fuzzy_score = fuzz.token_set_ratio(post_text, issue_text)

        # Penalize short text — token_set_ratio produces false positives when
        # the post has few tokens (a single matching word → 100% ratio).
        min_text_length = self.config.get("min_text_length", 50)
        post_text_length = len(post_text.strip())
        if post_text_length < min_text_length:
            length_ratio = post_text_length / min_text_length
            fuzzy_score = fuzzy_score * length_ratio

        # Penalize long issue bodies — token_set_ratio produces false positives
        # when the issue has many tokens (large token pool overlaps with any
        # Aurora-related post). Symmetric with short-text penalty above. (#1298)
        max_issue_length = self.config.get("max_issue_length", 500)
        long_issue_exponent = self.config.get("long_issue_exponent", 0.15)
        issue_text_length = len(issue_text.strip())
        if issue_text_length > max_issue_length and long_issue_exponent > 0:
            length_ratio = (max_issue_length / issue_text_length) ** long_issue_exponent
            fuzzy_score = fuzzy_score * length_ratio

        # Keyword counting bonus
        keyword_bonus = self._keyword_bonus(post_text)

        # Known author bonus
        author_bonus = 0
        author = post.get("author", "")
        if author in self.known_authors:
            author_bonus = self.known_authors[author].get("bonus", 0)

        # Weighted score: fuzzy is primary, keywords and author are additive
        score = fuzzy_score + (keyword_bonus * 0.5) + author_bonus

        return min(score, 100)  # Cap at 100 for routing purposes

    def _keyword_bonus(self, text):
        """Count keyword matches across priority tiers."""
        bonus = 0
        for kw in self.keywords.get("high", []):
            if kw.lower() in text:
                bonus += 6
        for kw in self.keywords.get("medium", []):
            if kw.lower() in text:
                bonus += 3
        return bonus

    def _detect_cross_references(self, post):
        """Detect links to Aurora Forums or YouTube in post or comment text."""
        text = f"{post.get('title', '')} {post.get('selftext', '')} {post.get('body', '')}"
        refs = []

        forum_urls = re.findall(r'https?://aurora2\.pentarch\.org\S*', text)
        for url in forum_urls:
            refs.append({"type": "forum", "url": url})

        youtube_urls = re.findall(
            r'https?://(?:www\.)?(?:youtube\.com|youtu\.be)\S*', text
        )
        for url in youtube_urls:
            refs.append({"type": "youtube", "url": url})

        return refs

    def _route(self, score):
        """Determine routing based on score."""
        if score >= self.thresholds["high"]:
            return "auto_comment"
        elif score >= self.thresholds["medium"]:
            return "auto_comment"
        elif score >= self.thresholds["low"]:
            return "triage"
        return "ignore"

    def find_matches(self, posts):
        """Find matches for a list of posts/comments against all loaded issues.

        Returns a list of match results, one per item. Each result includes
        the best matching issue (if any), score, routing, cross-references,
        and for comments: content_type="comment" and parent_post_id.
        """
        results = []
        for post in posts:
            is_comment = "body" in post and "selftext" not in post
            content_type = "comment" if is_comment else "post"
            parent_post_id = None
            if is_comment:
                # parent_id is like "t3_abc123" for top-level comments
                raw_parent = post.get("parent_id", "")
                if raw_parent.startswith("t3_"):
                    parent_post_id = raw_parent[3:]
                elif raw_parent.startswith("t1_"):
                    parent_post_id = raw_parent[3:]

            cross_refs = self._detect_cross_references(post)

            # Score against all issues
            issue_scores = []
            for issue in self.issues:
                score = self.score_match(post, issue)
                if score >= self.thresholds["low"]:
                    issue_scores.append((issue, score))

            # Sort by score descending
            issue_scores.sort(key=lambda x: x[1], reverse=True)

            # Apply multi-match penalty
            if len(issue_scores) > 1:
                penalized = []
                for i, (issue, score) in enumerate(issue_scores):
                    penalty = i * self.multi_match_penalty
                    penalized.append((issue, max(0, score - penalty)))
                issue_scores = penalized

            # Extract quote from appropriate field
            quote_text = post.get("body", "") if is_comment else post.get("selftext", "")

            if issue_scores:
                best_issue, best_score = issue_scores[0]
                routing = self._route(best_score)
                result = {
                    "post_id": post["id"],
                    "subreddit": post.get("subreddit", ""),
                    "author": post.get("author", ""),
                    "title": post.get("title", ""),
                    "permalink": post.get("permalink", ""),
                    "created_utc": post.get("created_utc"),
                    "score": best_score,
                    "routing": routing,
                    "issue": best_issue["number"] if routing == "auto_comment" else None,
                    "issue_title": best_issue["title"] if routing == "auto_comment" else None,
                    "quote": _extract_quote(quote_text),
                    "cross_references": cross_refs if cross_refs else None,
                    "content_type": content_type,
                    "parent_post_id": parent_post_id,
                }
                results.append(result)
            else:
                # No issue match — check for relevance via keywords/cross-refs
                routing = "triage" if cross_refs else "ignore"
                result = {
                    "post_id": post["id"],
                    "subreddit": post.get("subreddit", ""),
                    "author": post.get("author", ""),
                    "title": post.get("title", ""),
                    "permalink": post.get("permalink", ""),
                    "created_utc": post.get("created_utc"),
                    "score": 0,
                    "routing": routing,
                    "issue": None,
                    "issue_title": None,
                    "quote": _extract_quote(quote_text),
                    "cross_references": cross_refs if cross_refs else None,
                    "content_type": content_type,
                    "parent_post_id": parent_post_id,
                }
                results.append(result)

        return results


def _extract_quote(text, max_length=200):
    """Extract a representative quote from post text.

    Newlines are replaced with spaces to keep markdown table rows intact.
    Pipe characters are replaced to avoid breaking table columns.
    """
    if not text:
        return ""
    # Collapse newlines and normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Escape pipe characters that would break markdown tables
    text = text.replace('|', '\\|')
    # Take first meaningful sentence
    sentences = re.split(r'[.!?]\s+', text)
    if sentences:
        quote = sentences[0].strip()
        if len(quote) > max_length:
            quote = quote[:max_length] + "..."
        return quote
    return text[:max_length] + "..." if len(text) > max_length else text
