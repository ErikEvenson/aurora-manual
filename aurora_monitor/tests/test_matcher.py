"""Tests for the matcher module."""

import json
import os
import pytest

from aurora_monitor.matcher import Matcher

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")


@pytest.fixture
def issues():
    with open(os.path.join(FIXTURES_DIR, "github_issues.json")) as f:
        return json.load(f)


@pytest.fixture
def posts():
    with open(os.path.join(FIXTURES_DIR, "reddit_posts.json")) as f:
        return json.load(f)


@pytest.fixture
def config():
    return {
        "matching": {
            "thresholds": {"high": 80, "medium": 60, "low": 40},
            "known_authors": {
                "SteveWalmsley": {"bonus": 30, "note": "Aurora developer"},
            },
            "multi_match_penalty": 10,
            "keywords": {
                "high": [
                    "box launcher",
                    "fuel consumption",
                    "fire control",
                    "ground forces",
                    "fortification",
                    "ordnance transfer",
                ],
                "medium": [
                    "aurora c#",
                    "game mechanics",
                    "damage calculation",
                    "shipyard",
                ],
                "aurora_terms": [
                    "aurora",
                    "trans-newtonian",
                    "duranium",
                    "PDC",
                    "CIWS",
                ],
            },
        },
    }


@pytest.fixture
def matcher(config, issues):
    m = Matcher(config)
    m.issues = issues
    return m


class TestMatchScoring:
    """Test individual match scoring."""

    def test_high_confidence_match(self, matcher, posts):
        """Post about box launcher reload should match issue #1230 with high confidence."""
        post = posts[0]  # post_high_match - box launcher reload
        issue = matcher.issues[2]  # issue 1230 - box launcher reload
        score = matcher.score_match(post, issue)
        assert score >= 80, f"Expected high confidence (>=80), got {score}"

    def test_medium_confidence_match(self, matcher, posts):
        """Post about fuel consumption should match issue #1214 with medium+ confidence."""
        post = posts[1]  # post_medium_match - fuel consumption question
        issue = matcher.issues[5]  # issue 1214 - fuel consumption
        score = matcher.score_match(post, issue)
        assert 60 <= score, f"Expected medium+ confidence (>=60), got {score}"

    def test_no_match_routes_low(self, matcher, posts):
        """AAR post should not route to auto_comment for any issue."""
        post = posts[3]  # post_no_match - AAR post
        for issue in matcher.issues:
            score = matcher.score_match(post, issue)
            assert score < 60, (
                f"AAR post should not reach medium confidence for "
                f"issue #{issue['number']}, got {score}"
            )

    def test_known_author_boost(self, matcher, posts):
        """Posts by known authors get a score bonus."""
        post = posts[2]  # post_known_author - SteveWalmsley
        issue = matcher.issues[3]  # issue 1229 - THM fortification
        score_known = matcher.score_match(post, issue)

        # Same post but with unknown author
        post_unknown = {**post, "author": "RandomUser"}
        score_unknown = matcher.score_match(post_unknown, issue)

        assert score_known > score_unknown, (
            f"Known author ({score_known}) should score higher than unknown ({score_unknown})"
        )
        assert score_known - score_unknown >= 20, (
            "Author bonus should be significant (>=20 points)"
        )


class TestMatchRouting:
    """Test match finding and routing decisions."""

    def test_find_matches_returns_results(self, matcher, posts):
        """find_matches should return a list of match results."""
        matches = matcher.find_matches(posts)
        assert isinstance(matches, list)
        assert len(matches) > 0

    def test_high_match_routes_to_auto_comment(self, matcher, posts):
        """High confidence matches route to auto_comment."""
        matches = matcher.find_matches([posts[0]])  # box launcher post
        high_matches = [m for m in matches if m["routing"] == "auto_comment"]
        assert len(high_matches) > 0, "High confidence match should route to auto_comment"

    def test_low_match_routes_to_ignore(self, matcher, posts):
        """Low/no confidence matches route to ignore."""
        matches = matcher.find_matches([posts[3]])  # AAR post
        for m in matches:
            assert m["routing"] in ("ignore", "triage"), (
                f"AAR post should route to ignore or triage, got {m['routing']}"
            )

    def test_known_author_high_confidence(self, matcher, posts):
        """Developer posts on matching topics get high confidence."""
        matches = matcher.find_matches([posts[2]])  # SteveWalmsley post
        auto_matches = [m for m in matches if m["routing"] == "auto_comment"]
        assert len(auto_matches) > 0, "Developer post should get auto_comment routing"

    def test_multi_match_penalty(self, matcher, posts):
        """Posts matching many issues get penalized per additional match."""
        matches = matcher.find_matches([posts[6]])  # multi_match post
        # The multi-match post mentions 5+ different topics
        # Individual scores should be lower than a focused post on the same topic
        if matches:
            scores = [m["score"] for m in matches if m.get("issue")]
            if len(scores) > 1:
                # At least some scores should reflect the penalty
                assert any(s < 80 for s in scores), (
                    "Multi-match should penalize at least some scores"
                )


class TestCrossReferences:
    """Test cross-reference detection."""

    def test_forum_cross_reference(self, matcher, posts):
        """Posts linking to aurora2.pentarch.org are flagged as forum cross-refs."""
        matches = matcher.find_matches([posts[4]])  # forum link post
        cross_refs = [m for m in matches if m.get("cross_references")]
        assert len(cross_refs) > 0, "Forum link should be detected as cross-reference"
        ref = cross_refs[0]["cross_references"][0]
        assert ref["type"] == "forum"

    def test_youtube_cross_reference(self, matcher, posts):
        """Posts linking to youtube.com are flagged as YouTube cross-refs."""
        matches = matcher.find_matches([posts[5]])  # youtube link post
        cross_refs = [m for m in matches if m.get("cross_references")]
        assert len(cross_refs) > 0, "YouTube link should be detected as cross-reference"
        ref = cross_refs[0]["cross_references"][0]
        assert ref["type"] == "youtube"


class TestMatchResult:
    """Test match result structure."""

    def test_match_result_has_required_fields(self, matcher, posts):
        """Each match result has the required metadata fields."""
        matches = matcher.find_matches([posts[0]])
        assert len(matches) > 0
        result = matches[0]
        required_fields = ["post_id", "subreddit", "author", "title",
                           "permalink", "score", "routing"]
        for field in required_fields:
            assert field in result, f"Missing required field: {field}"

    def test_auto_comment_match_has_issue(self, matcher, posts):
        """auto_comment matches include the matched issue number."""
        matches = matcher.find_matches([posts[0]])
        auto_matches = [m for m in matches if m["routing"] == "auto_comment"]
        for m in auto_matches:
            assert "issue" in m and m["issue"] is not None, (
                "auto_comment match must include issue number"
            )


class TestCommentMatching:
    """Test matching of Reddit comments (body field, no title/selftext)."""

    def test_score_match_handles_comment_body(self, matcher):
        """score_match builds text from body field when title/selftext absent."""
        comment = {
            "id": "comment_1",
            "subreddit": "aurora4x",
            "author": "Tester",
            "body": "I tested box launcher reload at OTPs and it's 10x slower than hangars. Confirmed with Mark IV launchers.",
            "permalink": "/r/aurora4x/comments/abc123/test/comment_1/",
            "created_utc": 1708000000,
            "parent_id": "t3_abc123",
        }
        issue = matcher.issues[2]  # issue 1230 - box launcher reload
        score = matcher.score_match(comment, issue)
        assert score >= 60, f"Comment about box launchers should score >=60, got {score}"

    def test_find_matches_comment_has_content_type(self, matcher):
        """find_matches returns content_type='comment' for comment-shaped input."""
        comment = {
            "id": "comment_2",
            "subreddit": "aurora4x",
            "author": "MechanicsGuy",
            "body": "Box launcher reload at OTPs is definitely 10x slower than hangars.",
            "permalink": "/r/aurora4x/comments/abc123/test/comment_2/",
            "created_utc": 1708000000,
            "parent_id": "t3_abc123",
        }
        matches = matcher.find_matches([comment])
        assert len(matches) > 0
        assert matches[0]["content_type"] == "comment"

    def test_find_matches_comment_has_parent_post_id(self, matcher):
        """find_matches includes parent_post_id for comments."""
        comment = {
            "id": "comment_3",
            "subreddit": "aurora4x",
            "author": "Verifier",
            "body": "I can confirm fuel consumption scales with actual travel speed, not rated speed.",
            "permalink": "/r/aurora4x/comments/def456/fuel/comment_3/",
            "created_utc": 1708100000,
            "parent_id": "t3_def456",
        }
        matches = matcher.find_matches([comment])
        assert len(matches) > 0
        assert matches[0]["parent_post_id"] == "def456"

    def test_find_matches_post_has_content_type_post(self, matcher, posts):
        """find_matches returns content_type='post' for regular posts."""
        matches = matcher.find_matches([posts[0]])
        assert len(matches) > 0
        assert matches[0]["content_type"] == "post"

    def test_cross_reference_detected_in_comment_body(self, matcher):
        """Cross-references in comment body field are detected."""
        comment = {
            "id": "comment_xref",
            "subreddit": "aurora4x",
            "author": "Helper",
            "body": "See the forum post about this: https://aurora2.pentarch.org/index.php?topic=12345.0",
            "permalink": "/r/aurora4x/comments/xyz/test/comment_xref/",
            "created_utc": 1708000000,
            "parent_id": "t3_xyz",
        }
        matches = matcher.find_matches([comment])
        assert len(matches) > 0
        xrefs = matches[0].get("cross_references")
        assert xrefs is not None and len(xrefs) > 0
        assert xrefs[0]["type"] == "forum"

    def test_short_comment_scores_low(self, matcher):
        """Comments with very short body text should score low."""
        comment = {
            "id": "comment_short",
            "subreddit": "aurora4x",
            "author": "Brief",
            "body": "Thanks!",
            "permalink": "/r/aurora4x/comments/xyz/test/comment_short/",
            "created_utc": 1708000000,
            "parent_id": "t3_xyz",
        }
        for issue in matcher.issues:
            score = matcher.score_match(comment, issue)
            assert score < 60, (
                f"Short comment should not reach medium confidence for "
                f"issue #{issue['number']}, got {score}"
            )


class TestShortTextPenalty:
    """Test that short/empty posts are penalized to prevent false positives."""

    def test_short_title_only_post_scores_low(self, matcher):
        """Post with only a short title and empty body should score low."""
        post = {
            "id": "post_short_title",
            "subreddit": "aurora4x",
            "author": "MemeUser",
            "title": "Every time",
            "selftext": "",
            "permalink": "/r/aurora4x/comments/xyz/every_time/",
            "created_utc": 1708000000,
        }
        for issue in matcher.issues:
            score = matcher.score_match(post, issue)
            assert score < 60, (
                f"Short title-only post should not reach medium confidence "
                f"for issue #{issue['number']}, got {score}"
            )

    def test_empty_body_image_post_scores_low(self, matcher):
        """Image post with no selftext should score low."""
        post = {
            "id": "post_image",
            "subreddit": "aurora4x",
            "author": "ImagePoster",
            "title": "Check out my fleet",
            "selftext": "",
            "permalink": "/r/aurora4x/comments/xyz/fleet/",
            "created_utc": 1708000000,
            "url": "https://i.redd.it/abc123.png",
        }
        for issue in matcher.issues:
            score = matcher.score_match(post, issue)
            assert score < 60, (
                f"Image-only post should not reach medium confidence "
                f"for issue #{issue['number']}, got {score}"
            )

    def test_single_word_post_scores_low(self, matcher):
        """Post with a single common word should not match."""
        post = {
            "id": "post_single_word",
            "subreddit": "aurora4x",
            "author": "OneWordUser",
            "title": "Performance",
            "selftext": "",
            "permalink": "/r/aurora4x/comments/xyz/performance/",
            "created_utc": 1708000000,
        }
        for issue in matcher.issues:
            score = matcher.score_match(post, issue)
            assert score < 60, (
                f"Single-word post should not reach medium confidence "
                f"for issue #{issue['number']}, got {score}"
            )

    def test_substantive_post_unaffected(self, matcher, posts):
        """Posts with sufficient text should score normally (no penalty)."""
        # The high-match post has 300+ chars
        post = posts[0]  # box launcher test post
        issue = matcher.issues[2]  # issue 1230 - box launcher reload
        score = matcher.score_match(post, issue)
        assert score >= 80, (
            f"Substantive post should still score high, got {score}"
        )

    def test_penalty_scales_with_length(self, matcher):
        """Shorter posts should get proportionally more penalty."""
        issue = matcher.issues[5]  # fuel consumption issue

        short_post = {
            "id": "p1", "subreddit": "aurora4x", "author": "User",
            "title": "fuel", "selftext": "",
            "permalink": "/r/aurora4x/comments/a/b/", "created_utc": 1708000000,
        }
        medium_post = {
            "id": "p2", "subreddit": "aurora4x", "author": "User",
            "title": "fuel consumption question about speed",
            "selftext": "",
            "permalink": "/r/aurora4x/comments/a/b/", "created_utc": 1708000000,
        }

        short_score = matcher.score_match(short_post, issue)
        medium_score = matcher.score_match(medium_post, issue)
        assert short_score < medium_score, (
            f"Shorter post ({short_score}) should score lower than "
            f"medium-length post ({medium_score})"
        )


class TestLongIssuePenalty:
    """Test that issues with very long bodies are penalized to prevent false positives."""

    LONG_ISSUE_BODY = (
        "Verify: Section 12.2 beam weapons damage calculations. "
        "Claim 1: beam fire control tracks targets. "
        "Claim 2: gauss cannon damage scales with calibre. "
        "Claim 3: railgun penetration uses armor column formula. "
        "Claim 4: laser damage reduces with range. "
        "Claim 5: meson weapons ignore armor and shields. "
        "Claim 6: microwave weapons cause electronic damage. "
        "Claim 7: particle beams have shorter range than lasers. "
        "Claim 8: plasma weapons have area effect damage. "
        "Claim 9: turrets allow tracking of faster targets. "
        "Claim 10: point defense mode reduces beam range. "
        "Claim 11: CIWS combines gauss cannon and fire control. "
        "Claim 12: ECM reduces fire control accuracy. "
        "Claim 13: ECCM counters ECM effects. "
        "Claim 14: shield regeneration rate depends on technology. "
        "Claim 15: armor depth affects damage penetration. "
        "Additional unverified claims about combat resolution order, "
        "missile interception mechanics, and sensor detection thresholds."
    )

    GENERIC_POST = {
        "id": "post_generic",
        "subreddit": "aurora4x",
        "author": "NewPlayer",
        "title": "Aurora combat question",
        "selftext": (
            "I just started playing Aurora and I'm trying to understand "
            "how combat works. My ships keep getting destroyed."
        ),
        "permalink": "/r/aurora4x/comments/xyz/combat/",
        "created_utc": 1708000000,
    }

    SPECIFIC_POST = {
        "id": "post_specific",
        "subreddit": "aurora4x",
        "author": "Tester",
        "title": "Tested: beam fire control tracking speed formula",
        "selftext": (
            "I tested beam fire control tracking speed and confirmed "
            "the formula in the database. BFC tracking speed is "
            "calculated from the fire control speed rating. "
            "Fire control accuracy drops with ECM."
        ),
        "permalink": "/r/aurora4x/comments/xyz/bfc_test/",
        "created_utc": 1708000000,
    }

    def _make_long_issue(self, body_multiplier=1):
        return {
            "number": 9999,
            "title": "Verify beam weapon claims",
            "body": self.LONG_ISSUE_BODY * body_multiplier,
        }

    def test_long_issue_penalizes_generic_match(self, config):
        """Generic Aurora post should score <40 against a long issue."""
        m = Matcher(config)
        issue = self._make_long_issue()
        score = m.score_match(self.GENERIC_POST, issue)
        assert score < 40, (
            f"Generic post should score <40 against long issue, got {score}"
        )

    def test_long_issue_specific_match_still_scores(self, config):
        """Specific post with keyword matches should still reach triage."""
        config_with_keywords = {
            "matching": {
                **config["matching"],
                "keywords": {
                    **config["matching"]["keywords"],
                    "high": config["matching"]["keywords"]["high"]
                    + ["beam fire control", "tracking speed"],
                },
            },
        }
        m = Matcher(config_with_keywords)
        issue = self._make_long_issue()
        score = m.score_match(self.SPECIFIC_POST, issue)
        assert score >= 40, (
            f"Specific post should still reach triage (>=40), got {score}"
        )

    def test_penalty_scales_with_issue_length(self, config):
        """Longer issues should produce lower scores for the same post."""
        m = Matcher(config)
        issue_1x = self._make_long_issue(body_multiplier=1)
        issue_3x = self._make_long_issue(body_multiplier=3)
        score_1x = m.score_match(self.GENERIC_POST, issue_1x)
        score_3x = m.score_match(self.GENERIC_POST, issue_3x)
        assert score_3x < score_1x, (
            f"3x longer issue ({score_3x}) should score lower than "
            f"1x issue ({score_1x}) for the same post"
        )

    def test_normal_issue_unaffected(self, matcher, posts):
        """Fixture issues (under 500 chars) should score the same as before."""
        post = posts[0]  # box launcher post
        issue = matcher.issues[2]  # issue 1230 - box launcher reload
        score = matcher.score_match(post, issue)
        assert score >= 80, (
            f"Normal-length issue should still score high, got {score}"
        )

    def test_penalty_disabled_when_exponent_zero(self, config):
        """Setting long_issue_exponent=0 should disable the penalty."""
        config_disabled = {
            "matching": {
                **config["matching"],
                "long_issue_exponent": 0,
            },
        }
        m_disabled = Matcher(config_disabled)
        m_enabled = Matcher(config)
        issue = self._make_long_issue()
        score_disabled = m_disabled.score_match(self.GENERIC_POST, issue)
        score_enabled = m_enabled.score_match(self.GENERIC_POST, issue)
        assert score_disabled >= score_enabled, (
            f"Disabled penalty ({score_disabled}) should score >= "
            f"enabled penalty ({score_enabled})"
        )
