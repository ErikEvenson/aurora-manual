"""Reddit JSON API fetcher for r/aurora4x and r/aurora."""

import time
import requests


class RedditFetcher:
    """Fetch posts and comments from Reddit subreddits via JSON API."""

    BASE_URL = "https://www.reddit.com"

    def __init__(self, config):
        reddit_cfg = config["reddit"]
        self.subreddits = reddit_cfg["subreddits"]
        self.user_agent = reddit_cfg["user_agent"]
        self.rate_limit_delay = reddit_cfg.get("rate_limit_delay", 1.0)
        self.max_retries = reddit_cfg.get("max_retries", 3)
        self.backfill_max_pages = reddit_cfg.get("backfill_max_pages", 10)
        self.skip_flairs = set(
            f.lower() for f in reddit_cfg.get("skip_flairs", [])
        )

    def _get(self, url):
        """Make a rate-limited GET request with retry on 429."""
        headers = {"User-Agent": self.user_agent}
        for attempt in range(self.max_retries):
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
            if response.status_code == 429:
                wait = float(response.headers.get("Retry-After", 2 ** attempt))
                time.sleep(wait)
                continue
            response.raise_for_status()
        raise Exception(f"Max retries ({self.max_retries}) exceeded for {url}")

    def fetch_new_posts(self, subreddit, after=None):
        """Fetch new posts from a subreddit.

        Returns (posts, after_token) where posts is a list of normalized dicts
        and after_token is the pagination cursor for the next page.
        """
        url = f"{self.BASE_URL}/r/{subreddit}/new.json?limit=100&raw_json=1"
        if after:
            url += f"&after={after}"

        data = self._get(url)
        listing = data.get("data", {})
        after_token = listing.get("after")

        posts = []
        for child in listing.get("children", []):
            if child["kind"] != "t3":
                continue
            post = child["data"]
            normalized = self._normalize_post(post, subreddit)
            if self._should_skip(normalized):
                continue
            posts.append(normalized)

        if self.rate_limit_delay > 0:
            time.sleep(self.rate_limit_delay)

        return posts, after_token

    def fetch_post_comments(self, subreddit, post_id):
        """Fetch comments for a specific post.

        Returns a list of normalized comment dicts.
        """
        url = f"{self.BASE_URL}/r/{subreddit}/comments/{post_id}.json?raw_json=1"
        data = self._get(url)

        comments = []
        if len(data) < 2:
            return comments

        comment_listing = data[1].get("data", {})
        for child in comment_listing.get("children", []):
            if child["kind"] != "t1":
                continue
            comment = child["data"]
            comments.append(self._normalize_comment(comment, subreddit))

        if self.rate_limit_delay > 0:
            time.sleep(self.rate_limit_delay)

        return comments

    def backfill(self, subreddit):
        """Paginate through a subreddit's history, up to backfill_max_pages.

        Returns all fetched posts as normalized dicts.
        """
        all_posts = []
        after = None
        for page in range(self.backfill_max_pages):
            posts, after = self.fetch_new_posts(subreddit, after=after)
            all_posts.extend(posts)
            if not after:
                break
        return all_posts

    def _should_skip(self, post):
        """Check if a post should be skipped based on flair."""
        flair = (post.get("link_flair_text") or "").lower()
        return flair in self.skip_flairs

    @staticmethod
    def _normalize_post(post, subreddit):
        """Normalize a Reddit post dict to our standard format."""
        return {
            "id": post["id"],
            "subreddit": post.get("subreddit", subreddit),
            "author": post.get("author", "[deleted]"),
            "title": post.get("title", ""),
            "selftext": post.get("selftext", ""),
            "permalink": post.get("permalink", ""),
            "created_utc": post.get("created_utc"),
            "link_flair_text": post.get("link_flair_text"),
            "url": post.get("url", ""),
            "num_comments": post.get("num_comments", 0),
        }

    @staticmethod
    def _normalize_comment(comment, subreddit):
        """Normalize a Reddit comment dict to our standard format."""
        return {
            "id": comment["id"],
            "subreddit": subreddit,
            "author": comment.get("author", "[deleted]"),
            "body": comment.get("body", ""),
            "permalink": comment.get("permalink", ""),
            "created_utc": comment.get("created_utc"),
            "parent_id": comment.get("parent_id", ""),
        }
