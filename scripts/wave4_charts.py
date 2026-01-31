#!/usr/bin/env python3
"""
Generate Wave 4: Logistics & Commander Charts for Aurora Manual
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# Dark theme colors
BG_COLOR = '#1a1a2e'
GRID_COLOR = '#2d2d44'
TEXT_COLOR = '#ffffff'
CYAN = '#4ecdc4'
RED = '#ff6b6b'
YELLOW = '#ffe66d'
GREEN = '#95d5b2'
PURPLE = '#9b5de5'
ORANGE = '#f4a261'

# Set up dark style
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
})


def create_chart_dir(subdir):
    """Create chart directory if it doesn't exist."""
    path = f'/Users/eevenson/Documents/Projects/aurora-manual/images/charts/{subdir}'
    os.makedirs(path, exist_ok=True)
    return path


def chart_14_1_fuel_consumption_vs_speed():
    """
    Issue #1151: Fuel Consumption vs Ship Speed Chart
    Fuel consumption scales with speed squared.
    """
    chart_dir = create_chart_dir('14-logistics')

    fig, ax = plt.subplots(figsize=(10, 6))

    # Speed as percentage of maximum (10% to 100%)
    speed_pct = np.linspace(10, 100, 100)

    # Relative fuel consumption (normalized to 100% at max speed)
    # Fuel consumption ~ speed^2
    fuel_consumption = (speed_pct / 100) ** 2 * 100

    # Efficiency curve (distance per unit fuel, inverse of consumption per distance)
    # Higher speed = more fuel per km, but faster travel
    # Range efficiency = speed / fuel_consumption_rate ~ speed / speed^2 = 1/speed
    range_efficiency = (100 / speed_pct) * 100  # Normalized so 100% speed = 100% reference

    ax.plot(speed_pct, fuel_consumption, color=CYAN, linewidth=2.5, label='Fuel Consumption Rate')
    ax.plot(speed_pct, range_efficiency, color=GREEN, linewidth=2.5, linestyle='--', label='Range Efficiency')

    # Fill between to show the efficiency gap
    ax.fill_between(speed_pct, fuel_consumption, alpha=0.3, color=CYAN)

    # Mark key efficiency points
    ax.axvline(x=50, color=YELLOW, linewidth=1.5, linestyle=':', alpha=0.8)
    ax.text(51, 85, '50% Speed:\n25% Fuel Rate\n200% Range', fontsize=9, color=YELLOW, va='top')

    ax.axvline(x=70, color=ORANGE, linewidth=1.5, linestyle=':', alpha=0.8)
    ax.text(71, 65, '70% Speed:\n49% Fuel Rate\n143% Range', fontsize=9, color=ORANGE, va='top')

    # Annotations
    ax.annotate('Speed^2 Relationship:\nDouble speed = 4x fuel consumption',
                xy=(80, 64), xytext=(60, 45),
                arrowprops=dict(arrowstyle='->', color=RED),
                fontsize=9, color=RED,
                bbox=dict(boxstyle='round', facecolor=BG_COLOR, edgecolor=RED))

    ax.set_xlabel('Ship Speed (% of Maximum)', fontsize=12)
    ax.set_ylabel('Relative Value (%)', fontsize=12)
    ax.set_title('Fuel Consumption vs Ship Speed\n(Square Relationship)', fontsize=14, fontweight='bold')
    ax.set_xlim(0, 105)
    ax.set_ylim(0, 200)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{chart_dir}/14.1.2-fuel-consumption-vs-speed.png', dpi=150, facecolor=BG_COLOR)
    plt.close()
    print(f"Created: {chart_dir}/14.1.2-fuel-consumption-vs-speed.png")


def chart_14_2_maintenance_failure_curve():
    """
    Issue #1153: Maintenance Clock vs Failure Risk Curve
    Failure risk escalates as maintenance clock exceeds rated life.
    """
    chart_dir = create_chart_dir('14-logistics')

    fig, ax = plt.subplots(figsize=(10, 6))

    # Maintenance clock as percentage of rated maintenance life
    maint_pct = np.linspace(0, 200, 200)

    # Failure probability model:
    # - Near zero until ~80% of maintenance life
    # - Gradual increase 80-100%
    # - Rapid escalation beyond 100%
    # Using a sigmoid-like curve shifted to 100%
    def failure_prob(x):
        # Low probability phase (0-80%)
        if x < 80:
            return 0.5 * (x / 80) ** 3
        # Transition phase (80-100%)
        elif x < 100:
            return 0.5 + 9.5 * ((x - 80) / 20) ** 2
        # Critical phase (>100%)
        else:
            return min(95, 10 + 85 * (1 - np.exp(-(x - 100) / 30)))

    failure_probs = np.array([failure_prob(x) for x in maint_pct])

    ax.plot(maint_pct, failure_probs, color=RED, linewidth=3)

    # Zone coloring
    ax.axvspan(0, 80, alpha=0.2, color=GREEN, label='Safe Operating Zone (0-80%)')
    ax.axvspan(80, 100, alpha=0.2, color=YELLOW, label='Caution Zone (80-100%)')
    ax.axvspan(100, 200, alpha=0.2, color=RED, label='Critical Zone (>100%)')

    # Critical threshold markers
    ax.axvline(x=100, color=RED, linewidth=2, linestyle='--')
    ax.text(102, 50, 'Maintenance Life\nExceeded', fontsize=10, color=RED, fontweight='bold')

    ax.axvline(x=80, color=YELLOW, linewidth=1.5, linestyle='--')
    ax.text(82, 10, 'Schedule\nOverhaul', fontsize=9, color=YELLOW)

    # Add explanation box
    textstr = 'Failure Escalation:\n- 0-80%: Minimal risk\n- 80-100%: Rising risk\n- >100%: Rapid escalation\n- >150%: Near-certain failures'
    props = dict(boxstyle='round', facecolor=BG_COLOR, edgecolor=CYAN, alpha=0.9)
    ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=props, color=TEXT_COLOR)

    ax.set_xlabel('Maintenance Clock (% of Rated Life)', fontsize=12)
    ax.set_ylabel('Component Failure Probability (%)', fontsize=12)
    ax.set_title('Maintenance Clock vs Component Failure Risk', fontsize=14, fontweight='bold')
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 100)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='center right', fontsize=9)

    plt.tight_layout()
    plt.savefig(f'{chart_dir}/14.2.1-maintenance-failure-curve.png', dpi=150, facecolor=BG_COLOR)
    plt.close()
    print(f"Created: {chart_dir}/14.2.1-maintenance-failure-curve.png")


def chart_14_2_maintenance_capacity():
    """
    Issue #1160: Maintenance Facility Capacity Scaling Chart
    Based on tech levels from database: 1,000 to 6,250 tons capacity.
    """
    chart_dir = create_chart_dir('14-logistics')

    fig, ax = plt.subplots(figsize=(10, 6))

    # Fleet tonnage ranges (in thousands of tons)
    fleet_tonnage = np.array([10, 25, 50, 100, 200, 400, 800, 1600]) * 1000

    # Tech levels and their capacity per facility (from database ref 14.2-2)
    tech_levels = [
        ('Base', 1000),
        ('Level 3', 1500),
        ('Level 5', 2500),
        ('Level 7', 4000),
        ('Level 9', 6250),
    ]

    colors = [GREEN, YELLOW, ORANGE, RED, PURPLE]

    for (tech_name, capacity), color in zip(tech_levels, colors):
        facilities_needed = fleet_tonnage / capacity
        ax.plot(fleet_tonnage / 1000, facilities_needed,
                color=color, linewidth=2.5, marker='o', markersize=6,
                label=f'{tech_name} ({capacity:,} tons/facility)')

    # Add reference lines for common facility counts
    for fac_count in [5, 10, 20, 50]:
        ax.axhline(y=fac_count, color=GRID_COLOR, linewidth=1, linestyle=':', alpha=0.5)
        ax.text(1610, fac_count + 1, f'{fac_count} facilities', fontsize=8, color=TEXT_COLOR, alpha=0.7)

    # Annotations
    ax.annotate('Higher tech = fewer facilities needed',
                xy=(400, 160), xytext=(600, 400),
                arrowprops=dict(arrowstyle='->', color=CYAN),
                fontsize=10, color=CYAN)

    ax.set_xlabel('Fleet Tonnage (thousands of tons)', fontsize=12)
    ax.set_ylabel('Maintenance Facilities Required', fontsize=12)
    ax.set_title('Maintenance Facility Requirements by Fleet Size and Tech Level', fontsize=14, fontweight='bold')
    ax.set_xlim(0, 1700)
    ax.set_ylim(0, 500)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', fontsize=9)

    # Use log scale for better readability
    ax.set_yscale('log')
    ax.set_ylim(1, 2000)

    plt.tight_layout()
    plt.savefig(f'{chart_dir}/14.2.2-maintenance-capacity-scaling.png', dpi=150, facecolor=BG_COLOR)
    plt.close()
    print(f"Created: {chart_dir}/14.2.2-maintenance-capacity-scaling.png")


def chart_16_1_officer_type_distribution():
    """
    Issue #1119: Officer Type Generation Probability by Commandant Chart
    Shows base distribution and commandant influence.
    """
    chart_dir = create_chart_dir('16-commanders')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Base distribution (no commandant)
    officer_types = ['Naval\nOfficer', 'Ground Forces\nOfficer', 'Administrator', 'Scientist']
    base_probs = [60, 25, 8, 7]

    # Colors for each type
    colors = [CYAN, GREEN, YELLOW, PURPLE]

    # Pie chart for base distribution
    wedges, texts, autotexts = ax1.pie(base_probs, labels=officer_types, autopct='%1.0f%%',
                                        colors=colors, explode=[0.02]*4,
                                        textprops={'color': TEXT_COLOR, 'fontsize': 11})
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontweight('bold')
    ax1.set_title('Base Officer Type Distribution\n(No Commandant)', fontsize=13, fontweight='bold')

    # Bar chart for commandant influence
    commandant_types = ['Naval\nOfficer', 'Ground Forces\nOfficer', 'Scientist', 'Administrator']
    same_type_chance = [80, 40, 14, 16]  # From ref 16.1-1
    fallback_chance = [20, 60, 86, 84]   # Remainder goes to base distribution

    x = np.arange(len(commandant_types))
    width = 0.35

    bars1 = ax2.bar(x - width/2, same_type_chance, width, color=CYAN, label='Same Type as Commandant')
    bars2 = ax2.bar(x + width/2, fallback_chance, width, color=GREEN, alpha=0.7, label='Base Distribution')

    ax2.set_xlabel('Commandant Type', fontsize=12)
    ax2.set_ylabel('Probability (%)', fontsize=12)
    ax2.set_title('Effect of Commandant on Officer Type Generation', fontsize=13, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(commandant_types)
    ax2.set_ylim(0, 100)
    ax2.legend(loc='upper right', fontsize=10)
    ax2.grid(True, axis='y', alpha=0.3)

    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax2.annotate(f'{int(height)}%',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontsize=9, color=CYAN)

    plt.tight_layout()
    plt.savefig(f'{chart_dir}/16.1.1-officer-type-distribution.png', dpi=150, facecolor=BG_COLOR)
    plt.close()
    print(f"Created: {chart_dir}/16.1.1-officer-type-distribution.png")


def chart_16_1_retirement_time_by_rank():
    """
    Issue #1124: Minimum Retirement Time by Rank Chart
    From ref 16.1-4: 10 years for lowest rank, +5 years per rank above.
    """
    chart_dir = create_chart_dir('16-commanders')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Naval ranks
    naval_ranks = ['Lt Commander', 'Commander', 'Captain', 'Rear Adm (LH)',
                   'Rear Adm (UH)', 'Vice Admiral', 'Admiral', 'Fleet Admiral']
    naval_years = [10, 15, 20, 25, 30, 35, 40, 45]

    y_pos = np.arange(len(naval_ranks))
    bars1 = ax1.barh(y_pos, naval_years, color=CYAN, height=0.6)
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(naval_ranks)
    ax1.set_xlabel('Minimum Years Before Retirement', fontsize=12)
    ax1.set_title('Naval Officer Minimum Retirement Time', fontsize=13, fontweight='bold')
    ax1.set_xlim(0, 50)
    ax1.grid(True, axis='x', alpha=0.3)

    # Add value labels
    for bar in bars1:
        width = bar.get_width()
        ax1.annotate(f'{int(width)} yrs',
                    xy=(width, bar.get_y() + bar.get_height()/2),
                    xytext=(3, 0), textcoords='offset points',
                    ha='left', va='center', fontsize=9, color=TEXT_COLOR)

    # Career types comparison
    career_types = ['Naval\n(lowest rank)', 'Naval\n(Captain)', 'Ground\n(lowest rank)',
                    'Ground\n(Colonel)', 'Scientists', 'Administrators']
    min_years = [10, 20, 20, 30, 40, 40]

    colors = [CYAN, CYAN, GREEN, GREEN, PURPLE, YELLOW]
    bars2 = ax2.bar(career_types, min_years, color=colors)
    ax2.set_xlabel('Career Type', fontsize=12)
    ax2.set_ylabel('Minimum Years Before Retirement', fontsize=12)
    ax2.set_title('Retirement Eligibility by Career Type', fontsize=13, fontweight='bold')
    ax2.set_ylim(0, 50)
    ax2.grid(True, axis='y', alpha=0.3)

    # Add value labels
    for bar in bars2:
        height = bar.get_height()
        ax2.annotate(f'{int(height)} yrs',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontsize=9, color=TEXT_COLOR)

    # Add note about retirement probability
    textstr = 'After eligibility:\n20% chance/year (assigned)\n40% chance/year (unassigned)'
    props = dict(boxstyle='round', facecolor=BG_COLOR, edgecolor=RED, alpha=0.9)
    ax2.text(0.98, 0.02, textstr, transform=ax2.transAxes, fontsize=9,
            verticalalignment='bottom', horizontalalignment='right', bbox=props, color=RED)

    plt.tight_layout()
    plt.savefig(f'{chart_dir}/16.1.4-retirement-time-by-rank.png', dpi=150, facecolor=BG_COLOR)
    plt.close()
    print(f"Created: {chart_dir}/16.1.4-retirement-time-by-rank.png")


def chart_16_2_skill_bonus_generation():
    """
    Issue #1130: Skill Bonus Generation Probability Chart
    From section 16.2.2 bonus generation table.
    """
    chart_dir = create_chart_dir('16-commanders')

    fig, ax = plt.subplots(figsize=(12, 7))

    # Bonus types and their generation chances (from 16.2.2)
    bonus_types = ['Crew Training', 'Ground Combat\n(Off/Def)', 'Logistics\n(Naval)',
                   'Light Tactical', 'Production/Mining/\nTerraforming', 'Tactical', 'Engineering']
    gen_chances = [80, 50, 50, 40, 20, 20, 20]

    colors = [CYAN, GREEN, YELLOW, PURPLE, ORANGE, RED, '#7fb3d5']

    x = np.arange(len(bonus_types))
    bars = ax.bar(x, gen_chances, color=colors, width=0.6, edgecolor=TEXT_COLOR, linewidth=1)

    ax.set_xlabel('Bonus Type', fontsize=12)
    ax.set_ylabel('Generation Probability (%)', fontsize=12)
    ax.set_title('Skill Bonus Generation Probability at Officer Creation', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(bonus_types, fontsize=10)
    ax.set_ylim(0, 100)
    ax.grid(True, axis='y', alpha=0.3)

    # Add value labels on bars
    for bar, chance in zip(bars, gen_chances):
        height = bar.get_height()
        ax.annotate(f'{int(chance)}%',
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', va='bottom', fontsize=11, fontweight='bold', color=TEXT_COLOR)

    # Add frequency bands
    ax.axhline(y=80, color=CYAN, linewidth=1, linestyle='--', alpha=0.5)
    ax.axhline(y=50, color=YELLOW, linewidth=1, linestyle='--', alpha=0.5)
    ax.axhline(y=20, color=RED, linewidth=1, linestyle='--', alpha=0.5)

    ax.text(6.8, 82, 'Very Common', fontsize=9, color=CYAN, ha='right')
    ax.text(6.8, 52, 'Common', fontsize=9, color=YELLOW, ha='right')
    ax.text(6.8, 22, 'Uncommon', fontsize=9, color=RED, ha='right')

    # Add note about bonus bands
    textstr = 'Notes:\n- Crew Training concentrated in 5-10% bands\n- Political bonuses capped above 10%\n- Commandants grant double-roll advantage'
    props = dict(boxstyle='round', facecolor=BG_COLOR, edgecolor=GREEN, alpha=0.9)
    ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=props, color=TEXT_COLOR)

    plt.tight_layout()
    plt.savefig(f'{chart_dir}/16.2.2-skill-bonus-generation.png', dpi=150, facecolor=BG_COLOR)
    plt.close()
    print(f"Created: {chart_dir}/16.2.2-skill-bonus-generation.png")


def chart_16_2_crew_training_grade():
    """
    Issue #1131: Crew Training Grade Accumulation Curve Graph
    Formula: Grade Bonus = SQRT(Grade Points) - 10, max 1000 points
    """
    chart_dir = create_chart_dir('16-commanders')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Grade points from 0 to 1000
    grade_points = np.linspace(0, 1000, 200)

    # Grade bonus formula: SQRT(Grade Points) - 10
    grade_bonus = np.sqrt(grade_points) - 10
    grade_bonus = np.maximum(grade_bonus, 0)  # Floor at 0

    ax1.plot(grade_points, grade_bonus, color=CYAN, linewidth=3)
    ax1.fill_between(grade_points, grade_bonus, alpha=0.3, color=CYAN)

    # Mark key milestones
    milestones = [(100, 'Novice'), (250, 'Trained'), (500, 'Veteran'), (750, 'Elite'), (1000, 'Maximum')]
    for points, label in milestones:
        bonus = np.sqrt(points) - 10
        ax1.scatter([points], [bonus], color=YELLOW, s=80, zorder=5)
        ax1.annotate(f'{label}\n{bonus:.1f}%',
                    xy=(points, bonus), xytext=(5, 10),
                    textcoords='offset points', fontsize=9, color=YELLOW)

    ax1.set_xlabel('Crew Grade Points', fontsize=12)
    ax1.set_ylabel('Crew Grade Bonus (%)', fontsize=12)
    ax1.set_title('Crew Training Grade Bonus\n(SQRT Formula: Diminishing Returns)', fontsize=13, fontweight='bold')
    ax1.set_xlim(0, 1050)
    ax1.set_ylim(0, 25)
    ax1.grid(True, alpha=0.3)

    # Marginal return curve
    marginal_points = np.linspace(100, 1000, 100)
    # Derivative of sqrt(x) - 10 is 1/(2*sqrt(x))
    marginal_return = 1 / (2 * np.sqrt(marginal_points)) * 100  # Per 100 points gained

    ax2.plot(marginal_points, marginal_return, color=RED, linewidth=3)
    ax2.fill_between(marginal_points, marginal_return, alpha=0.3, color=RED)

    ax2.set_xlabel('Current Grade Points', fontsize=12)
    ax2.set_ylabel('Bonus Gain per 100 Points', fontsize=12)
    ax2.set_title('Diminishing Returns:\nMarginal Bonus per Training Investment', fontsize=13, fontweight='bold')
    ax2.set_xlim(0, 1050)
    ax2.set_ylim(0, 6)
    ax2.grid(True, alpha=0.3)

    # Add annotation about investment efficiency
    ax2.annotate('Early training more\nefficient than later',
                xy=(200, 3.5), xytext=(400, 4.5),
                arrowprops=dict(arrowstyle='->', color=YELLOW),
                fontsize=10, color=YELLOW,
                bbox=dict(boxstyle='round', facecolor=BG_COLOR, edgecolor=YELLOW))

    # Add the formula as text
    textstr = 'Formula: Bonus = SQRT(Points) - 10\nMax Points: 1000\nMax Bonus: 21.6%'
    props = dict(boxstyle='round', facecolor=BG_COLOR, edgecolor=CYAN, alpha=0.9)
    ax1.text(0.02, 0.98, textstr, transform=ax1.transAxes, fontsize=10,
            verticalalignment='top', bbox=props, color=TEXT_COLOR)

    plt.tight_layout()
    plt.savefig(f'{chart_dir}/16.2.3-crew-training-grade.png', dpi=150, facecolor=BG_COLOR)
    plt.close()
    print(f"Created: {chart_dir}/16.2.3-crew-training-grade.png")


def chart_16_2_promotion_score_ranges():
    """
    Issue #1137: Promotion Score Ranges by Rank Chart
    From section 16.2.5.4 typical score ranges.
    """
    chart_dir = create_chart_dir('16-commanders')

    fig, ax = plt.subplots(figsize=(12, 7))

    # Ranks and their typical score ranges (from 16.2.5)
    ranks = ['Lt Commander', 'Commander', 'Captain', 'Rear Admiral\n(Lower Half)',
             'Rear Admiral\n(Upper Half)', 'Vice Admiral', 'Admiral', 'Fleet Admiral']

    # Score ranges [min, max]
    score_ranges = [
        (25, 412),
        (316, 553),
        (281, 725),
        (732, 914),
        (925, 1011),
        (1058, 1153),
        (1251, 1293),
        (1300, 1500),  # Approximate for Fleet Admiral
    ]

    y_pos = np.arange(len(ranks))

    # Plot ranges as horizontal bars
    for i, (rank, (min_score, max_score)) in enumerate(zip(ranks, score_ranges)):
        ax.barh(i, max_score - min_score, left=min_score, height=0.6,
                color=CYAN, alpha=0.7, edgecolor=TEXT_COLOR, linewidth=1)

        # Add min/max labels
        ax.text(min_score - 30, i, f'{min_score}', fontsize=9, va='center', ha='right', color=GREEN)
        ax.text(max_score + 10, i, f'{max_score}', fontsize=9, va='center', ha='left', color=RED)

        # Add median marker
        median = (min_score + max_score) / 2
        ax.scatter([median], [i], color=YELLOW, s=60, zorder=5, marker='|')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(ranks)
    ax.set_xlabel('Promotion Score', fontsize=12)
    ax.set_title('Typical Promotion Score Ranges by Rank', fontsize=14, fontweight='bold')
    ax.set_xlim(0, 1600)
    ax.grid(True, axis='x', alpha=0.3)

    # Add legend for markers
    legend_elements = [
        mpatches.Patch(facecolor=CYAN, alpha=0.7, edgecolor=TEXT_COLOR, label='Score Range'),
        plt.Line2D([0], [0], marker='|', color=YELLOW, markersize=10,
                   linestyle='None', label='Median'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=10)

    # Add note about score sources
    textstr = 'Score Sources:\n- Medals & Ribbons\n- Research Completions (scientists)\n- Time in Grade (eligibility factor)'
    props = dict(boxstyle='round', facecolor=BG_COLOR, edgecolor=PURPLE, alpha=0.9)
    ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=9,
            verticalalignment='bottom', horizontalalignment='right', bbox=props, color=TEXT_COLOR)

    # Add progression arrow
    ax.annotate('', xy=(1400, 7), xytext=(200, 0),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2, ls='--'))
    ax.text(800, 3.5, 'Career\nProgression', fontsize=11, color=GREEN,
            ha='center', va='center', rotation=25)

    plt.tight_layout()
    plt.savefig(f'{chart_dir}/16.2.5-promotion-score-ranges.png', dpi=150, facecolor=BG_COLOR)
    plt.close()
    print(f"Created: {chart_dir}/16.2.5-promotion-score-ranges.png")


if __name__ == '__main__':
    print("Generating Wave 4: Logistics & Commander Charts...")

    chart_14_1_fuel_consumption_vs_speed()
    chart_14_2_maintenance_failure_curve()
    chart_14_2_maintenance_capacity()
    chart_16_1_officer_type_distribution()
    chart_16_1_retirement_time_by_rank()
    chart_16_2_skill_bonus_generation()
    chart_16_2_crew_training_grade()
    chart_16_2_promotion_score_ranges()

    print("\nAll Wave 4 charts generated successfully!")
