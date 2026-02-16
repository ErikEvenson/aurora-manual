"""Tests for the Reddit fetcher module."""

import json
import os
from unittest.mock import patch, MagicMock
import pytest

from aurora_monitor.sources.reddit import RedditFetcher

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")


@pytest.fixture
def config():
    return {
        "reddit": {
            "subreddits": ["aurora4x", "aurora"],
            "user_agent": "aurora-manual-monitor/1.0 (test)",
            "rate_limit_delay": 0,  # No delay in tests
            "max_retries": 3,
            "backfill_max_pages": 2,
            "skip_flairs": ["Captain's Log", "Skunkworks", "Out of this World", "META"],
        }
    }


@pytest.fixture
def fetcher(config):
    return RedditFetcher(config)


@pytest.fixture
def mock_listing():
    """A Reddit JSON listing response."""
    return {
        "kind": "Listing",
        "data": {
            "after": "t3_next_page",
            "children": [
                {
                    "kind": "t3",
                    "data": {
                        "id": "abc123",
                        "subreddit": "aurora4x",
                        "author": "TestUser",
                        "title": "Test post about missiles",
                        "selftext": "Testing missile fire control mechanics.",
                        "permalink": "/r/aurora4x/comments/abc123/test_post/",
                        "created_utc": 1708000000.0,
                        "link_flair_text": "Mechanics",
                        "url": "https://www.reddit.com/r/aurora4x/comments/abc123/",
                        "num_comments": 5,
                    },
                },
                {
                    "kind": "t3",
                    "data": {
                        "id": "def456",
                        "subreddit": "aurora4x",
                        "author": "AnotherUser",
                        "title": "My fleet design",
                        "selftext": "Here's my destroyer class.",
                        "permalink": "/r/aurora4x/comments/def456/my_fleet/",
                        "created_utc": 1708100000.0,
                        "link_flair_text": None,
                        "url": "https://www.reddit.com/r/aurora4x/comments/def456/",
                        "num_comments": 2,
                    },
                },
            ],
        },
    }


@pytest.fixture
def mock_comments():
    """A Reddit comments response (post + comments)."""
    return [
        {
            "kind": "Listing",
            "data": {
                "children": [
                    {
                        "kind": "t3",
                        "data": {
                            "id": "abc123",
                            "title": "Test post",
                            "selftext": "Original post text.",
                        },
                    }
                ]
            },
        },
        {
            "kind": "Listing",
            "data": {
                "children": [
                    {
                        "kind": "t1",
                        "data": {
                            "id": "comment1",
                            "author": "Commenter1",
                            "body": "I tested this and got the same result.",
                            "permalink": "/r/aurora4x/comments/abc123/test/comment1/",
                            "created_utc": 1708050000.0,
                            "parent_id": "t3_abc123",
                        },
                    },
                    {
                        "kind": "t1",
                        "data": {
                            "id": "comment2",
                            "author": "Commenter2",
                            "body": "Interesting finding!",
                            "permalink": "/r/aurora4x/comments/abc123/test/comment2/",
                            "created_utc": 1708060000.0,
                            "parent_id": "t3_abc123",
                        },
                    },
                ],
            },
        },
    ]


class TestFetchPosts:
    """Test fetching new posts from a subreddit."""

    @patch("aurora_monitor.sources.reddit.requests.get")
    def test_fetch_new_posts(self, mock_get, fetcher, mock_listing):
        """Should return normalized post dicts from Reddit API."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_listing
        mock_get.return_value = mock_response

        posts, after = fetcher.fetch_new_posts("aurora4x")

        assert len(posts) == 2
        assert posts[0]["id"] == "abc123"
        assert posts[0]["subreddit"] == "aurora4x"
        assert posts[0]["author"] == "TestUser"
        assert posts[0]["title"] == "Test post about missiles"
        assert after == "t3_next_page"

    @patch("aurora_monitor.sources.reddit.requests.get")
    def test_fetch_with_after_token(self, mock_get, fetcher, mock_listing):
        """Should pass after token for pagination."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_listing
        mock_get.return_value = mock_response

        fetcher.fetch_new_posts("aurora4x", after="t3_prev_page")

        call_args = mock_get.call_args
        assert "after=t3_prev_page" in call_args[0][0] or \
               call_args[1].get("params", {}).get("after") == "t3_prev_page"


class TestFetchComments:
    """Test fetching comments for a post."""

    @patch("aurora_monitor.sources.reddit.requests.get")
    def test_fetch_post_comments(self, mock_get, fetcher, mock_comments):
        """Should return normalized comment dicts."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_comments
        mock_get.return_value = mock_response

        comments = fetcher.fetch_post_comments("aurora4x", "abc123")

        assert len(comments) == 2
        assert comments[0]["id"] == "comment1"
        assert comments[0]["author"] == "Commenter1"
        assert "tested this" in comments[0]["body"]


class TestRateLimiting:
    """Test rate limiting and error handling."""

    @patch("aurora_monitor.sources.reddit.requests.get")
    def test_429_retry(self, mock_get, fetcher, mock_listing):
        """Should retry on 429 with backoff."""
        mock_429 = MagicMock()
        mock_429.status_code = 429
        mock_429.headers = {"Retry-After": "1"}
        mock_429.raise_for_status.side_effect = Exception("429 Too Many Requests")

        mock_ok = MagicMock()
        mock_ok.status_code = 200
        mock_ok.json.return_value = mock_listing

        mock_get.side_effect = [mock_429, mock_ok]

        posts, after = fetcher.fetch_new_posts("aurora4x")
        assert len(posts) == 2
        assert mock_get.call_count == 2

    @patch("aurora_monitor.sources.reddit.requests.get")
    def test_max_retries_exceeded(self, mock_get, fetcher):
        """Should raise after max retries."""
        mock_429 = MagicMock()
        mock_429.status_code = 429
        mock_429.headers = {"Retry-After": "1"}
        mock_429.raise_for_status.side_effect = Exception("429")

        mock_get.return_value = mock_429

        with pytest.raises(Exception):
            fetcher.fetch_new_posts("aurora4x")


class TestBackfill:
    """Test backfill pagination."""

    @patch("aurora_monitor.sources.reddit.requests.get")
    def test_backfill_paginates(self, mock_get, fetcher):
        """Backfill should follow pagination tokens."""
        page1 = {
            "kind": "Listing",
            "data": {
                "after": "t3_page2",
                "children": [
                    {
                        "kind": "t3",
                        "data": {
                            "id": f"post_{i}",
                            "subreddit": "aurora4x",
                            "author": "User",
                            "title": f"Post {i}",
                            "selftext": "Content",
                            "permalink": f"/r/aurora4x/comments/post_{i}/",
                            "created_utc": 1708000000.0 + i,
                            "link_flair_text": None,
                            "url": f"https://reddit.com/r/aurora4x/post_{i}",
                            "num_comments": 0,
                        },
                    }
                    for i in range(100)
                ],
            },
        }
        page2 = {
            "kind": "Listing",
            "data": {
                "after": None,
                "children": [
                    {
                        "kind": "t3",
                        "data": {
                            "id": f"post_{100 + i}",
                            "subreddit": "aurora4x",
                            "author": "User",
                            "title": f"Post {100 + i}",
                            "selftext": "Content",
                            "permalink": f"/r/aurora4x/comments/post_{100+i}/",
                            "created_utc": 1708100000.0 + i,
                            "link_flair_text": None,
                            "url": f"https://reddit.com/r/aurora4x/post_{100+i}",
                            "num_comments": 0,
                        },
                    }
                    for i in range(50)
                ],
            },
        }

        mock_resp1 = MagicMock(status_code=200)
        mock_resp1.json.return_value = page1
        mock_resp2 = MagicMock(status_code=200)
        mock_resp2.json.return_value = page2
        mock_get.side_effect = [mock_resp1, mock_resp2]

        posts = fetcher.backfill("aurora4x")
        assert len(posts) == 150
        assert mock_get.call_count == 2


class TestFlairFiltering:
    """Test flair-based post filtering."""

    @patch("aurora_monitor.sources.reddit.requests.get")
    def test_skip_aar_flair(self, mock_get, fetcher):
        """Posts with Captain's Log flair should be skipped."""
        listing = {
            "kind": "Listing",
            "data": {
                "after": None,
                "children": [
                    {
                        "kind": "t3",
                        "data": {
                            "id": "aar_post",
                            "subreddit": "aurora4x",
                            "author": "AARWriter",
                            "title": "My Campaign Part 7",
                            "selftext": "Long AAR narrative...",
                            "permalink": "/r/aurora4x/comments/aar_post/",
                            "created_utc": 1708000000.0,
                            "link_flair_text": "Captain's Log",
                            "url": "https://reddit.com/r/aurora4x/aar_post",
                            "num_comments": 10,
                        },
                    },
                    {
                        "kind": "t3",
                        "data": {
                            "id": "mechanics_post",
                            "subreddit": "aurora4x",
                            "author": "Tester",
                            "title": "Testing fuel consumption",
                            "selftext": "I tested fuel consumption at half speed.",
                            "permalink": "/r/aurora4x/comments/mechanics_post/",
                            "created_utc": 1708100000.0,
                            "link_flair_text": "The Academy",
                            "url": "https://reddit.com/r/aurora4x/mechanics_post",
                            "num_comments": 3,
                        },
                    },
                    {
                        "kind": "t3",
                        "data": {
                            "id": "ship_post",
                            "subreddit": "aurora4x",
                            "author": "Designer",
                            "title": "My destroyer design",
                            "selftext": "Here's my ship.",
                            "permalink": "/r/aurora4x/comments/ship_post/",
                            "created_utc": 1708200000.0,
                            "link_flair_text": "Skunkworks",
                            "url": "https://reddit.com/r/aurora4x/ship_post",
                            "num_comments": 5,
                        },
                    },
                ],
            },
        }
        mock_response = MagicMock(status_code=200)
        mock_response.json.return_value = listing
        mock_get.return_value = mock_response

        posts, _ = fetcher.fetch_new_posts("aurora4x")
        assert len(posts) == 1
        assert posts[0]["id"] == "mechanics_post"

    @patch("aurora_monitor.sources.reddit.requests.get")
    def test_no_flair_passes_through(self, mock_get, fetcher):
        """Posts without flair should not be filtered."""
        listing = {
            "kind": "Listing",
            "data": {
                "after": None,
                "children": [
                    {
                        "kind": "t3",
                        "data": {
                            "id": "no_flair_post",
                            "subreddit": "aurora4x",
                            "author": "User",
                            "title": "Question about missiles",
                            "selftext": "How do missiles work?",
                            "permalink": "/r/aurora4x/comments/no_flair/",
                            "created_utc": 1708000000.0,
                            "link_flair_text": None,
                            "url": "https://reddit.com/r/aurora4x/no_flair",
                            "num_comments": 2,
                        },
                    },
                ],
            },
        }
        mock_response = MagicMock(status_code=200)
        mock_response.json.return_value = listing
        mock_get.return_value = mock_response

        posts, _ = fetcher.fetch_new_posts("aurora4x")
        assert len(posts) == 1

    @patch("aurora_monitor.sources.reddit.requests.get")
    def test_flair_case_insensitive(self, mock_get, fetcher):
        """Flair filtering should be case-insensitive."""
        listing = {
            "kind": "Listing",
            "data": {
                "after": None,
                "children": [
                    {
                        "kind": "t3",
                        "data": {
                            "id": "case_post",
                            "subreddit": "aurora4x",
                            "author": "User",
                            "title": "My log",
                            "selftext": "Story...",
                            "permalink": "/r/aurora4x/comments/case_post/",
                            "created_utc": 1708000000.0,
                            "link_flair_text": "CAPTAIN'S LOG",
                            "url": "https://reddit.com/r/aurora4x/case_post",
                            "num_comments": 1,
                        },
                    },
                ],
            },
        }
        mock_response = MagicMock(status_code=200)
        mock_response.json.return_value = listing
        mock_get.return_value = mock_response

        posts, _ = fetcher.fetch_new_posts("aurora4x")
        assert len(posts) == 0
