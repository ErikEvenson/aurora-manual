#!/usr/bin/env python3
"""Add section art to x.y markdown files."""

import re
from pathlib import Path

def add_section_art(md_path: Path):
    """Add section art image after the Updated line in a section file."""
    content = md_path.read_text()

    # Check if art already added
    if 'section-art' in content:
        print(f"  Skipping {md_path} - art already present")
        return False

    # Extract section number from filename (e.g., 1.1, 12.3)
    match = re.match(r'(\d+\.\d+)', md_path.stem)
    if not match:
        print(f"  Warning: Cannot extract section number from {md_path}")
        return False

    section_id = match.group(1)
    art_file = f'{section_id}.png'
    art_path = Path(f'images/art/section-art/{art_file}')

    # Check if art file exists
    if not art_path.exists():
        print(f"  Warning: Art file not found: {art_path}")
        return False

    # Extract section title from the heading
    heading_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if not heading_match:
        print(f"  Warning: No heading found in {md_path}")
        return False

    section_title = heading_match.group(1)

    # Find the FIRST Updated line (after top-level heading) and insert after it
    # Use count=1 to only replace the first occurrence, not subsection Updated lines
    updated_pattern = r'(\*Updated: v[\d.]+\*\n)'

    if re.search(updated_pattern, content):
        # Insert image after FIRST Updated line only (count=1 prevents duplicates)
        image_md = f'\n![{section_title}](../images/art/section-art/{art_file})\n'
        new_content = re.sub(updated_pattern, r'\1' + image_md, content, count=1)
        md_path.write_text(new_content)
        print(f"  Added art to {md_path}")
        return True
    else:
        # Try inserting after heading if no Updated line
        heading_pattern = r'(^# .+\n)'
        if re.search(heading_pattern, content, re.MULTILINE):
            image_md = f'\n![{section_title}](../images/art/section-art/{art_file})\n'
            new_content = re.sub(heading_pattern, r'\1' + image_md, content, count=1, flags=re.MULTILINE)
            md_path.write_text(new_content)
            print(f"  Added art to {md_path} (after heading)")
            return True

    print(f"  Warning: Could not find insertion point in {md_path}")
    return False


def main():
    """Add section art to all x.y section files."""
    base_path = Path('.')
    added_count = 0
    skipped_count = 0

    # Find all section files (x.y-*.md pattern)
    for chapter_dir in sorted(base_path.glob('[0-9]*-*/')):
        for md_file in sorted(chapter_dir.glob('[0-9]*.[0-9]-*.md')):
            if md_file.name == 'index.md':
                continue

            print(f"Processing {md_file}...")
            if add_section_art(md_file):
                added_count += 1
            else:
                skipped_count += 1

    print(f"\nDone. Added: {added_count}, Skipped: {skipped_count}")


if __name__ == '__main__':
    main()
