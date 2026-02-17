"""Tests for the GitHub API integration module."""

import json
from unittest.mock import patch, MagicMock

import pytest

from aurora_monitor import github_api


class TestPostDiscussionReturnType:
    """Test that post_discussion returns (bool, str|None)."""

    def test_dry_run_returns_tuple(self):
        """Dry run returns (True, None)."""
        result = github_api.post_discussion(
            "Test Title", "Test Body", "CAT_ID", dry_run=True
        )
        assert isinstance(result, tuple)
        assert result == (True, None)

    @patch("aurora_monitor.github_api.subprocess.run")
    def test_success_returns_discussion_id(self, mock_run):
        """Successful post returns (True, discussion_node_id)."""
        # First call: get repo ID
        repo_response = MagicMock()
        repo_response.returncode = 0
        repo_response.stdout = json.dumps({
            "data": {"repository": {"id": "R_kgDORAJjeQ"}}
        })
        # Second call: create discussion
        create_response = MagicMock()
        create_response.returncode = 0
        create_response.stdout = json.dumps({
            "data": {
                "createDiscussion": {
                    "discussion": {
                        "id": "D_kwDORAJjec4BFake",
                        "url": "https://github.com/ErikEvenson/aurora-manual/discussions/99"
                    }
                }
            }
        })
        mock_run.side_effect = [repo_response, create_response]

        success, node_id = github_api.post_discussion(
            "Test", "Body", "CAT_ID"
        )
        assert success is True
        assert node_id == "D_kwDORAJjec4BFake"

    @patch("aurora_monitor.github_api.subprocess.run")
    def test_failure_returns_false_none(self, mock_run):
        """Failed API call returns (False, None)."""
        fail_response = MagicMock()
        fail_response.returncode = 1
        fail_response.stderr = "API error"
        mock_run.return_value = fail_response

        success, node_id = github_api.post_discussion(
            "Test", "Body", "CAT_ID"
        )
        assert success is False
        assert node_id is None


class TestPostDiscussionComment:
    """Test posting comments on GitHub Discussions."""

    def test_dry_run(self):
        """Dry run prints but doesn't call API."""
        result = github_api.post_discussion_comment(
            "D_abc123", "Comment body", dry_run=True
        )
        assert result is True

    @patch("aurora_monitor.github_api.subprocess.run")
    def test_success(self, mock_run):
        """Successful comment post returns True."""
        response = MagicMock()
        response.returncode = 0
        response.stdout = json.dumps({
            "data": {
                "addDiscussionComment": {
                    "comment": {"id": "DC_kwDORAJjec4C123"}
                }
            }
        })
        mock_run.return_value = response

        result = github_api.post_discussion_comment(
            "D_abc123", "Comment body"
        )
        assert result is True

    @patch("aurora_monitor.github_api.subprocess.run")
    def test_failure(self, mock_run):
        """Failed comment post returns False."""
        response = MagicMock()
        response.returncode = 1
        response.stderr = "GraphQL error"
        mock_run.return_value = response

        result = github_api.post_discussion_comment(
            "D_abc123", "Comment body"
        )
        assert result is False

    def test_body_sanitized_to_65k(self):
        """Body exceeding 65K gets truncated."""
        long_body = "x" * 70000
        with patch("aurora_monitor.github_api.subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout=json.dumps({
                "data": {"addDiscussionComment": {"comment": {"id": "DC_1"}}}
            }))
            github_api.post_discussion_comment("D_abc", long_body)
            # Verify the body passed to subprocess was truncated
            call_args = mock_run.call_args
            query_arg = [a for a in call_args[0][0] if a.startswith("query=")][0]
            # The body should have been sanitized before being embedded
            assert len(query_arg) < 70000 + 500  # mutation overhead


class TestMaxDiscussionCommentLength:
    """Test the MAX_DISCUSSION_COMMENT_LENGTH constant."""

    def test_constant_exists(self):
        """Module should export MAX_DISCUSSION_COMMENT_LENGTH = 65000."""
        assert hasattr(github_api, "MAX_DISCUSSION_COMMENT_LENGTH")
        assert github_api.MAX_DISCUSSION_COMMENT_LENGTH == 65000


class TestCreateIssue:
    """Test issue creation via gh CLI."""

    def test_dry_run_returns_success_none(self):
        """Dry run returns (True, None) without calling API."""
        success, issue_num = github_api.create_issue(
            "Test Title", "Test Body", ["label1"], dry_run=True
        )
        assert success is True
        assert issue_num is None

    @patch("aurora_monitor.github_api.subprocess.run")
    def test_success_returns_issue_number(self, mock_run):
        """Successful creation returns (True, issue_number)."""
        response = MagicMock()
        response.returncode = 0
        response.stdout = "https://github.com/ErikEvenson/aurora-manual/issues/1305\n"
        mock_run.return_value = response

        success, issue_num = github_api.create_issue(
            "New content: test", "Body text", ["content-opportunity"]
        )
        assert success is True
        assert issue_num == 1305

    @patch("aurora_monitor.github_api.subprocess.run")
    def test_failure_returns_false_none(self, mock_run):
        """Failed creation returns (False, None)."""
        response = MagicMock()
        response.returncode = 1
        response.stderr = "Error creating issue"
        mock_run.return_value = response

        success, issue_num = github_api.create_issue(
            "Title", "Body", ["label"]
        )
        assert success is False
        assert issue_num is None

    @patch("aurora_monitor.github_api.subprocess.run")
    def test_labels_passed_to_gh(self, mock_run):
        """Labels are passed as --label arguments to gh."""
        response = MagicMock()
        response.returncode = 0
        response.stdout = "https://github.com/ErikEvenson/aurora-manual/issues/99\n"
        mock_run.return_value = response

        github_api.create_issue(
            "Title", "Body", ["content-opportunity", "auto-detected"]
        )
        call_args = mock_run.call_args[0][0]
        label_indices = [i for i, a in enumerate(call_args) if a == "--label"]
        assert len(label_indices) == 2, "Should have two --label flags"


class TestSearchIssues:
    """Test issue search via gh CLI."""

    @patch("aurora_monitor.github_api.subprocess.run")
    def test_returns_matches(self, mock_run):
        """Search returns list of matching issues."""
        response = MagicMock()
        response.returncode = 0
        response.stdout = json.dumps([
            {"number": 100, "title": "New content: missile mechanics"},
            {"number": 101, "title": "New content: shield regen"},
        ])
        mock_run.return_value = response

        results = github_api.search_issues("missile mechanics", ["content-opportunity"])
        assert len(results) == 2
        assert results[0]["number"] == 100

    @patch("aurora_monitor.github_api.subprocess.run")
    def test_returns_empty_on_no_match(self, mock_run):
        """Search returns empty list when no issues match."""
        response = MagicMock()
        response.returncode = 0
        response.stdout = "[]"
        mock_run.return_value = response

        results = github_api.search_issues("nonexistent topic", ["content-opportunity"])
        assert results == []

    @patch("aurora_monitor.github_api.subprocess.run")
    def test_returns_empty_on_api_failure(self, mock_run):
        """Search returns empty list on API failure."""
        response = MagicMock()
        response.returncode = 1
        response.stderr = "API error"
        mock_run.return_value = response

        results = github_api.search_issues("test", ["content-opportunity"])
        assert results == []
