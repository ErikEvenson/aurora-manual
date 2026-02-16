"""Tests for the state management module."""

import json
import os
import tempfile
import pytest

from aurora_monitor.state import load_state, save_state, is_seen, mark_seen


class TestLoadState:
    """Test state loading."""

    def test_load_existing_state(self, tmp_path):
        """Should load state from an existing JSON file."""
        state_file = tmp_path / "reddit.json"
        state_data = {
            "backfill_complete": True,
            "seen_posts": {"abc123": 1708000000},
            "seen_comments": {"comment1": 1708050000},
            "last_run": "2026-02-16T07:00:00Z",
        }
        state_file.write_text(json.dumps(state_data))

        state = load_state(str(state_file))
        assert state["backfill_complete"] is True
        assert "abc123" in state["seen_posts"]
        assert state["last_run"] == "2026-02-16T07:00:00Z"

    def test_load_missing_file_creates_default(self, tmp_path):
        """Should return default state if file doesn't exist."""
        state_file = tmp_path / "nonexistent.json"
        state = load_state(str(state_file))
        assert state["backfill_complete"] is False
        assert state["seen_posts"] == {}
        assert state["seen_comments"] == {}
        assert state["last_run"] is None


class TestSaveState:
    """Test state persistence."""

    def test_save_state(self, tmp_path):
        """Should write state as JSON."""
        state_file = tmp_path / "reddit.json"
        state = {
            "backfill_complete": True,
            "seen_posts": {"abc123": 1708000000},
            "seen_comments": {},
            "last_run": "2026-02-16T07:00:00Z",
        }
        save_state(str(state_file), state)

        loaded = json.loads(state_file.read_text())
        assert loaded == state

    def test_save_creates_directory(self, tmp_path):
        """Should create parent directories if needed."""
        state_file = tmp_path / "nested" / "dir" / "reddit.json"
        state = {"backfill_complete": False, "seen_posts": {}, "seen_comments": {}, "last_run": None}
        save_state(str(state_file), state)
        assert state_file.exists()


class TestDedup:
    """Test deduplication checking."""

    def test_is_seen_post(self):
        """Should detect already-seen posts."""
        state = {"seen_posts": {"abc123": 1708000000}, "seen_comments": {}}
        assert is_seen(state, "abc123", kind="post") is True
        assert is_seen(state, "xyz789", kind="post") is False

    def test_is_seen_comment(self):
        """Should detect already-seen comments."""
        state = {"seen_posts": {}, "seen_comments": {"comment1": 1708050000}}
        assert is_seen(state, "comment1", kind="comment") is True
        assert is_seen(state, "comment99", kind="comment") is False

    def test_mark_seen_post(self):
        """Should add post ID to seen set."""
        state = {"seen_posts": {}, "seen_comments": {}}
        mark_seen(state, "new_post", kind="post", timestamp=1708000000)
        assert "new_post" in state["seen_posts"]
        assert state["seen_posts"]["new_post"] == 1708000000

    def test_mark_seen_comment(self):
        """Should add comment ID to seen set."""
        state = {"seen_posts": {}, "seen_comments": {}}
        mark_seen(state, "new_comment", kind="comment", timestamp=1708050000)
        assert "new_comment" in state["seen_comments"]


class TestBackfillSafety:
    """Test backfill safety check."""

    def test_backfill_not_complete_blocks_steady_state(self):
        """State with backfill_complete=False should be detectable."""
        state = load_state("/nonexistent/path.json")
        assert state["backfill_complete"] is False
