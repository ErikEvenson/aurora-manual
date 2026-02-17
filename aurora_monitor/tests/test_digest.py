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

    def test_digest_has_issue_matches_section(self, generator, matches, stats):
        """Digest summary should contain Issue Matches with issue numbers."""
        digest = generator.generate_digest(matches, stats)
        assert "## Issue Matches" in digest
        assert "#1230" in digest
        assert "#1214" in digest

    def test_digest_has_triage_section(self, generator, matches, stats):
        """Digest summary should reference triage items."""
        digest = generator.generate_digest(matches, stats)
        assert "## Triage" in digest
        assert "2 items" in digest

    def test_digest_has_cross_ref_section(self, generator, matches, stats):
        """Digest summary should reference cross-references."""
        digest = generator.generate_digest(matches, stats)
        assert "## Cross-References" in digest
        assert "1 links" in digest

    def test_digest_has_stats_section(self, generator, matches, stats):
        """Digest should contain a Statistics section."""
        digest = generator.generate_digest(matches, stats)
        assert "## Statistics" in digest
        assert "150" in digest  # posts scanned
        assert "320" in digest  # comments scanned

    def test_digest_issue_details_in_outputs(self, generator, matches, stats):
        """Full match details should be in issue_comments, not summary."""
        outputs = generator.generate_outputs(matches, stats)
        # Issue comments have the detailed author/quote info
        assert 1230 in outputs["issue_comments"]
        assert "TestUser1" in outputs["issue_comments"][1230]
        assert 1214 in outputs["issue_comments"]
        assert "AuroraPlayer42" in outputs["issue_comments"][1214]

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


def _make_match(post_id, routing, issue=None, score=85, subreddit="aurora4x",
                author="TestUser", title="Test post", quote="Test quote",
                cross_refs=None, created_utc=1708000000):
    """Helper to create match dicts for tests."""
    return {
        "post_id": post_id,
        "subreddit": subreddit,
        "author": author,
        "title": title,
        "permalink": f"/r/{subreddit}/comments/{post_id}/test/",
        "created_utc": created_utc,
        "score": score,
        "routing": routing,
        "issue": issue,
        "issue_title": f"Verify: issue {issue}" if issue else None,
        "quote": quote,
        "cross_references": cross_refs,
    }


def _make_comment_match(post_id, routing, issue=None, score=85,
                        subreddit="aurora4x", author="Commenter",
                        quote="Test comment", parent_post_id="parent1",
                        parent_title="Parent post", cross_refs=None,
                        created_utc=1708000000):
    """Helper to create comment match dicts for tests."""
    return {
        "post_id": post_id,
        "subreddit": subreddit,
        "author": author,
        "title": "",
        "permalink": f"/r/{subreddit}/comments/{parent_post_id}/test/{post_id}/",
        "created_utc": created_utc,
        "score": score,
        "routing": routing,
        "issue": issue,
        "issue_title": f"Verify: issue {issue}" if issue else None,
        "quote": quote,
        "cross_references": cross_refs,
        "content_type": "comment",
        "parent_post_id": parent_post_id,
        "parent_title": parent_title,
    }


def _make_stats(**overrides):
    """Helper to create stats dicts for tests."""
    defaults = {
        "posts_scanned": 1961,
        "comments_scanned": 0,
        "matches": 35,
        "triage_items": 1318,
        "cross_references": 219,
        "skipped": 389,
    }
    defaults.update(overrides)
    return defaults


class TestGenerateOutputs:
    """Test multi-tier output generation."""

    def test_returns_structured_dict(self, generator):
        """generate_outputs returns dict with four required keys."""
        matches = [_make_match("a1", "auto_comment", issue=100)]
        outputs = generator.generate_outputs(matches, _make_stats())
        assert "summary_body" in outputs
        assert "issue_comments" in outputs
        assert "triage_comments" in outputs
        assert "cross_ref_comments" in outputs

    def test_issue_comments_grouped_by_issue(self, generator):
        """issue_comments groups matched items by issue number."""
        matches = [
            _make_match("a1", "auto_comment", issue=100, quote="Quote A"),
            _make_match("a2", "auto_comment", issue=100, quote="Quote B"),
            _make_match("a3", "auto_comment", issue=200, quote="Quote C"),
        ]
        outputs = generator.generate_outputs(matches, _make_stats())
        assert 100 in outputs["issue_comments"]
        assert 200 in outputs["issue_comments"]
        # Issue 100 should contain both quotes
        assert "Quote A" in outputs["issue_comments"][100]
        assert "Quote B" in outputs["issue_comments"][100]
        # Issue 200 only has one
        assert "Quote C" in outputs["issue_comments"][200]

    def test_issue_comment_under_10k(self, generator):
        """Each issue comment must be under 10K chars."""
        # 50 matches on one issue — each ~200 chars = ~10K
        matches = [
            _make_match(f"m{i}", "auto_comment", issue=100,
                        quote=f"Detailed quote number {i} about game mechanics " * 3)
            for i in range(50)
        ]
        outputs = generator.generate_outputs(matches, _make_stats())
        for issue_num, comments in outputs["issue_comments"].items():
            if isinstance(comments, list):
                for c in comments:
                    assert len(c) <= 10000, f"Issue #{issue_num} comment exceeds 10K"
            else:
                assert len(comments) <= 10000, f"Issue #{issue_num} comment exceeds 10K"

    def test_triage_uses_task_list_format(self, generator):
        """Triage comments use - [ ] checkbox format."""
        matches = [_make_match("t1", "triage", quote="Triage item")]
        outputs = generator.generate_outputs(matches, _make_stats())
        assert len(outputs["triage_comments"]) >= 1
        assert "- [ ]" in outputs["triage_comments"][0]

    def test_triage_paginated_under_65k(self, generator):
        """Each triage comment must be under 65K chars."""
        # 1318 triage items — should paginate across multiple comments
        matches = [
            _make_match(f"t{i}", "triage",
                        quote=f"Triage quote {i} about some game mechanic")
            for i in range(1318)
        ]
        outputs = generator.generate_outputs(matches, _make_stats())
        assert len(outputs["triage_comments"]) > 1, "1318 items should require multiple comments"
        for i, comment in enumerate(outputs["triage_comments"]):
            assert len(comment) <= 65000, f"Triage comment {i} exceeds 65K"

    def test_cross_refs_grouped_by_type(self, generator):
        """cross_ref_comments groups by type (forum, youtube)."""
        matches = [
            _make_match("c1", "triage", cross_refs=[
                {"type": "forum", "url": "https://aurora2.pentarch.org/topic1"}
            ]),
            _make_match("c2", "triage", cross_refs=[
                {"type": "youtube", "url": "https://youtube.com/watch?v=abc"}
            ]),
        ]
        outputs = generator.generate_outputs(matches, _make_stats())
        assert "forum" in outputs["cross_ref_comments"]
        assert "youtube" in outputs["cross_ref_comments"]

    def test_cross_ref_comments_chunked(self, generator):
        """Cross-ref comments are chunked to stay under 65K."""
        matches = [
            _make_match(f"c{i}", "triage", cross_refs=[
                {"type": "forum", "url": f"https://aurora2.pentarch.org/index.php?topic={i}.0"}
            ])
            for i in range(200)
        ]
        outputs = generator.generate_outputs(matches, _make_stats())
        for comment in outputs["cross_ref_comments"].get("forum", []):
            assert len(comment) <= 65000

    def test_summary_under_65k(self, generator):
        """Summary body must be under 65K chars."""
        matches = [
            _make_match(f"m{i}", "auto_comment", issue=i)
            for i in range(35)
        ]
        outputs = generator.generate_outputs(matches, _make_stats())
        assert len(outputs["summary_body"]) <= 65000

    def test_summary_contains_issue_overview(self, generator):
        """Summary should contain an issue overview table."""
        matches = [_make_match("m1", "auto_comment", issue=100)]
        outputs = generator.generate_outputs(matches, _make_stats())
        assert "#100" in outputs["summary_body"]
        assert "posts_scanned" in outputs["summary_body"] or "1961" in outputs["summary_body"]

    def test_empty_matches_produce_valid_output(self, generator):
        """Empty matches should still produce valid structured output."""
        outputs = generator.generate_outputs([], _make_stats(matches=0, triage_items=0, cross_references=0))
        assert outputs["summary_body"]
        assert outputs["issue_comments"] == {}
        assert outputs["triage_comments"] == []
        assert outputs["cross_ref_comments"] == {}

    def test_backward_compatible_generate_digest(self, generator, matches, stats):
        """generate_digest() returns summary_body from generate_outputs()."""
        digest = generator.generate_digest(matches, stats)
        outputs = generator.generate_outputs(matches, stats)
        assert digest == outputs["summary_body"]
        assert "## Statistics" in digest


class TestNewContentInDigest:
    """Test new content opportunities in digest outputs."""

    def test_new_content_in_summary(self, generator):
        """Summary includes New Content Opportunities section when provided."""
        matches = [_make_match("m1", "auto_comment", issue=100)]
        new_content = [
            {
                "post_id": "nc1",
                "score": 75,
                "chapters": [(12, "Combat", 0.5)],
                "title": "Missile mechanics discovery",
                "author": "Tester",
                "permalink": "/r/aurora4x/comments/nc1/test/",
                "signals": ["evidence: tested"],
            },
        ]
        outputs = generator.generate_outputs(matches, _make_stats(), new_content=new_content)
        assert "## New Content Opportunities" in outputs["summary_body"]
        assert "Missile mechanics" in outputs["summary_body"]

    def test_new_content_comments_generated(self, generator):
        """New content opportunities produce discussion comments."""
        new_content = [
            {
                "post_id": f"nc{i}",
                "score": 75 - i,
                "chapters": [(12, "Combat", 0.5)],
                "title": f"Discovery {i}",
                "author": "User",
                "permalink": f"/r/aurora4x/comments/nc{i}/test/",
                "signals": ["evidence: tested"],
            }
            for i in range(5)
        ]
        outputs = generator.generate_outputs([], _make_stats(), new_content=new_content)
        assert "new_content_comments" in outputs
        assert len(outputs["new_content_comments"]) >= 1

    def test_backward_compat_no_new_content(self, generator):
        """generate_outputs without new_content param still works."""
        matches = [_make_match("m1", "auto_comment", issue=100)]
        outputs = generator.generate_outputs(matches, _make_stats())
        assert "new_content_comments" in outputs
        assert outputs["new_content_comments"] == []
        # Summary should not have new content section
        assert "## New Content Opportunities" not in outputs["summary_body"]


class TestCommentFormatting:
    """Test formatting of comment-sourced matches in digest outputs."""

    def test_mixed_post_and_comment_matches(self, generator):
        """generate_outputs handles mixed post + comment matches."""
        matches = [
            _make_match("p1", "auto_comment", issue=100, quote="Post quote"),
            _make_comment_match("c1", "auto_comment", issue=100,
                                quote="Comment confirms this",
                                parent_post_id="p1",
                                parent_title="Original post title"),
        ]
        outputs = generator.generate_outputs(matches, _make_stats())
        assert 100 in outputs["issue_comments"]
        comment_text = outputs["issue_comments"][100]
        # Both post and comment should appear
        assert "Post quote" in comment_text
        assert "Comment confirms this" in comment_text

    def test_comment_match_shows_parent_context(self, generator):
        """Comment matches in issue_comments show 'Reply to' with parent post link."""
        matches = [
            _make_comment_match("c1", "auto_comment", issue=200,
                                quote="Tested and confirmed",
                                parent_post_id="abc123",
                                parent_title="Testing thread"),
        ]
        outputs = generator.generate_outputs(matches, _make_stats())
        comment_text = outputs["issue_comments"][200]
        # Should explicitly say "Reply to" and link to parent post
        assert "Reply to" in comment_text
        assert "abc123" in comment_text

    def test_comment_attribution_distinct_from_post(self, generator):
        """Comment-sourced matches show 'Reply to' prefix that posts don't have."""
        post_matches = [
            _make_match("p1", "auto_comment", issue=300, quote="Same quote"),
        ]
        comment_matches = [
            _make_comment_match("c1", "auto_comment", issue=300,
                                quote="Same quote",
                                parent_post_id="p1",
                                parent_title="Parent post"),
        ]
        post_output = generator.generate_outputs(post_matches, _make_stats())
        comment_output = generator.generate_outputs(comment_matches, _make_stats())
        post_text = post_output["issue_comments"][300]
        comment_text = comment_output["issue_comments"][300]
        # Post should NOT have "Reply to"
        assert "Reply to" not in post_text
        # Comment should have "Reply to"
        assert "Reply to" in comment_text
