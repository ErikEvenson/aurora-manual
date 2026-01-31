#!/usr/bin/env python3
"""
Update section dates in markdown files based on git history.

For each section (## heading), finds the last commit that modified that section
and injects/updates an "*Updated: YYYY.MM.DD*" line after the heading.

Usage:
    ./scripts/update-section-dates.py [--dry-run] [file ...]

If no files specified, processes all markdown files in the manual.
"""

import subprocess
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime


# Pattern to match section headings (# or ## with optional numbering)
HEADING_PATTERN = re.compile(r'^(#{1,2})\s+(\d+\.[\d.]*\s+)?(.+)$')

# Pattern to match existing Added/Updated lines
DATE_LINE_PATTERN = re.compile(r'^\*(Added|Updated|Last verified):\s*v?[\d.]+\*\s*$')

# Sections to skip (boilerplate, not content)
SKIP_HEADINGS = {'Related Sections', 'References', 'UI References'}

# Front matter pattern
FRONT_MATTER_PATTERN = re.compile(r'^---\s*$')


def get_manual_files():
    """Get all markdown files that are part of the manual."""
    root = Path(__file__).parent.parent

    # Directories containing manual content
    content_dirs = [
        '1-introduction', '2-game-setup', '3-user-interface',
        '4-systems-and-bodies', '5-colonies', '6-economy-and-industry',
        '7-research', '8-ship-design', '9-fleet-management',
        '10-navigation', '11-sensors-and-detection', '12-combat',
        '13-ground-forces', '14-logistics', '15-diplomacy',
        '16-commanders', '17-exploration', '18-advanced-topics',
        'appendices', 'examples'
    ]

    files = []
    for dir_name in content_dirs:
        dir_path = root / dir_name
        if dir_path.exists():
            files.extend(dir_path.glob('*.md'))

    return sorted(files)


def get_section_last_modified(filepath: Path, start_line: int, end_line: int) -> str | None:
    """
    Get the last modification date for a line range using git log -L.

    Returns date as YYYY.MM.DD or None if not in git/no history.
    """
    try:
        # git log -L uses 1-based line numbers
        cmd = [
            'git', 'log', '-1', '--format=%cs',
            f'-L{start_line},{end_line}:{filepath}'
        ]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=filepath.parent.parent,
            timeout=10
        )

        if result.returncode == 0 and result.stdout.strip():
            # Convert YYYY-MM-DD to YYYY.MM.DD
            date_str = result.stdout.strip().split('\n')[0]
            return date_str.replace('-', '.')

    except (subprocess.TimeoutExpired, Exception) as e:
        print(f"  Warning: git log failed for {filepath}:{start_line}-{end_line}: {e}",
              file=sys.stderr)

    return None


def find_sections(lines: list[str]) -> list[dict]:
    """
    Find all sections in the file and their line ranges.

    Returns list of dicts with:
        - heading_line: 0-based line index of the heading
        - start_line: 1-based line number for git (heading line)
        - end_line: 1-based line number for git (last line of section)
        - level: heading level (1 or 2)
        - has_date_line: whether next non-empty line is a date line
        - date_line_idx: 0-based index of existing date line (or None)
    """
    sections = []
    in_front_matter = False
    front_matter_count = 0
    in_code_block = False

    for i, line in enumerate(lines):
        # Track code blocks (``` markers)
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        # Track front matter
        if FRONT_MATTER_PATTERN.match(line):
            front_matter_count += 1
            if front_matter_count == 1:
                in_front_matter = True
            elif front_matter_count == 2:
                in_front_matter = False
            continue

        if in_front_matter:
            continue

        # Check for heading
        match = HEADING_PATTERN.match(line)
        if match:
            level = len(match.group(1))
            heading_text = match.group(3).strip()

            # Skip boilerplate sections
            if heading_text in SKIP_HEADINGS:
                continue

            # Look for existing date line (next non-empty line)
            date_line_idx = None
            has_date_line = False
            for j in range(i + 1, min(i + 3, len(lines))):
                if lines[j].strip() == '':
                    continue
                if DATE_LINE_PATTERN.match(lines[j]):
                    has_date_line = True
                    date_line_idx = j
                break

            sections.append({
                'heading_line': i,
                'start_line': i + 1,  # 1-based for git
                'level': level,
                'has_date_line': has_date_line,
                'date_line_idx': date_line_idx,
            })

    # Calculate end lines (each section ends where the next same-or-higher level starts)
    for i, section in enumerate(sections):
        end_line = len(lines)  # Default to end of file

        for j in range(i + 1, len(sections)):
            if sections[j]['level'] <= section['level']:
                end_line = sections[j]['start_line'] - 1
                break

        section['end_line'] = end_line

    return sections


def update_file(filepath: Path, dry_run: bool = False) -> tuple[int, int]:
    """
    Update section dates in a file.

    Returns (sections_found, sections_updated).
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Preserve original line endings
    original_content = ''.join(lines)

    sections = find_sections(lines)

    if not sections:
        return 0, 0

    updates = []  # (line_idx, action, new_line)

    for section in sections:
        # Skip top-level file headings (# X.Y Title) - only update subsections
        # Actually, let's update all numbered sections

        date = get_section_last_modified(
            filepath,
            section['start_line'],
            section['end_line']
        )

        if not date:
            continue

        new_date_line = f'*Updated: v{date}*\n'

        if section['has_date_line']:
            # Replace existing date line - ensure blank line after
            date_idx = section['date_line_idx']
            old_line = lines[date_idx]

            # Check if there's a blank line after the date line
            next_idx = date_idx + 1
            has_blank_after = (next_idx < len(lines) and
                               lines[next_idx].strip() == '')

            if old_line.strip() != new_date_line.strip() or not has_blank_after:
                if has_blank_after:
                    updates.append((date_idx, 'replace', new_date_line))
                else:
                    # Add blank line after date
                    updates.append((date_idx, 'replace', new_date_line + '\n'))
        else:
            # Insert new date line after heading
            insert_idx = section['heading_line'] + 1

            # Check if there's already a blank line after heading
            has_blank_after = (insert_idx < len(lines) and
                               lines[insert_idx].strip() == '')

            if has_blank_after:
                # Replace the blank line with: blank + date + blank
                updates.append((insert_idx, 'replace', f'\n{new_date_line}\n'))
            else:
                # Insert: blank + date + blank before content
                updates.append((insert_idx, 'insert', f'\n{new_date_line}\n'))

    if not updates:
        return len(sections), 0

    # Apply updates in reverse order to preserve line indices
    updates.sort(key=lambda x: x[0], reverse=True)

    for line_idx, action, new_line in updates:
        if action == 'replace':
            lines[line_idx] = new_line
        elif action == 'insert':
            lines.insert(line_idx, new_line)

    new_content = ''.join(lines)

    if new_content != original_content:
        if dry_run:
            print(f"  Would update {len(updates)} section(s)")
        else:
            with open(filepath, 'w') as f:
                f.write(new_content)
        return len(sections), len(updates)

    return len(sections), 0


def main():
    parser = argparse.ArgumentParser(description='Update section dates from git history')
    parser.add_argument('files', nargs='*', help='Files to process (default: all manual files)')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='Show what would be changed without modifying files')
    args = parser.parse_args()

    if args.files:
        files = [Path(f) for f in args.files]
    else:
        files = get_manual_files()

    total_sections = 0
    total_updated = 0
    files_modified = 0

    for filepath in files:
        if not filepath.exists():
            print(f"Warning: {filepath} not found", file=sys.stderr)
            continue

        print(f"Processing {filepath.name}...")
        sections, updated = update_file(filepath, args.dry_run)
        total_sections += sections
        total_updated += updated
        if updated > 0:
            files_modified += 1

    action = "Would update" if args.dry_run else "Updated"
    print(f"\n{action} {total_updated} sections across {files_modified} files")
    print(f"Total sections scanned: {total_sections}")


if __name__ == '__main__':
    main()
