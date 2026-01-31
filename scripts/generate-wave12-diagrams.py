#!/usr/bin/env python3
"""
Generate Wave 12: Commander & Exploration Diagrams for Aurora Manual
Creates matplotlib visualizations at 150 DPI with dark theme
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
from matplotlib.lines import Line2D
import numpy as np
import os

# Dark theme colors
COLORS = {
    'bg': '#1a1a2e',
    'teal': '#4ecdc4',
    'red': '#ff6b6b',
    'yellow': '#ffe66d',
    'green': '#95d5b2',
    'white': '#ffffff',
    'gray': '#2d2d44',
    'light_gray': '#4a4a6a'
}

def setup_dark_theme(fig, ax):
    """Apply dark theme to figure and axes"""
    fig.patch.set_facecolor(COLORS['bg'])
    ax.set_facecolor(COLORS['bg'])
    ax.tick_params(colors=COLORS['white'])
    for spine in ax.spines.values():
        spine.set_color(COLORS['teal'])

def save_diagram(fig, filename):
    """Save diagram with standard settings"""
    output_dir = os.path.dirname(filename)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    fig.savefig(filename, dpi=150, facecolor=COLORS['bg'],
                edgecolor='none', bbox_inches='tight', pad_inches=0.2)
    plt.close(fig)
    print(f"Saved: {filename}")


def create_commander_bonus_stacking(output_path):
    """Issue #1133: Commander Bonus Stacking Hierarchy Diagram"""
    fig, ax = plt.subplots(figsize=(12, 9))
    setup_dark_theme(fig, ax)

    # Title
    ax.set_title('Commander Bonus Stacking Hierarchy',
                 color=COLORS['white'], fontsize=16, fontweight='bold', pad=20)

    # Define hierarchy levels
    levels = [
        ('Fleet Commander', 'Fleet-wide bonuses\n(Reaction Rating)', COLORS['yellow'], 0.9),
        ('Task Group Commander', 'Fleet Tactics bonus\nFormation control', COLORS['teal'], 0.7),
        ('Ship Commander', 'Personal skill bonuses\n(50% for Crew Training,\nSurvey, Engineering, Tactical)', COLORS['green'], 0.5),
        ('Specialist Officers', 'Full bonus in specialty\n(XO, Science, CAG, Engineer, Tactical)', COLORS['red'], 0.3),
    ]

    # Draw hierarchy boxes
    box_width = 0.35
    box_height = 0.12

    for i, (title, desc, color, y) in enumerate(levels):
        # Main box
        box = FancyBboxPatch((0.32, y - box_height/2), box_width, box_height,
                              boxstyle="round,pad=0.02", facecolor=COLORS['gray'],
                              edgecolor=color, linewidth=2)
        ax.add_patch(box)

        # Title text
        ax.text(0.5, y + 0.02, title, ha='center', va='center',
               fontsize=11, fontweight='bold', color=color)

        # Description text
        ax.text(0.5, y - 0.03, desc, ha='center', va='center',
               fontsize=8, color=COLORS['white'])

        # Connecting arrow
        if i < len(levels) - 1:
            ax.annotate('', xy=(0.5, levels[i+1][3] + box_height/2 + 0.01),
                       xytext=(0.5, y - box_height/2 - 0.01),
                       arrowprops=dict(arrowstyle='->', color=COLORS['teal'], lw=1.5))

    # Stacking rules panel
    rules_box = FancyBboxPatch((0.72, 0.25), 0.25, 0.55,
                                boxstyle="round,pad=0.02", facecolor=COLORS['gray'],
                                edgecolor=COLORS['teal'], linewidth=2, linestyle='--')
    ax.add_patch(rules_box)

    ax.text(0.845, 0.77, 'Stacking Rules', ha='center', va='center',
           fontsize=10, fontweight='bold', color=COLORS['yellow'])

    rules = [
        ('Additive:', 'Most bonuses stack\nup to cap limits'),
        ('Cap:', '150% maximum for\nmost bonus types'),
        ('Scope:', 'Fleet > TG > Ship\nhierarchy applies'),
        ('XO Bonus:', 'Full Crew Training\n(Commander = 50%)'),
    ]

    for i, (rule_title, rule_desc) in enumerate(rules):
        y_pos = 0.68 - i * 0.12
        ax.text(0.74, y_pos, rule_title, ha='left', va='center',
               fontsize=9, fontweight='bold', color=COLORS['teal'])
        ax.text(0.74, y_pos - 0.04, rule_desc, ha='left', va='center',
               fontsize=8, color=COLORS['white'])

    # Example calculation box
    example_box = FancyBboxPatch((0.02, 0.02), 0.28, 0.22,
                                  boxstyle="round,pad=0.02", facecolor=COLORS['gray'],
                                  edgecolor=COLORS['green'], linewidth=2)
    ax.add_patch(example_box)

    ax.text(0.16, 0.21, 'Example: Crew Training', ha='center', va='center',
           fontsize=9, fontweight='bold', color=COLORS['green'])
    ax.text(0.04, 0.16, 'Captain: 20% x 0.5 = 10%', ha='left', fontsize=8, color=COLORS['white'])
    ax.text(0.04, 0.12, 'XO: 25% x 1.0 = 25%', ha='left', fontsize=8, color=COLORS['white'])
    ax.text(0.04, 0.08, 'Total: 35% training bonus', ha='left', fontsize=8, color=COLORS['yellow'])
    ax.text(0.04, 0.04, '(Points/Year = Combined %)', ha='left', fontsize=7, color=COLORS['light_gray'])

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    save_diagram(fig, output_path)


def create_auto_assignment_priority(output_path):
    """Issue #1143: Auto-Assignment Priority Flow Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    setup_dark_theme(fig, ax)

    ax.set_title('Naval Commander Auto-Assignment Priority Flow',
                 color=COLORS['white'], fontsize=16, fontweight='bold', pad=20)

    # Flow diagram nodes
    nodes = [
        (0.15, 0.88, 'Start: Ship Needs\nCommander', 'rect', COLORS['yellow']),
        (0.15, 0.72, 'Sort Ships by:\n1. Commander Priority\n2. Primary Assignment\n3. Size (descending)', 'rect', COLORS['teal']),
        (0.15, 0.54, 'Check Ship Type', 'diamond', COLORS['green']),
        (0.50, 0.72, 'Required Bonus\nLookup Table', 'rect', COLORS['gray']),
        (0.15, 0.36, 'Find Unassigned\nOfficer with\nRequired Bonus', 'rect', COLORS['teal']),
        (0.15, 0.18, 'Officer Found?', 'diamond', COLORS['red']),
        (0.40, 0.18, 'Assign Officer\nto Ship', 'rect', COLORS['green']),
        (0.65, 0.18, 'Next Ship', 'rect', COLORS['yellow']),
        (0.15, 0.04, 'Supplementary Passes\n(Reaction > Engineering > Tactical)', 'rect', COLORS['light_gray']),
    ]

    # Draw nodes
    for x, y, label, shape, color in nodes:
        if shape == 'rect':
            box = FancyBboxPatch((x - 0.12, y - 0.06), 0.24, 0.12,
                                  boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                                  edgecolor=color, linewidth=2)
            ax.add_patch(box)
        elif shape == 'diamond':
            diamond = plt.Polygon([(x, y + 0.07), (x + 0.1, y), (x, y - 0.07), (x - 0.1, y)],
                                  facecolor=COLORS['gray'], edgecolor=color, linewidth=2)
            ax.add_patch(diamond)

        ax.text(x, y, label, ha='center', va='center',
               fontsize=8, color=COLORS['white'], wrap=True)

    # Priority table
    table_x, table_y = 0.75, 0.72
    ax.text(table_x, table_y + 0.16, 'Ship Type Priority Table', ha='center',
           fontsize=10, fontweight='bold', color=COLORS['yellow'])

    priorities = [
        ('1', 'Survey Ships', 'Survey'),
        ('2', 'Protected Vessels', 'Crew Training'),
        ('3', 'Military Ships', 'Crew Training'),
        ('4', 'Construction Ships', 'Production'),
        ('5', 'Terraformers', 'Terraforming'),
        ('6', 'Harvesters', 'Mining'),
        ('7', 'Asteroid Miners', 'Mining'),
        ('8', 'Salvagers', 'Production'),
        ('9', 'All Others', 'Logistics'),
    ]

    # Table header
    header_y = table_y + 0.10
    ax.text(table_x - 0.15, header_y, 'Pri', ha='center', fontsize=8, fontweight='bold', color=COLORS['teal'])
    ax.text(table_x - 0.02, header_y, 'Ship Type', ha='center', fontsize=8, fontweight='bold', color=COLORS['teal'])
    ax.text(table_x + 0.13, header_y, 'Required Bonus', ha='center', fontsize=8, fontweight='bold', color=COLORS['teal'])

    for i, (pri, ship_type, bonus) in enumerate(priorities):
        row_y = header_y - 0.04 - i * 0.035
        ax.text(table_x - 0.15, row_y, pri, ha='center', fontsize=7, color=COLORS['white'])
        ax.text(table_x - 0.02, row_y, ship_type, ha='center', fontsize=7, color=COLORS['white'])
        ax.text(table_x + 0.13, row_y, bonus, ha='center', fontsize=7, color=COLORS['green'])

    # Draw table border
    table_box = FancyBboxPatch((table_x - 0.22, table_y - 0.22), 0.44, 0.50,
                                boxstyle="round,pad=0.01", facecolor='none',
                                edgecolor=COLORS['teal'], linewidth=1.5, linestyle='--')
    ax.add_patch(table_box)

    # Arrows
    arrows = [
        ((0.15, 0.82), (0.15, 0.78)),  # Start to Sort
        ((0.15, 0.66), (0.15, 0.61)),  # Sort to Check
        ((0.25, 0.54), (0.38, 0.72)),  # Check to Table (curved)
        ((0.15, 0.47), (0.15, 0.42)),  # Check to Find
        ((0.15, 0.30), (0.15, 0.25)),  # Find to Found?
        ((0.25, 0.18), (0.28, 0.18)),  # Yes arrow
        ((0.52, 0.18), (0.53, 0.18)),  # Assign to Next
        ((0.15, 0.11), (0.15, 0.10)),  # No arrow
    ]

    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color=COLORS['teal'], lw=1.5))

    # Yes/No labels
    ax.text(0.22, 0.21, 'Yes', fontsize=8, color=COLORS['green'])
    ax.text(0.12, 0.10, 'No', fontsize=8, color=COLORS['red'])

    # Secondary officer positions box
    secondary_box = FancyBboxPatch((0.50, 0.02), 0.45, 0.12,
                                    boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                                    edgecolor=COLORS['light_gray'], linewidth=1.5)
    ax.add_patch(secondary_box)
    ax.text(0.725, 0.11, 'Secondary Positions (after Ship Commanders)', ha='center',
           fontsize=8, fontweight='bold', color=COLORS['white'])
    ax.text(0.725, 0.05, 'XO (Aux Control) | Science Officer | CAG | Chief Engineer | Tactical Officer',
           ha='center', fontsize=7, color=COLORS['light_gray'])

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    save_diagram(fig, output_path)


def create_governor_strategy_matrix(output_path):
    """Issue #1147: Governor Strategy Matrix Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    setup_dark_theme(fig, ax)

    ax.set_title('Governor Strategy Matrix: Colony Type vs Development Phase',
                 color=COLORS['white'], fontsize=16, fontweight='bold', pad=20)

    # Colony types (rows) and phases (columns)
    colony_types = ['Industrial Hub', 'Mining Colony', 'Population Center',
                    'Research Hub', 'Homeworld', 'Logistics Base']
    phases = ['Early (Establishing)', 'Growth (Expanding)', 'Mature (Optimizing)']

    # Matrix data: [1st priority, 2nd priority, 3rd priority]
    matrix_data = {
        'Industrial Hub': {
            'Early': ('Production', 'Pop Growth', 'Mining'),
            'Growth': ('Production', 'Wealth', 'Pop Growth'),
            'Mature': ('Production', 'Wealth', 'Logistics'),
        },
        'Mining Colony': {
            'Early': ('Mining', 'Pop Growth', 'Production'),
            'Growth': ('Mining', 'Production', 'Logistics'),
            'Mature': ('Mining', 'Logistics', 'Production'),
        },
        'Population Center': {
            'Early': ('Pop Growth', 'Production', 'Wealth'),
            'Growth': ('Pop Growth', 'Wealth', 'Production'),
            'Mature': ('Wealth', 'Pop Growth', 'Production'),
        },
        'Research Hub': {
            'Early': ('Research Admin', 'Pop Growth', 'Production'),
            'Growth': ('Research Admin', 'Production', 'Pop Growth'),
            'Mature': ('Research Admin', 'Wealth', 'Production'),
        },
        'Homeworld': {
            'Early': ('Production', 'Mining', 'Pop Growth'),
            'Growth': ('Production', 'Research Admin', 'Mining'),
            'Mature': ('Production', 'Wealth', 'Logistics'),
        },
        'Logistics Base': {
            'Early': ('Logistics', 'Production', 'Mining'),
            'Growth': ('Logistics', 'Production', 'Mining'),
            'Mature': ('Logistics', 'Wealth', 'Production'),
        },
    }

    # Draw matrix grid
    cell_width = 0.22
    cell_height = 0.11
    start_x = 0.22
    start_y = 0.78

    # Color coding for priorities
    priority_colors = {
        'Production': COLORS['green'],
        'Mining': COLORS['yellow'],
        'Pop Growth': COLORS['teal'],
        'Wealth': COLORS['red'],
        'Research Admin': '#9b59b6',  # Purple
        'Logistics': '#3498db',  # Blue
    }

    # Draw column headers
    for j, phase in enumerate(phases):
        x = start_x + j * cell_width + cell_width/2
        ax.text(x, start_y + 0.06, phase, ha='center', va='center',
               fontsize=9, fontweight='bold', color=COLORS['teal'])

    # Draw row headers and cells
    for i, colony_type in enumerate(colony_types):
        y = start_y - i * cell_height

        # Row header
        ax.text(start_x - 0.02, y - cell_height/2, colony_type, ha='right', va='center',
               fontsize=9, fontweight='bold', color=COLORS['yellow'])

        for j, phase in enumerate(phases):
            x = start_x + j * cell_width
            phase_key = phase.split()[0]

            priorities = matrix_data[colony_type][phase_key]

            # Cell background
            cell = FancyBboxPatch((x + 0.005, y - cell_height + 0.005),
                                   cell_width - 0.01, cell_height - 0.01,
                                   boxstyle="round,pad=0.005", facecolor=COLORS['gray'],
                                   edgecolor=COLORS['light_gray'], linewidth=1)
            ax.add_patch(cell)

            # Priority text
            for k, pri in enumerate(priorities):
                pri_y = y - 0.02 - k * 0.03
                color = priority_colors.get(pri, COLORS['white'])
                marker = ['1.', '2.', '3.'][k]
                ax.text(x + 0.01, pri_y, f"{marker}", ha='left', va='center',
                       fontsize=7, color=COLORS['white'])
                ax.text(x + 0.035, pri_y, pri, ha='left', va='center',
                       fontsize=7, color=color)

    # Legend
    legend_x = 0.02
    legend_y = 0.25
    ax.text(legend_x, legend_y + 0.05, 'Priority Bonus Types:', ha='left',
           fontsize=10, fontweight='bold', color=COLORS['white'])

    for i, (bonus, color) in enumerate(priority_colors.items()):
        row = i // 2
        col = i % 2
        lx = legend_x + col * 0.15
        ly = legend_y - row * 0.04
        ax.add_patch(Rectangle((lx, ly - 0.01), 0.02, 0.02, facecolor=color))
        ax.text(lx + 0.03, ly, bonus, ha='left', va='center', fontsize=8, color=COLORS['white'])

    # Tips box
    tips_box = FancyBboxPatch((0.55, 0.02), 0.43, 0.20,
                               boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                               edgecolor=COLORS['green'], linewidth=2)
    ax.add_patch(tips_box)

    ax.text(0.765, 0.19, 'Governor Assignment Tips', ha='center',
           fontsize=10, fontweight='bold', color=COLORS['green'])
    tips = [
        '- Homeworld governor is CRITICAL early game',
        '- Set High Importance for key worlds',
        '- Use auto-assignment cascading priorities',
        '- Only Administrators can be governors',
        '- One governor per colony maximum',
    ]
    for i, tip in enumerate(tips):
        ax.text(0.57, 0.15 - i * 0.028, tip, ha='left', fontsize=7, color=COLORS['white'])

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    save_diagram(fig, output_path)


def create_survey_ship_tradeoff(output_path):
    """Issue #1161: Survey Ship Design Trade-off Space Diagram"""
    fig, ax = plt.subplots(figsize=(12, 10))
    setup_dark_theme(fig, ax)

    ax.set_title('Survey Ship Design Trade-off Space',
                 color=COLORS['white'], fontsize=16, fontweight='bold', pad=20)

    # Create scatter plot showing different design philosophies
    # X-axis: Speed (km/s), Y-axis: Survey Rate (points/day)

    designs = [
        # (speed, survey_rate, tonnage, label, color)
        (1500, 24, 1500, 'Early Scout\n1x Geo Sensor', COLORS['green']),
        (2500, 24, 2000, 'Fast Scout\n1x Sensor, Large Engine', COLORS['teal']),
        (2000, 48, 3500, 'Balanced Surveyor\n2x Sensors', COLORS['yellow']),
        (3000, 72, 5000, 'Mid-Game Standard\n3x Sensors + Jump Drive', COLORS['teal']),
        (2500, 120, 7000, 'Sensor Heavy\n5x Sensors', COLORS['red']),
        (4000, 72, 6000, 'Speed Focused\n3x Sensors, High Engine', COLORS['green']),
        (3500, 144, 10000, 'Late Game Cruiser\n6x Advanced Sensors', COLORS['yellow']),
    ]

    for speed, rate, tonnage, label, color in designs:
        size = tonnage / 100  # Scale point size by tonnage
        ax.scatter(speed, rate, s=size, c=color, alpha=0.7, edgecolors='white', linewidth=1)
        ax.annotate(label, (speed, rate), textcoords="offset points",
                   xytext=(10, 5), fontsize=7, color=COLORS['white'],
                   ha='left')

    # Add design regions
    from matplotlib.patches import Ellipse

    regions = [
        (1800, 30, 1500, 40, 'Budget Scouts\n(Cheap, Slow)', COLORS['green']),
        (3000, 60, 1500, 50, 'Balanced\n(Versatile)', COLORS['teal']),
        (2300, 130, 1200, 50, 'Sensor-Heavy\n(Survey Speed)', COLORS['red']),
        (3800, 100, 1000, 80, 'Speed-Focused\n(Transit Time)', COLORS['yellow']),
    ]

    for cx, cy, width, height, label, color in regions:
        ellipse = Ellipse((cx, cy), width, height, fill=False,
                          edgecolor=color, linewidth=2, linestyle='--', alpha=0.5)
        ax.add_patch(ellipse)
        ax.text(cx, cy - height/2 - 15, label, ha='center', fontsize=8,
               color=color, style='italic')

    # Axis labels
    ax.set_xlabel('Ship Speed (km/s)', color=COLORS['white'], fontsize=11)
    ax.set_ylabel('Survey Rate (points/day)', color=COLORS['white'], fontsize=11)

    ax.set_xlim(1000, 5000)
    ax.set_ylim(0, 180)

    # Grid
    ax.grid(True, alpha=0.2, color=COLORS['teal'])

    # Trade-off annotations
    ax.annotate('', xy=(4500, 30), xytext=(1500, 30),
               arrowprops=dict(arrowstyle='->', color=COLORS['teal'], lw=2))
    ax.text(3000, 22, 'Speed Priority (sparse systems, long transits)',
           ha='center', fontsize=8, color=COLORS['teal'])

    ax.annotate('', xy=(1200, 160), xytext=(1200, 40),
               arrowprops=dict(arrowstyle='->', color=COLORS['red'], lw=2))
    ax.text(1350, 100, 'Survey Rate\nPriority\n(dense systems)',
           ha='left', fontsize=8, color=COLORS['red'])

    # Legend for tonnage
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['white'],
               markersize=5, label='1,500t'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['white'],
               markersize=8, label='5,000t'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['white'],
               markersize=12, label='10,000t'),
    ]
    legend = ax.legend(handles=legend_elements, loc='upper left', title='Ship Tonnage',
                       framealpha=0.8, facecolor=COLORS['gray'])
    legend.get_title().set_color(COLORS['white'])
    for text in legend.get_texts():
        text.set_color(COLORS['white'])

    # Key insights box
    insights_text = (
        "Key Design Factors:\n"
        "- More sensors = faster survey, larger ship\n"
        "- Faster engines = quicker transit, more fuel\n"
        "- Jump drive adds ~1000t but enables independence\n"
        "- Consider: fuel range, maintenance, build cost"
    )
    props = dict(boxstyle='round', facecolor=COLORS['gray'], edgecolor=COLORS['teal'], alpha=0.9)
    ax.text(0.98, 0.02, insights_text, transform=ax.transAxes, fontsize=8,
           verticalalignment='bottom', horizontalalignment='right',
           bbox=props, color=COLORS['white'])

    save_diagram(fig, output_path)


def create_production_formula(output_path):
    """Issue #1164: Production Formula Breakdown Diagram"""
    fig, ax = plt.subplots(figsize=(14, 9))
    setup_dark_theme(fig, ax)

    ax.set_title('Production Formula Breakdown',
                 color=COLORS['white'], fontsize=16, fontweight='bold', pad=20)

    # Main formula box at top
    formula_box = FancyBboxPatch((0.15, 0.82), 0.7, 0.12,
                                  boxstyle="round,pad=0.02", facecolor=COLORS['gray'],
                                  edgecolor=COLORS['yellow'], linewidth=3)
    ax.add_patch(formula_box)
    ax.text(0.5, 0.90, 'Total BP/Year = Factories x BP/Factory x Governor x Sector',
           ha='center', va='center', fontsize=12, fontweight='bold', color=COLORS['yellow'])
    ax.text(0.5, 0.85, '(Each component shown below with technology modifiers)',
           ha='center', va='center', fontsize=9, color=COLORS['light_gray'])

    # Component boxes
    components = [
        {
            'title': 'Number of Factories',
            'x': 0.08, 'y': 0.55,
            'color': COLORS['teal'],
            'details': [
                'Construction Factories',
                '(or Conventional Industry)',
                '',
                'CI: 1/10th TN rate',
                'Build more = more output',
            ]
        },
        {
            'title': 'BP per Factory',
            'x': 0.33, 'y': 0.55,
            'color': COLORS['green'],
            'details': [
                'Base: 10 BP/year (TN)',
                'Base: 1 BP/year (CI)',
                '',
                'Tech upgrades:',
                '12 > 14 > 16 > 20 > 25...',
            ]
        },
        {
            'title': 'Governor Bonus',
            'x': 0.58, 'y': 0.55,
            'color': COLORS['yellow'],
            'details': [
                '1 + (Production%/100)',
                '',
                'Example:',
                '30% Production bonus',
                '= 1.30x multiplier',
            ]
        },
        {
            'title': 'Sector Bonus',
            'x': 0.83, 'y': 0.55,
            'color': COLORS['red'],
            'details': [
                'Governor Production x 0.25',
                '',
                'From sector commander',
                'Stacks with local gov',
                '(if under sector)',
            ]
        },
    ]

    box_width = 0.20
    box_height = 0.25

    for comp in components:
        # Box
        box = FancyBboxPatch((comp['x'], comp['y'] - box_height/2),
                              box_width, box_height,
                              boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                              edgecolor=comp['color'], linewidth=2)
        ax.add_patch(box)

        # Title
        ax.text(comp['x'] + box_width/2, comp['y'] + box_height/2 - 0.02,
               comp['title'], ha='center', va='center',
               fontsize=9, fontweight='bold', color=comp['color'])

        # Details
        for i, detail in enumerate(comp['details']):
            ax.text(comp['x'] + 0.01, comp['y'] + box_height/2 - 0.06 - i*0.035,
                   detail, ha='left', va='center', fontsize=7, color=COLORS['white'])

        # Arrow from formula
        ax.annotate('', xy=(comp['x'] + box_width/2, comp['y'] + box_height/2),
                   xytext=(comp['x'] + box_width/2, 0.82),
                   arrowprops=dict(arrowstyle='->', color=comp['color'], lw=1.5))

    # Related formulas
    related_y = 0.18
    related_formulas = [
        ('Mining Output:', 'Mines x Accessibility x Tech_Modifier', COLORS['yellow']),
        ('Fuel Production:', 'Refineries x 40,000L x Tech_Modifier', COLORS['teal']),
        ('Research Output:', 'Labs x RP_Rate x Scientist_Bonus', COLORS['green']),
    ]

    ax.text(0.5, related_y + 0.08, 'Related Production Formulas', ha='center',
           fontsize=11, fontweight='bold', color=COLORS['white'])

    for i, (name, formula, color) in enumerate(related_formulas):
        x = 0.10 + i * 0.30
        box = FancyBboxPatch((x, related_y - 0.08), 0.25, 0.12,
                              boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                              edgecolor=color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x + 0.125, related_y, name, ha='center', fontsize=8,
               fontweight='bold', color=color)
        ax.text(x + 0.125, related_y - 0.04, formula, ha='center', fontsize=7,
               color=COLORS['white'])

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    save_diagram(fig, output_path)


def create_combat_subpulse_sequence(output_path):
    """Issue #1166: Combat Sub-Pulse Sequence Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    setup_dark_theme(fig, ax)

    ax.set_title('Combat Sub-Pulse Sequence (5-second resolution)',
                 color=COLORS['white'], fontsize=16, fontweight='bold', pad=20)

    # Define sequence steps
    steps = [
        ('1', 'Movement Phase', 'All ships and missiles move\nsimultaneously based on\ncurrent orders and speed', COLORS['teal']),
        ('2', 'Fire Control Check', 'Weapons verify their\nassigned targets', COLORS['green']),
        ('3', 'Point Defense', 'CIWS and PD weapons\nengage incoming missiles\n(Final Fire mode)', COLORS['red']),
        ('4', 'Beam Weapon Fire', 'Beam weapons fire at\ntheir assigned targets', COLORS['yellow']),
        ('5', 'Missile Launch', 'Missile launchers release\nordnance at designated\ntargets', COLORS['teal']),
        ('6', 'Missile Tracking', 'Active missiles update\ntracking toward targets', COLORS['green']),
        ('7', 'Damage Resolution', 'All hits resolved:\narmor/shields reduced,\ninternal components checked', COLORS['red']),
    ]

    # Draw vertical timeline
    timeline_x = 0.15
    start_y = 0.88
    step_height = 0.11

    # Timeline line
    ax.plot([timeline_x, timeline_x], [start_y, start_y - len(steps) * step_height + 0.05],
           color=COLORS['teal'], linewidth=3)

    for i, (num, title, desc, color) in enumerate(steps):
        y = start_y - i * step_height

        # Step circle
        circle = Circle((timeline_x, y), 0.02, facecolor=color, edgecolor='white', linewidth=2)
        ax.add_patch(circle)
        ax.text(timeline_x, y, num, ha='center', va='center',
               fontsize=10, fontweight='bold', color=COLORS['bg'])

        # Step box
        box = FancyBboxPatch((0.22, y - 0.04), 0.35, 0.08,
                              boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                              edgecolor=color, linewidth=2)
        ax.add_patch(box)

        # Title and description
        ax.text(0.24, y + 0.02, title, ha='left', va='center',
               fontsize=10, fontweight='bold', color=color)
        ax.text(0.24, y - 0.02, desc, ha='left', va='center',
               fontsize=7, color=COLORS['white'])

        # Connector
        ax.plot([timeline_x + 0.02, 0.22], [y, y], color=color, linewidth=1.5)

    # Repeat arrow
    ax.annotate('', xy=(timeline_x - 0.04, start_y),
               xytext=(timeline_x - 0.04, start_y - len(steps) * step_height + 0.05),
               arrowprops=dict(arrowstyle='->', color=COLORS['yellow'], lw=2,
                              connectionstyle='arc3,rad=0.3'))
    ax.text(timeline_x - 0.08, start_y - len(steps) * step_height / 2,
           'Repeat\nEvery\n5 sec', ha='center', va='center',
           fontsize=8, color=COLORS['yellow'])

    # Key concepts panel
    concepts_x = 0.62
    concepts = [
        ('Simultaneous Movement', 'All entities move at once;\nno first-mover advantage'),
        ('Point Defense Priority', 'PD fires BEFORE beam weapons;\nprotects against incoming missiles'),
        ('Damage at End', 'All damage applied after\nall attacks resolved'),
        ('Sub-Pulse vs Increment', '5-sec sub-pulse for combat;\nlarger increments for travel'),
    ]

    ax.text(concepts_x + 0.17, 0.90, 'Key Combat Timing Concepts', ha='center',
           fontsize=11, fontweight='bold', color=COLORS['white'])

    for i, (concept_title, concept_desc) in enumerate(concepts):
        y = 0.82 - i * 0.12
        box = FancyBboxPatch((concepts_x, y - 0.04), 0.35, 0.10,
                              boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                              edgecolor=COLORS['light_gray'], linewidth=1.5)
        ax.add_patch(box)
        ax.text(concepts_x + 0.01, y + 0.03, concept_title, ha='left',
               fontsize=9, fontweight='bold', color=COLORS['teal'])
        ax.text(concepts_x + 0.01, y - 0.015, concept_desc, ha='left',
               fontsize=7, color=COLORS['white'])

    # Combat engagement note
    note_box = FancyBboxPatch((0.62, 0.02), 0.35, 0.10,
                               boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                               edgecolor=COLORS['red'], linewidth=2)
    ax.add_patch(note_box)
    ax.text(0.795, 0.09, 'Active Combat Detection', ha='center',
           fontsize=9, fontweight='bold', color=COLORS['red'])
    ax.text(0.795, 0.05, 'Game automatically switches to 5-sec\nresolution when combat detected',
           ha='center', fontsize=7, color=COLORS['white'])

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    save_diagram(fig, output_path)


def create_beam_tohit_calculation(output_path):
    """Issue #1168: Beam Weapon To-Hit Calculation Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    setup_dark_theme(fig, ax)

    ax.set_title('Beam Weapon To-Hit Calculation Flow',
                 color=COLORS['white'], fontsize=16, fontweight='bold', pad=20)

    # Main formula
    ax.text(0.5, 0.92, 'Final Hit Chance = Base Hit % x Tracking Modifier x ECM/ECCM Modifier',
           ha='center', fontsize=12, fontweight='bold', color=COLORS['yellow'])

    # Three main components
    components = [
        {
            'title': 'Base Hit Chance',
            'formula': '(Max Range - Current Range)\n/ Max Range x 100',
            'x': 0.08,
            'color': COLORS['teal'],
            'examples': [
                'At point blank: ~100%',
                'At half range: ~50%',
                'At max range: ~0%',
            ],
            'note': 'Linear falloff with distance'
        },
        {
            'title': 'Tracking Modifier',
            'formula': 'min(1.0, Weapon Tracking\n/ Target Speed)',
            'x': 0.38,
            'color': COLORS['green'],
            'examples': [
                'Track 5000, Target 3000: 100%',
                'Track 3000, Target 5000: 60%',
                'Track 1000, Target 8000: 12.5%',
            ],
            'note': 'Caps at 100% when tracking exceeds speed'
        },
        {
            'title': 'ECM/ECCM Modifier',
            'formula': 'ECM reduces hit chance\nECCM counters ECM\n(point for point)',
            'x': 0.68,
            'color': COLORS['red'],
            'examples': [
                'No ECM: 100%',
                'ECM-3: -30% accuracy',
                'ECM-3 vs ECCM-2: -10%',
            ],
            'note': 'Each ECM level = 10% reduction'
        },
    ]

    for comp in components:
        y = 0.70
        box_width = 0.26
        box_height = 0.35

        # Main box
        box = FancyBboxPatch((comp['x'], y - box_height/2), box_width, box_height,
                              boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                              edgecolor=comp['color'], linewidth=2)
        ax.add_patch(box)

        # Title
        ax.text(comp['x'] + box_width/2, y + box_height/2 - 0.03, comp['title'],
               ha='center', fontsize=11, fontweight='bold', color=comp['color'])

        # Formula
        ax.text(comp['x'] + box_width/2, y + box_height/2 - 0.10, comp['formula'],
               ha='center', fontsize=8, color=COLORS['white'])

        # Examples header
        ax.text(comp['x'] + 0.01, y - 0.02, 'Examples:', ha='left',
               fontsize=8, fontweight='bold', color=COLORS['light_gray'])

        # Example list
        for i, example in enumerate(comp['examples']):
            ax.text(comp['x'] + 0.01, y - 0.06 - i*0.035, f"  {example}",
                   ha='left', fontsize=7, color=COLORS['white'])

        # Note
        ax.text(comp['x'] + box_width/2, y - box_height/2 + 0.02, comp['note'],
               ha='center', fontsize=7, style='italic', color=COLORS['light_gray'])

        # Arrow from top
        ax.annotate('', xy=(comp['x'] + box_width/2, y + box_height/2),
                   xytext=(comp['x'] + box_width/2, 0.89),
                   arrowprops=dict(arrowstyle='->', color=comp['color'], lw=1.5))

    # Turret tracking note
    turret_box = FancyBboxPatch((0.08, 0.12), 0.40, 0.18,
                                 boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                                 edgecolor=COLORS['yellow'], linewidth=2)
    ax.add_patch(turret_box)
    ax.text(0.28, 0.27, 'Turret Tracking Rules', ha='center',
           fontsize=10, fontweight='bold', color=COLORS['yellow'])
    turret_notes = [
        '- Turrets use their own tracking speed',
        '- Fire controls multiply base tracking (up to 4x)',
        '- Lower of turret/FC tracking is used',
        '- Non-turret weapons use ship speed as cap',
    ]
    for i, note in enumerate(turret_notes):
        ax.text(0.10, 0.23 - i*0.03, note, ha='left', fontsize=7, color=COLORS['white'])

    # Practical example
    example_box = FancyBboxPatch((0.52, 0.02), 0.45, 0.28,
                                  boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                                  edgecolor=COLORS['teal'], linewidth=2)
    ax.add_patch(example_box)
    ax.text(0.745, 0.27, 'Worked Example', ha='center',
           fontsize=10, fontweight='bold', color=COLORS['teal'])

    example_lines = [
        'Scenario: 20cm Laser at 200K km (max 400K km)',
        'Target: 4000 km/s with ECM-2',
        'Weapon: 6000 km/s tracking, Fire Control has ECCM-1',
        '',
        'Base Hit: (400K - 200K) / 400K = 50%',
        'Tracking: min(1.0, 6000/4000) = 100%',
        'ECM/ECCM: ECM-2 - ECCM-1 = ECM-1 = -10%',
        '',
        'Final: 50% x 100% x 90% = 45% to hit',
    ]
    for i, line in enumerate(example_lines):
        color = COLORS['yellow'] if 'Final:' in line else COLORS['white']
        ax.text(0.54, 0.24 - i*0.025, line, ha='left', fontsize=7, color=color)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    save_diagram(fig, output_path)


def create_mineral_dependencies(output_path):
    """Issue #1170: Mineral Dependencies Network Diagram"""
    fig, ax = plt.subplots(figsize=(16, 12))
    setup_dark_theme(fig, ax)

    ax.set_title('Mineral Dependencies by Installation',
                 color=COLORS['white'], fontsize=18, fontweight='bold', pad=20)

    # Define minerals with their colors
    minerals = {
        'Duranium': (0.15, 0.85, COLORS['teal']),
        'Neutronium': (0.35, 0.85, COLORS['green']),
        'Corbomite': (0.55, 0.85, COLORS['yellow']),
        'Tritanium': (0.75, 0.85, COLORS['red']),
        'Boronide': (0.15, 0.65, '#9b59b6'),  # Purple
        'Mercassium': (0.35, 0.65, '#3498db'),  # Blue
        'Vendarite': (0.55, 0.65, '#e67e22'),  # Orange
        'Corundium': (0.75, 0.65, '#1abc9c'),  # Cyan
    }

    # Define installations with their mineral requirements
    installations = {
        'Infrastructure': (['Duranium', 'Mercassium'], (0.08, 0.35)),
        'Maintenance Facility': (['Duranium', 'Neutronium'], (0.22, 0.35)),
        'Construction Factory': (['Duranium', 'Neutronium'], (0.36, 0.35)),
        'Research Facility': (['Duranium', 'Mercassium'], (0.50, 0.35)),
        'Terraforming': (['Duranium', 'Boronide'], (0.64, 0.35)),
        'Mass Driver': (['Duranium', 'Neutronium', 'Boronide'], (0.78, 0.35)),
        'Mine': (['Corundium'], (0.08, 0.15)),
        'Fuel Refinery': (['Boronide'], (0.25, 0.15)),
        'Ordnance Factory': (['Tritanium'], (0.42, 0.15)),
        'Fighter Factory': (['Vendarite'], (0.59, 0.15)),
        'Financial Centre': (['Corbomite'], (0.76, 0.15)),
    }

    # Draw mineral nodes
    for mineral, (x, y, color) in minerals.items():
        circle = Circle((x, y), 0.04, facecolor=color, edgecolor='white', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, mineral[:3], ha='center', va='center',
               fontsize=8, fontweight='bold', color=COLORS['bg'])
        ax.text(x, y + 0.06, mineral, ha='center', va='center',
               fontsize=8, color=COLORS['white'])

    # Draw installation nodes and connections
    for inst_name, (required_minerals, (x, y)) in installations.items():
        # Installation box
        box_width = 0.12
        box_height = 0.08
        box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height,
                              boxstyle="round,pad=0.005", facecolor=COLORS['gray'],
                              edgecolor=COLORS['teal'], linewidth=1.5)
        ax.add_patch(box)

        # Split long names
        if len(inst_name) > 12:
            words = inst_name.split()
            if len(words) > 1:
                line1 = ' '.join(words[:len(words)//2 + 1])
                line2 = ' '.join(words[len(words)//2 + 1:])
                ax.text(x, y + 0.01, line1, ha='center', va='center', fontsize=6, color=COLORS['white'])
                ax.text(x, y - 0.015, line2, ha='center', va='center', fontsize=6, color=COLORS['white'])
            else:
                ax.text(x, y, inst_name, ha='center', va='center', fontsize=6, color=COLORS['white'])
        else:
            ax.text(x, y, inst_name, ha='center', va='center', fontsize=7, color=COLORS['white'])

        # Draw connections to minerals
        for mineral in required_minerals:
            if mineral in minerals:
                mx, my, color = minerals[mineral]
                ax.annotate('', xy=(x, y + box_height/2), xytext=(mx, my - 0.04),
                           arrowprops=dict(arrowstyle='->', color=color, lw=1, alpha=0.6))

    # Legend showing mineral primary uses
    legend_data = [
        ('Duranium', 'Hulls, basic structures', COLORS['teal']),
        ('Neutronium', 'Shipyards, advanced armor', COLORS['green']),
        ('Corbomite', 'Shields, financial', COLORS['yellow']),
        ('Tritanium', 'Missiles, ordnance', COLORS['red']),
        ('Boronide', 'Power, terraforming', '#9b59b6'),
        ('Mercassium', 'Research, electronics', '#3498db'),
        ('Vendarite', 'Gauss, ground forces', '#e67e22'),
        ('Corundium', 'Energy weapons, mining', '#1abc9c'),
    ]

    legend_x = 0.02
    legend_y = 0.52
    ax.text(legend_x, legend_y + 0.04, 'Mineral Primary Uses:', ha='left',
           fontsize=10, fontweight='bold', color=COLORS['white'])

    for i, (mineral, use, color) in enumerate(legend_data):
        row = i % 4
        col = i // 4
        lx = legend_x + col * 0.20
        ly = legend_y - row * 0.035
        ax.add_patch(Rectangle((lx, ly - 0.008), 0.015, 0.015, facecolor=color))
        ax.text(lx + 0.02, ly, f"{mineral}: {use}", ha='left', va='center',
               fontsize=6, color=COLORS['white'])

    # Critical bottlenecks note
    note_box = FancyBboxPatch((0.55, 0.48), 0.42, 0.10,
                               boxstyle="round,pad=0.01", facecolor=COLORS['gray'],
                               edgecolor=COLORS['red'], linewidth=2)
    ax.add_patch(note_box)
    ax.text(0.76, 0.555, 'Common Bottlenecks', ha='center',
           fontsize=9, fontweight='bold', color=COLORS['red'])
    ax.text(0.76, 0.52, 'Gallicite (engines) | Sorium (fuel) | Mercassium (research labs)',
           ha='center', fontsize=7, color=COLORS['white'])
    ax.text(0.76, 0.495, 'Secure multiple sources of these minerals early!',
           ha='center', fontsize=7, style='italic', color=COLORS['yellow'])

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    save_diagram(fig, output_path)


def main():
    """Generate all Wave 12 diagrams"""
    base_path = '/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams'

    print("Generating Wave 12: Commander & Exploration Diagrams...")
    print("=" * 60)

    # Issue #1133: Commander Bonus Stacking Hierarchy
    create_commander_bonus_stacking(
        f'{base_path}/16-commanders/16.2-commander-bonus-stacking.png')

    # Issue #1143: Auto-Assignment Priority Flow
    create_auto_assignment_priority(
        f'{base_path}/16-commanders/16.3-auto-assignment-priority.png')

    # Issue #1147: Governor Strategy Matrix
    create_governor_strategy_matrix(
        f'{base_path}/16-commanders/16.3-governor-strategy-matrix.png')

    # Issue #1161: Survey Ship Design Trade-off Space
    create_survey_ship_tradeoff(
        f'{base_path}/17-exploration/17.1-survey-ship-tradeoff.png')

    # Issue #1164: Production Formula Breakdown
    create_production_formula(
        f'{base_path}/18-advanced-topics/18.1-production-formula-breakdown.png')

    # Issue #1166: Combat Sub-Pulse Sequence
    create_combat_subpulse_sequence(
        f'{base_path}/18-advanced-topics/18.1-combat-subpulse-sequence.png')

    # Issue #1168: Beam Weapon To-Hit Calculation
    create_beam_tohit_calculation(
        f'{base_path}/18-advanced-topics/18.1-beam-tohit-flow.png')

    # Issue #1170: Mineral Dependencies Network
    create_mineral_dependencies(
        f'{base_path}/appendices/d-mineral-dependencies-network.png')

    print("=" * 60)
    print("All diagrams generated successfully!")


if __name__ == '__main__':
    main()
