#!/usr/bin/env python3
"""Generate Wave 9: Ship Design Diagrams for Aurora 4X Manual.

Issues addressed:
- #1047 - Section 4.1: Spectral Type Visual Reference Card
- #1049 - Section 8.1: Ship Role Specialization Matrix Diagram
- #1055 - Section 9.1: Shipyard Workforce Scaling Visualization
- #1063 - Section 10.1: Fuel Consumption Mechanics Diagram
- #1066 - Section 10.1: Range Calculation Visualization
- #1069 - Section 11.4: Cloaking Effect on Detection Range Visualization
- #1084 - Section 12.1: Point Defense Engagement Sequence Diagram
- #1088 - Section 12.0: Combat Phase Sequence Visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle, Circle, FancyBboxPatch, Polygon, FancyArrowPatch,
    Arrow, Wedge
)
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
from pathlib import Path
import os

# Dark theme colors
BG_COLOR = '#1a1a2e'
CYAN = '#4ecdc4'
YELLOW = '#ffe66d'
RED = '#ff6b6b'
GREEN = '#95d5b2'
WHITE = '#ffffff'
GRAY = '#888888'
DARK_GRAY = '#2d2d44'

# Star colors for spectral types
STAR_COLORS = {
    'O': '#9bb0ff',  # Blue
    'B': '#aabfff',  # Blue-white
    'A': '#cad7ff',  # White
    'F': '#f8f7ff',  # Yellow-white
    'G': '#fff4ea',  # Yellow (Sol-type)
    'K': '#ffd2a1',  # Orange
    'M': '#ffcc6f',  # Red
}


def setup_figure(width=10, height=6, dpi=150):
    """Create figure with standard dark theme setup."""
    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.tick_params(colors=WHITE, which='both')
    for spine in ax.spines.values():
        spine.set_color(GRAY)
    return fig, ax


def save_figure(fig, filepath, dpi=150):
    """Save figure with standard settings."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fig.savefig(filepath, facecolor=BG_COLOR, edgecolor='none',
                bbox_inches='tight', pad_inches=0.2, dpi=dpi)
    plt.close()
    print(f"Generated: {filepath}")


# =============================================================================
# Diagram 1: Spectral Type Visual Reference Card (#1047)
# =============================================================================
def gen_spectral_reference_card(output_path):
    """Generate a visual reference card for star spectral types."""
    fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')

    # Title
    ax.text(0.5, 0.95, 'Star Spectral Types Reference Card',
            transform=ax.transAxes, fontsize=18, fontweight='bold',
            color=WHITE, ha='center', va='top')

    # Spectral data: type, temp_range, color_name, frequency, relative_size
    spectral_data = [
        ('O', '30,000-50,000K', 'Blue', '0.2%', 2.5),
        ('B', '11,000-28,000K', 'Blue-white', '0.3%', 2.0),
        ('A', '7,750-10,000K', 'White', '5.1%', 1.7),
        ('F', '6,150-7,500K', 'Yellow-white', '10.1%', 1.4),
        ('G', '5,100-6,000K', 'Yellow (Sol)', '40.6%', 1.1),
        ('K', '3,650-5,000K', 'Orange', '20.4%', 0.8),
        ('M', '2,300-3,920K', 'Red', '12.3%', 0.5),
    ]

    # Draw each star type
    y_positions = np.linspace(0.82, 0.12, 7)

    for i, (stype, temp, color_name, freq, size) in enumerate(spectral_data):
        y = y_positions[i]
        star_color = STAR_COLORS[stype]

        # Star circle (size scaled)
        circle_radius = size * 0.035
        circle = Circle((0.08, y), circle_radius, transform=ax.transAxes,
                        facecolor=star_color, edgecolor='white', linewidth=0.5, alpha=0.9)
        ax.add_patch(circle)

        # Glow effect
        for r_mult, alpha in [(1.5, 0.2), (2.0, 0.1), (2.5, 0.05)]:
            glow = Circle((0.08, y), circle_radius * r_mult, transform=ax.transAxes,
                         facecolor=star_color, edgecolor='none', alpha=alpha)
            ax.add_patch(glow)

        # Spectral type letter
        ax.text(0.18, y, stype, transform=ax.transAxes, fontsize=24, fontweight='bold',
                color=star_color, ha='center', va='center', family='monospace')

        # Temperature range
        ax.text(0.32, y, temp, transform=ax.transAxes, fontsize=11,
                color=WHITE, ha='left', va='center')

        # Color description
        ax.text(0.52, y, color_name, transform=ax.transAxes, fontsize=11,
                color=GRAY, ha='left', va='center')

        # Frequency bar
        freq_val = float(freq.replace('%', ''))
        bar_width = freq_val / 50  # Scale to max ~0.8
        ax.add_patch(Rectangle((0.70, y - 0.015), bar_width, 0.03,
                               transform=ax.transAxes, facecolor=star_color, alpha=0.7))
        ax.text(0.70 + bar_width + 0.02, y, freq, transform=ax.transAxes,
                fontsize=10, color=WHITE, ha='left', va='center')

    # Column headers
    ax.text(0.08, 0.92, 'Size', transform=ax.transAxes, fontsize=10,
            color=GRAY, ha='center', va='center')
    ax.text(0.18, 0.92, 'Type', transform=ax.transAxes, fontsize=10,
            color=GRAY, ha='center', va='center')
    ax.text(0.32, 0.92, 'Temperature', transform=ax.transAxes, fontsize=10,
            color=GRAY, ha='left', va='center')
    ax.text(0.52, 0.92, 'Color', transform=ax.transAxes, fontsize=10,
            color=GRAY, ha='left', va='center')
    ax.text(0.78, 0.92, 'Frequency in Aurora', transform=ax.transAxes, fontsize=10,
            color=GRAY, ha='center', va='center')

    # Notes at bottom
    notes = [
        "Mnemonic: Oh Be A Fine Girl/Guy, Kiss Me",
        "G-type dominance (40.6%) is an Aurora design choice; real space is dominated by M-type red dwarfs",
        "Lower subdivision numbers (e.g., G2 vs G9) indicate hotter stars within the class"
    ]
    for i, note in enumerate(notes):
        ax.text(0.02, 0.06 - i * 0.025, f"  {note}", transform=ax.transAxes,
                fontsize=8, color=GRAY, ha='left', va='center')

    save_figure(fig, output_path)


# =============================================================================
# Diagram 2: Ship Role Specialization Matrix (#1049)
# =============================================================================
def gen_ship_role_matrix(output_path):
    """Generate ship role specialization matrix diagram."""
    fig, ax = plt.subplots(figsize=(14, 10), dpi=150)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')

    # Title
    ax.text(0.5, 0.97, 'Ship Role Specialization Matrix',
            transform=ax.transAxes, fontsize=18, fontweight='bold',
            color=WHITE, ha='center', va='top')

    # Define roles and their characteristics
    roles = [
        ('Beam Combatant', 'Combat', ['Speed', 'Armor', 'Beam Weapons', 'Fire Controls'], CYAN),
        ('Missile Combatant', 'Combat', ['Launchers', 'Magazines', 'MFCs', 'Range'], RED),
        ('Carrier', 'Combat', ['Hangars', 'Fighters', 'PD', 'Flag Bridge'], YELLOW),
        ('PD Escort', 'Combat', ['CIWS', 'Tracking Speed', 'AMM Launchers'], GREEN),
        ('Scout', 'Support', ['Speed', 'Sensors', 'Stealth'], CYAN),
        ('Survey Ship', 'Support', ['Survey Sensors', 'Range', 'Fuel'], GREEN),
        ('Tanker', 'Logistics', ['Fuel Storage', 'Refueling System', 'Commercial Engines'], YELLOW),
        ('Freighter', 'Logistics', ['Cargo Hold', 'Shuttle Bays', 'Commercial Engines'], GRAY),
        ('Colony Ship', 'Logistics', ['Colonist Capacity', 'Cryo Berths'], GREEN),
        ('Jump Tender', 'Fleet', ['Squadron Jump Drive', 'Fuel', 'Speed'], CYAN),
    ]

    # Layout
    y_start = 0.88
    y_step = 0.078

    # Category labels
    categories = {'Combat': 0.88, 'Support': 0.56, 'Logistics': 0.40, 'Fleet': 0.16}
    for cat, y_pos in categories.items():
        ax.text(0.02, y_pos, cat, transform=ax.transAxes, fontsize=12, fontweight='bold',
                color=GRAY, ha='left', va='center', rotation=90)

    current_y = y_start
    prev_cat = None
    for role, category, features, color in roles:
        if category != prev_cat and prev_cat is not None:
            current_y -= 0.02  # Gap between categories

        # Role box
        box = FancyBboxPatch((0.08, current_y - 0.03), 0.22, 0.055,
                             boxstyle="round,pad=0.01", transform=ax.transAxes,
                             facecolor=DARK_GRAY, edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(0.19, current_y, role, transform=ax.transAxes, fontsize=11,
                fontweight='bold', color=color, ha='center', va='center')

        # Feature tags
        x_offset = 0.34
        for feature in features:
            tag_width = len(feature) * 0.008 + 0.02
            tag = FancyBboxPatch((x_offset, current_y - 0.015), tag_width, 0.03,
                                 boxstyle="round,pad=0.005", transform=ax.transAxes,
                                 facecolor=color, edgecolor='none', alpha=0.3)
            ax.add_patch(tag)
            ax.text(x_offset + tag_width/2, current_y, feature, transform=ax.transAxes,
                    fontsize=8, color=WHITE, ha='center', va='center')
            x_offset += tag_width + 0.01

        prev_cat = category
        current_y -= y_step

    # Design philosophy note
    ax.text(0.5, 0.05, 'Design Principle: Each ship should excel at ONE role.',
            transform=ax.transAxes, fontsize=11, color=YELLOW, ha='center', va='center',
            style='italic')
    ax.text(0.5, 0.02, 'Multi-role ships cost more and perform worse than specialized alternatives.',
            transform=ax.transAxes, fontsize=9, color=GRAY, ha='center', va='center')

    save_figure(fig, output_path)


# =============================================================================
# Diagram 3: Shipyard Workforce Scaling (#1055)
# =============================================================================
def gen_workforce_scaling(output_path):
    """Generate shipyard workforce scaling visualization."""
    fig, ax = setup_figure(12, 7)

    # Title
    ax.set_title('Shipyard Workforce Scaling', fontsize=16, fontweight='bold',
                 color=WHITE, pad=20)

    # Data for naval vs commercial shipyards
    capacities = np.array([1000, 5000, 10000, 20000, 50000, 100000])

    # Naval: 250 workers per ton per slipway
    naval_1slip = capacities * 250
    naval_3slip = capacities * 250 * 3

    # Commercial: 25 workers per ton per slipway
    commercial_1slip = capacities * 25
    commercial_3slip = capacities * 25 * 3

    # Plot lines
    ax.plot(capacities, naval_1slip / 1e6, 'o-', color=RED, linewidth=2,
            label='Naval (1 slipway)', markersize=8)
    ax.plot(capacities, naval_3slip / 1e6, 's--', color=RED, linewidth=2,
            label='Naval (3 slipways)', markersize=8, alpha=0.7)
    ax.plot(capacities, commercial_1slip / 1e6, 'o-', color=CYAN, linewidth=2,
            label='Commercial (1 slipway)', markersize=8)
    ax.plot(capacities, commercial_3slip / 1e6, 's--', color=CYAN, linewidth=2,
            label='Commercial (3 slipways)', markersize=8, alpha=0.7)

    # Labels and formatting
    ax.set_xlabel('Shipyard Capacity (tons)', fontsize=12, color=WHITE)
    ax.set_ylabel('Workers Required (millions)', fontsize=12, color=WHITE)
    ax.set_xscale('log')
    ax.set_yscale('log')

    # Grid
    ax.grid(True, alpha=0.3, color=GRAY)
    ax.legend(loc='upper left', facecolor=DARK_GRAY, edgecolor=GRAY,
              labelcolor=WHITE, fontsize=10)

    # Annotations
    ax.annotate('Naval: 250 workers/ton/slipway\nCommercial: 25 workers/ton/slipway',
                xy=(0.98, 0.02), xycoords='axes fraction', fontsize=9,
                color=GRAY, ha='right', va='bottom',
                bbox=dict(boxstyle='round', facecolor=DARK_GRAY, edgecolor=GRAY))

    # Example callouts
    ax.annotate('10,000t Naval, 1 slip\n= 2.5M workers',
                xy=(10000, 2.5), xytext=(20000, 5),
                fontsize=9, color=WHITE,
                arrowprops=dict(arrowstyle='->', color=GRAY))

    save_figure(fig, output_path)


# =============================================================================
# Diagram 4: Fuel Consumption Mechanics (#1063)
# =============================================================================
def gen_fuel_consumption(output_path):
    """Generate fuel consumption mechanics diagram."""
    fig, ax = setup_figure(12, 7)

    ax.set_title('Fuel Consumption vs. Speed', fontsize=16, fontweight='bold',
                 color=WHITE, pad=20)

    # Speed as percentage of max
    speed_pct = np.linspace(10, 100, 100)

    # Fuel consumption increases with square of speed
    # Normalized to 100 at max speed
    consumption = (speed_pct / 100) ** 2 * 100

    # Plot
    ax.fill_between(speed_pct, 0, consumption, color=YELLOW, alpha=0.2)
    ax.plot(speed_pct, consumption, color=YELLOW, linewidth=3, label='Fuel Consumption')

    # Key points
    key_points = [
        (25, 6.25, '25% speed\n= 6.25% fuel'),
        (50, 25, '50% speed\n= 25% fuel'),
        (75, 56.25, '75% speed\n= 56.25% fuel'),
        (100, 100, '100% speed\n= 100% fuel'),
    ]

    for x, y, label in key_points:
        ax.scatter(x, y, s=100, color=CYAN, zorder=5)
        ax.annotate(label, xy=(x, y), xytext=(x - 8, y + 12),
                    fontsize=9, color=WHITE, ha='center')

    # Labels
    ax.set_xlabel('Speed (% of Maximum)', fontsize=12, color=WHITE)
    ax.set_ylabel('Fuel Consumption (relative)', fontsize=12, color=WHITE)

    ax.set_xlim(0, 110)
    ax.set_ylim(0, 120)
    ax.grid(True, alpha=0.3, color=GRAY)

    # Key insight box
    ax.text(0.02, 0.98, 'Key Insight: Fuel consumption scales with speed squared.',
            transform=ax.transAxes, fontsize=11, color=GREEN, ha='left', va='top',
            fontweight='bold')
    ax.text(0.02, 0.92, 'Doubling speed quadruples fuel consumption.',
            transform=ax.transAxes, fontsize=10, color=GRAY, ha='left', va='top')

    save_figure(fig, output_path)


# =============================================================================
# Diagram 5: Range Calculation Visualization (#1066)
# =============================================================================
def gen_range_calculation(output_path):
    """Generate range calculation visualization."""
    fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # Title
    ax.text(50, 96, 'Range Calculation: Speed vs. Distance Trade-off',
            fontsize=16, fontweight='bold', color=WHITE, ha='center', va='top')

    # Central ship
    ship_x, ship_y = 50, 50
    ax.scatter(ship_x, ship_y, s=200, color=CYAN, zorder=10)
    ax.text(ship_x, ship_y - 5, 'Your Ship', fontsize=10, color=WHITE, ha='center')

    # Range circles at different speeds
    ranges = [
        (100, 40, 'Max Speed (100%)', RED),
        (75, 30, '75% Speed', YELLOW),
        (50, 20, '50% Speed', GREEN),
        (25, 10, '25% Speed (4x range)', CYAN),
    ]

    for speed_pct, radius, label, color in ranges:
        circle = plt.Circle((ship_x, ship_y), radius, fill=False,
                            edgecolor=color, linewidth=2, linestyle='--', alpha=0.7)
        ax.add_patch(circle)
        # Label at top of circle
        ax.text(ship_x, ship_y + radius + 2, label, fontsize=9, color=color, ha='center')

    # Legend/formula box
    formula_box = FancyBboxPatch((65, 10), 32, 25, boxstyle="round,pad=0.02",
                                  facecolor=DARK_GRAY, edgecolor=GRAY, linewidth=1)
    ax.add_patch(formula_box)
    ax.text(81, 30, 'Range Formula:', fontsize=10, color=WHITE, ha='center', fontweight='bold')
    ax.text(81, 24, 'Range = Fuel / Consumption', fontsize=9, color=CYAN, ha='center')
    ax.text(81, 18, 'Consumption ~ Speed^2', fontsize=9, color=YELLOW, ha='center')
    ax.text(81, 12, 'Half speed = 4x range', fontsize=9, color=GREEN, ha='center')

    # Destination markers
    destinations = [
        (20, 70, 'Nearby Colony'),
        (85, 30, 'Distant Target'),
    ]
    for dx, dy, dlabel in destinations:
        ax.scatter(dx, dy, s=100, color=GREEN, marker='s')
        ax.text(dx, dy + 4, dlabel, fontsize=8, color=WHITE, ha='center')

    save_figure(fig, output_path)


# =============================================================================
# Diagram 6: Cloaking Effect on Detection Range (#1069)
# =============================================================================
def gen_cloaking_effect(output_path):
    """Generate cloaking effect on detection range visualization."""
    fig, ax = plt.subplots(figsize=(12, 8), dpi=150)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # Title
    ax.text(50, 96, 'Cloaking Effect on Detection Range',
            fontsize=16, fontweight='bold', color=WHITE, ha='center', va='top')

    # Two scenarios side by side
    # Left: Uncloaked
    uncloaked_x = 25
    ax.text(uncloaked_x, 85, 'UNCLOAKED', fontsize=12, fontweight='bold',
            color=RED, ha='center')

    # Ship
    ax.scatter(uncloaked_x, 50, s=150, color=RED, zorder=10)
    ax.text(uncloaked_x, 43, 'Ship', fontsize=9, color=WHITE, ha='center')

    # Detection envelope (full)
    for r, alpha in [(35, 0.1), (30, 0.15), (25, 0.2)]:
        circle = plt.Circle((uncloaked_x, 50), r, facecolor=RED, edgecolor=RED,
                            alpha=alpha, linewidth=1)
        ax.add_patch(circle)
    ax.text(uncloaked_x, 50 + 28, '100% Detection\nRange', fontsize=8, color=WHITE, ha='center')

    # Right: 90% Cloaked
    cloaked_x = 75
    ax.text(cloaked_x, 85, '90% CLOAKED', fontsize=12, fontweight='bold',
            color=GREEN, ha='center')

    # Ship (dimmer)
    ax.scatter(cloaked_x, 50, s=100, color=GREEN, alpha=0.6, zorder=10)
    ax.text(cloaked_x, 43, 'Ship', fontsize=9, color=WHITE, ha='center')

    # Reduced detection envelope (sqrt(0.1) = 0.316 of original)
    reduced_radius = 35 * 0.316  # ~11
    for r, alpha in [(reduced_radius, 0.15), (reduced_radius * 0.8, 0.2)]:
        circle = plt.Circle((cloaked_x, 50), r, facecolor=GREEN, edgecolor=GREEN,
                            alpha=alpha, linewidth=1)
        ax.add_patch(circle)
    ax.text(cloaked_x, 50 + 15, '31.6% Detection\nRange', fontsize=8, color=WHITE, ha='center')

    # Arrow and comparison
    ax.annotate('', xy=(55, 50), xytext=(45, 50),
                arrowprops=dict(arrowstyle='->', color=YELLOW, lw=2))

    # Formula box at bottom
    formula_y = 12
    ax.text(50, formula_y + 8, 'Detection Range Formula with Cloaking:',
            fontsize=10, color=WHITE, ha='center', fontweight='bold')
    ax.text(50, formula_y,
            'Detection = sqrt(Sensor x Signature x (1 - Cloak%)) x 250,000 km',
            fontsize=9, color=CYAN, ha='center', family='monospace')
    ax.text(50, formula_y - 6,
            '90% cloak reduces signature to 10%, detection range to sqrt(0.1) = 31.6%',
            fontsize=8, color=GRAY, ha='center')

    save_figure(fig, output_path)


# =============================================================================
# Diagram 7: Point Defense Engagement Sequence (#1084)
# =============================================================================
def gen_pd_sequence(output_path):
    """Generate point defense engagement sequence diagram."""
    fig, ax = plt.subplots(figsize=(14, 10), dpi=150)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # Title
    ax.text(50, 97, 'Point Defense Engagement Sequence',
            fontsize=18, fontweight='bold', color=WHITE, ha='center', va='top')

    # Sequence boxes
    steps = [
        ('1. DETECTION', 'Active sensors detect\nincoming missiles', CYAN, 88),
        ('2. TRACKING', 'Fire control acquires\ntarget lock', GREEN, 74),
        ('3. AMM LAUNCH', 'Anti-Missile Missiles\nengage at range', YELLOW, 60),
        ('4. RANGED PD', 'Beam weapons fire\n(Movement Phase)', CYAN, 46),
        ('5. AREA DEFENCE', 'Fleet-wide coverage\n(Naval Combat Phase)', GREEN, 32),
        ('6. CIWS', 'Close-in weapons\n(10,000 km)', RED, 18),
    ]

    box_width = 25
    box_height = 10
    x_center = 50

    for step_name, description, color, y in steps:
        # Main box
        box = FancyBboxPatch((x_center - box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.02",
                             facecolor=DARK_GRAY, edgecolor=color, linewidth=2)
        ax.add_patch(box)

        # Step name
        ax.text(x_center, y + 2, step_name, fontsize=11, fontweight='bold',
                color=color, ha='center', va='center')

        # Description
        ax.text(x_center, y - 2.5, description, fontsize=8,
                color=WHITE, ha='center', va='center')

        # Arrow to next step (except last)
        if y > 18:
            ax.annotate('', xy=(x_center, y - box_height/2 - 2),
                       xytext=(x_center, y - box_height/2),
                       arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.5))

    # Side annotations
    ax.text(80, 88, 'Long Range', fontsize=10, color=GRAY, ha='left')
    ax.text(80, 50, 'Mid Range', fontsize=10, color=GRAY, ha='left')
    ax.text(80, 18, 'Close Range', fontsize=10, color=GRAY, ha='left')

    # Distance scale on right
    ax.annotate('', xy=(85, 85), xytext=(85, 20),
                arrowprops=dict(arrowstyle='<->', color=GRAY, lw=1))

    # Key insight
    ax.text(50, 5, 'Layered defense: Each layer reduces missiles before the next engages',
            fontsize=10, color=YELLOW, ha='center', style='italic')

    save_figure(fig, output_path)


# =============================================================================
# Diagram 8: Combat Phase Sequence (#1088)
# =============================================================================
def gen_combat_phases(output_path):
    """Generate combat phase sequence visualization."""
    fig, ax = plt.subplots(figsize=(14, 9), dpi=150)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # Title
    ax.text(50, 96, 'Combat Phase Sequence (Per Tick)',
            fontsize=18, fontweight='bold', color=WHITE, ha='center', va='top')

    # Phases in order
    phases = [
        ('MOVEMENT PHASE', [
            'Ships execute movement orders',
            'Ranged Defensive Fire (PD)',
            'Point Blank Defensive Fire'
        ], CYAN),
        ('NAVAL COMBAT PHASE', [
            'Beam weapons fire at targets',
            'Area Defence PD fires'
        ], RED),
        ('MISSILE LAUNCH PHASE', [
            'MFCs launch missiles at targets',
            'Post-launch detection check'
        ], YELLOW),
        ('MISSILE MOVEMENT', [
            'In-flight missiles advance',
            'Terminal approach to targets'
        ], GREEN),
        ('DAMAGE RESOLUTION', [
            'Beam and missile hits resolved',
            'Armor penetration calculated',
            'Components damaged/destroyed'
        ], RED),
    ]

    # Layout: horizontal flow
    phase_width = 16
    gap = 3
    start_x = 8
    y_center = 55

    for i, (phase_name, details, color) in enumerate(phases):
        x = start_x + i * (phase_width + gap)

        # Phase box
        box_height = 35
        box = FancyBboxPatch((x, y_center - box_height/2), phase_width, box_height,
                             boxstyle="round,pad=0.02",
                             facecolor=DARK_GRAY, edgecolor=color, linewidth=2)
        ax.add_patch(box)

        # Phase number
        ax.text(x + phase_width/2, y_center + box_height/2 - 4, f'{i+1}',
                fontsize=14, fontweight='bold', color=color, ha='center')

        # Phase name
        ax.text(x + phase_width/2, y_center + box_height/2 - 10, phase_name,
                fontsize=8, fontweight='bold', color=WHITE, ha='center')

        # Details
        for j, detail in enumerate(details):
            ax.text(x + phase_width/2, y_center + 2 - j * 6, detail,
                    fontsize=7, color=GRAY, ha='center')

        # Arrow to next phase
        if i < len(phases) - 1:
            ax.annotate('', xy=(x + phase_width + gap - 1, y_center),
                       xytext=(x + phase_width + 1, y_center),
                       arrowprops=dict(arrowstyle='->', color=GRAY, lw=2))

    # Loop arrow (phases repeat each tick)
    ax.annotate('', xy=(start_x - 2, y_center + 20),
                xytext=(start_x + (len(phases)-1) * (phase_width + gap) + phase_width + 2, y_center + 20),
                arrowprops=dict(arrowstyle='->', color=YELLOW, lw=2,
                               connectionstyle="arc3,rad=0.3"))
    ax.text(50, 85, 'Cycle repeats each time increment', fontsize=10, color=YELLOW, ha='center')

    # Warning at bottom
    ax.text(50, 15, 'WARNING: Use 30-second or shorter time increments during combat',
            fontsize=11, fontweight='bold', color=RED, ha='center')
    ax.text(50, 10, 'Longer increments may cause missiles to skip through defensive fire envelopes',
            fontsize=9, color=GRAY, ha='center')

    save_figure(fig, output_path)


# =============================================================================
# Main execution
# =============================================================================
def main():
    base_path = Path('/Users/eevenson/Documents/Projects/aurora-manual/images/diagrams')

    # Create directories if needed
    (base_path / '4-systems-and-bodies').mkdir(parents=True, exist_ok=True)
    (base_path / '8-ship-design').mkdir(parents=True, exist_ok=True)
    (base_path / '9-fleet-management').mkdir(parents=True, exist_ok=True)
    (base_path / '10-navigation').mkdir(parents=True, exist_ok=True)
    (base_path / '11-sensors-and-detection').mkdir(parents=True, exist_ok=True)
    (base_path / '12-combat').mkdir(parents=True, exist_ok=True)

    # Generate all diagrams
    print("Generating Wave 9 diagrams...")

    gen_spectral_reference_card(base_path / '4-systems-and-bodies' / '4.1-spectral-reference.png')
    gen_ship_role_matrix(base_path / '8-ship-design' / '8.1-ship-role-matrix.png')
    gen_workforce_scaling(base_path / '9-fleet-management' / '9.1-workforce-scaling.png')
    gen_fuel_consumption(base_path / '10-navigation' / '10.1-fuel-consumption.png')
    gen_range_calculation(base_path / '10-navigation' / '10.1-range-calculation.png')
    gen_cloaking_effect(base_path / '11-sensors-and-detection' / '11.4-cloaking-detection.png')
    gen_pd_sequence(base_path / '12-combat' / '12.4-pd-engagement-sequence.png')
    gen_combat_phases(base_path / '12-combat' / '12.0-combat-phases.png')

    print("\nAll diagrams generated successfully!")


if __name__ == '__main__':
    main()
