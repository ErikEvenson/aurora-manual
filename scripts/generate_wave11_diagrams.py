#!/usr/bin/env python3
"""
Generate Wave 11: Logistics & Personnel Diagrams for Aurora Manual
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Polygon
import matplotlib.patheffects as path_effects
import numpy as np

# Theme colors
DARK_BG = '#1a1a2e'
TEAL = '#4ecdc4'
CORAL = '#ff6b6b'
YELLOW = '#ffe66d'
GREEN = '#95d5b2'
LIGHT_TEXT = '#ffffff'
GRID_COLOR = '#2a2a4e'

def setup_figure(figsize=(12, 8)):
    """Set up a figure with dark theme."""
    fig, ax = plt.subplots(figsize=figsize, facecolor=DARK_BG)
    ax.set_facecolor(DARK_BG)
    ax.tick_params(colors=LIGHT_TEXT)
    for spine in ax.spines.values():
        spine.set_color(GRID_COLOR)
    return fig, ax

def add_box(ax, x, y, width, height, text, color=TEAL, text_color=LIGHT_TEXT, fontsize=10):
    """Add a rounded box with text."""
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.02,rounding_size=0.1",
                         facecolor=color, edgecolor=LIGHT_TEXT, linewidth=2,
                         alpha=0.9)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=text_color, fontweight='bold', wrap=True)

def add_arrow(ax, start, end, color=LIGHT_TEXT):
    """Add an arrow between two points."""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2))

# =============================================================================
# Diagram 1: Sorium Harvester Automation Cycle (#1142)
# =============================================================================
def create_harvester_automation():
    fig, ax = setup_figure(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Sorium Harvester Automation Cycle', ha='center', va='center',
            fontsize=18, fontweight='bold', color=LIGHT_TEXT)

    # Main cycle nodes - circular arrangement
    center_x, center_y = 7, 5
    radius = 3

    nodes = [
        ('Deploy to\nGas Giant', 0),
        ('Harvest\nSorium', 1),
        ('Monitor\nHold Capacity', 2),
        ('When Tanks\nFull (Trigger)', 3),
        ('Transfer\nto Tanker', 4),
        ('Return to\nGas Giant', 5),
    ]

    colors = [TEAL, GREEN, YELLOW, CORAL, TEAL, GREEN]

    positions = []
    for i, (text, idx) in enumerate(nodes):
        angle = np.pi/2 - (2 * np.pi * i / len(nodes))
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)
        positions.append((x, y))
        add_box(ax, x, y, 2.2, 1.2, text, colors[i], fontsize=9)

    # Draw arrows between nodes
    for i in range(len(positions)):
        start = positions[i]
        end = positions[(i + 1) % len(positions)]

        # Calculate arrow start/end points offset from box centers
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        dist = np.sqrt(dx**2 + dy**2)

        arrow_start = (start[0] + 1.1 * dx/dist, start[1] + 0.6 * dy/dist)
        arrow_end = (end[0] - 1.1 * dx/dist, end[1] - 0.6 * dy/dist)

        add_arrow(ax, arrow_start, arrow_end, LIGHT_TEXT)

    # Side box for tanker/depot
    add_box(ax, 12, 5, 2, 1.5, 'Tanker/\nFuel Depot', CORAL, fontsize=9)
    ax.annotate('', xy=(11, 5), xytext=(9.5, 4),
                arrowprops=dict(arrowstyle='<->', color=YELLOW, lw=2))

    # Legend
    ax.text(1.5, 1.5, 'Legend:', fontsize=11, color=LIGHT_TEXT, fontweight='bold')
    legend_items = [
        (TEAL, 'Movement Phase'),
        (GREEN, 'Operation Phase'),
        (YELLOW, 'Monitoring'),
        (CORAL, 'Trigger/Transfer'),
    ]
    for i, (color, label) in enumerate(legend_items):
        ax.add_patch(Rectangle((1, 1 - i*0.4), 0.3, 0.25, facecolor=color))
        ax.text(1.5, 1.1 - i*0.4, label, fontsize=9, color=LIGHT_TEXT, va='center')

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/14-logistics/14.1-harvester-automation-cycle.png',
                dpi=150, facecolor=DARK_BG, bbox_inches='tight')
    plt.close()
    print("Created: 14.1-harvester-automation-cycle.png")

# =============================================================================
# Diagram 2: Maintenance vs Deployment Clock Comparison (#1157)
# =============================================================================
def create_maintenance_deployment_comparison():
    fig, ax = setup_figure(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Maintenance Clock vs Deployment Clock', ha='center', va='center',
            fontsize=18, fontweight='bold', color=LIGHT_TEXT)

    # Two columns
    # Left: Maintenance Clock
    ax.text(3.5, 8.5, 'MAINTENANCE CLOCK', ha='center', fontsize=14,
            fontweight='bold', color=TEAL)

    maint_items = [
        ('Measures', 'Time since last overhaul'),
        ('Affects', 'Component failure probability'),
        ('Limit Set By', 'Maintenance Life\n(engineering + MSP)'),
        ('Warning Signs', 'Random component failures'),
        ('Reset By', 'Overhaul at shipyard'),
    ]

    for i, (label, value) in enumerate(maint_items):
        y = 7.5 - i * 1.3
        add_box(ax, 2, y, 2, 0.8, label, TEAL, fontsize=9)
        add_box(ax, 5, y, 3, 0.8, value, GRID_COLOR, fontsize=8)

    # Right: Deployment Clock
    ax.text(10.5, 8.5, 'DEPLOYMENT CLOCK', ha='center', fontsize=14,
            fontweight='bold', color=CORAL)

    deploy_items = [
        ('Measures', 'Time since last overhaul'),
        ('Affects', 'Crew morale'),
        ('Limit Set By', 'Intended Deployment Time\n(class designer)'),
        ('Warning Signs', 'Morale degradation,\nstanding order failures'),
        ('Reset By', 'Overhaul at shipyard'),
    ]

    for i, (label, value) in enumerate(deploy_items):
        y = 7.5 - i * 1.3
        add_box(ax, 9, y, 2, 0.8, label, CORAL, fontsize=9)
        add_box(ax, 12, y, 3, 0.8, value, GRID_COLOR, fontsize=8)

    # Center connection
    ax.text(7, 4.5, 'BOTH RESET BY', ha='center', fontsize=12,
            fontweight='bold', color=YELLOW)
    add_box(ax, 7, 3.5, 4, 1, 'Naval Shipyard\nOverhaul', YELLOW, DARK_BG, fontsize=11)

    # Warning box
    ax.text(7, 1.5, 'WARNING: Refuelling and resupplying does NOT reset either clock!',
            ha='center', fontsize=10, color=CORAL, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=DARK_BG, edgecolor=CORAL, linewidth=2))

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/14-logistics/14.2-maintenance-deployment-clocks.png',
                dpi=150, facecolor=DARK_BG, bbox_inches='tight')
    plt.close()
    print("Created: 14.2-maintenance-deployment-clocks.png")

# =============================================================================
# Diagram 3: NPR Attribute Impact Matrix (#1074)
# =============================================================================
def create_npr_attribute_matrix():
    fig, ax = setup_figure(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'NPR Attribute Impact Matrix', ha='center', va='center',
            fontsize=18, fontweight='bold', color=LIGHT_TEXT)

    # Attributes and their impacts
    attributes = [
        ('Xenophobia\n(1-100)', CORAL, [
            'Diplomatic point generation',
            'Territorial responses',
            'Communication willingness',
            '100 = Auto-hostile'
        ]),
        ('Militancy\n(1-100)', CORAL, [
            'Willingness to use force',
            'Territorial resistance',
            'Fleet-building priority',
            'Combat aggression'
        ]),
        ('Determination\n(1-100)', YELLOW, [
            'Holds positions/claims',
            'Yield to demands',
            'Resistance calculation',
            'Treaty firmness'
        ]),
        ('Diplomacy\n(1-100)', GREEN, [
            'Negotiate willingness',
            'Treaty acceptance',
            'Communication initiation',
            'Peace seeking'
        ]),
        ('Trade\n(1-100)', TEAL, [
            'Economic cooperation',
            'Trade agreement value',
            'Resource sharing',
            'Commercial activity'
        ]),
    ]

    y_start = 8
    for i, (attr, color, impacts) in enumerate(attributes):
        y = y_start - i * 1.5

        # Attribute box
        add_box(ax, 2, y, 2.5, 1.2, attr, color, fontsize=9)

        # Impact boxes
        for j, impact in enumerate(impacts):
            x = 5 + j * 2.5
            box = FancyBboxPatch((x - 1.1, y - 0.4), 2.2, 0.8,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=GRID_COLOR, edgecolor=color, linewidth=1.5)
            ax.add_patch(box)
            ax.text(x, y, impact, ha='center', va='center', fontsize=7,
                    color=LIGHT_TEXT, wrap=True)

    # Cross-attribute note
    ax.text(7, 0.7, 'Hostility Modifier (game option): Adds to Xenophobia/Militancy, subtracts from Diplomacy/Trade',
            ha='center', fontsize=9, color=YELLOW,
            bbox=dict(boxstyle='round', facecolor=DARK_BG, edgecolor=YELLOW, linewidth=1))

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/15-diplomacy/15.1-npr-attribute-matrix.png',
                dpi=150, facecolor=DARK_BG, bbox_inches='tight')
    plt.close()
    print("Created: 15.1-npr-attribute-matrix.png")

# =============================================================================
# Diagram 4: Communication Rating Impact Levels (#1085)
# =============================================================================
def create_communication_rating_impact():
    fig, ax = setup_figure(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(7, 7.5, 'Communication Rating Impact Levels', ha='center', va='center',
            fontsize=18, fontweight='bold', color=LIGHT_TEXT)

    # Communication levels with their impacts
    levels = [
        ('0%', 'None', 'No communication possible', CORAL),
        ('1-19%', 'Minimal', 'Basic concepts only; frequent misunderstandings', CORAL),
        ('20-39%', 'Basic', 'Simple intentions; nuance lost', YELLOW),
        ('40-59%', 'Functional', 'Diplomatic proposals possible', YELLOW),
        ('60-79%', 'Good', 'Most options available; rare misunderstandings', GREEN),
        ('80-99%', 'Excellent', 'Full functionality; occasional ambiguity', TEAL),
        ('100%', 'Perfect', 'Complete mutual understanding', TEAL),
    ]

    # Draw gradient bar
    bar_height = 0.8
    bar_y = 6
    for i, (pct, quality, desc, color) in enumerate(levels):
        x = 1 + i * 1.8
        width = 1.7
        rect = Rectangle((x, bar_y), width, bar_height, facecolor=color, alpha=0.8)
        ax.add_patch(rect)
        ax.text(x + width/2, bar_y + bar_height + 0.15, pct, ha='center',
                fontsize=9, color=LIGHT_TEXT, fontweight='bold')

    # Available actions by level
    ax.text(7, 5, 'Available Diplomatic Actions by Communication Level',
            ha='center', fontsize=12, fontweight='bold', color=LIGHT_TEXT)

    actions = [
        ('20-30%', 'Basic messages (peaceful intent, warnings)', YELLOW),
        ('40-50%', 'Treaty proposals, trade offers', GREEN),
        ('60-70%', 'Complex negotiations, demands', TEAL),
        ('80%+', 'Alliance proposals, full diplomacy', TEAL),
    ]

    for i, (level, action, color) in enumerate(actions):
        y = 4 - i * 0.8
        add_box(ax, 3, y, 2.5, 0.6, level, color, fontsize=9)
        ax.text(7.5, y, action, ha='left', va='center', fontsize=10, color=LIGHT_TEXT)

    # Key note
    ax.text(7, 0.7, 'Without Diplomacy Module in contact system: positive gains halved',
            ha='center', fontsize=10, color=CORAL,
            bbox=dict(boxstyle='round', facecolor=DARK_BG, edgecolor=CORAL, linewidth=1))

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/15-diplomacy/15.2-communication-rating-impact.png',
                dpi=150, facecolor=DARK_BG, bbox_inches='tight')
    plt.close()
    print("Created: 15.2-communication-rating-impact.png")

# =============================================================================
# Diagram 5: Translation Progress Timeline (#1087)
# =============================================================================
def create_translation_timeline():
    fig, ax = setup_figure(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(7, 7.5, 'Translation Progress Timeline', ha='center', va='center',
            fontsize=18, fontweight='bold', color=LIGHT_TEXT)

    # Timeline
    timeline_y = 5.5
    ax.plot([1, 13], [timeline_y, timeline_y], color=LIGHT_TEXT, linewidth=3)

    milestones = [
        (1.5, '0%', 'First\nContact', CORAL),
        (4, '20%', 'Basic\nCommunication', YELLOW),
        (6.5, '50%', 'Functional\nDiplomacy', YELLOW),
        (9, '80%', 'Full\nDiplomacy', GREEN),
        (12, '100%', 'Perfect\nUnderstanding', TEAL),
    ]

    for x, pct, label, color in milestones:
        # Milestone marker
        circle = Circle((x, timeline_y), 0.2, facecolor=color, edgecolor=LIGHT_TEXT, linewidth=2)
        ax.add_patch(circle)
        ax.text(x, timeline_y + 0.5, pct, ha='center', fontsize=10,
                fontweight='bold', color=color)
        ax.text(x, timeline_y - 0.6, label, ha='center', fontsize=8, color=LIGHT_TEXT)

    # Factors affecting speed
    ax.text(7, 3.5, 'Factors Affecting Translation Speed', ha='center',
            fontsize=12, fontweight='bold', color=LIGHT_TEXT)

    factors = [
        ('Accelerating', [
            'More Xenology Labs',
            'Diplomacy Modules in contact',
            'High Diplomacy commander skill',
            'Human NPR bonus (+20)',
        ], GREEN),
        ('Slowing', [
            'High target Xenophobia',
            'No active sensors (no detection)',
            'No Diplomacy Module (halved gains)',
            'Communication status not "Attempting"',
        ], CORAL),
    ]

    for i, (title, items, color) in enumerate(factors):
        x = 4 + i * 6
        ax.text(x, 2.8, title, ha='center', fontsize=11, fontweight='bold', color=color)
        for j, item in enumerate(items):
            ax.text(x, 2.2 - j * 0.5, f'  {item}', ha='center', fontsize=9, color=LIGHT_TEXT)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/15-diplomacy/15.2-translation-timeline.png',
                dpi=150, facecolor=DARK_BG, bbox_inches='tight')
    plt.close()
    print("Created: 15.2-translation-timeline.png")

# =============================================================================
# Diagram 6: Treaty Types and Benefits Matrix (#1090)
# =============================================================================
def create_treaty_matrix():
    fig, ax = setup_figure(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Treaty Types and Benefits Matrix', ha='center', va='center',
            fontsize=18, fontweight='bold', color=LIGHT_TEXT)

    # Headers
    headers = ['Treaty Type', 'Comm. Req.', 'Relationship', 'Points/Year', 'Key Benefit']
    header_x = [1.5, 4, 6, 8, 11]

    for x, header in zip(header_x, headers):
        ax.text(x, 8.7, header, ha='center', fontsize=10, fontweight='bold', color=YELLOW)

    # Treaty data
    treaties = [
        ('Non-Aggression', '30%', 'Neutral+', '-', 'Mutual non-attack', TEAL),
        ('Transit Rights', '40%', 'Neutral+', '-', 'Movement through territory', TEAL),
        ('Trade Agreement', '50%', 'Friendly+', '100', 'Mineral exchange & wealth', GREEN),
        ('Geo Survey', '40%', 'Neutral+', '100', 'Shared mineral data', GREEN),
        ('Grav Survey', '40%', 'Neutral+', '100', 'Shared jump point data', GREEN),
        ('Research Treaty', '70%', 'Friendly+', '200', 'Technology sharing', YELLOW),
        ('Mutual Defense', '60%', 'Friendly+', '-', 'Military assistance', CORAL),
        ('Alliance', '80%', '75+ points', '200', 'Full cooperation', CORAL),
    ]

    for i, (name, comm, rel, pts, benefit, color) in enumerate(treaties):
        y = 8 - i * 0.85

        # Treaty name with colored background
        add_box(ax, 1.5, y, 2.5, 0.6, name, color, fontsize=8)

        # Other columns
        ax.text(4, y, comm, ha='center', fontsize=9, color=LIGHT_TEXT)
        ax.text(6, y, rel, ha='center', fontsize=9, color=LIGHT_TEXT)
        ax.text(8, y, pts, ha='center', fontsize=9, color=LIGHT_TEXT)
        ax.text(11, y, benefit, ha='center', fontsize=8, color=LIGHT_TEXT)

    # Formula note
    ax.text(7, 0.7, 'Points Formula: Base x (1 - Xenophobia/100) per year',
            ha='center', fontsize=10, color=YELLOW,
            bbox=dict(boxstyle='round', facecolor=DARK_BG, edgecolor=YELLOW, linewidth=1))

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/15-diplomacy/15.3-treaty-matrix.png',
                dpi=150, facecolor=DARK_BG, bbox_inches='tight')
    plt.close()
    print("Created: 15.3-treaty-matrix.png")

# =============================================================================
# Diagram 7: Independence Process Flow (#1097)
# =============================================================================
def create_independence_flow():
    fig, ax = setup_figure(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Independence Process Flow', ha='center', va='center',
            fontsize=18, fontweight='bold', color=LIGHT_TEXT)

    # Main flow
    flow_steps = [
        ('Colony\nDevelops', 1.5, 7.5, TEAL),
        ('Independence\nTriggered', 4, 7.5, YELLOW),
        ('New Race\nCreated', 7, 7.5, GREEN),
        ('Resources\nDistributed', 10, 7.5, CORAL),
        ('Autonomous\nNPR', 12.5, 7.5, TEAL),
    ]

    for text, x, y, color in flow_steps:
        add_box(ax, x, y, 2, 1.2, text, color, fontsize=9)

    # Arrows
    for i in range(len(flow_steps) - 1):
        x1 = flow_steps[i][1] + 1
        x2 = flow_steps[i+1][1] - 1
        add_arrow(ax, (x1, 7.5), (x2, 7.5))

    # Trigger methods
    ax.text(4, 5.8, 'Triggers', ha='center', fontsize=11, fontweight='bold', color=YELLOW)
    triggers = ['Manual Grant', 'Rebellion']
    for i, trigger in enumerate(triggers):
        add_box(ax, 3 + i * 2, 5, 1.8, 0.7, trigger, GRID_COLOR, fontsize=8)

    # What's transferred
    ax.text(7, 4, 'What New Race Receives', ha='center', fontsize=11,
            fontweight='bold', color=GREEN)

    transfers = [
        ('Identity', 'Name from population,\nauto-flag, themes'),
        ('Wealth', 'Proportional to\npopulation ratio'),
        ('Commanders', 'Proportional to\npopulation ratio'),
        ('Knowledge', 'All surveys, tech,\ndesigns, intel'),
    ]

    for i, (title, desc) in enumerate(transfers):
        x = 2 + i * 3.3
        add_box(ax, x, 3, 1.5, 0.6, title, TEAL, fontsize=9)
        ax.text(x, 2.2, desc, ha='center', fontsize=7, color=LIGHT_TEXT)

    # Fleet note
    ax.text(7, 1, 'Fleet Transfer: Manual independence requires explicit Fleet Transfer;\nRebellion may transfer ships automatically based on crew loyalty',
            ha='center', fontsize=9, color=LIGHT_TEXT,
            bbox=dict(boxstyle='round', facecolor=DARK_BG, edgecolor=CORAL, linewidth=1))

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/15-diplomacy/15.3-independence-flow.png',
                dpi=150, facecolor=DARK_BG, bbox_inches='tight')
    plt.close()
    print("Created: 15.3-independence-flow.png")

# =============================================================================
# Diagram 8: Hostility Spiral Prevention (#1104)
# =============================================================================
def create_hostility_spiral():
    fig, ax = setup_figure(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Hostility Spiral Prevention', ha='center', va='center',
            fontsize=18, fontweight='bold', color=LIGHT_TEXT)

    # Spiral stages (left side - the problem)
    ax.text(3.5, 8.5, 'ESCALATION PATH', ha='center', fontsize=12,
            fontweight='bold', color=CORAL)

    spiral_stages = [
        ('1. Territorial\nIntrusion', 'Ships enter NPR space'),
        ('2. Penalties\nAccumulate', 'Relations drop'),
        ('3. NPR\nWarnings', 'Patrols increase'),
        ('4. Skirmish\nOccurs', 'Patrol contact'),
        ('5. Combat\nDamage', 'Instant -100'),
        ('6. WAR', 'Full hostilities'),
    ]

    for i, (stage, desc) in enumerate(spiral_stages):
        y = 7.5 - i * 1.1
        add_box(ax, 2.5, y, 2, 0.8, stage, CORAL, fontsize=8)
        ax.text(4.8, y, desc, ha='left', va='center', fontsize=8, color=LIGHT_TEXT)
        if i < len(spiral_stages) - 1:
            add_arrow(ax, (2.5, y - 0.5), (2.5, y - 0.8))

    # Prevention strategies (right side - the solution)
    ax.text(10.5, 8.5, 'INTERVENTION POINTS', ha='center', fontsize=12,
            fontweight='bold', color=GREEN)

    interventions = [
        ('Monitor ship\nlocations', 'Know where your ships are'),
        ('Respect NPR\nterritory', 'Avoid valued systems'),
        ('Respond to\nwarnings', 'Withdraw when warned'),
        ('Configure\nstanding orders', 'Avoid neutral/friendly'),
        ('Send diplomatic\nships', 'Reduce intrusion penalties'),
        ('Establish\ntreaties early', 'Buffer against incidents'),
    ]

    for i, (action, benefit) in enumerate(interventions):
        y = 7.5 - i * 1.1
        add_box(ax, 9.5, y, 2.2, 0.8, action, GREEN, fontsize=8)
        ax.text(11.8, y, benefit, ha='left', va='center', fontsize=8, color=LIGHT_TEXT)

    # Key warning
    ax.text(7, 0.7, 'KEY: A single point of combat damage drops relations to Hostile instantly!',
            ha='center', fontsize=10, color=CORAL, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=DARK_BG, edgecolor=CORAL, linewidth=2))

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/15-diplomacy/15.4-hostility-spiral.png',
                dpi=150, facecolor=DARK_BG, bbox_inches='tight')
    plt.close()
    print("Created: 15.4-hostility-spiral.png")

# =============================================================================
# Diagram 9: ELINT Module Detection and Intelligence Gathering (#1115)
# =============================================================================
def create_elint_diagram():
    fig, ax = setup_figure(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'ELINT Module Detection and Intelligence Gathering', ha='center', va='center',
            fontsize=18, fontweight='bold', color=LIGHT_TEXT)

    # ELINT ship in center
    add_box(ax, 3, 6, 2.5, 1.5, 'ELINT Ship\n(10 HS Module)', TEAL, fontsize=10)

    # Detection range circle
    circle = Circle((3, 6), 2.5, fill=False, edgecolor=YELLOW, linestyle='--', linewidth=2)
    ax.add_patch(circle)
    ax.text(5.5, 7.5, 'Detection Range', fontsize=9, color=YELLOW, style='italic')

    # Targets
    targets = [
        ('Alien\nPopulation', 8, 7.5, GREEN),
        ('Active\nSensors', 8, 5, GREEN),
        ('Ships\n(detected)', 8, 2.5, CORAL),
    ]

    for text, x, y, color in targets:
        add_box(ax, x, y, 2, 1, text, color, fontsize=9)
        add_arrow(ax, (4.5, 6), (7, y))

    # Intelligence gathering rates
    ax.text(11.5, 8.5, 'Gathering Rate', ha='center', fontsize=12,
            fontweight='bold', color=LIGHT_TEXT)

    rates = [
        ('Base: 1 point/day per module', TEAL),
        ('x Commander Intel Bonus', GREEN),
        ('x (100 - Xenophobia)/100', YELLOW),
        ('x 0.20 if untranslated', CORAL),
    ]

    for i, (rate, color) in enumerate(rates):
        y = 7.5 - i * 0.7
        ax.text(11.5, y, rate, ha='center', fontsize=9, color=color)

    # Module specs table
    ax.text(11.5, 4.5, 'Module Specifications', ha='center', fontsize=11,
            fontweight='bold', color=LIGHT_TEXT)

    specs = [
        ('Str 5', '100 BP'),
        ('Str 6', '120 BP'),
        ('Str 8', '160 BP'),
        ('Str 11', '220 BP'),
        ('Str 14', '280 BP'),
    ]

    for i, (strength, cost) in enumerate(specs):
        y = 3.8 - i * 0.5
        ax.text(10.5, y, strength, ha='center', fontsize=8, color=TEAL)
        ax.text(12.5, y, cost, ha='center', fontsize=8, color=LIGHT_TEXT)

    # Key note
    ax.text(7, 0.7, 'No diplomatic penalty for ELINT operations - undetectable passive gathering',
            ha='center', fontsize=10, color=GREEN,
            bbox=dict(boxstyle='round', facecolor=DARK_BG, edgecolor=GREEN, linewidth=1))

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/15-diplomacy/15.5-elint-gathering.png',
                dpi=150, facecolor=DARK_BG, bbox_inches='tight')
    plt.close()
    print("Created: 15.5-elint-gathering.png")

# =============================================================================
# Diagram 10: Crew and Officer Generation Pipeline (#1122)
# =============================================================================
def create_officer_pipeline():
    fig, ax = setup_figure(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Crew and Officer Generation Pipeline', ha='center', va='center',
            fontsize=18, fontweight='bold', color=LIGHT_TEXT)

    # Main pipeline flow
    # Source: Population
    add_box(ax, 2, 7, 2.5, 1.5, 'POPULATION\n(Source)', TEAL, fontsize=10)

    # Two branches
    # Branch 1: Crew
    add_box(ax, 5.5, 8, 2.5, 1, 'Annual Crew\nGeneration', GREEN, fontsize=9)
    add_box(ax, 9, 8, 2.5, 1, 'Crew Pool', GREEN, fontsize=9)
    add_box(ax, 12, 8, 2, 1, 'Ship\nCrews', GREEN, fontsize=9)

    # Branch 2: Officers
    add_box(ax, 5.5, 6, 2.5, 1, 'Naval\nAcademy', CORAL, fontsize=9)
    add_box(ax, 9, 6, 2.5, 1, 'Officer Pool', CORAL, fontsize=9)
    add_box(ax, 12, 6, 2, 1, 'Ship\nCommands', CORAL, fontsize=9)

    # Arrows
    add_arrow(ax, (3.3, 7.5), (4.2, 8))
    add_arrow(ax, (3.3, 6.5), (4.2, 6))
    add_arrow(ax, (6.8, 8), (7.7, 8))
    add_arrow(ax, (6.8, 6), (7.7, 6))
    add_arrow(ax, (10.3, 8), (11, 8))
    add_arrow(ax, (10.3, 6), (11, 6))

    # Officer type distribution
    ax.text(5.5, 4.5, 'Officer Type Distribution', ha='center', fontsize=11,
            fontweight='bold', color=LIGHT_TEXT)

    types = [
        ('Naval', '60%', TEAL),
        ('Ground', '25%', CORAL),
        ('Admin', '8%', YELLOW),
        ('Scientist', '7%', GREEN),
    ]

    for i, (type_name, pct, color) in enumerate(types):
        x = 3.5 + i * 1.5
        add_box(ax, x, 3.8, 1.3, 0.6, type_name, color, fontsize=8)
        ax.text(x, 3.2, pct, ha='center', fontsize=9, color=LIGHT_TEXT)

    # Commandant effects
    ax.text(11, 4.5, 'Commandant Effects', ha='center', fontsize=11,
            fontweight='bold', color=LIGHT_TEXT)

    effects = [
        'Naval: 80% same type',
        'Ground: 40% same type',
        'Scientist: 14% same type',
        'Quality: Double-roll bonuses',
    ]

    for i, effect in enumerate(effects):
        ax.text(11, 3.8 - i * 0.5, effect, ha='center', fontsize=8, color=LIGHT_TEXT)

    # Academy quality setting
    ax.text(7, 1.5, 'Academy Quality Setting (1-5): Trades quantity for quality',
            ha='center', fontsize=9, color=YELLOW)
    ax.text(7, 1, '1 = Max quantity, min quality (default) | 5 = Max quality, min quantity',
            ha='center', fontsize=8, color=LIGHT_TEXT)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/16-commanders/16.1-officer-generation-pipeline.png',
                dpi=150, facecolor=DARK_BG, bbox_inches='tight')
    plt.close()
    print("Created: 16.1-officer-generation-pipeline.png")

# =============================================================================
# Main execution
# =============================================================================
if __name__ == '__main__':
    print("Generating Wave 11 diagrams...")

    create_harvester_automation()
    create_maintenance_deployment_comparison()
    create_npr_attribute_matrix()
    create_communication_rating_impact()
    create_translation_timeline()
    create_treaty_matrix()
    create_independence_flow()
    create_hostility_spiral()
    create_elint_diagram()
    create_officer_pipeline()

    print("\nAll diagrams generated successfully!")
