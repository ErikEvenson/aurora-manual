#!/usr/bin/env python3
"""
Generate Wave 1: Core Game Setup Charts for Aurora Manual
Creates matplotlib visualizations for issues #1048, #1067, #1076, #1080, #1096, #1106, #1110, #1114
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# Ensure output directory exists
os.makedirs('/Users/eevenson/Documents/Projects/aurora-manual/images/charts', exist_ok=True)

# Define dark theme colors
BG_COLOR = '#1a1a2e'
GRID_COLOR = '#2d2d4a'
TEXT_COLOR = '#e0e0e0'
CYAN = '#4ecdc4'
RED = '#ff6b6b'
YELLOW = '#ffe66d'
GREEN = '#95d5b2'
PURPLE = '#a78bfa'
ORANGE = '#fb923c'

def setup_dark_theme():
    """Set up the dark theme for matplotlib."""
    plt.rcParams.update({
        'figure.facecolor': BG_COLOR,
        'axes.facecolor': BG_COLOR,
        'axes.edgecolor': TEXT_COLOR,
        'axes.labelcolor': TEXT_COLOR,
        'text.color': TEXT_COLOR,
        'xtick.color': TEXT_COLOR,
        'ytick.color': TEXT_COLOR,
        'grid.color': GRID_COLOR,
        'legend.facecolor': BG_COLOR,
        'legend.edgecolor': TEXT_COLOR,
        'font.size': 10,
        'axes.titlesize': 12,
        'axes.labelsize': 10,
    })

# ============================================================================
# Chart 1: System Requirements Visualization (#1048 - Section 1.2)
# ============================================================================
def create_system_requirements_chart():
    """Create a bar chart showing minimum vs recommended system specs."""
    setup_dark_theme()

    fig, ax = plt.subplots(figsize=(10, 6))

    categories = ['RAM\n(GB)', 'Display Width\n(pixels)', 'Disk Space\n(MB)', '.NET Framework\n(version)']
    minimum = [4, 1440, 130, 4.0]
    recommended = [8, 1920, 500, 4.0]  # Disk 500MB for save games

    x = np.arange(len(categories))
    width = 0.35

    bars1 = ax.bar(x - width/2, minimum, width, label='Minimum', color=YELLOW, edgecolor=TEXT_COLOR, linewidth=1)
    bars2 = ax.bar(x + width/2, recommended, width, label='Recommended', color=CYAN, edgecolor=TEXT_COLOR, linewidth=1)

    ax.set_ylabel('Value', fontweight='bold')
    ax.set_title('Aurora C# System Requirements\nMinimum vs Recommended', fontweight='bold', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend(loc='upper right')
    ax.set_ylim(0, max(recommended) * 1.2)

    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height:.0f}' if height >= 10 else f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, color=TEXT_COLOR)

    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height:.0f}' if height >= 10 else f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, color=TEXT_COLOR)

    # Add note about CPU
    ax.text(0.02, 0.98, 'Note: CPU requirements vary; faster single-thread performance\nhelps with turn processing for large games',
            transform=ax.transAxes, fontsize=8, verticalalignment='top',
            color=TEXT_COLOR, style='italic')

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/1.2-system-requirements.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none')
    plt.close()
    print("Created: 1.2-system-requirements.png")

# ============================================================================
# Chart 2: Time Increment Impact Chart (#1067 - Section 1.3)
# ============================================================================
def create_time_increment_chart():
    """Create a chart showing time increments and their use cases."""
    setup_dark_theme()

    fig, ax = plt.subplots(figsize=(12, 7))

    # Time increments from smallest to largest
    increments = ['5 sec', '30 sec', '2 min', '5 min', '20 min', '1 hr', '3 hr', '8 hr', '1 day', '5 day', '30 day']

    # Processing time scale (relative - higher = faster real-world processing)
    processing_speed = [1, 1.5, 2, 3, 5, 8, 15, 25, 40, 60, 80]

    # Combat accuracy (higher = more precise combat resolution)
    combat_accuracy = [100, 95, 80, 60, 40, 20, 10, 5, 2, 1, 0.5]

    x = np.arange(len(increments))

    # Create twin axis
    ax2 = ax.twinx()

    # Plot processing speed
    line1 = ax.plot(x, processing_speed, 'o-', color=CYAN, linewidth=2, markersize=8, label='Processing Speed (relative)')
    ax.fill_between(x, processing_speed, alpha=0.3, color=CYAN)

    # Plot combat accuracy
    line2 = ax2.plot(x, combat_accuracy, 's-', color=RED, linewidth=2, markersize=8, label='Combat Accuracy (%)')
    ax2.fill_between(x, combat_accuracy, alpha=0.3, color=RED)

    ax.set_xlabel('Time Increment', fontweight='bold')
    ax.set_ylabel('Processing Speed (relative)', color=CYAN, fontweight='bold')
    ax2.set_ylabel('Combat Accuracy (%)', color=RED, fontweight='bold')
    ax.set_title('Time Increment Trade-offs\nProcessing Speed vs Combat Resolution Precision', fontweight='bold', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(increments, rotation=45, ha='right')

    # Add use case annotations
    annotations = [
        (0, 'Missile\nCombat'),
        (4, 'Fleet\nMovement'),
        (8, 'Peacetime\nDevelopment'),
        (10, 'Long\nCampaigns'),
    ]

    for idx, label in annotations:
        ax.annotate(label, xy=(idx, processing_speed[idx]),
                    xytext=(0, 30), textcoords='offset points',
                    ha='center', fontsize=8, color=YELLOW,
                    arrowprops=dict(arrowstyle='->', color=YELLOW, lw=1))

    # Combine legends
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc='center right')

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/1.3-time-increment-impact.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none')
    plt.close()
    print("Created: 1.3-time-increment-impact.png")

# ============================================================================
# Chart 3: Disaster Scenario Comparison Timeline (#1076 - Section 2.1)
# ============================================================================
def create_disaster_timeline_chart():
    """Create a timeline comparing different disaster scenarios."""
    setup_dark_theme()

    fig, ax = plt.subplots(figsize=(12, 6))

    # Disaster scenarios
    scenarios = [
        ('No Disaster', None, None, GREEN),
        ('Earth Death Spiral (0.01 AU/yr)', 150, 'Gradual temperature increase', YELLOW),
        ('Earth Death Spiral (0.02 AU/yr)', 75, 'Rapid temperature increase', ORANGE),
        ('Earth Death Spiral (0.03 AU/yr)', 50, 'Extreme urgency', RED),
        ('Solar Destruction (Easy)', 100, 'Sun explodes after year 50 (2%/yr chance)', YELLOW),
        ('Solar Destruction (Medium)', 75, 'Higher radiation, faster urgency', ORANGE),
        ('Solar Destruction (Hard)', 50, 'Extreme radiation from start', RED),
    ]

    y_pos = np.arange(len(scenarios))

    for i, (name, deadline, note, color) in enumerate(scenarios):
        if deadline:
            ax.barh(i, deadline, color=color, edgecolor=TEXT_COLOR, linewidth=1, height=0.6)
            ax.text(deadline + 2, i, f'{deadline} years', va='center', fontsize=9, color=TEXT_COLOR)
        else:
            ax.barh(i, 200, color=color, edgecolor=TEXT_COLOR, linewidth=1, height=0.6, alpha=0.5)
            ax.text(100, i, 'No time limit', va='center', ha='center', fontsize=9, color=TEXT_COLOR)

    ax.set_yticks(y_pos)
    ax.set_yticklabels([s[0] for s in scenarios])
    ax.set_xlabel('Approximate Years Until Destruction', fontweight='bold')
    ax.set_title('Disaster Scenario Timelines\nUrgency Comparison for Sol System Challenges', fontweight='bold', fontsize=14)
    ax.set_xlim(0, 200)

    # Add vertical line at year 50 for Solar Destruction
    ax.axvline(x=50, color=PURPLE, linestyle='--', linewidth=1, alpha=0.7)
    ax.text(52, 4.5, 'Year 50:\nSun explosion\nchance begins', fontsize=8, color=PURPLE)

    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/2.1-disaster-timeline.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none')
    plt.close()
    print("Created: 2.1-disaster-timeline.png")

# ============================================================================
# Chart 4: Game Settings Impact Matrix (#1080 - Section 2.1)
# ============================================================================
def create_settings_impact_matrix():
    """Create a matrix showing how game settings affect difficulty, performance, and pacing."""
    setup_dark_theme()

    fig, ax = plt.subplots(figsize=(12, 8))

    settings = [
        'NPR Generation %',
        'NPR Difficulty Modifier',
        'Research Speed %',
        'Terraforming Speed %',
        'Orbital Motion',
        'One Second Sub Pulse',
        'Generate Precursors',
        'Generate Raiders',
        'Number of NPRs',
        'Max Systems',
    ]

    impacts = ['Difficulty', 'Performance', 'Game Pacing', 'Replayability']

    # Impact matrix: -2 (major decrease) to +2 (major increase)
    # For each setting: [difficulty, performance, pacing, replayability]
    data = np.array([
        [2, -1, 0, 1],    # NPR Generation %
        [2, 0, 1, 1],     # NPR Difficulty Modifier
        [-1, 0, -1, 0],   # Research Speed %
        [0, -1, -1, 0],   # Terraforming Speed %
        [0, -1, 0, 0],    # Orbital Motion
        [0, -1, 0, 0],    # One Second Sub Pulse
        [1, -1, 0, 2],    # Generate Precursors
        [2, -1, 1, 2],    # Generate Raiders
        [2, -2, 1, 1],    # Number of NPRs
        [1, -2, 1, 2],    # Max Systems
    ])

    # Create heatmap
    cmap = plt.cm.RdYlGn_r  # Red-Yellow-Green reversed (green = easy/fast)
    im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=-2, vmax=2)

    # Set ticks
    ax.set_xticks(np.arange(len(impacts)))
    ax.set_yticks(np.arange(len(settings)))
    ax.set_xticklabels(impacts, fontweight='bold')
    ax.set_yticklabels(settings)

    # Add text annotations
    for i in range(len(settings)):
        for j in range(len(impacts)):
            val = data[i, j]
            text = '+' + str(val) if val > 0 else str(val) if val < 0 else '0'
            color = 'black' if abs(val) <= 1 else 'white'
            ax.text(j, i, text, ha='center', va='center', color=color, fontweight='bold')

    ax.set_title('Game Settings Impact Matrix\nHow Settings Affect Your Game Experience', fontweight='bold', fontsize=14)

    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.6)
    cbar.set_label('Impact (Higher Value = Increase)', fontweight='bold')
    cbar.set_ticks([-2, -1, 0, 1, 2])
    cbar.set_ticklabels(['Major\nDecrease', 'Minor\nDecrease', 'Neutral', 'Minor\nIncrease', 'Major\nIncrease'])

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/2.1-settings-impact-matrix.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none')
    plt.close()
    print("Created: 2.1-settings-impact-matrix.png")

# ============================================================================
# Chart 5: Starting Installation Trade-offs (#1096 - Section 2.2)
# ============================================================================
def create_installation_tradeoffs_chart():
    """Create a chart comparing starting installation production rates."""
    setup_dark_theme()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Installation production rates
    installations = ['Shipyards\n(per slipway)', 'Research Labs', 'Construction\nFactories',
                     'Mines\n(100% access)', 'Fuel Refineries', 'Ordnance\nFactories']

    production_rate = [400, 200, 10, 10, 40000, 10]  # Per year at base tech
    units = ['BP/yr', 'RP/yr', 'BP/yr', 'tons/yr', 'litres/yr', 'BP/yr']

    colors = [CYAN, GREEN, YELLOW, ORANGE, PURPLE, RED]

    # Bar chart of production rates (normalized for display)
    # Normalize to show relative scale
    normalized = [400, 200, 10, 10, 40, 10]  # Fuel at 40 for display (actual is 40k)

    bars = ax1.barh(installations, normalized, color=colors, edgecolor=TEXT_COLOR, linewidth=1)
    ax1.set_xlabel('Production Rate (relative scale)', fontweight='bold')
    ax1.set_title('Installation Production Rates\n(Base Technology)', fontweight='bold', fontsize=12)

    # Add actual values as labels
    for bar, rate, unit in zip(bars, production_rate, units):
        width = bar.get_width()
        label = f'{rate:,} {unit}'
        ax1.text(width + 5, bar.get_y() + bar.get_height()/2, label,
                 va='center', fontsize=9, color=TEXT_COLOR)

    ax1.set_xlim(0, 500)

    # Government type starting installations comparison
    gov_types = ['Player Race', 'Military\nDictatorship', 'Contemplative', 'Corporate']

    # Percentages from game data
    shipyards = [20, 30, 10, 15]
    labs = [20, 10, 40, 20]
    construction = [30, 25, 30, 30]
    mines = [20, 20, 10, 30]

    x = np.arange(len(gov_types))
    width = 0.2

    ax2.bar(x - 1.5*width, shipyards, width, label='Shipyards', color=CYAN, edgecolor=TEXT_COLOR)
    ax2.bar(x - 0.5*width, labs, width, label='Research Labs', color=GREEN, edgecolor=TEXT_COLOR)
    ax2.bar(x + 0.5*width, construction, width, label='Construction', color=YELLOW, edgecolor=TEXT_COLOR)
    ax2.bar(x + 1.5*width, mines, width, label='Mines', color=ORANGE, edgecolor=TEXT_COLOR)

    ax2.set_ylabel('Starting Installations (%)', fontweight='bold')
    ax2.set_title('Government Type Starting Installations\n(Relative Allocation)', fontweight='bold', fontsize=12)
    ax2.set_xticks(x)
    ax2.set_xticklabels(gov_types)
    ax2.legend(loc='upper right', fontsize=8)
    ax2.set_ylim(0, 50)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/2.2-installation-tradeoffs.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none')
    plt.close()
    print("Created: 2.2-installation-tradeoffs.png")

# ============================================================================
# Chart 6: Accessibility Degradation Graph (#1106 - Section 2.3)
# ============================================================================
def create_accessibility_degradation_chart():
    """Create a graph showing mineral accessibility decline over mining."""
    setup_dark_theme()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Simulate accessibility degradation curve
    # Accessibility decreases as deposit is depleted
    percent_mined = np.linspace(0, 100, 100)

    # Different starting accessibilities
    start_access = [1.0, 0.8, 0.5, 0.3]
    colors = [CYAN, GREEN, YELLOW, RED]

    for access, color in zip(start_access, colors):
        # Accessibility degrades proportionally as deposit depletes
        # When half the original amount is mined, accessibility halves
        remaining = 1 - (percent_mined / 100)
        current_access = access * np.sqrt(remaining)  # Square root decay approximation
        ax1.plot(percent_mined, current_access, color=color, linewidth=2,
                 label=f'Starting: {access:.1f}')

    ax1.set_xlabel('Deposit Mined (%)', fontweight='bold')
    ax1.set_ylabel('Current Accessibility', fontweight='bold')
    ax1.set_title('Mineral Accessibility Degradation\nOver Deposit Lifetime', fontweight='bold', fontsize=12)
    ax1.legend(loc='upper right')
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 1.1)
    ax1.grid(True, alpha=0.3)

    # Add annotations for decision points
    ax1.axhline(y=0.3, color=ORANGE, linestyle='--', alpha=0.7)
    ax1.text(50, 0.32, 'Consider relocating mines', fontsize=8, color=ORANGE)
    ax1.axhline(y=0.1, color=RED, linestyle='--', alpha=0.7)
    ax1.text(50, 0.12, 'Economically unviable', fontsize=8, color=RED)

    # Effective mining rate over time
    years = np.linspace(0, 100, 100)

    # 10 mines at different accessibilities
    mine_output_base = 10  # tons per mine per year
    for access, color in zip(start_access, colors):
        # Simulate declining output as deposit depletes and accessibility drops
        deposit_remaining = 10000 * np.exp(-0.03 * years)  # Exponential depletion
        current_access = access * np.sqrt(deposit_remaining / 10000)
        output = 10 * mine_output_base * current_access
        ax2.plot(years, output, color=color, linewidth=2, label=f'Start Access: {access:.1f}')

    ax2.set_xlabel('Years of Mining', fontweight='bold')
    ax2.set_ylabel('Annual Output (tons)', fontweight='bold')
    ax2.set_title('10 Mines Output Over Time\n(10,000 ton deposit)', fontweight='bold', fontsize=12)
    ax2.legend(loc='upper right')
    ax2.set_xlim(0, 100)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/2.3-accessibility-degradation.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none')
    plt.close()
    print("Created: 2.3-accessibility-degradation.png")

# ============================================================================
# Chart 7: Species Attribute Impact Matrix (#1110 - Section 2.4)
# ============================================================================
def create_species_attribute_matrix():
    """Create a matrix showing how species traits affect colonization options."""
    setup_dark_theme()

    fig, ax = plt.subplots(figsize=(12, 8))

    traits = [
        'High Temp Tolerance',
        'Wide Gravity Range',
        'Exotic Atmosphere',
        'High Pop Growth',
        'High Production',
        'High Research',
        'High Ground Combat',
    ]

    outcomes = ['Habitable\nWorlds', 'Colony\nCost', 'Terraforming\nNeeded',
                'Economic\nOutput', 'Military\nStrength', 'Tech\nAdvancement']

    # Impact matrix: -2 to +2
    data = np.array([
        [2, -1, -1, 0, 0, 0],    # High Temp Tolerance
        [2, -1, -1, 0, 0, 0],    # Wide Gravity Range
        [1, 0, 1, 0, 0, 0],      # Exotic Atmosphere
        [0, 0, 0, 1, 0, 0],      # High Pop Growth
        [0, 0, 0, 2, 1, -1],     # High Production
        [0, 0, 0, -1, 0, 2],     # High Research
        [0, 0, 0, 0, 2, 0],      # High Ground Combat
    ])

    cmap = plt.cm.RdYlGn
    im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=-2, vmax=2)

    ax.set_xticks(np.arange(len(outcomes)))
    ax.set_yticks(np.arange(len(traits)))
    ax.set_xticklabels(outcomes, fontweight='bold')
    ax.set_yticklabels(traits)

    # Add text annotations
    for i in range(len(traits)):
        for j in range(len(outcomes)):
            val = data[i, j]
            if val != 0:
                text = '+' + str(val) if val > 0 else str(val)
                color = 'black' if abs(val) <= 1 else 'white'
                ax.text(j, i, text, ha='center', va='center', color=color, fontweight='bold')

    ax.set_title('Species Trait Impact on Colonization & Gameplay\nChoose Traits to Match Your Strategy', fontweight='bold', fontsize=14)

    cbar = plt.colorbar(im, ax=ax, shrink=0.6)
    cbar.set_label('Impact', fontweight='bold')
    cbar.set_ticks([-2, -1, 0, 1, 2])
    cbar.set_ticklabels(['Strong\nNegative', 'Negative', 'Neutral', 'Positive', 'Strong\nPositive'])

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/2.4-species-attribute-matrix.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none')
    plt.close()
    print("Created: 2.4-species-attribute-matrix.png")

# ============================================================================
# Chart 8: Economic Modifier Stacking Graph (#1114 - Section 2.4)
# ============================================================================
def create_economic_modifier_stacking_chart():
    """Create a graph showing compound effects of economic modifiers over time."""
    setup_dark_theme()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    years = np.arange(0, 101, 1)

    # Population growth with different modifiers
    base_pop = 1000  # 1 billion starting population
    growth_rate_base = 0.02  # 2% annual growth

    modifiers = [0.7, 1.0, 1.1, 1.3, 1.5]
    colors = [RED, TEXT_COLOR, YELLOW, GREEN, CYAN]

    for mod, color in zip(modifiers, colors):
        effective_rate = growth_rate_base * mod
        population = base_pop * np.exp(effective_rate * years)
        ax1.plot(years, population / 1000, color=color, linewidth=2, label=f'{mod}x growth')

    ax1.set_xlabel('Years', fontweight='bold')
    ax1.set_ylabel('Population (billions)', fontweight='bold')
    ax1.set_title('Population Growth Over 100 Years\nWith Different Growth Rate Modifiers', fontweight='bold', fontsize=12)
    ax1.legend(loc='upper left')
    ax1.set_xlim(0, 100)
    ax1.set_yscale('log')
    ax1.grid(True, alpha=0.3)

    # Add annotation showing difference at year 100
    ax1.axvline(x=100, color=GRID_COLOR, linestyle='--', alpha=0.5)

    # Production output with stacking modifiers
    base_production = 100  # Base annual production

    # Different stacking scenarios
    scenarios = {
        'Base (1.0x)': [1.0],
        'Species 1.1x': [1.1],
        'Species 1.3x': [1.3],
        'Species 1.1x + Tech 1.2x': [1.1, 1.2],
        'Species 1.3x + Tech 1.4x': [1.3, 1.4],
        'Species 1.3x + Tech 1.4x + Gov 1.2x': [1.3, 1.4, 1.2],
    }

    scenario_names = list(scenarios.keys())
    total_multipliers = []

    for name, mods in scenarios.items():
        total = 1.0
        for m in mods:
            total *= m
        total_multipliers.append(total)

    colors = [TEXT_COLOR, YELLOW, GREEN, ORANGE, CYAN, PURPLE]
    bars = ax2.barh(scenario_names, total_multipliers, color=colors, edgecolor=TEXT_COLOR, linewidth=1)

    ax2.set_xlabel('Total Multiplier', fontweight='bold')
    ax2.set_title('Economic Modifier Stacking\n(Multiplicative Bonuses)', fontweight='bold', fontsize=12)
    ax2.set_xlim(0, 2.5)

    # Add value labels
    for bar in bars:
        width = bar.get_width()
        ax2.text(width + 0.02, bar.get_y() + bar.get_height()/2, f'{width:.2f}x',
                 va='center', fontsize=9, color=TEXT_COLOR)

    # Add reference line at 1.0
    ax2.axvline(x=1.0, color=RED, linestyle='--', alpha=0.7, linewidth=1)
    ax2.text(1.02, 0, 'Base', fontsize=8, color=RED)

    plt.tight_layout()
    plt.savefig('/Users/eevenson/Documents/Projects/aurora-manual/images/charts/2.4-economic-modifier-stacking.png',
                dpi=150, facecolor=BG_COLOR, edgecolor='none')
    plt.close()
    print("Created: 2.4-economic-modifier-stacking.png")

# ============================================================================
# Main execution
# ============================================================================
if __name__ == '__main__':
    print("Generating Wave 1 Charts...")
    print("-" * 50)

    create_system_requirements_chart()       # #1048
    create_time_increment_chart()            # #1067
    create_disaster_timeline_chart()         # #1076
    create_settings_impact_matrix()          # #1080
    create_installation_tradeoffs_chart()    # #1096
    create_accessibility_degradation_chart() # #1106
    create_species_attribute_matrix()        # #1110
    create_economic_modifier_stacking_chart() # #1114

    print("-" * 50)
    print("All Wave 1 charts generated successfully!")
