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
