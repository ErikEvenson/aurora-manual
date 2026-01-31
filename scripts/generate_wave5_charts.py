#!/usr/bin/env python3
"""
Generate Wave 5: Diplomacy & Exploration Charts for Aurora Manual
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# Dark theme colors
BACKGROUND = '#1a1a2e'
GRID_COLOR = '#2a2a4e'
TEXT_COLOR = '#ffffff'
CYAN = '#4ecdc4'
RED = '#ff6b6b'
YELLOW = '#ffe66d'
GREEN = '#95d5b2'
PURPLE = '#a78bfa'
ORANGE = '#f97316'
PINK = '#ec4899'

# Set matplotlib style
plt.style.use('dark_background')
plt.rcParams['figure.facecolor'] = BACKGROUND
plt.rcParams['axes.facecolor'] = BACKGROUND
plt.rcParams['axes.edgecolor'] = GRID_COLOR
plt.rcParams['axes.labelcolor'] = TEXT_COLOR
plt.rcParams['text.color'] = TEXT_COLOR
plt.rcParams['xtick.color'] = TEXT_COLOR
plt.rcParams['ytick.color'] = TEXT_COLOR
plt.rcParams['grid.color'] = GRID_COLOR
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 11

# Create output directories
os.makedirs('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/15-diplomacy', exist_ok=True)
os.makedirs('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/17-exploration', exist_ok=True)
os.makedirs('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/appendices', exist_ok=True)


def chart_1_territory_intrusion():
    """Issue #1078 - Territory Intrusion Penalty Calculation Chart"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Territory Intrusion Penalty Calculation', fontsize=16, color=TEXT_COLOR, y=0.98)

    # Left chart: Base threat by system value with xenophobia modifiers
    ax1 = axes[0]
    system_values = ['Secondary', 'Primary', 'Core', 'Capital']
    base_threat = [2.5, 5, 10, 20]

    # Xenophobia levels
    xenophobia_levels = [25, 50, 75, 100]
    colors = [GREEN, CYAN, YELLOW, RED]

    x = np.arange(len(system_values))
    width = 0.2

    for i, (xeno, color) in enumerate(zip(xenophobia_levels, colors)):
        modifier = xeno / 100
        threat_values = [b * modifier for b in base_threat]
        ax1.bar(x + (i - 1.5) * width, threat_values, width, label=f'{xeno}% Xenophobia', color=color, alpha=0.8)

    ax1.set_xlabel('System Value Category')
    ax1.set_ylabel('Threat Level')
    ax1.set_title('Threat Level by System Value & Xenophobia')
    ax1.set_xticks(x)
    ax1.set_xticklabels(system_values)
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 25)

    # Right chart: Diplomatic penalty formula visualization
    ax2 = axes[1]

    # Show penalty curves for different threat levels
    tonnage = np.linspace(1000, 100000, 100)
    threat_levels = [2.5, 5, 10, 20]
    threat_names = ['Secondary (2.5)', 'Primary (5)', 'Core (10)', 'Capital (20)']
    colors = [GREEN, CYAN, YELLOW, RED]

    for threat, name, color in zip(threat_levels, threat_names, colors):
        # Penalty = sqrt(tonnage) * threat_level
        penalty = np.sqrt(tonnage) * threat
        ax2.plot(tonnage / 1000, penalty, label=name, color=color, linewidth=2)

    ax2.set_xlabel('Detected Ship Tonnage (thousands)')
    ax2.set_ylabel('Diplomatic Point Penalty')
    ax2.set_title('Intrusion Penalty by Fleet Size')
    ax2.legend(loc='upper left')
    ax2.grid(True, alpha=0.3)

    # Add formula annotation
    ax2.annotate('Penalty = sqrt(Tonnage) x Threat Level',
                 xy=(0.5, 0.95), xycoords='axes fraction',
                 fontsize=10, color=YELLOW, ha='center',
                 bbox=dict(boxstyle='round', facecolor=BACKGROUND, edgecolor=YELLOW, alpha=0.8))

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/15-diplomacy/15.1.4-territory-intrusion-penalty.png',
                dpi=150, facecolor=BACKGROUND, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 15.1.4-territory-intrusion-penalty.png")


def chart_2_npr_archetypes():
    """Issue #1079 - NPR Behavior Archetypes Chart (4 personality types matrix)"""
    fig, ax = plt.subplots(figsize=(12, 10))

    # Create 2x2 matrix for archetypes
    # X-axis: Diplomacy/Trade (low to high)
    # Y-axis: Militancy/Xenophobia (low to high)

    # Define archetypes with their characteristics
    archetypes = {
        'Peaceful Trader': {
            'pos': (0.75, 0.25),
            'color': GREEN,
            'attrs': 'High Diplomacy/Trade\nLow Militancy',
            'behavior': 'Seeks treaties\nAvoids conflict\nPrioritizes commerce',
            'response': 'Build relations early\nOffer trade agreements\nReliable allies'
        },
        'Aggressive Expansionist': {
            'pos': (0.25, 0.75),
            'color': RED,
            'attrs': 'High Militancy/Expansion\nLow Diplomacy',
            'behavior': 'Builds military\nClaims territory\nMay attack',
            'response': 'Military deterrence\nStrong border defense\nPrepare for conflict'
        },
        'Xenophobic Isolationist': {
            'pos': (0.25, 0.25),
            'color': PURPLE,
            'attrs': 'High Xenophobia/Determination\nLow Trade',
            'behavior': 'Refuses contact\nHeavy intrusion penalty\nWill not negotiate',
            'response': 'Avoid their territory\nMinimal diplomacy ROI\nCoexist or conflict'
        },
        'Balanced Competitor': {
            'pos': (0.75, 0.75),
            'color': CYAN,
            'attrs': 'Moderate all attributes',
            'behavior': 'Responds in kind\nPursues own interests\nWill negotiate or fight',
            'response': 'Standard diplomacy\nMilitary + treaties\nReliable but competitive'
        }
    }

    # Draw quadrants
    ax.axhline(y=0.5, color=GRID_COLOR, linewidth=2, linestyle='--')
    ax.axvline(x=0.5, color=GRID_COLOR, linewidth=2, linestyle='--')

    # Draw archetype boxes
    for name, data in archetypes.items():
        x, y = data['pos']

        # Draw box with archetype
        box = mpatches.FancyBboxPatch((x-0.2, y-0.18), 0.4, 0.36,
                                       boxstyle="round,pad=0.02",
                                       facecolor=BACKGROUND,
                                       edgecolor=data['color'],
                                       linewidth=3,
                                       alpha=0.9)
        ax.add_patch(box)

        # Add text
        ax.text(x, y+0.12, name, fontsize=12, fontweight='bold',
                ha='center', va='center', color=data['color'])
        ax.text(x, y+0.02, data['attrs'], fontsize=8,
                ha='center', va='center', color=TEXT_COLOR, alpha=0.9)
        ax.text(x, y-0.1, data['response'], fontsize=7,
                ha='center', va='center', color=YELLOW, style='italic')

    # Labels
    ax.set_xlabel('Diplomacy / Trade Level', fontsize=12, labelpad=10)
    ax.set_ylabel('Militancy / Xenophobia Level', fontsize=12, labelpad=10)
    ax.set_title('NPR Behavior Archetypes Matrix', fontsize=16, pad=20)

    # Axis labels
    ax.text(0.25, -0.05, 'LOW', ha='center', fontsize=10, color=TEXT_COLOR)
    ax.text(0.75, -0.05, 'HIGH', ha='center', fontsize=10, color=TEXT_COLOR)
    ax.text(-0.05, 0.25, 'LOW', ha='center', va='center', fontsize=10, color=TEXT_COLOR, rotation=90)
    ax.text(-0.05, 0.75, 'HIGH', ha='center', va='center', fontsize=10, color=TEXT_COLOR, rotation=90)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/15-diplomacy/15.4.6-npr-behavior-archetypes.png',
                dpi=150, facecolor=BACKGROUND, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 15.4.6-npr-behavior-archetypes.png")


def chart_3_relationship_status():
    """Issue #1101 - Relationship Status Effects Table (as visual chart)"""
    fig, ax = plt.subplots(figsize=(14, 8))

    # Status levels with their thresholds and effects
    statuses = ['Hostile', 'Unfriendly', 'Neutral', 'Friendly', 'Allied']
    thresholds = ['< -100', '-100 to -25', '-25 to +25', '+25 to +75', '> +75']
    colors = [RED, ORANGE, YELLOW, GREEN, CYAN]

    # Effects categories
    categories = ['Trade', 'Transit', 'Intel Gain', 'Military', 'Treaties']

    # Effects matrix (1-5 scale for visualization)
    # [Trade, Transit, Intel, Military cooperation, Treaties available]
    effects = {
        'Hostile':    [0, 0, 5, 0, 0],  # No trade/transit, full intel, no cooperation
        'Unfriendly': [0, 1, 4, 1, 0],  # Limited, high intel gain
        'Neutral':    [2, 2, 3, 2, 2],  # Moderate all
        'Friendly':   [4, 4, 1, 3, 4],  # Good trade/transit, low intel
        'Allied':     [5, 5, 0.5, 5, 5] # Full cooperation, minimal intel
    }

    # Create horizontal bar sections
    y_positions = np.arange(len(statuses))
    bar_height = 0.15

    for i, status in enumerate(statuses):
        # Draw status label box
        rect = mpatches.FancyBboxPatch((-2.5, i-0.3), 2.2, 0.6,
                                        boxstyle="round,pad=0.02",
                                        facecolor=colors[i],
                                        alpha=0.3,
                                        edgecolor=colors[i])
        ax.add_patch(rect)
        ax.text(-1.4, i, f'{status}\n{thresholds[i]}', ha='center', va='center',
                fontsize=10, fontweight='bold', color=colors[i])

        # Draw effect bars
        for j, (cat, val) in enumerate(zip(categories, effects[status])):
            bar_y = i + (j - 2) * bar_height
            ax.barh(bar_y, val, height=bar_height*0.8, left=0,
                   color=colors[i], alpha=0.6 + j*0.08)

    # Add category labels at top
    for j, cat in enumerate(categories):
        ax.text(2.5, 4.5 + (j-2)*bar_height, cat, ha='center', va='center',
               fontsize=9, color=TEXT_COLOR)

    # Add scale
    ax.set_xlim(-3, 6)
    ax.set_ylim(-0.8, 5.2)
    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xticklabels(['None', 'Minimal', 'Limited', 'Moderate', 'Good', 'Full'])
    ax.set_yticks([])
    ax.set_xlabel('Availability / Effect Level', fontsize=11)
    ax.set_title('Relationship Status Effects on Gameplay', fontsize=16, pad=10)

    # Add legend for categories
    ax.axhline(y=4.3, color=GRID_COLOR, linewidth=1, linestyle='-', xmin=0.25)

    # Notes
    ax.text(3, -0.6, 'Intel Gain: Higher = more intelligence from interrogation',
            fontsize=8, color=YELLOW, style='italic', ha='center')

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/15-diplomacy/15.4.1-relationship-status-effects.png',
                dpi=150, facecolor=BACKGROUND, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 15.4.1-relationship-status-effects.png")


def chart_4_intelligence_thresholds():
    """Issue #1111 - Intelligence Point Conversion Thresholds Chart"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Intelligence Gathering System', fontsize=16, color=TEXT_COLOR, y=0.98)

    # Left: Population Intelligence Thresholds
    ax1 = axes[0]
    thresholds = [100, 200, 300, 500]
    labels = ['Population size\n& installation count',
              'Factory, mine,\nspaceport data',
              'Refinery &\nmaintenance info',
              'Research &\ntraining facilities']
    colors = [CYAN, GREEN, YELLOW, RED]

    # Create stacked horizontal bars showing thresholds
    for i, (thresh, label, color) in enumerate(zip(thresholds, labels, colors)):
        ax1.barh(i, thresh, color=color, alpha=0.8, height=0.6)
        ax1.text(thresh + 10, i, f'{thresh} pts', va='center', fontsize=10, color=color)
        ax1.text(5, i, label, va='center', fontsize=9, color=TEXT_COLOR)

    ax1.set_xlim(0, 600)
    ax1.set_ylim(-0.5, 3.5)
    ax1.set_xlabel('Intelligence Points Required')
    ax1.set_title('Population Intelligence Thresholds')
    ax1.set_yticks([])
    ax1.grid(True, axis='x', alpha=0.3)

    # Right: Racial Intelligence Check Results
    ax2 = axes[1]

    # At 100 points, automated check occurs
    results = ['Technology\nTheft', 'Missile\nBlueprints', 'Grav Survey\nData',
               'Geo Survey\nData', 'System\nLocations', 'Ship Class\nSummaries']

    # Create pie chart showing possible results
    sizes = [1, 1, 1, 1, 1, 1]  # Equal probability (simplified)
    result_colors = [RED, ORANGE, YELLOW, GREEN, CYAN, PURPLE]

    wedges, texts = ax2.pie(sizes, colors=result_colors, startangle=90,
                            wedgeprops=dict(width=0.5, edgecolor=BACKGROUND))

    # Add labels around pie
    for i, (wedge, label) in enumerate(zip(wedges, results)):
        ang = (wedge.theta2 - wedge.theta1)/2. + wedge.theta1
        x = np.cos(np.deg2rad(ang))
        y = np.sin(np.deg2rad(ang))
        ax2.annotate(label, xy=(x*0.75, y*0.75), fontsize=8,
                    ha='center', va='center', color=TEXT_COLOR)

    # Center text
    ax2.text(0, 0, '100 pts\ntriggers\ncheck', ha='center', va='center',
            fontsize=11, fontweight='bold', color=YELLOW)

    ax2.set_title('Racial Intelligence Check Results\n(at 100 accumulated points)')

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/15-diplomacy/15.5.7-intelligence-thresholds.png',
                dpi=150, facecolor=BACKGROUND, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 15.5.7-intelligence-thresholds.png")


def chart_5_survey_points_body_type():
    """Issue #1154 - Survey Points by Body Type Chart (update/replace existing)"""
    fig, ax = plt.subplots(figsize=(12, 7))

    # Body types with approximate survey point requirements
    body_types = ['Asteroids', 'Comets', 'Small Moons\n(<1000km)',
                  'Large Moons\n(1000-3000km)', 'Dwarf Planets',
                  'Terrestrial\nPlanets', 'Gas Giants']

    # Survey point ranges (min, typical, max)
    min_pts = [10, 15, 30, 80, 100, 200, 400]
    typical_pts = [25, 35, 75, 150, 175, 325, 550]
    max_pts = [50, 60, 120, 220, 250, 450, 700]

    x = np.arange(len(body_types))
    width = 0.25

    # Plot bars
    ax.bar(x - width, min_pts, width, label='Minimum', color=GREEN, alpha=0.8)
    ax.bar(x, typical_pts, width, label='Typical', color=CYAN, alpha=0.8)
    ax.bar(x + width, max_pts, width, label='Maximum', color=YELLOW, alpha=0.8)

    # Add value labels on typical bars
    for i, v in enumerate(typical_pts):
        ax.text(i, v + 15, str(v), ha='center', fontsize=9, color=CYAN)

    ax.set_xlabel('Body Type')
    ax.set_ylabel('Survey Points Required')
    ax.set_title('Geological Survey Points by Celestial Body Type', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(body_types, fontsize=9)
    ax.legend(loc='upper left')
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_ylim(0, 800)

    # Add note about size dependency
    ax.text(0.98, 0.95, 'Survey points scale with body radius\nLarger bodies require more points',
           transform=ax.transAxes, fontsize=9, va='top', ha='right',
           bbox=dict(boxstyle='round', facecolor=BACKGROUND, edgecolor=YELLOW, alpha=0.8),
           color=YELLOW)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/17-exploration/17.1.1-survey-points-by-body-type.png',
                dpi=150, facecolor=BACKGROUND, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 17.1.1-survey-points-by-body-type.png")


def chart_6_survey_time_examples():
    """Issue #1158 - Survey Time Calculation Examples Chart"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Survey Time Calculation Examples', fontsize=16, color=TEXT_COLOR, y=0.98)

    # Left: Survey time by sensor count
    ax1 = axes[0]

    # Example: Terrestrial planet requiring 300 survey points
    planet_pts = 300
    sensor_configs = [
        ('1x Base\n(1 pt/hr)', 24),
        ('2x Base\n(2 pt/hr)', 48),
        ('3x Base\n(3 pt/hr)', 72),
        ('1x Improved\n(2 pt/hr)', 48),
        ('2x Improved\n(4 pt/hr)', 96),
        ('1x Advanced\n(3 pt/hr)', 72),
        ('1x Phased\n(5 pt/hr)', 120)
    ]

    configs = [c[0] for c in sensor_configs]
    pts_per_day = [c[1] for c in sensor_configs]
    survey_days = [planet_pts / p for p in pts_per_day]

    colors_gradient = [plt.cm.viridis(i/len(configs)) for i in range(len(configs))]
    bars = ax1.bar(range(len(configs)), survey_days, color=colors_gradient)

    # Add day labels
    for i, (bar, days) in enumerate(zip(bars, survey_days)):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f'{days:.1f}d', ha='center', fontsize=9, color=TEXT_COLOR)

    ax1.set_xlabel('Sensor Configuration')
    ax1.set_ylabel('Days to Complete Survey')
    ax1.set_title(f'Survey Time for Terrestrial Planet ({planet_pts} pts)')
    ax1.set_xticks(range(len(configs)))
    ax1.set_xticklabels(configs, fontsize=8, rotation=45, ha='right')
    ax1.grid(True, axis='y', alpha=0.3)

    # Right: Comparison across body types with same sensor
    ax2 = axes[1]

    # Using 2x Improved sensors (4 pts/hr = 96 pts/day)
    pts_per_day_standard = 96

    body_types = ['Asteroid\n(25 pts)', 'Comet\n(35 pts)', 'Small Moon\n(75 pts)',
                  'Large Moon\n(150 pts)', 'Terrestrial\n(300 pts)', 'Gas Giant\n(500 pts)']
    pts_required = [25, 35, 75, 150, 300, 500]
    days_required = [p / pts_per_day_standard for p in pts_required]

    colors = [GREEN, GREEN, CYAN, CYAN, YELLOW, RED]
    bars2 = ax2.barh(range(len(body_types)), days_required, color=colors, alpha=0.8)

    # Add labels
    for i, (bar, days) in enumerate(zip(bars2, days_required)):
        ax2.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                f'{days:.1f} days', va='center', fontsize=9, color=TEXT_COLOR)

    ax2.set_xlabel('Days to Complete Survey')
    ax2.set_ylabel('Body Type')
    ax2.set_title('Survey Time with 2x Improved Sensors (96 pts/day)')
    ax2.set_yticks(range(len(body_types)))
    ax2.set_yticklabels(body_types, fontsize=9)
    ax2.grid(True, axis='x', alpha=0.3)
    ax2.set_xlim(0, 6)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/17-exploration/17.1.2-survey-time-examples.png',
                dpi=150, facecolor=BACKGROUND, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: 17.1.2-survey-time-examples.png")


def chart_7_installation_costs():
    """Issue #1169 - Installation Build Costs and Mineral Dependencies Chart"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle('Installation Build Costs and Mineral Requirements', fontsize=16, color=TEXT_COLOR, y=0.98)

    # Installation data from appendix D
    installations = [
        ('Infrastructure', 2, {'Duranium': 1, 'Mercassium': 1}),
        ('Maintenance Facility', 60, {'Duranium': 30, 'Neutronium': 30}),
        ('Mine', 120, {'Corundium': 120}),
        ('Construction Factory', 120, {'Duranium': 60, 'Neutronium': 60}),
        ('Ordnance Factory', 120, {'Tritanium': 120}),
        ('Fighter Factory', 120, {'Vendarite': 120}),
        ('Fuel Refinery', 120, {'Boronide': 120}),
        ('Financial Centre', 120, {'Corbomite': 120}),
        ('Automated Mine', 240, {'Corundium': 240}),
        ('Terraforming', 300, {'Duranium': 150, 'Boronide': 150}),
        ('Mass Driver', 300, {'Duranium': 100, 'Neutronium': 100, 'Boronide': 100}),
        ('GF Construction', 2400, {'Vendarite': 2400}),
        ('Research Facility', 2400, {'Duranium': 1200, 'Mercassium': 1200}),
    ]

    # Left chart: BP costs
    ax1 = axes[0]
    names = [i[0] for i in installations]
    bp_costs = [i[1] for i in installations]

    # Color by cost tier
    colors = []
    for bp in bp_costs:
        if bp <= 60:
            colors.append(GREEN)
        elif bp <= 150:
            colors.append(CYAN)
        elif bp <= 400:
            colors.append(YELLOW)
        else:
            colors.append(RED)

    bars = ax1.barh(range(len(names)), bp_costs, color=colors, alpha=0.8)

    # Add BP labels
    for i, (bar, bp) in enumerate(zip(bars, bp_costs)):
        ax1.text(bar.get_width() + 20, bar.get_y() + bar.get_height()/2,
                f'{bp} BP', va='center', fontsize=9, color=TEXT_COLOR)

    ax1.set_xlabel('Build Points (BP)')
    ax1.set_yticks(range(len(names)))
    ax1.set_yticklabels(names, fontsize=9)
    ax1.set_title('Installation Build Costs')
    ax1.grid(True, axis='x', alpha=0.3)
    ax1.set_xlim(0, 3000)

    # Right chart: Mineral composition stacked bar
    ax2 = axes[1]

    # Mineral types and colors
    minerals = ['Duranium', 'Neutronium', 'Corbomite', 'Tritanium',
                'Boronide', 'Mercassium', 'Vendarite', 'Corundium']
    mineral_colors = {
        'Duranium': '#6366f1',   # Indigo
        'Neutronium': '#8b5cf6', # Violet
        'Corbomite': '#ec4899',  # Pink
        'Tritanium': '#f97316',  # Orange
        'Boronide': '#84cc16',   # Lime
        'Mercassium': '#14b8a6', # Teal
        'Vendarite': '#f43f5e',  # Rose
        'Corundium': '#fbbf24',  # Amber
    }

    # Build stacked data
    y_pos = np.arange(len(installations))
    left = np.zeros(len(installations))

    for mineral in minerals:
        values = []
        for inst in installations:
            minerals_dict = inst[2]
            values.append(minerals_dict.get(mineral, 0))
        if sum(values) > 0:
            ax2.barh(y_pos, values, left=left, label=mineral,
                    color=mineral_colors[mineral], alpha=0.8)
            left += values

    ax2.set_xlabel('Mineral Units Required')
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([i[0] for i in installations], fontsize=9)
    ax2.set_title('Mineral Composition by Installation')
    ax2.legend(loc='lower right', fontsize=8, ncol=2)
    ax2.grid(True, axis='x', alpha=0.3)
    ax2.set_xlim(0, 2800)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/appendices/D.2.1-installation-costs.png',
                dpi=150, facecolor=BACKGROUND, edgecolor='none', bbox_inches='tight')
    plt.close()
    print("Created: D.2.1-installation-costs.png")


if __name__ == '__main__':
    print("Generating Wave 5 Charts...")
    print("-" * 40)

    chart_1_territory_intrusion()
    chart_2_npr_archetypes()
    chart_3_relationship_status()
    chart_4_intelligence_thresholds()
    chart_5_survey_points_body_type()
    chart_6_survey_time_examples()
    chart_7_installation_costs()

    print("-" * 40)
    print("All charts generated successfully!")
