#!/usr/bin/env python3
"""
Generate Wave 7: UI & Interface Diagrams for Aurora Manual
Dark theme with colors: #1a1a2e (background), #4ecdc4 (cyan), #ff6b6b (red),
#ffe66d (yellow), #95d5b2 (green)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Circle, Wedge, Polygon
from matplotlib.lines import Line2D
import numpy as np
import os

# Color scheme
DARK_BG = '#1a1a2e'
CYAN = '#4ecdc4'
RED = '#ff6b6b'
YELLOW = '#ffe66d'
GREEN = '#95d5b2'
WHITE = '#ffffff'
LIGHT_GRAY = '#a0a0a0'
DARK_GRAY = '#404060'

# Output directory
OUTPUT_DIR = '/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams'


def setup_dark_figure(figsize=(12, 8)):
    """Create a figure with dark theme."""
    fig, ax = plt.subplots(figsize=figsize, facecolor=DARK_BG)
    ax.set_facecolor(DARK_BG)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    return fig, ax


def add_title(ax, title, y=9.5):
    """Add a title to the diagram."""
    ax.text(5, y, title, ha='center', va='top', fontsize=16,
            fontweight='bold', color=WHITE)


def draw_rounded_box(ax, x, y, width, height, color, text, text_color=WHITE, fontsize=10):
    """Draw a rounded rectangle with centered text."""
    box = FancyBboxPatch((x, y), width, height,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=color, edgecolor=WHITE, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text, ha='center', va='center',
            fontsize=fontsize, color=text_color, wrap=True)


def save_figure(fig, subdir, filename):
    """Save figure to the appropriate directory."""
    path = os.path.join(OUTPUT_DIR, subdir)
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, filename)
    fig.savefig(filepath, dpi=150, facecolor=DARK_BG, edgecolor='none',
                bbox_inches='tight', pad_inches=0.2)
    plt.close(fig)
    print(f"Saved: {filepath}")


# ============================================================================
# Issue #1123 - Section 2.5: Starting Ship Designs Infographic
# ============================================================================
def create_starting_ships_infographic():
    """Create infographic showing starting ship designs for TN start."""
    fig, ax = setup_dark_figure(figsize=(14, 10))

    add_title(ax, "Starting Ship Designs (TN Start)", y=9.8)
    ax.text(5, 9.3, "86,100 Build Points Available for Instant Construction",
            ha='center', va='top', fontsize=11, color=LIGHT_GRAY)

    # Ship type data
    ships = [
        {"name": "Gravitational\nSurvey Ship", "size": "3-5k tons", "cost": "300-500 BP",
         "purpose": "Find jump points", "priority": "HIGH", "color": CYAN,
         "components": "Grav Sensor\nJump Drive\nFuel Tanks", "mission": "Survey\nlocations 1-30"},
        {"name": "Geological\nSurvey Ship", "size": "3-5k tons", "cost": "300-500 BP",
         "purpose": "Find minerals", "priority": "HIGH", "color": CYAN,
         "components": "Geo Sensor\nFuel Tanks\nCrew Quarters", "mission": "Survey all\nbodies"},
        {"name": "Fuel Harvester", "size": "20-50k tons", "cost": "200-500 BP",
         "purpose": "Fuel from gas giants", "priority": "HIGH", "color": GREEN,
         "components": "Harvesters\nFuel Storage\nSlow Engine", "mission": "Gas giant\norbits"},
        {"name": "Colony Ship", "size": "30-50k tons", "cost": "300-600 BP",
         "purpose": "Transport colonists", "priority": "MEDIUM", "color": YELLOW,
         "components": "Cryo Berths\nFuel Tanks\nCommercial", "mission": "New world\ncolonization"},
        {"name": "Freighter", "size": "30-50k tons", "cost": "200-400 BP",
         "purpose": "Move cargo", "priority": "MEDIUM", "color": YELLOW,
         "components": "Cargo Holds\nFuel Tanks\nCommercial", "mission": "Supply\nroutes"},
    ]

    # Draw ship boxes
    box_width = 1.7
    box_height = 2.2
    start_x = 0.5
    spacing = 1.9

    for i, ship in enumerate(ships):
        x = start_x + i * spacing
        y = 5.5

        # Main ship box
        box = FancyBboxPatch((x, y), box_width, box_height,
                              boxstyle="round,pad=0.02,rounding_size=0.08",
                              facecolor=DARK_GRAY, edgecolor=ship['color'], linewidth=2)
        ax.add_patch(box)

        # Ship name
        ax.text(x + box_width/2, y + box_height - 0.25, ship['name'],
                ha='center', va='top', fontsize=9, fontweight='bold', color=WHITE)

        # Size and cost
        ax.text(x + box_width/2, y + box_height - 0.7, f"{ship['size']}",
                ha='center', va='top', fontsize=8, color=LIGHT_GRAY)
        ax.text(x + box_width/2, y + box_height - 0.9, f"{ship['cost']}",
                ha='center', va='top', fontsize=8, color=ship['color'])

        # Purpose
        ax.text(x + box_width/2, y + 0.9, ship['purpose'],
                ha='center', va='center', fontsize=8, color=WHITE)

        # Components below
        comp_y = y - 0.8
        ax.text(x + box_width/2, comp_y, "Key Components:",
                ha='center', va='top', fontsize=7, color=LIGHT_GRAY)
        ax.text(x + box_width/2, comp_y - 0.2, ship['components'],
                ha='center', va='top', fontsize=7, color=WHITE)

        # Priority indicator
        priority_color = CYAN if ship['priority'] == 'HIGH' else YELLOW
        ax.text(x + box_width/2, y + box_height + 0.15, f"Priority: {ship['priority']}",
                ha='center', va='bottom', fontsize=8, color=priority_color)

    # Build order recommendation
    ax.text(5, 2.5, "Recommended Build Order", ha='center', va='top',
            fontsize=12, fontweight='bold', color=WHITE)

    order_text = """1. Gravitational Survey Ships (x2) - Find jump points for expansion
2. Geological Survey Ships (x2) - Locate mineral deposits
3. Fuel Harvesters (x2) - Establish fuel independence from Sorium
4. Freighters (x4-6) - Support colony logistics
5. Colony Ships (x2) - Begin expansion to new worlds"""

    ax.text(5, 2.2, order_text, ha='center', va='top', fontsize=9,
            color=LIGHT_GRAY, family='monospace')

    # Budget example
    ax.text(5, 0.5, "Example Fleet: ~15,000 BP (leaves 71,000+ for future builds)",
            ha='center', va='center', fontsize=9, color=GREEN)

    save_figure(fig, '2-game-setup', '2.5-starting-ship-designs.png')


# ============================================================================
# Issue #1139 - Section 3.1: Economics Window Tab Organization Diagram
# ============================================================================
def create_economics_tabs_diagram():
    """Create diagram showing Economics window 11-tab structure."""
    fig, ax = setup_dark_figure(figsize=(14, 10))

    add_title(ax, "Economics Window (F2) - Tab Organization", y=9.8)

    # Central hub
    hub_x, hub_y = 5, 5
    hub = Circle((hub_x, hub_y), 0.8, facecolor=CYAN, edgecolor=WHITE, linewidth=2)
    ax.add_patch(hub)
    ax.text(hub_x, hub_y, "Economics\nWindow", ha='center', va='center',
            fontsize=10, fontweight='bold', color=DARK_BG)

    # Tab data with positions (angle in degrees)
    tabs = [
        {"name": "Summary", "desc": "Colony overview\nPopulation, installations", "angle": 90, "color": CYAN},
        {"name": "Industry", "desc": "Construction queues\nFactory allocation", "angle": 60, "color": GREEN},
        {"name": "Mining", "desc": "Mine allocation\nExtraction rates", "angle": 30, "color": GREEN},
        {"name": "Wealth/Trade", "desc": "Finances\nTrade goods", "angle": 0, "color": YELLOW},
        {"name": "Research", "desc": "Scientist assignment\nProject progress", "angle": -30, "color": CYAN},
        {"name": "Shipyard", "desc": "Build queues\nRetooling", "angle": -60, "color": GREEN},
        {"name": "GU Training", "desc": "Ground units\nEquipment", "angle": -90, "color": RED},
        {"name": "Governor", "desc": "Automation settings\nAssignments", "angle": -120, "color": YELLOW},
        {"name": "Civilian Economy", "desc": "Shipping lines\nContracts", "angle": -150, "color": YELLOW},
        {"name": "Empire Mining", "desc": "All colonies\nMining overview", "angle": 180, "color": GREEN},
        {"name": "Environment", "desc": "Terraforming\nAtmosphere", "angle": 150, "color": CYAN},
    ]

    radius = 3.2
    for tab in tabs:
        angle_rad = np.radians(tab['angle'])
        x = hub_x + radius * np.cos(angle_rad)
        y = hub_y + radius * np.sin(angle_rad)

        # Connection line
        ax.plot([hub_x, x], [hub_y, y], color=DARK_GRAY, linewidth=1, zorder=1)

        # Tab box
        box_width = 1.8
        box_height = 0.8
        box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height,
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=DARK_GRAY, edgecolor=tab['color'], linewidth=2)
        ax.add_patch(box)

        # Tab name
        ax.text(x, y + 0.1, tab['name'], ha='center', va='center',
                fontsize=9, fontweight='bold', color=WHITE)

        # Description (positioned outside)
        desc_radius = radius + 1.3
        desc_x = hub_x + desc_radius * np.cos(angle_rad)
        desc_y = hub_y + desc_radius * np.sin(angle_rad)
        ax.text(desc_x, desc_y, tab['desc'], ha='center', va='center',
                fontsize=7, color=LIGHT_GRAY)

    # Legend
    legend_y = 0.8
    ax.text(1, legend_y, "Color Legend:", fontsize=9, fontweight='bold', color=WHITE)
    for i, (color, label) in enumerate([(GREEN, "Production"), (CYAN, "Information"),
                                         (YELLOW, "Economy"), (RED, "Military")]):
        ax.add_patch(Rectangle((2.5 + i*2, legend_y - 0.15), 0.3, 0.3, facecolor=color))
        ax.text(2.9 + i*2, legend_y, label, fontsize=8, color=WHITE, va='center')

    save_figure(fig, '3-user-interface', '3.1-economics-tabs.png')


# ============================================================================
# Issue #1141 - Section 3.1: Interrupt Events Decision Tree
# ============================================================================
def create_interrupt_decision_tree():
    """Create decision tree for handling interrupt events."""
    fig, ax = setup_dark_figure(figsize=(14, 11))

    add_title(ax, "Interrupt Events Decision Tree", y=9.8)

    # Decision tree structure
    # Level 0: Event occurs
    draw_rounded_box(ax, 4, 8.5, 2, 0.6, RED, "TIME STOPS\nInterrupt Event!", fontsize=9)

    # Level 1: Identify type
    ax.annotate('', xy=(5, 7.9), xytext=(5, 8.5),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))
    draw_rounded_box(ax, 3.5, 7.2, 3, 0.6, CYAN, "Identify Event Type", fontsize=10)

    # Level 2: Event type branches
    types = [
        {"x": 1, "name": "Hostile\nContact", "color": RED, "urgent": True},
        {"x": 3.5, "name": "Research\nComplete", "color": CYAN, "urgent": False},
        {"x": 6, "name": "Construction\nComplete", "color": GREEN, "urgent": False},
        {"x": 8.5, "name": "Unassigned\nLabs", "color": YELLOW, "urgent": False},
    ]

    for t in types:
        # Line from identify
        ax.plot([5, t['x'] + 0.75], [7.2, 6.4], color=DARK_GRAY, linewidth=1)
        draw_rounded_box(ax, t['x'], 5.6, 1.5, 0.7, DARK_GRAY, t['name'], fontsize=8)
        # Color indicator
        ax.add_patch(Rectangle((t['x'], 5.55), 1.5, 0.08, facecolor=t['color']))

    # Branch 1: Hostile Contact (urgent)
    ax.annotate('', xy=(1.75, 4.9), xytext=(1.75, 5.6),
                arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))
    draw_rounded_box(ax, 0.5, 4.2, 2.5, 0.6, RED, "REDUCE TIME\nto 30 sec or less", fontsize=8)
    ax.annotate('', xy=(1.75, 3.6), xytext=(1.75, 4.2),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))
    draw_rounded_box(ax, 0.5, 2.9, 2.5, 0.6, DARK_GRAY, "Open System Map\nAssess threat", fontsize=8)
    ax.annotate('', xy=(1.75, 2.3), xytext=(1.75, 2.9),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))
    draw_rounded_box(ax, 0.5, 1.6, 2.5, 0.6, DARK_GRAY, "Issue orders:\nEngage/Retreat", fontsize=8)
    ax.annotate('', xy=(1.75, 1.0), xytext=(1.75, 1.6),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))
    draw_rounded_box(ax, 0.5, 0.3, 2.5, 0.6, CYAN, "Advance at short\nincrements", fontsize=8)

    # Branch 2: Research Complete
    ax.annotate('', xy=(4.25, 4.9), xytext=(4.25, 5.6),
                arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5))
    draw_rounded_box(ax, 3.25, 4.2, 2, 0.6, DARK_GRAY, "Open Research\nWindow (Ctrl+F5)", fontsize=8)
    ax.annotate('', xy=(4.25, 3.6), xytext=(4.25, 4.2),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))
    draw_rounded_box(ax, 3.25, 2.9, 2, 0.6, DARK_GRAY, "Assign scientist\nto new project", fontsize=8)
    ax.annotate('', xy=(4.25, 2.3), xytext=(4.25, 2.9),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))
    draw_rounded_box(ax, 3.25, 1.6, 2, 0.6, CYAN, "Consider new\nship designs", fontsize=8)

    # Branch 3: Construction Complete
    ax.annotate('', xy=(6.75, 4.9), xytext=(6.75, 5.6),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))
    draw_rounded_box(ax, 5.75, 4.2, 2, 0.6, DARK_GRAY, "Check what\nwas built", fontsize=8)
    ax.annotate('', xy=(6.75, 3.6), xytext=(6.75, 4.2),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))

    # Split for ship vs installation
    ax.plot([6.75, 6], [3.6, 3.0], color=DARK_GRAY, linewidth=1)
    ax.plot([6.75, 7.5], [3.6, 3.0], color=DARK_GRAY, linewidth=1)
    draw_rounded_box(ax, 5.25, 2.3, 1.5, 0.6, DARK_GRAY, "Ship?\nAssign fleet", fontsize=7)
    draw_rounded_box(ax, 6.75, 2.3, 1.5, 0.6, DARK_GRAY, "Installation?\nVerify active", fontsize=7)

    # Branch 4: Unassigned Labs
    ax.annotate('', xy=(9.25, 4.9), xytext=(9.25, 5.6),
                arrowprops=dict(arrowstyle='->', color=YELLOW, lw=1.5))
    draw_rounded_box(ax, 8, 4.2, 2.5, 0.6, YELLOW, "WARNING:\nWasted capacity!", fontsize=8)
    ax.annotate('', xy=(9.25, 3.6), xytext=(9.25, 4.2),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))
    draw_rounded_box(ax, 8, 2.9, 2.5, 0.6, DARK_GRAY, "Open Research\nAssign labs", fontsize=8)

    # Legend
    ax.text(8.5, 1.2, "Urgency:", fontsize=9, fontweight='bold', color=WHITE)
    ax.add_patch(Rectangle((8.5, 0.7), 0.3, 0.3, facecolor=RED))
    ax.text(8.9, 0.85, "Immediate", fontsize=8, color=WHITE, va='center')
    ax.add_patch(Rectangle((8.5, 0.3), 0.3, 0.3, facecolor=CYAN))
    ax.text(8.9, 0.45, "Normal", fontsize=8, color=WHITE, va='center')

    save_figure(fig, '3-user-interface', '3.1-interrupt-decision-tree.png')


# ============================================================================
# Issue #1144 - Section 3.2: Display Toggles Reference Card
# ============================================================================
def create_display_toggles_card():
    """Create reference card showing all display toggles."""
    fig, ax = setup_dark_figure(figsize=(14, 10))

    add_title(ax, "System Map Display Toggles Reference Card", y=9.8)

    # Toggle categories
    categories = [
        {
            "name": "Orbital Bodies",
            "x": 0.5,
            "color": CYAN,
            "toggles": [
                ("Planets", "Major bodies", "Default ON"),
                ("Moons", "Satellites", "Can clutter"),
                ("Asteroids", "Belt objects", "Many entries"),
                ("Comets", "Icy bodies", "v2.7.0 toggle"),
                ("Comet Names", "Labels", "v2.7.0 separate"),
                ("Dwarf Planets", "Small bodies", "Hide at zoom"),
            ]
        },
        {
            "name": "Orbital Paths",
            "x": 3.5,
            "color": GREEN,
            "toggles": [
                ("Planet Orbits", "Orbital lines", "Geometry view"),
                ("Moon Orbits", "Satellite paths", "High clutter"),
                ("Ship Paths", "Movement lines", "Track fleets"),
                ("Selected Only", "One orbit", "Recommended"),
                ("All Orbits", "Every body", "Very cluttered"),
            ]
        },
        {
            "name": "Ships & Fleets",
            "x": 6.5,
            "color": YELLOW,
            "toggles": [
                ("Player Fleets", "Your ships", "Always ON"),
                ("Contacts", "Detected ships", "Sensor range"),
                ("Civilian Ships", "Freighters etc", "Trade routes"),
                ("Fleet Names", "Labels", "ID groups"),
                ("Fleet Icons", "Symbols", "Quick read"),
            ]
        },
        {
            "name": "Strategic",
            "x": 9.5,
            "color": RED,
            "toggles": [
                ("Jump Points", "Connections", "Navigation"),
                ("Survey Markers", "Grav waypoints", "Exploration"),
                ("Waypoints", "Custom markers", "Fleet orders"),
                ("Mineral Icons", "Deposit marks", "Mining"),
                ("Sensor Ranges", "Detection radii", "Combat setup"),
                ("Lagrange", "L4/L5 points", "Special orbits"),
            ]
        },
    ]

    for cat in categories:
        x = cat['x']
        # Category header
        ax.add_patch(FancyBboxPatch((x, 8.2), 2.5, 0.6,
                                     boxstyle="round,pad=0.02,rounding_size=0.05",
                                     facecolor=cat['color'], edgecolor=WHITE, linewidth=2))
        ax.text(x + 1.25, 8.5, cat['name'], ha='center', va='center',
                fontsize=11, fontweight='bold', color=DARK_BG)

        # Toggle entries
        for i, (toggle, desc, note) in enumerate(cat['toggles']):
            y = 7.4 - i * 1.0
            # Toggle box
            ax.add_patch(FancyBboxPatch((x, y), 2.5, 0.8,
                                         boxstyle="round,pad=0.02,rounding_size=0.03",
                                         facecolor=DARK_GRAY, edgecolor=cat['color'], linewidth=1))
            ax.text(x + 0.1, y + 0.55, toggle, fontsize=9, fontweight='bold', color=WHITE, va='center')
            ax.text(x + 0.1, y + 0.25, desc, fontsize=7, color=LIGHT_GRAY, va='center')
            ax.text(x + 2.4, y + 0.4, note, fontsize=7, color=cat['color'], va='center', ha='right')

    # Use case recommendations
    ax.text(5, 1.2, "Recommended Combinations", ha='center', va='top',
            fontsize=12, fontweight='bold', color=WHITE)

    recs = [
        (CYAN, "Exploration:", "Planets + Jump Points + Survey Markers + Fleet Names"),
        (GREEN, "Economy:", "Planets + Mineral Icons + Ship Paths (civilian)"),
        (RED, "Combat:", "Contacts + Sensor Ranges + Fleet Icons + Selected Orbits"),
    ]

    for i, (color, label, items) in enumerate(recs):
        y = 0.7 - i * 0.35
        ax.add_patch(Rectangle((1, y), 0.2, 0.2, facecolor=color))
        ax.text(1.3, y + 0.1, label, fontsize=9, fontweight='bold', color=WHITE, va='center')
        ax.text(3, y + 0.1, items, fontsize=8, color=LIGHT_GRAY, va='center')

    save_figure(fig, '3-user-interface', '3.2-display-toggles.png')


# ============================================================================
# Issue #1146 - Section 3.2: Zoom Level Use Cases Diagram
# ============================================================================
def create_zoom_levels_diagram():
    """Create diagram showing zoom level use cases."""
    fig, ax = setup_dark_figure(figsize=(14, 9))

    add_title(ax, "System Map Zoom Level Use Cases", y=9.5)

    # Zoom levels from left (zoomed out) to right (zoomed in)
    levels = [
        {
            "name": "System View",
            "scale": "Billions km",
            "x": 1,
            "color": CYAN,
            "uses": ["Jump point locations", "Overall fleet positions", "Inter-planet transits"],
            "when": "Planning exploration routes"
        },
        {
            "name": "Planet View",
            "scale": "Millions km",
            "x": 3.5,
            "color": GREEN,
            "uses": ["Orbital mechanics", "Moon positions", "Survey progress"],
            "when": "Managing colony systems"
        },
        {
            "name": "Orbital View",
            "scale": "100k-1M km",
            "x": 6,
            "color": YELLOW,
            "uses": ["Ship formations", "Refueling operations", "Transfer orbits"],
            "when": "Fleet management"
        },
        {
            "name": "Combat View",
            "scale": "10k-100k km",
            "x": 8.5,
            "color": RED,
            "uses": ["Weapon ranges", "Missile tracks", "Tactical positioning"],
            "when": "Active combat"
        },
    ]

    # Draw zoom progression arrow
    ax.annotate('', xy=(9.5, 8.2), xytext=(0.5, 8.2),
                arrowprops=dict(arrowstyle='->', color=LIGHT_GRAY, lw=2))
    ax.text(5, 8.5, "ZOOM IN -->", ha='center', fontsize=10, color=LIGHT_GRAY)
    ax.text(0.8, 8.5, "Wide", ha='center', fontsize=9, color=LIGHT_GRAY)
    ax.text(9.2, 8.5, "Detail", ha='center', fontsize=9, color=LIGHT_GRAY)

    for level in levels:
        x = level['x']

        # Main box
        ax.add_patch(FancyBboxPatch((x, 4.5), 2, 3.2,
                                     boxstyle="round,pad=0.02,rounding_size=0.05",
                                     facecolor=DARK_GRAY, edgecolor=level['color'], linewidth=2))

        # Name
        ax.text(x + 1, 7.4, level['name'], ha='center', fontsize=11,
                fontweight='bold', color=WHITE)

        # Scale
        ax.add_patch(Rectangle((x + 0.2, 6.9), 1.6, 0.35, facecolor=level['color'], alpha=0.3))
        ax.text(x + 1, 7.05, level['scale'], ha='center', fontsize=9, color=level['color'])

        # Uses
        for i, use in enumerate(level['uses']):
            ax.text(x + 0.2, 6.4 - i * 0.4, f"- {use}", fontsize=8, color=WHITE)

        # When to use
        ax.text(x + 1, 4.7, f"Use: {level['when']}", ha='center', fontsize=7,
                color=LIGHT_GRAY, style='italic')

    # Mouse controls
    ax.text(5, 3.5, "Zoom Controls", ha='center', fontsize=12, fontweight='bold', color=WHITE)
    controls = [
        ("Mouse Wheel", "Smooth zoom at cursor position"),
        ("Toolbar +/-", "Incremental zoom steps"),
        ("Preset Buttons", "Jump to standard scales"),
    ]

    for i, (key, desc) in enumerate(controls):
        y = 2.8 - i * 0.5
        ax.add_patch(FancyBboxPatch((2.5, y), 1.5, 0.4,
                                     boxstyle="round,pad=0.02,rounding_size=0.03",
                                     facecolor=CYAN, edgecolor=WHITE, linewidth=1))
        ax.text(3.25, y + 0.2, key, ha='center', fontsize=9, color=DARK_BG)
        ax.text(4.2, y + 0.2, desc, fontsize=9, color=LIGHT_GRAY, va='center')

    # Tip
    ax.text(5, 0.8, "Tip: Double-click an object to center and zoom to it automatically",
            ha='center', fontsize=9, color=GREEN, style='italic')

    save_figure(fig, '3-user-interface', '3.2-zoom-levels.png')


# ============================================================================
# Issue #1149 - Section 3.2: Click Interaction Flowchart
# ============================================================================
def create_click_flowchart():
    """Create flowchart showing mouse click interactions."""
    fig, ax = setup_dark_figure(figsize=(14, 11))

    add_title(ax, "System Map Click Interactions", y=9.8)

    # Left click section
    ax.add_patch(FancyBboxPatch((0.3, 5), 4, 4.3,
                                 boxstyle="round,pad=0.02,rounding_size=0.1",
                                 facecolor='none', edgecolor=CYAN, linewidth=2))
    ax.text(2.3, 9.0, "LEFT CLICK", ha='center', fontsize=12, fontweight='bold', color=CYAN)

    left_actions = [
        ("On Planet/Body", "Select body\nShow info panel", CYAN),
        ("On Fleet", "Select fleet\nShow composition", CYAN),
        ("On Jump Point", "Select JP\nShow destination", CYAN),
        ("On Contact", "Select contact\nShow signature data", CYAN),
        ("On Empty Space", "Deselect current\nobject", LIGHT_GRAY),
    ]

    for i, (target, action, color) in enumerate(left_actions):
        y = 8.2 - i * 0.8
        ax.add_patch(FancyBboxPatch((0.5, y), 1.5, 0.6,
                                     boxstyle="round,pad=0.02,rounding_size=0.03",
                                     facecolor=DARK_GRAY, edgecolor=color, linewidth=1))
        ax.text(1.25, y + 0.3, target, ha='center', fontsize=8, color=WHITE)
        ax.annotate('', xy=(3.5, y + 0.3), xytext=(2.1, y + 0.3),
                    arrowprops=dict(arrowstyle='->', color=color, lw=1))
        ax.text(3.6, y + 0.3, action, fontsize=8, color=LIGHT_GRAY, va='center')

    # Right click section
    ax.add_patch(FancyBboxPatch((5, 5), 4.7, 4.3,
                                 boxstyle="round,pad=0.02,rounding_size=0.1",
                                 facecolor='none', edgecolor=GREEN, linewidth=2))
    ax.text(7.35, 9.0, "RIGHT CLICK", ha='center', fontsize=12, fontweight='bold', color=GREEN)

    right_actions = [
        ("On Map", "Popup menu:\nFleets, Populations,\nJump Points nearby", GREEN),
        ("Fleet Selected +\nBody/Waypoint", "Issue move-to\norder", GREEN),
        ("Fleet Selected +\nAnother Fleet", "Intercept/Follow\noptions", GREEN),
        ("On Jump Point", "Switch to that\nsystem", GREEN),
    ]

    for i, (target, action, color) in enumerate(right_actions):
        y = 8.2 - i * 0.9
        ax.add_patch(FancyBboxPatch((5.2, y), 1.7, 0.7,
                                     boxstyle="round,pad=0.02,rounding_size=0.03",
                                     facecolor=DARK_GRAY, edgecolor=color, linewidth=1))
        ax.text(6.05, y + 0.35, target, ha='center', fontsize=7, color=WHITE)
        ax.annotate('', xy=(8.8, y + 0.35), xytext=(7.0, y + 0.35),
                    arrowprops=dict(arrowstyle='->', color=color, lw=1))
        ax.text(8.9, y + 0.35, action, fontsize=8, color=LIGHT_GRAY, va='center')

    # Double click section
    ax.add_patch(FancyBboxPatch((0.3, 2.5), 4, 2.2,
                                 boxstyle="round,pad=0.02,rounding_size=0.1",
                                 facecolor='none', edgecolor=YELLOW, linewidth=2))
    ax.text(2.3, 4.4, "DOUBLE CLICK", ha='center', fontsize=12, fontweight='bold', color=YELLOW)

    ax.text(2.3, 3.8, "Center view on object", ha='center', fontsize=9, color=WHITE)
    ax.text(2.3, 3.4, "- Planet: Center on planet", fontsize=8, color=LIGHT_GRAY, ha='center')
    ax.text(2.3, 3.1, "- Fleet: Center on fleet", fontsize=8, color=LIGHT_GRAY, ha='center')
    ax.text(2.3, 2.8, "- Event: Center on event location", fontsize=8, color=LIGHT_GRAY, ha='center')

    # Modifier keys section
    ax.add_patch(FancyBboxPatch((5, 2.5), 4.7, 2.2,
                                 boxstyle="round,pad=0.02,rounding_size=0.1",
                                 facecolor='none', edgecolor=RED, linewidth=2))
    ax.text(7.35, 4.4, "MODIFIERS", ha='center', fontsize=12, fontweight='bold', color=RED)

    modifiers = [
        ("Shift + Drag", "Measure distance"),
        ("Ctrl + Click", "Add to selection (grids)"),
        ("Right Drag", "Pan the map"),
    ]

    for i, (mod, action) in enumerate(modifiers):
        y = 3.8 - i * 0.5
        ax.add_patch(FancyBboxPatch((5.2, y), 1.5, 0.4,
                                     boxstyle="round,pad=0.02,rounding_size=0.02",
                                     facecolor=RED, edgecolor=WHITE, linewidth=1))
        ax.text(5.95, y + 0.2, mod, ha='center', fontsize=8, color=DARK_BG)
        ax.text(6.9, y + 0.2, action, fontsize=9, color=LIGHT_GRAY, va='center')

    # Quick tips
    ax.text(5, 1.8, "Quick Tips:", ha='center', fontsize=10, fontweight='bold', color=WHITE)
    ax.text(5, 1.4, "- Right-click context menu identifies overlapping objects",
            ha='center', fontsize=8, color=LIGHT_GRAY)
    ax.text(5, 1.1, "- Selected fleet + right-click target = quick movement orders",
            ha='center', fontsize=8, color=LIGHT_GRAY)
    ax.text(5, 0.8, "- Shift+drag shows distance for ship design range planning",
            ha='center', fontsize=8, color=GREEN)

    save_figure(fig, '3-user-interface', '3.2-click-interactions.png')


# ============================================================================
# Issue #1152 - Section 3.3: Keyboard Shortcut Reference Card
# ============================================================================
def create_keyboard_shortcuts_card():
    """Create printable keyboard shortcut reference card."""
    fig, ax = setup_dark_figure(figsize=(14, 10))

    add_title(ax, "Aurora C# Keyboard Shortcuts", y=9.8)
    ax.text(5, 9.4, "Quick Reference Card (v1.10.0+)", ha='center', fontsize=10, color=LIGHT_GRAY)

    # F-Key Windows
    ax.add_patch(FancyBboxPatch((0.2, 4.8), 4.5, 4.2,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=DARK_GRAY, edgecolor=CYAN, linewidth=2))
    ax.text(2.45, 8.7, "F-Key Windows", ha='center', fontsize=11, fontweight='bold', color=CYAN)

    fkeys = [
        ("F2", "Population Summary"),
        ("F3", "Commanders"),
        ("F4", "Naval Organization"),
        ("F5", "Class Design"),
        ("F6", "Diplomacy & Intelligence"),
        ("F7", "Race Window"),
        ("F8", "Ground Forces"),
        ("F9", "System View"),
        ("F10", "Create Project"),
        ("F11", "Galactic Map"),
        ("F12", "Toggle Auto-Turns"),
    ]

    for i, (key, window) in enumerate(fkeys):
        y = 8.3 - i * 0.32
        ax.add_patch(FancyBboxPatch((0.4, y), 0.7, 0.28,
                                     boxstyle="round,pad=0.01,rounding_size=0.02",
                                     facecolor=CYAN, edgecolor=WHITE, linewidth=1))
        ax.text(0.75, y + 0.14, key, ha='center', fontsize=8, fontweight='bold', color=DARK_BG)
        ax.text(1.2, y + 0.14, window, fontsize=8, color=WHITE, va='center')

    # Ctrl+F-Key Windows
    ax.add_patch(FancyBboxPatch((5, 4.8), 4.7, 4.2,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=DARK_GRAY, edgecolor=GREEN, linewidth=2))
    ax.text(7.35, 8.7, "Ctrl+F-Key Windows", ha='center', fontsize=11, fontweight='bold', color=GREEN)

    ctrl_fkeys = [
        ("Ctrl+F2", "Events"),
        ("Ctrl+F3", "Medals"),
        ("Ctrl+F4", "Industry"),
        ("Ctrl+F5", "Research"),
        ("Ctrl+F6", "Mining"),
        ("Ctrl+F7", "Wealth"),
        ("Ctrl+F8", "View Technology"),
        ("Ctrl+F9", "Sectors"),
        ("Ctrl+F10", "Missile Design"),
        ("Ctrl+F11", "Turret Design"),
        ("Ctrl+F12", "SM Mode"),
    ]

    for i, (key, window) in enumerate(ctrl_fkeys):
        y = 8.3 - i * 0.32
        ax.add_patch(FancyBboxPatch((5.2, y), 1.3, 0.28,
                                     boxstyle="round,pad=0.01,rounding_size=0.02",
                                     facecolor=GREEN, edgecolor=WHITE, linewidth=1))
        ax.text(5.85, y + 0.14, key, ha='center', fontsize=7, fontweight='bold', color=DARK_BG)
        ax.text(6.6, y + 0.14, window, fontsize=8, color=WHITE, va='center')

    # Map Navigation
    ax.add_patch(FancyBboxPatch((0.2, 0.5), 4.5, 4,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=DARK_GRAY, edgecolor=YELLOW, linewidth=2))
    ax.text(2.45, 4.2, "Map Navigation", ha='center', fontsize=11, fontweight='bold', color=YELLOW)

    nav_keys = [
        ("Arrow Keys", "Pan the map"),
        ("+/-", "Zoom in/out"),
        ("Mouse Wheel", "Smooth zoom"),
        ("Alt+F11", "Previous location (history)"),
        ("Alt+F12", "Next location (history)"),
        ("Shift+Drag", "Measure distance"),
        ("Right Drag", "Pan map"),
        ("Double-Click", "Center on object"),
    ]

    for i, (key, action) in enumerate(nav_keys):
        y = 3.7 - i * 0.4
        ax.add_patch(FancyBboxPatch((0.4, y), 1.5, 0.32,
                                     boxstyle="round,pad=0.01,rounding_size=0.02",
                                     facecolor=YELLOW, edgecolor=WHITE, linewidth=1))
        ax.text(1.15, y + 0.16, key, ha='center', fontsize=7, fontweight='bold', color=DARK_BG)
        ax.text(2, y + 0.16, action, fontsize=8, color=WHITE, va='center')

    # Special Modifiers
    ax.add_patch(FancyBboxPatch((5, 0.5), 4.7, 4,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=DARK_GRAY, edgecolor=RED, linewidth=2))
    ax.text(7.35, 4.2, "Special Modifiers", ha='center', fontsize=11, fontweight='bold', color=RED)

    special = [
        ("Shift + F-Key", "Open 2nd instance of window"),
        ("Shift + Button", "Open 2nd instance"),
        ("Ctrl+Shift+F4", "2nd Industry window"),
    ]

    for i, (key, action) in enumerate(special):
        y = 3.5 - i * 0.5
        ax.add_patch(FancyBboxPatch((5.2, y), 2, 0.4,
                                     boxstyle="round,pad=0.01,rounding_size=0.02",
                                     facecolor=RED, edgecolor=WHITE, linewidth=1))
        ax.text(6.2, y + 0.2, key, ha='center', fontsize=8, fontweight='bold', color=DARK_BG)
        ax.text(7.3, y + 0.2, action, fontsize=8, color=WHITE, va='center')

    ax.text(7.35, 1.8, "Standard Shortcuts", ha='center', fontsize=9, fontweight='bold', color=LIGHT_GRAY)
    ax.text(7.35, 1.4, "Ctrl+C/V = Copy/Paste (text fields)", ha='center', fontsize=8, color=LIGHT_GRAY)
    ax.text(7.35, 1.1, "Escape = Close window", ha='center', fontsize=8, color=LIGHT_GRAY)
    ax.text(7.35, 0.8, "Tab = Next field", ha='center', fontsize=8, color=LIGHT_GRAY)

    save_figure(fig, '3-user-interface', '3.3-keyboard-shortcuts.png')


# ============================================================================
# Issue #1159 - Section 3.4: Event Type Categories Visual Glossary
# ============================================================================
def create_event_glossary():
    """Create visual glossary of event types."""
    fig, ax = setup_dark_figure(figsize=(14, 11))

    add_title(ax, "Event Type Categories Visual Glossary", y=9.8)
    ax.text(5, 9.4, "240 Event Types in Database - Key Categories Shown",
            ha='center', fontsize=9, color=LIGHT_GRAY)

    categories = [
        {
            "name": "COMBAT",
            "color": RED,
            "x": 0.3,
            "events": [
                ("181", "Hostile Contact", "CRITICAL"),
                ("334-5", "Ship Combat", "HIGH"),
                ("27", "Ship Destroyed", "HIGH"),
                ("15", "Missile Launch", "HIGH"),
                ("28", "Damage Report", "MEDIUM"),
                ("221", "Crew Losses", "MEDIUM"),
            ]
        },
        {
            "name": "EXPLORATION",
            "color": CYAN,
            "x": 3.5,
            "events": [
                ("138", "Jump Point Found", "HIGH"),
                ("195", "New System", "HIGH"),
                ("143", "Survey Complete", "MEDIUM"),
                ("43", "Minerals Located", "MEDIUM"),
            ]
        },
        {
            "name": "RESEARCH",
            "color": GREEN,
            "x": 6.7,
            "events": [
                ("60", "Research Complete", "HIGH"),
                ("299", "Breakthrough", "MEDIUM"),
                ("88", "Research Started", "LOW"),
            ]
        },
    ]

    # Draw first row of categories
    for cat in categories:
        x = cat['x']
        # Header
        ax.add_patch(FancyBboxPatch((x, 7.8), 2.8, 0.6,
                                     boxstyle="round,pad=0.02,rounding_size=0.05",
                                     facecolor=cat['color'], edgecolor=WHITE, linewidth=2))
        ax.text(x + 1.4, 8.1, cat['name'], ha='center', fontsize=11,
                fontweight='bold', color=DARK_BG)

        # Events
        for i, (eid, name, priority) in enumerate(cat['events']):
            y = 7.2 - i * 0.55
            # Event box
            ax.add_patch(FancyBboxPatch((x, y), 2.8, 0.45,
                                         boxstyle="round,pad=0.01,rounding_size=0.02",
                                         facecolor=DARK_GRAY, edgecolor=cat['color'], linewidth=1))
            # ID
            ax.text(x + 0.35, y + 0.22, f"[{eid}]", fontsize=7, color=cat['color'],
                    va='center', family='monospace')
            # Name
            ax.text(x + 0.8, y + 0.22, name, fontsize=8, color=WHITE, va='center')
            # Priority indicator
            pcolor = {
                'CRITICAL': RED, 'HIGH': YELLOW, 'MEDIUM': LIGHT_GRAY, 'LOW': DARK_GRAY
            }[priority]
            ax.text(x + 2.65, y + 0.22, priority, fontsize=6, color=pcolor,
                    va='center', ha='right')

    # Second row of categories
    categories2 = [
        {
            "name": "ECONOMIC",
            "color": YELLOW,
            "x": 0.3,
            "events": [
                ("1", "Production", "MEDIUM"),
                ("2", "Ship Built", "HIGH"),
                ("125", "Shipyard Modified", "MEDIUM"),
                ("66", "Mineral Exhausted", "HIGH"),
                ("65/71", "Low/No Fuel", "HIGH"),
            ]
        },
        {
            "name": "COLONY",
            "color": GREEN,
            "x": 3.5,
            "events": [
                ("115", "Pop Status Change", "LOW"),
                ("77", "Terraforming", "LOW"),
                ("148-9", "Unrest Change", "MEDIUM"),
            ]
        },
        {
            "name": "COMMANDER",
            "color": LIGHT_GRAY,
            "x": 6.7,
            "events": [
                ("90", "Promoted", "LOW"),
                ("292", "Retirement", "LOW"),
                ("98/256-7", "New Officer", "LOW"),
            ]
        },
    ]

    for cat in categories2:
        x = cat['x']
        y_base = 3.6
        # Header
        ax.add_patch(FancyBboxPatch((x, y_base + 0.6), 2.8, 0.6,
                                     boxstyle="round,pad=0.02,rounding_size=0.05",
                                     facecolor=cat['color'], edgecolor=WHITE, linewidth=2))
        ax.text(x + 1.4, y_base + 0.9, cat['name'], ha='center', fontsize=11,
                fontweight='bold', color=DARK_BG if cat['color'] != LIGHT_GRAY else WHITE)

        # Events
        for i, (eid, name, priority) in enumerate(cat['events']):
            y = y_base - i * 0.55
            ax.add_patch(FancyBboxPatch((x, y), 2.8, 0.45,
                                         boxstyle="round,pad=0.01,rounding_size=0.02",
                                         facecolor=DARK_GRAY, edgecolor=cat['color'], linewidth=1))
            ax.text(x + 0.35, y + 0.22, f"[{eid}]", fontsize=7, color=cat['color'],
                    va='center', family='monospace')
            ax.text(x + 0.8, y + 0.22, name, fontsize=8, color=WHITE, va='center')
            pcolor = {
                'CRITICAL': RED, 'HIGH': YELLOW, 'MEDIUM': LIGHT_GRAY, 'LOW': DARK_GRAY
            }[priority]
            ax.text(x + 2.65, y + 0.22, priority, fontsize=6, color=pcolor,
                    va='center', ha='right')

    # Priority legend
    ax.text(5, 0.9, "Response Priority:", ha='center', fontsize=10, fontweight='bold', color=WHITE)
    priorities = [(RED, "CRITICAL"), (YELLOW, "HIGH"), (LIGHT_GRAY, "MEDIUM"), (DARK_GRAY, "LOW")]
    for i, (color, label) in enumerate(priorities):
        x = 2.5 + i * 1.5
        ax.add_patch(Rectangle((x, 0.4), 0.3, 0.3, facecolor=color))
        ax.text(x + 0.4, 0.55, label, fontsize=8, color=WHITE, va='center')

    save_figure(fig, '3-user-interface', '3.4-event-glossary.png')


# ============================================================================
# Issue #1162 - Section 3.4: Event Filtering Strategy Guide
# ============================================================================
def create_event_filtering_guide():
    """Create diagram showing event filtering strategies."""
    fig, ax = setup_dark_figure(figsize=(14, 10))

    add_title(ax, "Event Filtering Strategy Guide", y=9.8)

    # Game phases as columns
    phases = [
        {
            "name": "PEACETIME\nDEVELOPMENT",
            "color": GREEN,
            "x": 0.5,
            "show": ["Research Complete", "Construction Complete",
                     "Jump Point Found", "Minerals Located"],
            "hide": ["Commander Promotions", "Minor Colony Growth",
                     "Standard Fleet Moves"],
            "focus": "Progress milestones\nNew opportunities"
        },
        {
            "name": "ACTIVE\nCOMBAT",
            "color": RED,
            "x": 3.5,
            "show": ["Hostile Contact", "Ship Combat",
                     "Damage Reports", "Missile Launches"],
            "hide": ["Economic Events", "Research Completion",
                     "Routine Exploration"],
            "focus": "Tactical awareness\nThreat response"
        },
        {
            "name": "EXPLORATION\nPHASE",
            "color": CYAN,
            "x": 6.5,
            "show": ["Jump Point Discovery", "New System Entry",
                     "Survey Complete", "Minerals Found"],
            "hide": ["Routine Production", "Commander Events"],
            "focus": "New territories\nResource discovery"
        },
        {
            "name": "ECONOMIC\nBUILD-UP",
            "color": YELLOW,
            "x": 9.5,
            "show": ["Construction Done", "Mineral Depletion",
                     "Fuel Warnings"],
            "hide": ["Combat Events", "Routine Exploration"],
            "focus": "Production efficiency\nResource management"
        },
    ]

    for phase in phases:
        x = phase['x']

        # Phase header
        ax.add_patch(FancyBboxPatch((x - 0.2, 7.5), 2.8, 1.2,
                                     boxstyle="round,pad=0.02,rounding_size=0.05",
                                     facecolor=phase['color'], edgecolor=WHITE, linewidth=2))
        ax.text(x + 1.2, 8.1, phase['name'], ha='center', fontsize=10,
                fontweight='bold', color=DARK_BG)

        # SHOW section
        ax.text(x + 1.2, 7.2, "SHOW:", ha='center', fontsize=9,
                fontweight='bold', color=GREEN)
        for i, item in enumerate(phase['show']):
            ax.text(x + 0.1, 6.8 - i * 0.35, f"+ {item}", fontsize=7, color=WHITE)

        # HIDE section
        y_hide = 6.8 - len(phase['show']) * 0.35 - 0.3
        ax.text(x + 1.2, y_hide, "HIDE:", ha='center', fontsize=9,
                fontweight='bold', color=RED)
        for i, item in enumerate(phase['hide']):
            ax.text(x + 0.1, y_hide - 0.4 - i * 0.35, f"- {item}", fontsize=7, color=LIGHT_GRAY)

        # Focus
        y_focus = 3.2
        ax.add_patch(FancyBboxPatch((x - 0.2, y_focus), 2.8, 0.8,
                                     boxstyle="round,pad=0.02,rounding_size=0.03",
                                     facecolor=DARK_GRAY, edgecolor=phase['color'], linewidth=1))
        ax.text(x + 1.2, y_focus + 0.55, "Focus on:", fontsize=8,
                fontweight='bold', color=WHITE, ha='center')
        ax.text(x + 1.2, y_focus + 0.25, phase['focus'], fontsize=7,
                color=phase['color'], ha='center')

    # Filter mechanics explanation
    ax.add_patch(FancyBboxPatch((0.5, 0.5), 9, 2.2,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=DARK_GRAY, edgecolor=LIGHT_GRAY, linewidth=1))
    ax.text(5, 2.4, "How Filtering Works", ha='center', fontsize=11,
            fontweight='bold', color=WHITE)

    mechanics = [
        "- 240 individual event types can be shown/hidden separately",
        "- Settings stored per-race and persist across sessions",
        "- No category-based filtering - each type toggled individually",
        "- Export/Import via CSV for sharing configurations between games",
    ]
    for i, text in enumerate(mechanics):
        ax.text(0.8, 1.9 - i * 0.35, text, fontsize=8, color=LIGHT_GRAY)

    save_figure(fig, '3-user-interface', '3.4-event-filtering.png')


# ============================================================================
# Issue #1163 - Section 3.5: System Node Color Reference Card
# ============================================================================
def create_system_colors_card():
    """Create reference card showing system node colors on galactic map."""
    fig, ax = setup_dark_figure(figsize=(14, 9))

    add_title(ax, "Galactic Map - System Node Color Reference", y=9.5)

    # System colors
    colors_data = [
        {"color": "#90EE90", "name": "Light Green", "meaning": "Populated system (colony present)", "verified": True},
        {"color": "#228B22", "name": "Green", "meaning": "Population over 100 million", "verified": True},
        {"color": "#98FB98", "name": "Pale Green", "meaning": "Controlled, no direct colonies", "verified": False},
        {"color": "#800080", "name": "Purple", "meaning": "Black hole system (v2.6.0)", "verified": True},
        {"color": "#FF4444", "name": "Red", "meaning": "Hostile alien contact detected", "verified": False},
        {"color": "#FFFFA0", "name": "Yellow/White", "meaning": "Explored, no player presence", "verified": True},
        {"color": "#808080", "name": "Grey", "meaning": "Known but not yet visited", "verified": False},
    ]

    ax.text(5, 8.8, "System Node Colors", ha='center', fontsize=12, fontweight='bold', color=WHITE)

    for i, data in enumerate(colors_data):
        y = 8.0 - i * 0.8

        # Color sample circle
        circle = Circle((1.2, y), 0.25, facecolor=data['color'], edgecolor=WHITE, linewidth=1.5)
        ax.add_patch(circle)

        # Color name
        ax.text(1.7, y, data['name'], fontsize=10, color=WHITE, va='center', fontweight='bold')

        # Meaning
        ax.text(3.5, y, data['meaning'], fontsize=9, color=LIGHT_GRAY, va='center')

        # Verification status
        if data['verified']:
            ax.text(8, y, "Verified", fontsize=8, color=GREEN, va='center')
        else:
            ax.text(8, y, "Unverified", fontsize=8, color=YELLOW, va='center')

    # Jump point connections
    ax.add_patch(FancyBboxPatch((0.5, 1.5), 4, 2,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=DARK_GRAY, edgecolor=CYAN, linewidth=1))
    ax.text(2.5, 3.2, "Jump Point Connections", ha='center', fontsize=11,
            fontweight='bold', color=CYAN)

    ax.plot([0.8, 2], [2.5, 2.5], color=WHITE, linewidth=2)
    ax.text(2.2, 2.5, "Standard connection", fontsize=9, color=WHITE, va='center')

    ax.plot([0.8, 2], [2.0, 2.0], color=RED, linewidth=2, linestyle='--')
    ax.text(2.2, 2.0, "Military Restricted (optional display)", fontsize=9, color=LIGHT_GRAY, va='center')

    # System icons
    ax.add_patch(FancyBboxPatch((5, 1.5), 4.5, 2,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=DARK_GRAY, edgecolor=GREEN, linewidth=1))
    ax.text(7.25, 3.2, "System Icons", ha='center', fontsize=11,
            fontweight='bold', color=GREEN)

    icons = [
        ("Ships present", "Fleet icons"),
        ("Shipyards", "Production facilities"),
        ("Populations", "Colony markers"),
    ]

    for i, (icon, desc) in enumerate(icons):
        y = 2.6 - i * 0.4
        ax.text(5.3, y, f"- {icon}:", fontsize=9, color=WHITE)
        ax.text(6.8, y, desc, fontsize=8, color=LIGHT_GRAY)

    # Note about technology
    ax.text(5, 0.8, "Note: As of v2.4.0, system colors account for Colonization Cost Reduction technology",
            ha='center', fontsize=8, color=GREEN, style='italic')

    save_figure(fig, '3-user-interface', '3.5-system-colors.png')


# ============================================================================
# Issue #1165 - Section 3.5: Sector Organization Examples Diagram
# ============================================================================
def create_sector_examples():
    """Create example diagrams showing sector organization patterns."""
    fig, ax = setup_dark_figure(figsize=(14, 10))

    add_title(ax, "Sector Organization Examples", y=9.8)

    # Example 1: Defensive Perimeter
    ax.add_patch(FancyBboxPatch((0.3, 5.5), 4.5, 3.8,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor='none', edgecolor=RED, linewidth=2))
    ax.text(2.55, 9.0, "Defensive Perimeter", ha='center', fontsize=11,
            fontweight='bold', color=RED)

    # Draw schematic
    # Core
    core = Circle((2.5, 7.5), 0.4, facecolor=GREEN, edgecolor=WHITE, linewidth=1.5)
    ax.add_patch(core)
    ax.text(2.5, 7.5, "CORE", ha='center', va='center', fontsize=7, color=DARK_BG)

    # Perimeter systems
    perimeter_angles = [0, 60, 120, 180, 240, 300]
    for angle in perimeter_angles:
        rad = np.radians(angle)
        x = 2.5 + 1.2 * np.cos(rad)
        y = 7.5 + 1.2 * np.sin(rad)
        c = Circle((x, y), 0.25, facecolor=CYAN, edgecolor=WHITE, linewidth=1)
        ax.add_patch(c)
        # Connection
        ax.plot([2.5, x], [7.5, y], color=DARK_GRAY, linewidth=1, zorder=1)

    ax.text(2.55, 5.8, "Frontier systems form\ndefensive ring", ha='center',
            fontsize=8, color=LIGHT_GRAY)

    # Example 2: Economic Hub
    ax.add_patch(FancyBboxPatch((5, 5.5), 4.5, 3.8,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor='none', edgecolor=GREEN, linewidth=2))
    ax.text(7.25, 9.0, "Economic Hub", ha='center', fontsize=11,
            fontweight='bold', color=GREEN)

    # Hub center
    hub = Circle((7.25, 7.5), 0.5, facecolor=YELLOW, edgecolor=WHITE, linewidth=1.5)
    ax.add_patch(hub)
    ax.text(7.25, 7.5, "HUB", ha='center', va='center', fontsize=7, color=DARK_BG)

    # Mining systems
    mining_pos = [(6.2, 8.3), (8.3, 8.3), (6.0, 6.8), (8.5, 6.8)]
    for x, y in mining_pos:
        c = Circle((x, y), 0.2, facecolor=GREEN, edgecolor=WHITE, linewidth=1)
        ax.add_patch(c)
        ax.plot([7.25, x], [7.5, y], color=DARK_GRAY, linewidth=1, zorder=1)
        ax.text(x, y, "M", ha='center', va='center', fontsize=6, color=DARK_BG)

    ax.text(7.25, 5.8, "Mining systems feed\ncentral production hub",
            ha='center', fontsize=8, color=LIGHT_GRAY)

    # Example 3: Exploration Frontier
    ax.add_patch(FancyBboxPatch((0.3, 0.8), 4.5, 4.2,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor='none', edgecolor=CYAN, linewidth=2))
    ax.text(2.55, 4.7, "Exploration Frontier", ha='center', fontsize=11,
            fontweight='bold', color=CYAN)

    # Base
    base = Circle((1.5, 3), 0.35, facecolor=GREEN, edgecolor=WHITE, linewidth=1.5)
    ax.add_patch(base)
    ax.text(1.5, 3, "BASE", ha='center', va='center', fontsize=6, color=DARK_BG)

    # Frontier chain
    frontier_pos = [(2.5, 3.5), (3.5, 3), (4, 2), (3.5, 1.5)]
    prev_x, prev_y = 1.5, 3
    for i, (x, y) in enumerate(frontier_pos):
        c = Circle((x, y), 0.2, facecolor=CYAN if i < 2 else LIGHT_GRAY,
                   edgecolor=WHITE, linewidth=1)
        ax.add_patch(c)
        ax.plot([prev_x, x], [prev_y, y], color=DARK_GRAY, linewidth=1, zorder=1)
        if i >= 2:
            ax.text(x + 0.25, y, "?", fontsize=10, color=CYAN)
        prev_x, prev_y = x, y

    ax.text(2.55, 1.0, "Staged exploration from\nsecure base", ha='center',
            fontsize=8, color=LIGHT_GRAY)

    # Example 4: Strategic Chokepoint
    ax.add_patch(FancyBboxPatch((5, 0.8), 4.5, 4.2,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor='none', edgecolor=YELLOW, linewidth=2))
    ax.text(7.25, 4.7, "Strategic Chokepoint", ha='center', fontsize=11,
            fontweight='bold', color=YELLOW)

    # Choke system
    choke = Circle((7.25, 2.8), 0.45, facecolor=RED, edgecolor=WHITE, linewidth=2)
    ax.add_patch(choke)
    ax.text(7.25, 2.8, "GATE", ha='center', va='center', fontsize=7, color=WHITE)

    # Systems on each side
    friendly = [(5.8, 3.5), (5.5, 2.5), (5.8, 1.8)]
    enemy = [(8.7, 3.5), (9, 2.8), (8.7, 2)]

    for x, y in friendly:
        c = Circle((x, y), 0.2, facecolor=GREEN, edgecolor=WHITE, linewidth=1)
        ax.add_patch(c)
        ax.plot([7.25, x], [2.8, y], color=DARK_GRAY, linewidth=1, zorder=1)

    for x, y in enemy:
        c = Circle((x, y), 0.2, facecolor=LIGHT_GRAY, edgecolor=WHITE, linewidth=1)
        ax.add_patch(c)
        ax.plot([7.25, x], [2.8, y], color=DARK_GRAY, linewidth=1, zorder=1)

    ax.text(5.6, 1.3, "Your\nSpace", ha='center', fontsize=7, color=GREEN)
    ax.text(8.9, 1.4, "Unknown", ha='center', fontsize=7, color=LIGHT_GRAY)

    ax.text(7.25, 1.0, "Multiple connections =\nhigh strategic value",
            ha='center', fontsize=8, color=LIGHT_GRAY)

    save_figure(fig, '3-user-interface', '3.5-sector-examples.png')


# ============================================================================
# Issue #1167 - Section 3.5: Fleet Disposition Analysis Flowchart
# ============================================================================
def create_fleet_disposition_flowchart():
    """Create flowchart for analyzing fleet disposition from galactic map."""
    fig, ax = setup_dark_figure(figsize=(14, 11))

    add_title(ax, "Fleet Disposition Analysis Flowchart", y=9.8)

    # Start
    draw_rounded_box(ax, 4, 8.5, 2, 0.6, CYAN, "Open Galactic Map\n(F11)", fontsize=9)

    # Step 1: Identify fleet presence
    ax.annotate('', xy=(5, 7.9), xytext=(5, 8.5),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))
    draw_rounded_box(ax, 3.5, 7.2, 3, 0.6, DARK_GRAY, "Identify Systems with\nFleet Icons", fontsize=9)

    # Branch: Military vs Civilian
    ax.plot([5, 3], [7.2, 6.5], color=WHITE, linewidth=1)
    ax.plot([5, 7], [7.2, 6.5], color=WHITE, linewidth=1)

    draw_rounded_box(ax, 1.5, 5.8, 2.5, 0.6, GREEN, "Military Fleets", fontsize=9)
    draw_rounded_box(ax, 5.8, 5.8, 2.5, 0.6, YELLOW, "Civilian Ships", fontsize=9)

    # Military branch
    ax.annotate('', xy=(2.75, 5.2), xytext=(2.75, 5.8),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))
    draw_rounded_box(ax, 1.5, 4.5, 2.5, 0.6, DARK_GRAY, "Check Coverage:\nFrontier defended?", fontsize=8)

    ax.annotate('', xy=(2.75, 3.9), xytext=(2.75, 4.5),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))

    # Decision diamond (as rectangle)
    ax.add_patch(FancyBboxPatch((1.5, 3.2), 2.5, 0.6,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=YELLOW, edgecolor=WHITE, linewidth=1.5))
    ax.text(2.75, 3.5, "Gaps Found?", ha='center', va='center',
            fontsize=9, color=DARK_BG)

    # Yes branch
    ax.text(0.8, 3.5, "YES", fontsize=8, color=RED, ha='right')
    ax.plot([1.5, 0.8], [3.5, 3.5], color=RED, linewidth=1)
    ax.plot([0.8, 0.8], [3.5, 2.5], color=RED, linewidth=1)
    draw_rounded_box(ax, 0, 1.8, 2, 0.6, RED, "Plan Redeployment\nor New Builds", fontsize=8)

    # No branch
    ax.text(4.2, 3.5, "NO", fontsize=8, color=GREEN, ha='left')
    ax.plot([4, 4.5], [3.5, 3.5], color=GREEN, linewidth=1)
    ax.plot([4.5, 4.5], [3.5, 2.5], color=GREEN, linewidth=1)
    draw_rounded_box(ax, 3.5, 1.8, 2, 0.6, GREEN, "Coverage OK\nMonitor Status", fontsize=8)

    # Civilian branch
    ax.annotate('', xy=(7.05, 5.2), xytext=(7.05, 5.8),
                arrowprops=dict(arrowstyle='->', color=YELLOW, lw=1.5))
    draw_rounded_box(ax, 5.8, 4.5, 2.5, 0.6, DARK_GRAY, "Verify Trade Routes:\nNo hostile systems?", fontsize=8)

    ax.annotate('', xy=(7.05, 3.9), xytext=(7.05, 4.5),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))

    # Decision
    ax.add_patch(FancyBboxPatch((5.8, 3.2), 2.5, 0.6,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=YELLOW, edgecolor=WHITE, linewidth=1.5))
    ax.text(7.05, 3.5, "Routes Safe?", ha='center', va='center',
            fontsize=9, color=DARK_BG)

    # No branch
    ax.text(8.5, 3.5, "NO", fontsize=8, color=RED, ha='left')
    ax.plot([8.3, 9], [3.5, 3.5], color=RED, linewidth=1)
    ax.plot([9, 9], [3.5, 2.5], color=RED, linewidth=1)
    draw_rounded_box(ax, 8, 1.8, 2, 0.6, RED, "Set Military\nRestrictions", fontsize=8)

    # Yes branch
    ax.text(5.6, 3.5, "YES", fontsize=8, color=GREEN, ha='right')
    ax.plot([5.8, 5.2], [3.5, 3.5], color=GREEN, linewidth=1)
    ax.plot([5.2, 5.2], [3.5, 2.2], color=GREEN, linewidth=1)
    ax.plot([5.2, 5.5], [2.2, 2.2], color=GREEN, linewidth=1)

    # Response time analysis section
    ax.add_patch(FancyBboxPatch((0.5, 0.3), 9, 1.2,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=DARK_GRAY, edgecolor=CYAN, linewidth=1))
    ax.text(5, 1.2, "Response Time Analysis", ha='center', fontsize=10,
            fontweight='bold', color=CYAN)

    ax.text(0.8, 0.8, "- Click system to see distance from nearest military fleet",
            fontsize=8, color=LIGHT_GRAY)
    ax.text(0.8, 0.5, "- Calculate transit time: Distance / Fleet Speed = Response Time",
            fontsize=8, color=LIGHT_GRAY)
    ax.text(5.5, 0.65, "- Flag systems with response time > 30 days for patrol coverage",
            fontsize=8, color=YELLOW)

    save_figure(fig, '3-user-interface', '3.5-fleet-disposition.png')


# ============================================================================
# Main execution
# ============================================================================
def main():
    """Generate all Wave 7 diagrams."""
    print("Generating Wave 7: UI & Interface Diagrams")
    print("=" * 50)

    # Issue #1123
    print("\n#1123: Starting Ship Designs Infographic")
    create_starting_ships_infographic()

    # Issue #1139
    print("\n#1139: Economics Window Tab Organization")
    create_economics_tabs_diagram()

    # Issue #1141
    print("\n#1141: Interrupt Events Decision Tree")
    create_interrupt_decision_tree()

    # Issue #1144
    print("\n#1144: Display Toggles Reference Card")
    create_display_toggles_card()

    # Issue #1146
    print("\n#1146: Zoom Level Use Cases")
    create_zoom_levels_diagram()

    # Issue #1149
    print("\n#1149: Click Interaction Flowchart")
    create_click_flowchart()

    # Issue #1152
    print("\n#1152: Keyboard Shortcut Reference Card")
    create_keyboard_shortcuts_card()

    # Issue #1159
    print("\n#1159: Event Type Categories Visual Glossary")
    create_event_glossary()

    # Issue #1162
    print("\n#1162: Event Filtering Strategy Guide")
    create_event_filtering_guide()

    # Issue #1163
    print("\n#1163: System Node Color Reference Card")
    create_system_colors_card()

    # Issue #1165
    print("\n#1165: Sector Organization Examples")
    create_sector_examples()

    # Issue #1167
    print("\n#1167: Fleet Disposition Analysis Flowchart")
    create_fleet_disposition_flowchart()

    print("\n" + "=" * 50)
    print("All diagrams generated successfully!")


if __name__ == '__main__':
    main()
