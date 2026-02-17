"""Tests for the new content detection module."""

import json
import os
import pytest

from aurora_monitor.new_content import NewContentDetector

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")


@pytest.fixture
def posts():
    with open(os.path.join(FIXTURES_DIR, "new_content_posts.json")) as f:
        return json.load(f)


@pytest.fixture
def config():
    """Minimal config matching config.yaml new_content structure."""
    return {
        "matching": {
            "known_authors": {
                "SteveWalmsley": {"bonus": 30, "note": "Aurora developer"},
            },
            "keywords": {
                "aurora_terms": [
                    "aurora", "trans-newtonian", "duranium", "PDC", "CIWS",
                    "NPR", "jump gate", "lagrange point",
                ],
            },
        },
        "new_content": {
            "min_score": 40,
            "max_issues_backfill": 5,
            "max_issues_steady": 1,
            "labels": ["content-opportunity"],
            "evidence_keywords": [
                "formula", "tested", "confirmed", "verified",
                "i tested", "i confirmed", "i verified", "calculated",
                "measured", "data shows",
            ],
            "chapter_keywords": {
                8: {
                    "name": "Ship Design",
                    "keywords": ["ship design", "class design", "engine", "armor",
                                 "shield", "magazine", "hangar", "component",
                                 "hull", "tonnage", "crew quarters", "engineering"],
                },
                9: {
                    "name": "Fleet Management",
                    "keywords": ["fleet", "task group", "standing order",
                                 "fleet order", "waypoint", "formation"],
                },
                11: {
                    "name": "Sensors and Detection",
                    "keywords": ["sensor", "detection", "thermal", "EM",
                                 "active sensor", "passive sensor", "resolution",
                                 "cross section", "signature"],
                },
                12: {
                    "name": "Combat",
                    "keywords": ["combat", "weapon", "missile", "beam", "laser",
                                 "railgun", "gauss", "fire control", "point defense",
                                 "CIWS", "armor", "damage", "warhead", "turret",
                                 "ECM", "ECCM"],
                },
                14: {
                    "name": "Logistics",
                    "keywords": ["logistics", "fuel", "maintenance", "supply",
                                 "ordnance", "overhaul", "MSP", "tanker",
                                 "collier", "supply ship", "refueling"],
                },
            },
        },
    }


@pytest.fixture
def detector(config):
    return NewContentDetector(config)


class TestNewContentScoring:
    """Test scoring of posts for new content value."""

    def test_evidence_keywords_boost(self, detector, posts):
        """Posts with evidence keywords ('tested', 'confirmed', etc.) score higher."""
        evidence_post = posts[0]  # nc_evidence_rich
        generic_post = posts[1]   # nc_generic_aar
        evidence_score = detector.score_new_content(evidence_post)
        generic_score = detector.score_new_content(generic_post)
        assert evidence_score["score"] > generic_score["score"], (
            f"Evidence-rich post ({evidence_score['score']}) should outscore "
            f"generic AAR ({generic_score['score']})"
        )

    def test_known_author_bonus(self, detector, posts):
        """Posts by known authors get a score bonus."""
        dev_post = posts[2]  # nc_known_author (SteveWalmsley)
        result = detector.score_new_content(dev_post)
        # Re-score with unknown author
        unknown_post = {**dev_post, "author": "RandomUser"}
        unknown_result = detector.score_new_content(unknown_post)
        assert result["score"] > unknown_result["score"], (
            f"Known author ({result['score']}) should outscore "
            f"unknown ({unknown_result['score']})"
        )

    def test_keyword_density_bonus(self, detector):
        """Posts with high Aurora keyword density score higher."""
        dense_post = {
            "id": "dense", "subreddit": "aurora4x", "author": "User",
            "title": "Aurora PDC CIWS test",
            "selftext": "Testing aurora PDC and CIWS against NPR duranium armor with jump gate transit.",
            "permalink": "/r/aurora4x/comments/dense/test/",
            "created_utc": 1708000000,
        }
        sparse_post = {
            "id": "sparse", "subreddit": "aurora4x", "author": "User",
            "title": "General game discussion about strategy",
            "selftext": "I was thinking about how to play this game better with different approaches.",
            "permalink": "/r/aurora4x/comments/sparse/test/",
            "created_utc": 1708000000,
        }
        dense_result = detector.score_new_content(dense_post)
        sparse_result = detector.score_new_content(sparse_post)
        assert dense_result["score"] > sparse_result["score"], (
            f"Dense aurora-term post ({dense_result['score']}) should outscore "
            f"sparse post ({sparse_result['score']})"
        )

    def test_question_penalty(self, detector, posts):
        """Posts phrased as questions get a penalty."""
        question_post = posts[3]  # nc_question_post
        evidence_post = posts[0]  # nc_evidence_rich
        q_result = detector.score_new_content(question_post)
        e_result = detector.score_new_content(evidence_post)
        assert q_result["score"] < e_result["score"], (
            f"Question post ({q_result['score']}) should score lower than "
            f"evidence post ({e_result['score']})"
        )

    def test_text_length_bonus(self, detector, posts):
        """Longer posts get a length bonus."""
        long_post = posts[0]  # nc_evidence_rich (~500+ chars)
        short_post = posts[6]  # nc_short_empty
        long_result = detector.score_new_content(long_post)
        short_result = detector.score_new_content(short_post)
        assert long_result["score"] > short_result["score"], (
            f"Long post ({long_result['score']}) should outscore "
            f"short/empty ({short_result['score']})"
        )

    def test_cross_ref_bonus(self, detector, posts):
        """Posts with forum cross-references get a bonus."""
        forum_post = posts[4]  # nc_forum_crossref
        result = detector.score_new_content(forum_post)
        # Forum link should add +10
        assert result["score"] >= 10, (
            f"Forum cross-ref post should score >= 10, got {result['score']}"
        )

    def test_score_cap_at_100(self, detector):
        """Score should be capped at 100."""
        # Construct a post that would exceed 100
        super_post = {
            "id": "super", "subreddit": "aurora4x",
            "author": "SteveWalmsley",
            "title": "I tested formula confirmed verified measured calculated",
            "selftext": (
                "I tested and confirmed the formula for missile warhead damage. "
                "I verified the data shows the formula is correct. "
                "I calculated the measured values. Tested again with different ships. "
                "See https://aurora2.pentarch.org/index.php?topic=12345.0 for details. "
                "Also https://www.youtube.com/watch?v=test for video proof. "
                "The combat damage laser beam missile warhead fire control sensor "
                "armor shield engine fuel maintenance are all verified."
            ),
            "permalink": "/r/aurora4x/comments/super/test/",
            "created_utc": 1708000000,
        }
        result = detector.score_new_content(super_post)
        assert result["score"] <= 100, f"Score should cap at 100, got {result['score']}"

    def test_empty_post_scores_low(self, detector, posts):
        """Empty/minimal posts score very low."""
        empty_post = posts[6]  # nc_short_empty
        result = detector.score_new_content(empty_post)
        assert result["score"] < 20, f"Empty post should score < 20, got {result['score']}"


class TestChapterMapping:
    """Test mapping posts to manual chapters via keywords."""

    def test_combat_maps_to_chapter_12(self, detector, posts):
        """Post about missile/warhead/damage maps to Chapter 12 (Combat)."""
        evidence_post = posts[0]  # mentions missile, laser, warhead, damage
        chapters = detector.map_to_chapters(evidence_post)
        chapter_nums = [ch[0] for ch in chapters]
        assert 12 in chapter_nums, f"Expected Chapter 12 in {chapter_nums}"

    def test_logistics_maps_to_chapter_14(self, detector, posts):
        """Post about ordnance/collier maps to Chapter 14 (Logistics)."""
        logistics_post = posts[2]  # nc_known_author - ordnance transfer, collier
        chapters = detector.map_to_chapters(logistics_post)
        chapter_nums = [ch[0] for ch in chapters]
        assert 14 in chapter_nums, f"Expected Chapter 14 in {chapter_nums}"

    def test_multi_chapter_mapping(self, detector, posts):
        """Post spanning topics maps to multiple chapters."""
        multi_post = posts[7]  # nc_multi_chapter - combat + sensors + fleet
        chapters = detector.map_to_chapters(multi_post)
        chapter_nums = [ch[0] for ch in chapters]
        assert len(chapter_nums) >= 2, f"Expected 2+ chapters, got {chapter_nums}"

    def test_generic_post_maps_to_none(self, detector, posts):
        """Generic AAR with no specific mechanics maps to no chapters."""
        generic_post = posts[1]  # nc_generic_aar
        chapters = detector.map_to_chapters(generic_post)
        assert len(chapters) == 0, f"Generic AAR should not map to chapters, got {chapters}"

    def test_min_two_keywords_required(self, detector):
        """A single keyword match is not enough for chapter mapping."""
        post = {
            "id": "single_kw", "subreddit": "aurora4x",
            "author": "User",
            "title": "Something about armor",
            "selftext": "Just a quick mention of armor.",
            "permalink": "/r/aurora4x/comments/skw/test/",
            "created_utc": 1708000000,
        }
        chapters = detector.map_to_chapters(post)
        # "armor" appears in chapter 8 and 12, but only once per chapter
        # Need >=2 keywords from a single chapter to match
        assert len(chapters) == 0, f"Single keyword should not match, got {chapters}"

    def test_results_sorted_by_confidence(self, detector, posts):
        """Chapter matches should be sorted by confidence descending."""
        multi_post = posts[7]  # nc_multi_chapter
        chapters = detector.map_to_chapters(multi_post)
        if len(chapters) >= 2:
            confidences = [ch[2] for ch in chapters]
            assert confidences == sorted(confidences, reverse=True), (
                f"Chapters should be sorted by confidence descending: {confidences}"
            )


class TestAssessUnmatched:
    """Test the main entry point for assessing unmatched posts."""

    def _make_match_result(self, post_id, routing, issue=None, score=0):
        return {
            "post_id": post_id,
            "routing": routing,
            "issue": issue,
            "score": score,
        }

    def test_filters_to_unmatched_only(self, detector, posts):
        """assess_unmatched only processes posts routed as ignore or unmatched triage."""
        match_results = [
            self._make_match_result("nc_evidence_rich", "ignore"),
            self._make_match_result("nc_generic_aar", "auto_comment", issue=100),
            self._make_match_result("nc_question_post", "ignore"),
        ]
        posts_by_id = {p["id"]: p for p in posts}
        opportunities = detector.assess_unmatched(match_results, posts_by_id)
        opp_ids = [o["post_id"] for o in opportunities]
        assert "nc_generic_aar" not in opp_ids, "auto_comment posts should be excluded"

    def test_sorted_by_score_descending(self, detector, posts):
        """Results should be sorted by score descending."""
        match_results = [
            self._make_match_result(p["id"], "ignore") for p in posts
        ]
        posts_by_id = {p["id"]: p for p in posts}
        opportunities = detector.assess_unmatched(match_results, posts_by_id)
        if len(opportunities) >= 2:
            scores = [o["score"] for o in opportunities]
            assert scores == sorted(scores, reverse=True), (
                f"Should be sorted by score descending: {scores}"
            )

    def test_opportunities_have_required_fields(self, detector, posts):
        """Each opportunity dict has required fields."""
        match_results = [
            self._make_match_result("nc_evidence_rich", "ignore"),
        ]
        posts_by_id = {p["id"]: p for p in posts}
        opportunities = detector.assess_unmatched(match_results, posts_by_id)
        if opportunities:
            opp = opportunities[0]
            required = ["post_id", "score", "chapters", "title", "author",
                        "permalink", "signals"]
            for field in required:
                assert field in opp, f"Missing required field: {field}"

    def test_skips_matched_posts(self, detector, posts):
        """Posts with auto_comment routing are skipped entirely."""
        match_results = [
            self._make_match_result("nc_evidence_rich", "auto_comment", issue=100, score=85),
        ]
        posts_by_id = {p["id"]: p for p in posts}
        opportunities = detector.assess_unmatched(match_results, posts_by_id)
        assert len(opportunities) == 0 or all(
            o["post_id"] != "nc_evidence_rich" for o in opportunities
        )

    def test_empty_input(self, detector):
        """Empty inputs return empty list."""
        opportunities = detector.assess_unmatched([], {})
        assert opportunities == []


class TestIssueFormatting:
    """Test issue title and body formatting."""

    def test_title_format(self, detector, posts):
        """Title follows 'New content: [Section N] description' format."""
        opportunity = {
            "post_id": "nc_evidence_rich",
            "score": 75,
            "chapters": [(12, "Combat", 0.8)],
            "title": "I tested missile laser warhead mechanics extensively",
            "author": "MechanicsTester",
            "permalink": "/r/aurora4x/comments/nc001/missile_laser_warhead/",
            "signals": ["evidence: tested, confirmed, verified"],
        }
        title = detector.format_issue_title(opportunity)
        assert title.startswith("New content:"), f"Title should start with 'New content:': {title}"
        assert "[Section 12]" in title, f"Title should contain chapter: {title}"

    def test_title_truncation(self, detector):
        """Titles exceeding 128 chars are truncated."""
        opportunity = {
            "post_id": "long",
            "score": 50,
            "chapters": [(12, "Combat", 0.8)],
            "title": "A" * 200,
            "author": "User",
            "permalink": "/r/aurora4x/comments/long/test/",
            "signals": [],
        }
        title = detector.format_issue_title(opportunity)
        assert len(title) <= 128, f"Title should be <=128 chars, got {len(title)}"

    def test_title_no_chapters(self, detector):
        """Title without chapters uses 'General' instead of section number."""
        opportunity = {
            "post_id": "gen",
            "score": 50,
            "chapters": [],
            "title": "Some mechanics discussion",
            "author": "User",
            "permalink": "/r/aurora4x/comments/gen/test/",
            "signals": [],
        }
        title = detector.format_issue_title(opportunity)
        assert "New content:" in title

    def test_body_contains_link(self, detector):
        """Issue body contains the Reddit permalink."""
        opportunity = {
            "post_id": "nc001",
            "score": 75,
            "chapters": [(12, "Combat", 0.8)],
            "title": "Missile mechanics test",
            "author": "MechanicsTester",
            "permalink": "/r/aurora4x/comments/nc001/missile_laser_warhead/",
            "signals": ["evidence: tested"],
            "quote": "I tested the missile laser warhead formula in detail.",
            "subreddit": "aurora4x",
            "created_utc": 1708000000,
        }
        body = detector.format_issue_body(opportunity)
        assert "reddit.com" in body, "Body should contain Reddit link"
        assert "nc001" in body, "Body should reference the post"

    def test_body_contains_chapter_and_signals(self, detector):
        """Issue body includes suggested chapter and detected signals."""
        opportunity = {
            "post_id": "nc001",
            "score": 75,
            "chapters": [(12, "Combat", 0.8)],
            "title": "Missile mechanics test",
            "author": "MechanicsTester",
            "permalink": "/r/aurora4x/comments/nc001/missile_laser_warhead/",
            "signals": ["evidence: tested"],
            "quote": "I tested something",
            "subreddit": "aurora4x",
            "created_utc": 1708000000,
        }
        body = detector.format_issue_body(opportunity)
        assert "Combat" in body, "Body should mention suggested chapter"
        assert "evidence" in body.lower() or "signal" in body.lower(), (
            "Body should mention detected signals"
        )
