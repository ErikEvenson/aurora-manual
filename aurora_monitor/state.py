"""State management for community source monitors.

Handles load/save/dedup of seen post and comment IDs.
State is persisted as JSON files in the aurora_monitor/state/ directory.
"""

import json
import os


DEFAULT_STATE = {
    "backfill_complete": False,
    "seen_posts": {},
    "seen_comments": {},
    "last_run": None,
}


def load_state(path):
    """Load state from a JSON file. Returns default state if file doesn't exist."""
    if not os.path.exists(path):
        return {**DEFAULT_STATE, "seen_posts": {}, "seen_comments": {}}
    with open(path) as f:
        return json.load(f)


def save_state(path, state):
    """Save state to a JSON file, creating directories as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(state, f, indent=2)


def is_seen(state, item_id, kind="post"):
    """Check if a post or comment ID has already been processed."""
    key = "seen_posts" if kind == "post" else "seen_comments"
    return item_id in state[key]


def mark_seen(state, item_id, kind="post", timestamp=None):
    """Mark a post or comment ID as processed."""
    key = "seen_posts" if kind == "post" else "seen_comments"
    state[key][item_id] = timestamp
