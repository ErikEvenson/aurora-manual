"""Tests for the digest generator module."""

from datetime import date, datetime
import pytest

from aurora_monitor.digest import DigestGenerator


@pytest.fixture
def matches():
    return [
        {
            "post_id": "abc123",
            "subreddit": "aurora4x",
            "author": "TestUser1",
            "title": "Testing box launcher reload",
            "permalink": "/r/aurora4x/comments/abc123/test/",
            "created_utc": 1708000000,
            "score": 85,
            "routing": "auto_comment",
            "issue": 1230,
            "issue_title": "Verify: [8.5/12.3] Box launcher reload 10x slower",
            "quote": "I tested box launcher reload times at OTPs vs hangars",
            "cross_references": None,
        },
        {
            "post_id": "def456",
            "subreddit": "aurora4x",
            "author": "AuroraPlayer42",
            "title": "Fuel consumption question",
            "permalink": "/r/aurora4x/comments/def456/fuel/",
            "created_utc": 1708100000,
            "score": 65,
            "routing": "auto_comment",
            "issue": 1214,
            "issue_title": "Verify: Section 14.1.2 fuel consumption",
            "quote": "Does fuel consumption scale with travel speed",
            "cross_references": None,
        },
        {
            "post_id": "ghi789",
            "subreddit": "aurora4x",
            "author": "NewPlayer",
            "title": "Weird shipyard behavior",
            "permalink": "/r/aurora4x/comments/ghi789/shipyard/",
            "created_utc": 1708200000,
            "score": 45,
            "routing": "triage",
            "issue": None,
            "issue_title": None,
            "quote": "My shipyard seems to service multiple ships at once",
            "cross_references": None,
        },
        {
            "post_id": "jkl012",
            "subreddit": "aurora4x",
            "author": "ForumLinker",
            "title": "v2.8.0 changes discussion",
            "permalink": "/r/aurora4x/comments/jkl012/v280/",
            "created_utc": 1708300000,
            "score": 30,
            "routing": "triage",
            "issue": None,
            "issue_title": None,
            "quote": "Check out the forum post about v2.8.0",
            "cross_references": [
                {"type": "forum", "url": "https://aurora2.pentarch.org/index.php?topic=13884.0"}
            ],
        },
    ]


@pytest.fixture
def stats():
    return {
        "posts_scanned": 150,
        "comments_scanned": 320,
        "matches": 2,
        "triage_items": 2,
        "cross_references": 1,
        "skipped": 146,
    }


@pytest.fixture
def generator():
    return DigestGenerator()


class TestDigestGeneration:
    """Test digest markdown generation."""

    def test_digest_has_matched_section(self, generator, matches, stats):
        """Digest should contain a Matched section with auto_comment items."""
        digest = generator.generate_digest(matches, stats)
        assert "## Matched" in digest
        assert "#1230" in digest
        assert "#1214" in digest

    def test_digest_has_triage_section(self, generator, matches, stats):
        """Digest should contain a Triage section."""
        digest = generator.generate_digest(matches, stats)
        assert "## Triage" in digest
        assert "Weird shipyard behavior" in digest

    def test_digest_has_cross_ref_section(self, generator, matches, stats):
        """Digest should contain a Cross-References section."""
        digest = generator.generate_digest(matches, stats)
        assert "## Cross-References" in digest
        assert "aurora2.pentarch.org" in digest

    def test_digest_has_stats_section(self, generator, matches, stats):
        """Digest should contain a Statistics section."""
        digest = generator.generate_digest(matches, stats)
        assert "## Statistics" in digest
        assert "150" in digest  # posts scanned
        assert "320" in digest  # comments scanned

    def test_digest_attribution(self, generator, matches, stats):
        """Digest should include author attribution for all items."""
        digest = generator.generate_digest(matches, stats)
        assert "TestUser1" in digest
        assert "AuroraPlayer42" in digest
        assert "r/aurora4x" in digest

    def test_empty_digest(self, generator):
        """Empty matches should still produce a valid digest."""
        digest = generator.generate_digest([], {
            "posts_scanned": 50,
            "comments_scanned": 100,
            "matches": 0,
            "triage_items": 0,
            "cross_references": 0,
            "skipped": 50,
        })
        assert "## Statistics" in digest
        assert "No matches" in digest or "0" in digest


class TestDigestTiming:
    """Test digest posting schedule."""

    def test_should_post_on_sunday(self, generator):
        """should_post_digest returns True on Sunday."""
        sunday = date(2026, 2, 15)  # Sunday
        assert generator.should_post_digest(sunday) is True

    def test_should_not_post_on_weekday(self, generator):
        """should_post_digest returns False on non-Sunday."""
        monday = date(2026, 2, 16)  # Monday
        assert generator.should_post_digest(monday) is False


class TestDigestTitle:
    """Test digest title formatting."""

    def test_title_format(self, generator):
        """Title should follow [Reddit Monitor] Week of YYYY-MM-DD format."""
        title = generator.digest_title(date(2026, 2, 15))
        assert title == "[Reddit Monitor] Week of 2026-02-15"
