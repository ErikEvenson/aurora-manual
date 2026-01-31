#!/usr/bin/env python3
"""Add chapter art to index.md files."""

import re
from pathlib import Path

# Mapping of chapter directories to art files
CHAPTER_ART = {
    '1-introduction': '01-introduction.png',
    '2-game-setup': '02-game-setup.png',
    '3-user-interface': '03-user-interface.png',
    '4-systems-and-bodies': '04-systems-bodies.png',
    '5-colonies': '05-colonies.png',
    '6-economy-and-industry': '06-economy.png',
    '7-research': '07-research.png',
    '8-ship-design': '08-ship-design.png',
    '9-fleet-management': '09-fleet-management.png',
    '10-navigation': '10-navigation.png',
    '11-sensors-and-detection': '11-sensors.png',
    '12-combat': '12-combat.png',
    '13-ground-forces': '13-ground-forces.png',
    '14-logistics': '14-logistics.png',
    '15-diplomacy': '15-diplomacy.png',
    '16-commanders': '16-commanders.png',
    '17-exploration': '17-exploration.png',
    '18-advanced-topics': '18-advanced.png',
    'appendices': 'appendices.png',
}

def add_chapter_art(index_path: Path, art_file: str):
    """Add chapter art image after the Updated line."""
    content = index_path.read_text()

    # Check if art already added
    if 'chapter-art' in content:
        print(f"  Skipping {index_path} - art already present")
        return

    # Extract chapter name from the heading
    heading_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if not heading_match:
        print(f"  Warning: No heading found in {index_path}")
        return

    chapter_name = heading_match.group(1)

    # Find the Updated line and insert after it
    updated_pattern = r'(\*Updated: v[\d.]+\*\n)'

    if re.search(updated_pattern, content):
        # Insert image after Updated line
        image_md = f'\n![{chapter_name}](../images/art/chapter-art/{art_file})\n'
        new_content = re.sub(updated_pattern, r'\1' + image_md, content)
        index_path.write_text(new_content)
        print(f"  Added art to {index_path}")
    else:
        print(f"  Warning: No Updated line in {index_path}")


def main():
    base_path = Path('.')

    for chapter_dir, art_file in CHAPTER_ART.items():
        index_path = base_path / chapter_dir / 'index.md'

        if index_path.exists():
            print(f"Processing {chapter_dir}...")
            add_chapter_art(index_path, art_file)
        else:
            print(f"  Warning: {index_path} not found")


if __name__ == '__main__':
    main()
