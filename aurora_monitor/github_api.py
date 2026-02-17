"""GitHub API integration for posting issue comments and discussions.

Uses the `gh` CLI for issue operations and GraphQL for discussions.
"""

import json
import re
import subprocess


MAX_COMMENT_LENGTH = 10000
MAX_DISCUSSION_COMMENT_LENGTH = 65000
REPO = "ErikEvenson/aurora-manual"


def _sanitize(text, max_length=MAX_COMMENT_LENGTH):
    """Sanitize text for safe GitHub markdown posting."""
    if not text:
        return ""
    # Strip potential HTML/script injection
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    # Escape backtick sequences that could break markdown
    text = text.replace('```', '\\`\\`\\`')
    # Truncate to max length
    if len(text) > max_length:
        text = text[:max_length - 50] + "\n\n*[Truncated — exceeds character limit]*"
    return text


def post_issue_comment(issue_number, body, repo=REPO, dry_run=False):
    """Post a comment on a GitHub issue via `gh`."""
    body = _sanitize(body)
    if dry_run:
        print(f"[DRY RUN] Would comment on issue #{issue_number}:")
        print(body[:200])
        return True
    result = subprocess.run(
        ["gh", "issue", "comment", str(issue_number),
         "--repo", repo, "--body", body],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"Error commenting on issue #{issue_number}: {result.stderr}")
        return False
    return True


def check_existing_comment(issue_number, reddit_id, repo=REPO):
    """Check if a comment referencing this Reddit ID already exists on the issue."""
    result = subprocess.run(
        ["gh", "api", f"repos/{repo}/issues/{issue_number}/comments",
         "--jq", f'[.[] | select(.body | contains("{reddit_id}"))] | length'],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return False
    try:
        return int(result.stdout.strip()) > 0
    except ValueError:
        return False


def post_discussion(title, body, category_id, repo=REPO, dry_run=False):
    """Post a GitHub Discussion via GraphQL mutation.

    Returns (success: bool, discussion_node_id: str|None).
    """
    title = _sanitize(title, max_length=256)
    body = _sanitize(body, max_length=MAX_DISCUSSION_COMMENT_LENGTH)

    if dry_run:
        print(f"[DRY RUN] Would post discussion: {title}")
        print(body[:200])
        return (True, None)

    # Get repository ID
    repo_id_result = subprocess.run(
        ["gh", "api", "graphql", "-f", f'query=query {{ repository(owner: "{repo.split("/")[0]}", name: "{repo.split("/")[1]}") {{ id }} }}'],
        capture_output=True, text=True,
    )
    if repo_id_result.returncode != 0:
        print(f"Error getting repo ID: {repo_id_result.stderr}")
        return (False, None)

    repo_data = json.loads(repo_id_result.stdout)
    repo_id = repo_data["data"]["repository"]["id"]

    # Escape body for GraphQL JSON
    escaped_body = json.dumps(body)[1:-1]  # Remove outer quotes from json.dumps
    escaped_title = json.dumps(title)[1:-1]

    mutation = f'''mutation {{
        createDiscussion(input: {{
            repositoryId: "{repo_id}",
            categoryId: "{category_id}",
            title: "{escaped_title}",
            body: "{escaped_body}"
        }}) {{
            discussion {{ id url }}
        }}
    }}'''

    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={mutation}"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"Error posting discussion: {result.stderr}")
        return (False, None)

    data = json.loads(result.stdout)
    discussion = data.get("data", {}).get("createDiscussion", {}).get("discussion", {})
    url = discussion.get("url", "")
    node_id = discussion.get("id")
    if url:
        print(f"Posted discussion: {url}")
    return (True, node_id)


def create_issue(title, body, labels, repo=REPO, dry_run=False):
    """Create a GitHub issue via `gh issue create`.

    Returns (success: bool, issue_number: int|None).
    """
    title = _sanitize(title, max_length=256)
    body = _sanitize(body, max_length=MAX_COMMENT_LENGTH)

    if dry_run:
        print(f"[DRY RUN] Would create issue: {title}")
        print(body[:200])
        return (True, None)

    cmd = ["gh", "issue", "create", "--repo", repo, "--title", title, "--body", body]
    for label in labels:
        cmd.extend(["--label", label])

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error creating issue: {result.stderr}")
        return (False, None)

    # gh issue create prints the URL, extract issue number
    url = result.stdout.strip()
    match = re.search(r'/issues/(\d+)', url)
    if match:
        return (True, int(match.group(1)))
    return (True, None)


def search_issues(query, labels, repo=REPO):
    """Search for existing issues via `gh issue list --search`.

    Returns list of issue dicts with 'number' and 'title'.
    """
    cmd = [
        "gh", "issue", "list", "--repo", repo,
        "--search", query,
        "--json", "number,title",
        "--limit", "20",
    ]
    for label in labels:
        cmd.extend(["--label", label])

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Warning: Issue search failed: {result.stderr}")
        return []

    try:
        return json.loads(result.stdout)
    except (json.JSONDecodeError, ValueError):
        return []


def post_discussion_comment(discussion_id, body, repo=REPO, dry_run=False):
    """Post a comment on a GitHub Discussion via GraphQL mutation."""
    body = _sanitize(body, max_length=MAX_DISCUSSION_COMMENT_LENGTH)

    if dry_run:
        print(f"[DRY RUN] Would comment on discussion {discussion_id}:")
        print(body[:200])
        return True

    escaped_body = json.dumps(body)[1:-1]

    mutation = f'''mutation {{
        addDiscussionComment(input: {{
            discussionId: "{discussion_id}",
            body: "{escaped_body}"
        }}) {{
            comment {{ id }}
        }}
    }}'''

    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={mutation}"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"Error commenting on discussion: {result.stderr}")
        return False

    return True
