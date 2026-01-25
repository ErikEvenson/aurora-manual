#!/usr/bin/env python3
"""
Generate tech tree SVG files from Aurora database.
Usage: python3 generate-tech-trees.py
"""

import sqlite3
import subprocess
import os
import re
from pathlib import Path

DB_PATH = os.path.expanduser("~/Downloads/Aurora271Full/AuroraDB.db")
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "tech-trees"

# Color scheme
COLORS = {
    'conventional': '#d4edda',  # Green - starting techs
    'early': '#cce5ff',         # Blue - early TN techs
    'mid': '#fff3cd',           # Yellow - mid game
    'late': '#d4c4fb',          # Purple - late game
    'endgame': '#f8d7da',       # Pink - endgame
    'external': '#f0f0f0',      # Gray - external prerequisites
}

def sanitize_name(name):
    """Convert tech name to valid DOT node ID."""
    return re.sub(r'[^a-zA-Z0-9]', '_', name)[:30]

def get_color(cost):
    """Assign color based on research cost."""
    if cost <= 500:
        return COLORS['conventional']
    elif cost <= 10000:
        return COLORS['early']
    elif cost <= 100000:
        return COLORS['mid']
    elif cost <= 1000000:
        return COLORS['late']
    else:
        return COLORS['endgame']

def format_cost(cost):
    """Format cost with commas."""
    if cost >= 1000000:
        return f"{cost/1000000:.1f}M"
    elif cost >= 1000:
        return f"{cost/1000:.0f}K"
    return str(cost)

def generate_dot(category, techs, all_techs):
    """Generate DOT file content for a tech category.

    Returns tuple of (dot_content, external_prereqs_list).
    External prerequisites are NOT shown as nodes - they're returned for text listing.
    """
    tech_count = len(techs)
    # Use horizontal layout for small trees (<=6 techs), vertical for larger
    rankdir = 'LR' if tech_count <= 6 else 'TB'

    lines = [
        'digraph TechTree {',
        f'    rankdir={rankdir};',
        '    node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=10];',
        '    edge [arrowsize=0.7];',
        f'    label="{category}";',
        '    labelloc="t";',
        '    fontsize=14;',
        '    fontname="Helvetica-Bold";',
        '    nodesep=0.3;',
        '    ranksep=0.4;',
        '',
    ]

    # Track external prerequisites (for text output, not as nodes)
    external_prereqs = []
    tech_ids = {t[0] for t in techs}

    # Define nodes
    for tech in techs:
        tech_id, name, prereq1, prereq2, cost = tech
        node_id = sanitize_name(name)
        color = get_color(cost)
        label = f"{name}\\n{format_cost(cost)} RP"
        lines.append(f'    {node_id} [label="{label}", fillcolor="{color}"];')

        # Track external prerequisites for text listing
        if prereq1 and prereq1 not in tech_ids and prereq1 in all_techs:
            external_prereqs.append((name, all_techs[prereq1]))
        if prereq2 and prereq2 not in tech_ids and prereq2 in all_techs:
            external_prereqs.append((name, all_techs[prereq2]))

    # Define edges (only internal prerequisites - no external nodes)
    lines.append('')
    lines.append('    // Prerequisites (internal only)')
    for tech in techs:
        tech_id, name, prereq1, prereq2, cost = tech
        node_id = sanitize_name(name)

        if prereq1 and prereq1 in tech_ids:
            prereq_name = next(t[1] for t in techs if t[0] == prereq1)
            prereq_node = sanitize_name(prereq_name)
            lines.append(f'    {prereq_node} -> {node_id};')

        if prereq2 and prereq2 in tech_ids:
            prereq_name = next(t[1] for t in techs if t[0] == prereq2)
            prereq_node = sanitize_name(prereq_name)
            lines.append(f'    {prereq_node} -> {node_id};')

    lines.append('}')
    return '\n'.join(lines), external_prereqs

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Get all techs for prerequisite lookup
    cursor.execute("""
        SELECT TechSystemID, Name FROM FCT_TechSystem WHERE RaceID = 0
    """)
    all_techs = {row[0]: row[1] for row in cursor.fetchall()}

    # Get all categories
    cursor.execute("""
        SELECT DISTINCT tt.Description
        FROM FCT_TechSystem t
        LEFT JOIN DIM_TechType tt ON t.TechTypeID = tt.TechTypeID
        WHERE t.RaceID = 0 AND tt.Description IS NOT NULL
        ORDER BY tt.Description
    """)
    categories = [row[0] for row in cursor.fetchall()]

    # Also write external prereqs data for the appendix generator
    prereqs_data = {}

    generated = 0
    for category in categories:
        # Get techs for this category
        cursor.execute("""
            SELECT t.TechSystemID, t.Name, t.Prerequisite1, t.Prerequisite2, t.DevelopCost
            FROM FCT_TechSystem t
            LEFT JOIN DIM_TechType tt ON t.TechTypeID = tt.TechTypeID
            WHERE t.RaceID = 0 AND tt.Description = ?
            ORDER BY t.DevelopCost
        """, (category,))
        techs = cursor.fetchall()

        if not techs:
            continue

        # Generate DOT (now returns external prereqs too)
        dot_content, external_prereqs = generate_dot(category, techs, all_techs)

        # Create safe filename
        safe_name = re.sub(r'[^a-zA-Z0-9\-]', '-', category.lower())
        safe_name = re.sub(r'-+', '-', safe_name).strip('-')

        # Store external prereqs for this category
        if external_prereqs:
            prereqs_data[safe_name] = external_prereqs

        dot_path = f"/tmp/{safe_name}.dot"
        svg_path = OUTPUT_DIR / f"{safe_name}.svg"

        # Write DOT file
        with open(dot_path, 'w') as f:
            f.write(dot_content)

        # Generate SVG
        try:
            subprocess.run(['dot', '-Tsvg', dot_path, '-o', str(svg_path)], check=True)
            generated += 1
            print(f"Generated: {safe_name}.svg ({len(techs)} techs)")
        except subprocess.CalledProcessError as e:
            print(f"Error generating {safe_name}: {e}")

    # Write external prerequisites data as JSON for appendix generator
    import json
    prereqs_file = OUTPUT_DIR / "external-prereqs.json"
    with open(prereqs_file, 'w') as f:
        json.dump(prereqs_data, f, indent=2)
    print(f"Wrote external prerequisites to {prereqs_file}")

    conn.close()
    print(f"\nTotal: {generated} tech tree SVGs generated in {OUTPUT_DIR}")

if __name__ == '__main__':
    main()
