#!/bin/bash
#
# Install git hooks for aurora-manual development
#

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
HOOKS_SRC="$SCRIPT_DIR/hooks"
HOOKS_DST="$REPO_ROOT/.git/hooks"

echo "Installing git hooks..."

for hook in "$HOOKS_SRC"/*; do
    if [ -f "$hook" ]; then
        hook_name=$(basename "$hook")
        cp "$hook" "$HOOKS_DST/$hook_name"
        chmod +x "$HOOKS_DST/$hook_name"
        echo "  Installed: $hook_name"
    fi
done

echo "Done."
