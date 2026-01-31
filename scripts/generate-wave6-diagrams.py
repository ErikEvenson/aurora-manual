#!/usr/bin/env python3
"""
Generate Wave 6: Game Setup Diagrams for Aurora Manual
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge
from matplotlib.lines import Line2D
import numpy as np
import os

# Dark theme colors
BG_COLOR = '#1a1a2e'
CYAN = '#4ecdc4'
RED = '#ff6b6b'
YELLOW = '#ffe66d'
GREEN = '#95d5b2'
WHITE = '#ffffff'
GRAY = '#6c757d'
DARK_GRAY = '#2d3748'
PURPLE = '#a78bfa'
ORANGE = '#f59e0b'

# Ensure output directory exists
os.makedirs('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/1-introduction', exist_ok=True)
os.makedirs('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/2-game-setup', exist_ok=True)


def set_dark_theme(ax, fig):
    """Apply dark theme to figure and axes"""
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.tick_params(colors=WHITE)
    for spine in ax.spines.values():
        spine.set_color(GRAY)


def add_text_box(ax, x, y, text, width=0.15, height=0.08, color=CYAN, fontsize=9):
    """Add a rounded text box"""
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.01,rounding_size=0.02",
                         facecolor=color, edgecolor=WHITE, linewidth=1.5, alpha=0.9)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=WHITE if color not in [YELLOW] else BG_COLOR, fontweight='bold', wrap=True)


def draw_arrow(ax, start, end, color=WHITE):
    """Draw an arrow between two points"""
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=2))


def create_vb6_vs_csharp_comparison():
    """Issue #1043: VB6 vs C# Feature Comparison"""
    fig, ax = plt.subplots(figsize=(12, 8))
    set_dark_theme(ax, fig)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(6, 7.5, 'Aurora VB6 vs C# Comparison', ha='center', va='center',
            fontsize=18, color=WHITE, fontweight='bold')

    # Headers
    ax.text(3, 6.8, 'VB6 Aurora (2004-2012)', ha='center', va='center',
            fontsize=14, color=RED, fontweight='bold')
    ax.text(9, 6.8, 'C# Aurora (2020-present)', ha='center', va='center',
            fontsize=14, color=GREEN, fontweight='bold')

    # Divider line
    ax.axvline(x=6, ymin=0.1, ymax=0.82, color=GRAY, linewidth=2, linestyle='--')

    categories = [
        ('Database', 'Microsoft Access', 'SQLite', 6.2),
        ('Performance', 'Limited, lag with\nlarge games', 'Significantly improved\nNPR processing', 5.4),
        ('Interface', 'Tabbed forms', 'Multi-window\nfreely positionable', 4.6),
        ('Platform', 'Windows only\n32-bit', 'Windows\n64-bit compatible', 3.8),
        ('Ground Combat', 'Basic system', 'Redesigned with\nplayer formations', 3.0),
        ('Diplomacy', 'Diplomatic teams', 'New diplomacy\nmodule', 2.2),
        ('NPR AI', 'Functional', 'Enhanced\ndecision-making', 1.4),
        ('Development', 'Ceased 2012', 'Active updates', 0.6),
    ]

    for cat, vb6, csharp, y in categories:
        # Category label
        ax.text(6, y, cat, ha='center', va='center', fontsize=10, color=YELLOW, fontweight='bold')

        # VB6 feature box
        box_vb6 = FancyBboxPatch((0.8, y - 0.25), 4, 0.5,
                                  boxstyle="round,pad=0.02,rounding_size=0.05",
                                  facecolor=DARK_GRAY, edgecolor=RED, linewidth=1.5)
        ax.add_patch(box_vb6)
        ax.text(2.8, y, vb6, ha='center', va='center', fontsize=9, color=WHITE)

        # C# feature box
        box_cs = FancyBboxPatch((6.8, y - 0.25), 4.4, 0.5,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=DARK_GRAY, edgecolor=GREEN, linewidth=1.5)
        ax.add_patch(box_cs)
        ax.text(9, y, csharp, ha='center', va='center', fontsize=9, color=WHITE)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/1-introduction/1.1-vb6-vs-csharp.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 1.1-vb6-vs-csharp.png")


def create_community_resources_map():
    """Issue #1044: Community Resources Network Map"""
    fig, ax = plt.subplots(figsize=(10, 10))
    set_dark_theme(ax, fig)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axis('off')

    # Title
    ax.text(0, 4.5, 'Aurora Community Resources', ha='center', va='center',
            fontsize=16, color=WHITE, fontweight='bold')

    # Central node - Aurora Forums
    central = Circle((0, 0), 0.8, facecolor=CYAN, edgecolor=WHITE, linewidth=2)
    ax.add_patch(central)
    ax.text(0, 0, 'Aurora\nForums', ha='center', va='center', fontsize=11,
            color=BG_COLOR, fontweight='bold')
    ax.text(0, -1.1, '(Official)', ha='center', va='center', fontsize=8, color=CYAN)

    # Satellite resources
    resources = [
        (3, 2.5, 'AuroraWiki', GREEN, ['Mechanics', 'Formulas', 'Tutorials']),
        (3, -2.5, 'YouTube', RED, ['Video Tutorials', 'Let\'s Plays', 'Guides']),
        (-3, 2.5, 'Reddit', ORANGE, ['r/aurora4x', 'Quick Help', 'Discussion']),
        (-3, -2.5, 'Discord', PURPLE, ['Real-time Chat', 'Community', 'Support']),
        (0, 3.2, 'This Manual', YELLOW, ['Reference', 'Verified Info', 'Examples']),
        (0, -3.2, 'Game Files', GRAY, ['Database', 'Patches', 'Downloads']),
    ]

    for x, y, name, color, items in resources:
        # Node circle
        node = Circle((x, y), 0.6, facecolor=color, edgecolor=WHITE, linewidth=2, alpha=0.9)
        ax.add_patch(node)
        text_color = BG_COLOR if color in [YELLOW, GREEN, ORANGE] else WHITE
        ax.text(x, y, name, ha='center', va='center', fontsize=9,
                color=text_color, fontweight='bold')

        # Connection line to center
        ax.plot([0, x], [0, y], color=color, linewidth=2, alpha=0.5, linestyle='-')

        # Items list
        item_text = '\n'.join(items)
        text_x = x + 1.2 if x > 0 else x - 1.2 if x < 0 else x
        text_y = y + 0.9 if y > 0 else y - 0.9 if y < 0 else y
        ha = 'left' if x > 0 else 'right' if x < 0 else 'center'
        ax.text(text_x, text_y, item_text, ha=ha, va='center', fontsize=7, color=color)

    # Cross-connections (some resources link to each other)
    connections = [
        ((3, 2.5), (0, 3.2), GRAY),  # Wiki to Manual
        ((-3, 2.5), (0, 3.2), GRAY),  # Reddit to Manual
        ((3, -2.5), (3, 2.5), GRAY),  # YouTube to Wiki
    ]
    for start, end, color in connections:
        ax.plot([start[0], end[0]], [start[1], end[1]],
                color=color, linewidth=1, alpha=0.3, linestyle='--')

    # Legend
    ax.text(-4.5, -4.5, 'Solid lines: Primary connection to forums\nDashed: Cross-references',
            ha='left', va='bottom', fontsize=8, color=GRAY)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/1-introduction/1.1-community-resources.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 1.1-community-resources.png")


def create_folder_structure():
    """Issue #1046: Installation Folder Structure Diagram"""
    fig, ax = plt.subplots(figsize=(8, 10))
    set_dark_theme(ax, fig)
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(4, 9.5, 'Aurora Installation Folder Structure', ha='center', va='center',
            fontsize=14, color=WHITE, fontweight='bold')

    # Folder tree
    tree = [
        (0, 8.8, 'Aurora/', CYAN, 'Root installation folder'),
        (1, 8.2, 'Aurora.exe', GREEN, 'Main executable'),
        (1, 7.6, 'AuroraDB.db', YELLOW, 'Game database (YOUR SAVE)'),
        (1, 7.0, 'AuroraDB.db-journal', GRAY, 'Transaction log (auto)'),
        (1, 6.4, 'Aurora.exe.config', GRAY, '.NET configuration'),
        (1, 5.8, '*.dll', GRAY, 'Runtime dependencies'),
        (1, 5.2, 'Flags/', CYAN, 'Race flag images'),
        (2, 4.8, '*.png', GRAY, 'Flag image files'),
        (1, 4.2, 'Maps/', CYAN, 'System map backgrounds'),
        (2, 3.8, '*.png', GRAY, 'Map image files'),
        (1, 3.2, 'Hulls/', CYAN, 'Ship hull images'),
        (2, 2.8, '*.png', GRAY, 'Hull silhouettes'),
        (1, 2.2, 'Portraits/', CYAN, 'Race portraits'),
        (2, 1.8, '*.png', GRAY, 'Portrait images'),
        (1, 1.2, 'Stations/', CYAN, 'Station images'),
        (2, 0.8, '*.png', GRAY, 'Station silhouettes'),
    ]

    for indent, y, name, color, desc in tree:
        x = 0.5 + indent * 0.8
        # Draw tree lines
        if indent > 0:
            ax.plot([x - 0.4, x - 0.1], [y, y], color=GRAY, linewidth=1)
            ax.plot([x - 0.4, x - 0.4], [y, y + 0.4], color=GRAY, linewidth=1)

        # File/folder name
        ax.text(x, y, name, ha='left', va='center', fontsize=10, color=color, fontweight='bold')

        # Description
        ax.text(4.5, y, desc, ha='left', va='center', fontsize=9, color=GRAY)

    # Important callouts
    callout_box = FancyBboxPatch((5, 7.3), 2.5, 0.8,
                                  boxstyle="round,pad=0.02,rounding_size=0.05",
                                  facecolor=DARK_GRAY, edgecolor=YELLOW, linewidth=2)
    ax.add_patch(callout_box)
    ax.text(6.25, 7.7, 'BACKUP THIS FILE!', ha='center', va='center',
            fontsize=10, color=YELLOW, fontweight='bold')
    ax.text(6.25, 7.5, 'All game data lives here', ha='center', va='center',
            fontsize=8, color=WHITE)
    ax.annotate('', xy=(3.5, 7.6), xytext=(5, 7.5),
                arrowprops=dict(arrowstyle='->', color=YELLOW, lw=2))

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/1-introduction/1.2-folder-structure.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 1.2-folder-structure.png")


def create_backup_flowchart():
    """Issue #1052: Backup Strategy Flowchart"""
    fig, ax = plt.subplots(figsize=(10, 12))
    set_dark_theme(ax, fig)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Title
    ax.text(5, 11.5, 'Aurora Backup Strategy', ha='center', va='center',
            fontsize=16, color=WHITE, fontweight='bold')

    # When to backup section
    ax.text(2.5, 10.5, 'WHEN TO BACKUP', ha='center', va='center',
            fontsize=12, color=CYAN, fontweight='bold')

    when_items = [
        (2.5, 9.8, 'Before applying patches', YELLOW),
        (2.5, 9.3, 'Before major battles', RED),
        (2.5, 8.8, 'Before risky decisions', ORANGE),
        (2.5, 8.3, 'Every few play sessions', GREEN),
        (2.5, 7.8, 'Before starting new game', GRAY),
    ]

    for x, y, text, color in when_items:
        bullet = Circle((x - 1.5, y), 0.08, facecolor=color, edgecolor=color)
        ax.add_patch(bullet)
        ax.text(x, y, text, ha='center', va='center', fontsize=10, color=color)

    # What to backup section
    ax.text(7.5, 10.5, 'WHAT TO BACKUP', ha='center', va='center',
            fontsize=12, color=CYAN, fontweight='bold')

    what_box = FancyBboxPatch((5.5, 8.5), 4, 1.8,
                               boxstyle="round,pad=0.02,rounding_size=0.05",
                               facecolor=DARK_GRAY, edgecolor=YELLOW, linewidth=2)
    ax.add_patch(what_box)
    ax.text(7.5, 9.7, 'AuroraDB.db', ha='center', va='center',
            fontsize=11, color=YELLOW, fontweight='bold')
    ax.text(7.5, 9.2, 'This single file contains:', ha='center', va='center',
            fontsize=9, color=WHITE)
    ax.text(7.5, 8.8, 'All game state, ships, colonies,\nresearch, NPRs, everything',
            ha='center', va='center', fontsize=8, color=GRAY)

    # Backup flowchart
    ax.text(5, 7, 'BACKUP PROCESS', ha='center', va='center',
            fontsize=12, color=CYAN, fontweight='bold')

    # Flow boxes
    steps = [
        (2, 6, 'Save game in Aurora\n(Click disk icon)', GREEN),
        (2, 4.5, 'Close Aurora\n(optional but safe)', GRAY),
        (2, 3, 'Copy AuroraDB.db\nto backup folder', YELLOW),
        (2, 1.5, 'Name with date:\nAuroraDB_2050-01-01.db', CYAN),
    ]

    for i, (x, y, text, color) in enumerate(steps):
        box = FancyBboxPatch((x - 1.3, y - 0.5), 2.6, 1,
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=DARK_GRAY, edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, color=WHITE)

        # Number badge
        badge = Circle((x - 1.1, y + 0.35), 0.15, facecolor=color, edgecolor=WHITE)
        ax.add_patch(badge)
        ax.text(x - 1.1, y + 0.35, str(i + 1), ha='center', va='center',
                fontsize=9, color=BG_COLOR, fontweight='bold')

        # Arrow to next
        if i < len(steps) - 1:
            ax.annotate('', xy=(x, y - 0.6), xytext=(x, y - 0.9),
                        arrowprops=dict(arrowstyle='->', color=color, lw=2))

    # Restore section
    ax.text(7.5, 6, 'RESTORE PROCESS', ha='center', va='center',
            fontsize=12, color=CYAN, fontweight='bold')

    restore_steps = [
        (7.5, 5, 'Close Aurora\ncompletely', RED),
        (7.5, 3.5, 'Replace AuroraDB.db\nwith backup copy', YELLOW),
        (7.5, 2, 'Restart Aurora', GREEN),
    ]

    for i, (x, y, text, color) in enumerate(restore_steps):
        box = FancyBboxPatch((x - 1.3, y - 0.5), 2.6, 1,
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=DARK_GRAY, edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, color=WHITE)

        if i < len(restore_steps) - 1:
            ax.annotate('', xy=(x, y - 0.6), xytext=(x, y - 0.9),
                        arrowprops=dict(arrowstyle='->', color=color, lw=2))

    # Warning box
    warn_box = FancyBboxPatch((1, 0.2), 8, 0.8,
                               boxstyle="round,pad=0.02,rounding_size=0.05",
                               facecolor=DARK_GRAY, edgecolor=RED, linewidth=2)
    ax.add_patch(warn_box)
    ax.text(5, 0.6, 'Keep 2-3 rolling backups in case corruption is not immediately noticed',
            ha='center', va='center', fontsize=10, color=RED)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/1-introduction/1.2-backup-strategy.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 1.2-backup-strategy.png")


def create_first_steps_workflow():
    """Issue #1064: First Steps Workflow Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    set_dark_theme(ax, fig)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'First Steps: Your First 30 Minutes in Aurora', ha='center', va='center',
            fontsize=16, color=WHITE, fontweight='bold')

    # Main flow
    steps = [
        (2, 8, 'START', 'Create New Game', GREEN, ['Accept defaults', 'TN Start recommended']),
        (6, 8, 'SETUP', 'Open Key Windows', CYAN, ['System Map (F9)', 'Economics (F2)', 'Research (F5)']),
        (10, 8, 'RESEARCH', 'Assign Scientists', YELLOW, ['Pick 2-3 projects', 'Propulsion priority']),
        (2, 5, 'SURVEY', 'Start System Survey', GREEN, ['Find jump points', 'Locate minerals']),
        (6, 5, 'BUILD', 'Queue Production', CYAN, ['More mines', 'More factories']),
        (10, 5, 'DESIGN', 'First Ship Design', YELLOW, ['Fuel harvester', 'Survey ship']),
        (6, 2, 'EXPLORE', 'Transit Jump Points', GREEN, ['Discover new systems', 'Find new worlds']),
    ]

    for x, y, label, action, color, details in steps:
        # Main box
        box = FancyBboxPatch((x - 1.5, y - 0.8), 3, 1.6,
                              boxstyle="round,pad=0.02,rounding_size=0.08",
                              facecolor=DARK_GRAY, edgecolor=color, linewidth=2)
        ax.add_patch(box)

        # Label badge
        badge = FancyBboxPatch((x - 1.4, y + 0.5), 1.2, 0.3,
                                boxstyle="round,pad=0.01,rounding_size=0.02",
                                facecolor=color, edgecolor=color)
        ax.add_patch(badge)
        text_color = BG_COLOR if color in [YELLOW, GREEN] else WHITE
        ax.text(x - 0.8, y + 0.65, label, ha='center', va='center',
                fontsize=8, color=text_color, fontweight='bold')

        # Action text
        ax.text(x, y, action, ha='center', va='center',
                fontsize=10, color=WHITE, fontweight='bold')

        # Details
        detail_text = '\n'.join(details)
        ax.text(x, y - 0.4, detail_text, ha='center', va='center',
                fontsize=8, color=GRAY)

    # Arrows
    arrows = [
        ((3.5, 8), (4.5, 8)),  # Start to Setup
        ((7.5, 8), (8.5, 8)),  # Setup to Research
        ((2, 7.2), (2, 5.8)),  # Start down to Survey
        ((6, 7.2), (6, 5.8)),  # Setup down to Build
        ((10, 7.2), (10, 5.8)),  # Research down to Design
        ((3.5, 5), (4.5, 5)),  # Survey to Build
        ((7.5, 5), (8.5, 5)),  # Build to Design
        ((6, 4.2), (6, 2.8)),  # Build down to Explore
    ]

    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))

    # Decision diamond
    diamond_x, diamond_y = 12.5, 5
    diamond = plt.Polygon([(diamond_x, diamond_y + 0.6), (diamond_x + 0.6, diamond_y),
                           (diamond_x, diamond_y - 0.6), (diamond_x - 0.6, diamond_y)],
                          facecolor=ORANGE, edgecolor=WHITE, linewidth=2)
    ax.add_patch(diamond)
    ax.text(diamond_x, diamond_y, 'Ready\nfor\nCombat?', ha='center', va='center',
            fontsize=7, color=BG_COLOR, fontweight='bold')

    ax.annotate('', xy=(11.9, 5), xytext=(11.5, 5),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))

    # Tips box
    tips_box = FancyBboxPatch((10, 1), 3.5, 2,
                               boxstyle="round,pad=0.02,rounding_size=0.05",
                               facecolor=DARK_GRAY, edgecolor=PURPLE, linewidth=2)
    ax.add_patch(tips_box)
    ax.text(11.75, 2.6, 'Tips', ha='center', va='center',
            fontsize=10, color=PURPLE, fontweight='bold')
    tips = ['Use short time increments', 'Check Event Log often',
            'Save frequently!', 'First game is for learning']
    for i, tip in enumerate(tips):
        ax.text(11.75, 2.2 - i * 0.3, f'- {tip}', ha='center', va='center',
                fontsize=8, color=WHITE)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/1-introduction/1.3-first-steps.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 1.3-first-steps.png")


def create_npr_generation_flowchart():
    """Issue #1073: NPR Generation Flowchart"""
    fig, ax = plt.subplots(figsize=(12, 14))
    set_dark_theme(ax, fig)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 14)
    ax.axis('off')

    # Title
    ax.text(6, 13.5, 'NPR (Non-Player Race) Generation', ha='center', va='center',
            fontsize=16, color=WHITE, fontweight='bold')

    # Trigger section
    ax.text(6, 12.5, 'TRIGGER CONDITIONS', ha='center', va='center',
            fontsize=12, color=CYAN, fontweight='bold')

    # Start box
    start_box = FancyBboxPatch((4.5, 11.3), 3, 0.8,
                                boxstyle="round,pad=0.02,rounding_size=0.05",
                                facecolor=GREEN, edgecolor=WHITE, linewidth=2)
    ax.add_patch(start_box)
    ax.text(6, 11.7, 'Ship Transits Jump Point\nto Unexplored System',
            ha='center', va='center', fontsize=9, color=BG_COLOR, fontweight='bold')

    # Decision diamond
    def draw_diamond(x, y, text, color=ORANGE):
        diamond = plt.Polygon([(x, y + 0.5), (x + 0.7, y), (x, y - 0.5), (x - 0.7, y)],
                              facecolor=color, edgecolor=WHITE, linewidth=2)
        ax.add_patch(diamond)
        ax.text(x, y, text, ha='center', va='center', fontsize=8, color=BG_COLOR, fontweight='bold')

    # Player vs NPR exploration
    draw_diamond(3, 10, 'Player\nShip?')
    ax.annotate('', xy=(3, 10.5), xytext=(4.8, 11.3),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))

    # Player path
    ax.text(1.5, 10, 'YES', ha='center', va='center', fontsize=8, color=GREEN)
    player_box = FancyBboxPatch((0.3, 9), 2.4, 0.6,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=DARK_GRAY, edgecolor=CYAN, linewidth=1.5)
    ax.add_patch(player_box)
    ax.text(1.5, 9.3, '30% NPR Chance\n(default)', ha='center', va='center', fontsize=8, color=CYAN)
    ax.annotate('', xy=(1.5, 9), xytext=(2.3, 9.7),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))

    # NPR path
    ax.text(4.5, 10, 'NO', ha='center', va='center', fontsize=8, color=RED)
    npr_box = FancyBboxPatch((4.3, 9), 2.4, 0.6,
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=DARK_GRAY, edgecolor=RED, linewidth=1.5)
    ax.add_patch(npr_box)
    ax.text(5.5, 9.3, '10% NPR Chance\n(NPR exploration)', ha='center', va='center', fontsize=8, color=RED)
    ax.annotate('', xy=(4.5, 9.6), xytext=(3.7, 10),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))

    # Chance check
    draw_diamond(3, 8, 'Roll\nSucceeds?')
    ax.annotate('', xy=(1.5, 8.5), xytext=(1.5, 8.9),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))
    ax.annotate('', xy=(4.2, 8.5), xytext=(5.5, 9),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))

    # No NPR path
    ax.text(4.5, 8, 'NO', ha='center', va='center', fontsize=8, color=RED)
    no_npr = FancyBboxPatch((5, 7.5), 2.5, 0.6,
                             boxstyle="round,pad=0.02,rounding_size=0.05",
                             facecolor=DARK_GRAY, edgecolor=GRAY, linewidth=1.5)
    ax.add_patch(no_npr)
    ax.text(6.25, 7.8, 'Empty System\n(No NPR Generated)', ha='center', va='center', fontsize=8, color=GRAY)
    ax.annotate('', xy=(5, 7.8), xytext=(3.7, 8),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))

    # Yes - Generate NPR
    ax.text(1.5, 8, 'YES', ha='center', va='center', fontsize=8, color=GREEN)
    ax.annotate('', xy=(3, 7), xytext=(3, 7.5),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))

    # Tech Level section
    ax.text(6, 6.5, 'TECH LEVEL DETERMINATION', ha='center', va='center',
            fontsize=12, color=CYAN, fontweight='bold')

    tech_levels = [
        (1.5, 5.5, 'Pre-Industrial', '0% default', PURPLE),
        (4, 5.5, 'Industrial', '0% default', ORANGE),
        (6.5, 5.5, 'Minor TN', '25% default', YELLOW),
        (9.5, 5.5, 'Major TN', '75% default', GREEN),
    ]

    for x, y, name, chance, color in tech_levels:
        box = FancyBboxPatch((x - 1, y - 0.4), 2, 0.8,
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=DARK_GRAY, edgecolor=color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y + 0.1, name, ha='center', va='center', fontsize=9, color=color, fontweight='bold')
        ax.text(x, y - 0.15, chance, ha='center', va='center', fontsize=7, color=GRAY)

    ax.annotate('', xy=(3, 5.9), xytext=(3, 6.3),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=2))

    # Hostility section
    ax.text(6, 4.5, 'DISPOSITION MODIFIERS', ha='center', va='center',
            fontsize=12, color=CYAN, fontweight='bold')

    hostility_box = FancyBboxPatch((2, 3.2), 8, 1,
                                    boxstyle="round,pad=0.02,rounding_size=0.05",
                                    facecolor=DARK_GRAY, edgecolor=RED, linewidth=1.5)
    ax.add_patch(hostility_box)
    ax.text(6, 3.9, 'Hostility Modifier adds to Xenophobia + Militancy',
            ha='center', va='center', fontsize=9, color=RED)
    ax.text(6, 3.5, 'and subtracts from Diplomacy + Trade',
            ha='center', va='center', fontsize=9, color=WHITE)

    # Starting conditions
    ax.text(6, 2.5, 'STARTING CONDITIONS', ha='center', va='center',
            fontsize=12, color=CYAN, fontweight='bold')

    conditions = [
        (2.5, 1.5, 'Population\n(scales with player)', GREEN),
        (5.5, 1.5, 'Explored Systems\n(Base + Random)', YELLOW),
        (8.5, 1.5, 'Industry & Research\n(scales with pop)', CYAN),
    ]

    for x, y, text, color in conditions:
        box = FancyBboxPatch((x - 1.2, y - 0.5), 2.4, 1,
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=DARK_GRAY, edgecolor=color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=8, color=WHITE)

    # Difficulty modifier note
    diff_box = FancyBboxPatch((1, 0.3), 10, 0.6,
                               boxstyle="round,pad=0.02,rounding_size=0.05",
                               facecolor=DARK_GRAY, edgecolor=PURPLE, linewidth=1.5)
    ax.add_patch(diff_box)
    ax.text(6, 0.6, 'Difficulty Modifier (100 = Normal) scales NPR population, research rate, and growth',
            ha='center', va='center', fontsize=9, color=PURPLE)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/2-game-setup/2.1-npr-generation.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 2.1-npr-generation.png")


def create_government_decision_tree():
    """Issue #1093: Government Type Decision Tree"""
    fig, ax = plt.subplots(figsize=(14, 12))
    set_dark_theme(ax, fig)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Title
    ax.text(7, 11.5, 'Government Type Selection Guide', ha='center', va='center',
            fontsize=16, color=WHITE, fontweight='bold')

    # Start
    start = FancyBboxPatch((5.5, 10.2), 3, 0.8,
                            boxstyle="round,pad=0.02,rounding_size=0.08",
                            facecolor=GREEN, edgecolor=WHITE, linewidth=2)
    ax.add_patch(start)
    ax.text(7, 10.6, 'What is your\nplaystyle focus?', ha='center', va='center',
            fontsize=10, color=BG_COLOR, fontweight='bold')

    # Main branches
    branches = [
        (2.5, 8.5, 'Military\nConquest', RED, [
            ('Military Dictatorship', '+20 Militancy, +30% Shipyards'),
            ('Fascist', '+30 Militancy, 40% Heavy Armor'),
            ('Autocracy', '+15 Militancy, Balanced'),
        ]),
        (7, 8.5, 'Economic\nGrowth', YELLOW, [
            ('Corporate Government', '+30% Mines'),
            ('Representative Democracy', '+15 Trade, +10 Diplomacy'),
            ('Meritocracy', '+20 Diplomacy, Balanced'),
        ]),
        (11.5, 8.5, 'Research\nFocus', CYAN, [
            ('Contemplative', '+40% Labs, -Military'),
            ('Meritocracy', 'Balanced with bonus'),
        ]),
    ]

    for x, y, label, color, options in branches:
        # Branch box
        box = FancyBboxPatch((x - 1.3, y - 0.5), 2.6, 1,
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=DARK_GRAY, edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=10, color=color, fontweight='bold')

        # Arrow from start
        ax.annotate('', xy=(x, y + 0.5), xytext=(7, 10.2),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))

        # Options
        for i, (name, desc) in enumerate(options):
            opt_y = y - 1.5 - i * 1.2
            opt_box = FancyBboxPatch((x - 1.5, opt_y - 0.4), 3, 0.8,
                                      boxstyle="round,pad=0.02,rounding_size=0.05",
                                      facecolor=DARK_GRAY, edgecolor=color, linewidth=1, alpha=0.7)
            ax.add_patch(opt_box)
            ax.text(x, opt_y + 0.1, name, ha='center', va='center', fontsize=9, color=WHITE, fontweight='bold')
            ax.text(x, opt_y - 0.15, desc, ha='center', va='center', fontsize=7, color=GRAY)

            # Arrow
            if i == 0:
                ax.annotate('', xy=(x, opt_y + 0.4), xytext=(x, y - 0.5),
                            arrowprops=dict(arrowstyle='->', color=color, lw=1.5))
            else:
                ax.annotate('', xy=(x, opt_y + 0.4), xytext=(x, opt_y + 0.8),
                            arrowprops=dict(arrowstyle='->', color=color, lw=1))

    # Beginner recommendation
    beginner_box = FancyBboxPatch((4, 1), 6, 1.5,
                                   boxstyle="round,pad=0.02,rounding_size=0.08",
                                   facecolor=DARK_GRAY, edgecolor=GREEN, linewidth=2)
    ax.add_patch(beginner_box)
    ax.text(7, 2.1, 'BEGINNER RECOMMENDATION', ha='center', va='center',
            fontsize=10, color=GREEN, fontweight='bold')
    ax.text(7, 1.6, 'Player Race (default) or Representative Democracy',
            ha='center', va='center', fontsize=10, color=WHITE)
    ax.text(7, 1.3, 'Balanced modifiers, good for learning all systems',
            ha='center', va='center', fontsize=8, color=GRAY)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/2-game-setup/2.2-government-decision-tree.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 2.2-government-decision-tree.png")


def create_mineral_production_chain():
    """Issue #1100: Mineral Production Chain Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    set_dark_theme(ax, fig)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Mineral Production Chain', ha='center', va='center',
            fontsize=16, color=WHITE, fontweight='bold')

    # Minerals with their uses
    minerals = [
        ('Duranium', 0.8, 7.5, GRAY, ['Armor', 'Structure', 'Basic Construction']),
        ('Neutronium', 2.4, 7.5, GRAY, ['Advanced Armor', 'Heavy Structure']),
        ('Corbomite', 4.0, 7.5, PURPLE, ['Shields', 'Specialized Armor']),
        ('Tritanium', 5.6, 7.5, ORANGE, ['Engines', 'Reactors']),
        ('Boronide', 7.2, 7.5, GREEN, ['Engines', 'Refineries']),
        ('Mercassium', 8.8, 7.5, CYAN, ['Sensors', 'Fire Control']),
        ('Vendarite', 10.4, 7.5, YELLOW, ['Electronics', 'Fighters']),
        ('Sorium', 0.8, 5.5, RED, ['FUEL (Refine)', 'Fuel Components']),
        ('Uridium', 2.4, 5.5, PURPLE, ['Beam Weapons', 'Sensors']),
        ('Corundium', 4.0, 5.5, ORANGE, ['Missiles', 'Mines']),
        ('Gallicite', 5.6, 5.5, YELLOW, ['ENGINES (Critical)', 'Jump Drives']),
    ]

    for name, x, y, color, uses in minerals:
        # Mineral box
        box = FancyBboxPatch((x - 0.7, y - 0.4), 1.4, 0.8,
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=DARK_GRAY, edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y + 0.1, name, ha='center', va='center', fontsize=8, color=color, fontweight='bold')

        # Uses below
        use_text = '\n'.join(uses)
        ax.text(x, y - 0.7, use_text, ha='center', va='top', fontsize=6, color=GRAY)

    # Mining section
    ax.text(11, 7.5, 'EXTRACTION', ha='center', va='center', fontsize=10, color=CYAN, fontweight='bold')

    mining_items = [
        ('Mines', '10 tons/year\nper mine', 11, 6.8),
        ('Auto Mines', 'No pop needed\n240 BP cost', 11, 5.8),
        ('Mining Ships', 'Remote mining\nAsteroid access', 11, 4.8),
    ]

    for name, desc, x, y in mining_items:
        box = FancyBboxPatch((x - 0.8, y - 0.4), 1.6, 0.8,
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=DARK_GRAY, edgecolor=GREEN, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y + 0.1, name, ha='center', va='center', fontsize=8, color=GREEN, fontweight='bold')
        ax.text(x, y - 0.1, desc, ha='center', va='center', fontsize=6, color=GRAY)

    # Production section
    ax.text(7, 3.5, 'PRODUCTION', ha='center', va='center', fontsize=12, color=CYAN, fontweight='bold')

    production = [
        ('Construction\nFactories', 'Build\nInstallations', 2, 2.5, GREEN),
        ('Ordnance\nFactories', 'Build\nMissiles', 4, 2.5, RED),
        ('Fighter\nFactories', 'Build\nFighters', 6, 2.5, ORANGE),
        ('Shipyards', 'Build\nShips', 8, 2.5, CYAN),
        ('Fuel\nRefineries', 'Sorium to\nFuel', 10, 2.5, YELLOW),
    ]

    for name, output, x, y, color in production:
        box = FancyBboxPatch((x - 0.9, y - 0.6), 1.8, 1.2,
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=DARK_GRAY, edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y + 0.2, name, ha='center', va='center', fontsize=8, color=color, fontweight='bold')
        ax.text(x, y - 0.25, output, ha='center', va='center', fontsize=7, color=WHITE)

    # Arrows from minerals to production
    ax.annotate('', xy=(4, 3.1), xytext=(4, 4.4),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=2, connectionstyle="arc3,rad=0"))

    # Bottleneck warning
    warn_box = FancyBboxPatch((1, 0.5), 12, 1,
                               boxstyle="round,pad=0.02,rounding_size=0.05",
                               facecolor=DARK_GRAY, edgecolor=RED, linewidth=2)
    ax.add_patch(warn_box)
    ax.text(7, 1.2, 'COMMON BOTTLENECKS', ha='center', va='center',
            fontsize=10, color=RED, fontweight='bold')
    ax.text(7, 0.8, 'Gallicite (engines) | Sorium (fuel) | Duranium (everything) - Monitor these closely!',
            ha='center', va='center', fontsize=9, color=WHITE)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/2-game-setup/2.3-mineral-production-chain.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 2.3-mineral-production-chain.png")


def create_binary_trinary_visualization():
    """Issue #1102: Binary/Trinary System Visualization"""
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.patch.set_facecolor(BG_COLOR)

    titles = ['Single Star System', 'Binary Star System', 'Trinary Star System']

    for idx, ax in enumerate(axes):
        ax.set_facecolor(BG_COLOR)
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(titles[idx], color=WHITE, fontsize=12, fontweight='bold', pad=10)

        if idx == 0:  # Single star
            # Primary star
            star = Circle((0, 0), 0.8, facecolor=YELLOW, edgecolor=WHITE, linewidth=2)
            ax.add_patch(star)
            ax.text(0, 0, 'G', ha='center', va='center', fontsize=14, color=BG_COLOR, fontweight='bold')

            # Planetary orbits
            for r, planet_name in [(1.5, 'Inner'), (2.5, 'Habitable'), (3.5, 'Outer')]:
                orbit = Circle((0, 0), r, fill=False, edgecolor=GRAY, linewidth=1, linestyle='--')
                ax.add_patch(orbit)
                angle = np.random.uniform(0, 2*np.pi)
                px, py = r * np.cos(angle), r * np.sin(angle)
                planet = Circle((px, py), 0.15, facecolor=GREEN if planet_name == 'Habitable' else CYAN,
                               edgecolor=WHITE, linewidth=1)
                ax.add_patch(planet)

            ax.text(0, -4.5, 'Simple orbital mechanics\nAll planets orbit primary',
                    ha='center', va='center', fontsize=8, color=GRAY)

        elif idx == 1:  # Binary
            # Primary star
            star1 = Circle((-1, 0), 0.6, facecolor=YELLOW, edgecolor=WHITE, linewidth=2)
            ax.add_patch(star1)
            ax.text(-1, 0, 'G', ha='center', va='center', fontsize=12, color=BG_COLOR, fontweight='bold')

            # Secondary star (smaller, cooler)
            star2 = Circle((1.5, 0), 0.4, facecolor=ORANGE, edgecolor=WHITE, linewidth=2)
            ax.add_patch(star2)
            ax.text(1.5, 0, 'K', ha='center', va='center', fontsize=10, color=BG_COLOR, fontweight='bold')

            # Binary orbit path
            binary_orbit = Circle((0.25, 0), 1.6, fill=False, edgecolor=RED, linewidth=1.5, linestyle=':')
            ax.add_patch(binary_orbit)

            # Planetary orbits around primary
            for r in [1.8, 2.8]:
                orbit = Circle((-1, 0), r, fill=False, edgecolor=GRAY, linewidth=1, linestyle='--')
                ax.add_patch(orbit)
                angle = np.random.uniform(0, 2*np.pi)
                px, py = -1 + r * np.cos(angle), r * np.sin(angle)
                planet = Circle((px, py), 0.12, facecolor=GREEN, edgecolor=WHITE, linewidth=1)
                ax.add_patch(planet)

            # Planet around secondary
            orbit_s = Circle((1.5, 0), 1.2, fill=False, edgecolor=GRAY, linewidth=1, linestyle='--')
            ax.add_patch(orbit_s)
            planet_s = Circle((1.5, 1.2), 0.12, facecolor=CYAN, edgecolor=WHITE, linewidth=1)
            ax.add_patch(planet_s)

            ax.text(0, -4.5, 'Close binary: planets orbit\nindividual stars',
                    ha='center', va='center', fontsize=8, color=GRAY)

        else:  # Trinary
            # Primary star (center-ish)
            star1 = Circle((0, 1), 0.6, facecolor=YELLOW, edgecolor=WHITE, linewidth=2)
            ax.add_patch(star1)
            ax.text(0, 1, 'F', ha='center', va='center', fontsize=12, color=BG_COLOR, fontweight='bold')

            # Secondary pair (closer together)
            star2 = Circle((-1.5, -1.5), 0.4, facecolor=ORANGE, edgecolor=WHITE, linewidth=2)
            ax.add_patch(star2)
            ax.text(-1.5, -1.5, 'K', ha='center', va='center', fontsize=10, color=BG_COLOR, fontweight='bold')

            star3 = Circle((1.5, -1.5), 0.35, facecolor=RED, edgecolor=WHITE, linewidth=2)
            ax.add_patch(star3)
            ax.text(1.5, -1.5, 'M', ha='center', va='center', fontsize=8, color=WHITE, fontweight='bold')

            # Orbital relationships
            binary_orbit = Circle((0, -1.5), 1.8, fill=False, edgecolor=PURPLE, linewidth=1.5, linestyle=':')
            ax.add_patch(binary_orbit)

            # Planets around primary
            orbit1 = Circle((0, 1), 1.5, fill=False, edgecolor=GRAY, linewidth=1, linestyle='--')
            ax.add_patch(orbit1)
            planet1 = Circle((1.5, 1), 0.12, facecolor=GREEN, edgecolor=WHITE, linewidth=1)
            ax.add_patch(planet1)

            ax.text(0, -4.5, 'Complex: each star can\nhave its own planets',
                    ha='center', va='center', fontsize=8, color=GRAY)

    fig.suptitle('Multi-Star System Configurations', color=WHITE, fontsize=14, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/2-game-setup/2.3-binary-trinary-systems.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 2.3-binary-trinary-systems.png")


def create_known_vs_random_stars():
    """Issue #1128: Known Stars vs Random Stars Scale Diagram"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 8))
    fig.patch.set_facecolor(BG_COLOR)

    for idx, ax in enumerate(axes):
        ax.set_facecolor(BG_COLOR)
        ax.set_xlim(-6, 6)
        ax.set_ylim(-6, 6)
        ax.set_aspect('equal')
        ax.axis('off')

        if idx == 0:  # Known Stars
            ax.set_title('Known Star Systems\n(Hipparcos Catalogue)', color=CYAN, fontsize=12, fontweight='bold')

            # Sol at center
            sol = Circle((0, 0), 0.3, facecolor=YELLOW, edgecolor=WHITE, linewidth=2)
            ax.add_patch(sol)
            ax.text(0, 0.5, 'Sol', ha='center', va='center', fontsize=8, color=YELLOW)

            # Real nearby stars with approximate positions
            real_stars = [
                (1.2, 0.3, 'Alpha\nCentauri', 0.2, YELLOW),
                (1.8, -0.8, "Barnard's", 0.15, RED),
                (-1.5, 1.0, 'Sirius', 0.25, WHITE),
                (0.8, 1.8, 'Procyon', 0.2, YELLOW),
                (-2.0, -1.5, 'Epsilon\nEridani', 0.18, ORANGE),
                (2.5, 1.5, 'Tau Ceti', 0.17, YELLOW),
                (-1.0, -2.5, 'Altair', 0.22, WHITE),
            ]

            # More distant stars (scattered)
            np.random.seed(42)
            for _ in range(50):
                r = np.random.uniform(3, 5.5)
                theta = np.random.uniform(0, 2*np.pi)
                x, y = r * np.cos(theta), r * np.sin(theta)
                size = np.random.uniform(0.05, 0.12)
                color = np.random.choice([WHITE, YELLOW, ORANGE, RED])
                star = Circle((x, y), size, facecolor=color, edgecolor=color, alpha=0.6)
                ax.add_patch(star)

            for x, y, name, size, color in real_stars:
                star = Circle((x, y), size, facecolor=color, edgecolor=WHITE, linewidth=1)
                ax.add_patch(star)
                ax.text(x, y - 0.4, name, ha='center', va='top', fontsize=6, color=color)

            # Distance rings
            for r in [2, 4]:
                ring = Circle((0, 0), r, fill=False, edgecolor=GRAY, linewidth=0.5, linestyle=':')
                ax.add_patch(ring)
            ax.text(2, -0.3, '~20 ly', ha='center', va='center', fontsize=6, color=GRAY)
            ax.text(4, -0.3, '~100 ly', ha='center', va='center', fontsize=6, color=GRAY)

            # Stats box
            ax.text(0, -5.5, '63,000+ real stars\nHipparcos Catalogue\n775 light-year radius',
                    ha='center', va='center', fontsize=9, color=CYAN,
                    bbox=dict(boxstyle='round', facecolor=DARK_GRAY, edgecolor=CYAN))

        else:  # Random Stars
            ax.set_title('Random Star Systems\n(Procedural Generation)', color=GREEN, fontsize=12, fontweight='bold')

            # Sol at center
            sol = Circle((0, 0), 0.3, facecolor=YELLOW, edgecolor=WHITE, linewidth=2)
            ax.add_patch(sol)
            ax.text(0, 0.5, 'Sol', ha='center', va='center', fontsize=8, color=YELLOW)

            # Random distribution of stars
            np.random.seed(123)
            colors = [WHITE, YELLOW, ORANGE, RED, CYAN, PURPLE]

            # Jump point connections (web-like)
            connection_points = [(0, 0)]
            for i in range(25):
                parent = connection_points[np.random.randint(len(connection_points))]
                angle = np.random.uniform(0, 2*np.pi)
                dist = np.random.uniform(0.8, 2.0)
                new_x = parent[0] + dist * np.cos(angle)
                new_y = parent[1] + dist * np.sin(angle)
                if abs(new_x) < 5.5 and abs(new_y) < 5.5:
                    connection_points.append((new_x, new_y))
                    # Draw connection
                    ax.plot([parent[0], new_x], [parent[1], new_y],
                            color=GRAY, linewidth=0.5, alpha=0.4)
                    # Draw star
                    size = np.random.uniform(0.1, 0.2)
                    color = np.random.choice(colors)
                    star = Circle((new_x, new_y), size, facecolor=color, edgecolor=WHITE, linewidth=0.5)
                    ax.add_patch(star)

            # Some isolated stars
            for _ in range(15):
                x = np.random.uniform(-5, 5)
                y = np.random.uniform(-5, 5)
                if (x**2 + y**2) > 4:
                    size = np.random.uniform(0.08, 0.15)
                    color = np.random.choice(colors)
                    star = Circle((x, y), size, facecolor=color, edgecolor=color, alpha=0.5)
                    ax.add_patch(star)

            # Stats box
            ax.text(0, -5.5, 'Up to 1000 systems (configurable)\nProcedurally generated\nJump point web expansion',
                    ha='center', va='center', fontsize=9, color=GREEN,
                    bbox=dict(boxstyle='round', facecolor=DARK_GRAY, edgecolor=GREEN))

    fig.suptitle('Star System Generation Options', color=WHITE, fontsize=14, fontweight='bold', y=0.98)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams/2-game-setup/2.5-known-vs-random-stars.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 2.5-known-vs-random-stars.png")


if __name__ == '__main__':
    print("Generating Wave 6 diagrams...")

    create_vb6_vs_csharp_comparison()       # #1043
    create_community_resources_map()         # #1044
    create_folder_structure()                # #1046
    create_backup_flowchart()                # #1052
    create_first_steps_workflow()            # #1064
    create_npr_generation_flowchart()        # #1073
    create_government_decision_tree()        # #1093
    create_mineral_production_chain()        # #1100
    create_binary_trinary_visualization()    # #1102
    create_known_vs_random_stars()           # #1128

    print("\nAll diagrams generated successfully!")
