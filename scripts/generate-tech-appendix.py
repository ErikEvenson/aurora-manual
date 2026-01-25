#!/usr/bin/env python3
"""
Generate the tech trees appendix markdown file.
Usage: python3 generate-tech-appendix.py > appendices/E-tech-trees.md

SVG files are referenced for GitHub viewing. The build script converts
these to PDF references for LaTeX compatibility.
"""

import sqlite3
import os
import re
import json
from pathlib import Path

DB_PATH = os.path.expanduser("~/Downloads/Aurora271Full/AuroraDB.db")
PREREQS_FILE = Path(__file__).parent.parent / "images" / "tech-trees" / "external-prereqs.json"

FIELD_NAMES = {
    1: 'Power and Propulsion',
    2: 'Sensors and Fire Control',
    3: 'Energy Weapons',
    4: 'Missiles and Kinetics',
    5: 'Defensive Systems',
    6: 'Logistics and Construction',
    7: 'Ground Forces',
    8: 'Biology and Genetics',
}

def safe_filename(category):
    """Convert category name to safe filename."""
    safe_name = re.sub(r'[^a-zA-Z0-9\-]', '-', category.lower())
    return re.sub(r'-+', '-', safe_name).strip('-')

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Load external prerequisites data if available
    prereqs_data = {}
    if PREREQS_FILE.exists():
        with open(PREREQS_FILE) as f:
            prereqs_data = json.load(f)

    # Get categories organized by field
    cursor.execute("""
        SELECT
            tt.FieldID,
            tt.Description as Category,
            COUNT(*) as TechCount
        FROM FCT_TechSystem t
        LEFT JOIN DIM_TechType tt ON t.TechTypeID = tt.TechTypeID
        WHERE t.RaceID = 0 AND tt.Description IS NOT NULL
        GROUP BY tt.FieldID, tt.Description
        ORDER BY tt.FieldID, tt.Description
    """)

    categories = cursor.fetchall()
    conn.close()

    # Generate markdown
    print("# Appendix E: Technology Trees")
    print()
    print("*Added: v2026.01.25*")
    print()
    print("This appendix provides visual technology tree diagrams for all research categories in Aurora C#.")
    print("Technologies are color-coded by research cost:")
    print()
    print("| Color | Cost Range | Game Phase |")
    print("|-------|------------|------------|")
    print("| Green | 0-500 RP | Conventional/Starting |")
    print("| Blue | 500-10K RP | Early Trans-Newtonian |")
    print("| Yellow | 10K-100K RP | Mid Game |")
    print("| Purple | 100K-1M RP | Late Game |")
    print("| Pink | 1M+ RP | Endgame |")
    print()
    print("External prerequisites (technologies from other categories) are listed below each diagram.")
    print()

    current_field = None

    for field_id, category, tech_count in categories:
        field_name = FIELD_NAMES.get(field_id, 'Other')

        # New field section
        if field_name != current_field:
            current_field = field_name
            print(f"## E.{field_id} {field_name}")
            print()

        # Category subsection
        filename = safe_filename(category)
        print(f"### {category}")
        print()
        print(f"*{tech_count} technologies*")
        print()
        # Reference SVG for GitHub viewing (build script converts to PDF for LaTeX)
        print(f"![{category}](images/tech-trees/{filename}.svg)")
        print()

        # List external prerequisites as text if any
        if filename in prereqs_data:
            prereqs = prereqs_data[filename]
            # Group by tech that needs the prereq
            print("> **External Prerequisites:**")
            for tech_name, prereq_name in prereqs:
                print(f"> - {tech_name} requires *{prereq_name}*")
            print()

if __name__ == '__main__':
    main()
