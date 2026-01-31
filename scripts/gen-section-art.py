#!/usr/bin/env python3
"""Generate thematic section art for Aurora 4X Manual x.y sections."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Polygon, Circle, Ellipse, Rectangle, FancyBboxPatch,
    Wedge, Arc, RegularPolygon, PathPatch
)
from matplotlib.path import Path
from pathlib import Path as FilePath
import re
import sys
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

# Standard dimensions (smaller than chapter art)
WIDTH = 1000
HEIGHT = 150


def setup_axes(width=WIDTH, height=HEIGHT):
    """Create figure with standard dark theme setup."""
    fig, ax = plt.subplots(figsize=(width/100, height/100), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')
    ax.set_aspect('equal')
    return fig, ax


def add_stars(ax, width, height, num_stars=80, seed=None):
    """Add subtle background stars."""
    if seed:
        np.random.seed(seed)
    x = np.random.uniform(0, width, num_stars)
    y = np.random.uniform(0, height, num_stars)
    sizes = np.random.uniform(0.2, 1.2, num_stars)
    alphas = np.random.uniform(0.1, 0.3, num_stars)
    for xi, yi, s, a in zip(x, y, sizes, alphas):
        ax.scatter(xi, yi, s=s, c=WHITE, alpha=a, edgecolors='none', zorder=1)


def save_figure(fig, filepath):
    """Save figure with standard settings."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fig.savefig(
        filepath,
        facecolor=BG_COLOR,
        edgecolor='none',
        bbox_inches='tight',
        pad_inches=0,
        dpi=150
    )
    plt.close()


# ============================================================================
# SECTION ART GENERATORS - Organized by theme
# ============================================================================

def gen_stars_nebula(seed, accent=CYAN):
    """Stars with subtle nebula - for astronomy sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, WIDTH, HEIGHT, 120, seed)

    # Nebula clouds
    for _ in range(5):
        x, y = np.random.uniform(100, WIDTH-100), np.random.uniform(20, HEIGHT-20)
        size = np.random.uniform(40, 100)
        e = Ellipse((x, y), size*1.5, size*0.8, angle=np.random.uniform(0, 360),
                   facecolor=accent, alpha=0.08)
        ax.add_patch(e)

    # Bright stars
    for _ in range(8):
        x, y = np.random.uniform(50, WIDTH-50), np.random.uniform(20, HEIGHT-20)
        ax.scatter(x, y, s=np.random.uniform(10, 30), c=np.random.choice([WHITE, CYAN, YELLOW]),
                  alpha=0.7, edgecolors='none')
    return fig, ax


def gen_orbital_rings(seed, accent=CYAN, num_rings=4):
    """Orbital rings - for planetary/system sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, WIDTH, HEIGHT, 60, seed)

    cx, cy = WIDTH/2, HEIGHT/2
    ax.scatter(cx, cy, s=40, c=YELLOW, alpha=0.8)

    for i in range(num_rings):
        r = 30 + i * 25
        e = Ellipse((cx, cy), r*2, r*0.5, facecolor='none',
                   edgecolor=accent, linewidth=0.8, alpha=0.4 - i*0.08)
        ax.add_patch(e)
        # Planet
        theta = np.random.uniform(0, 2*np.pi)
        px = cx + r * np.cos(theta)
        py = cy + r * np.sin(theta) * 0.25
        ax.scatter(px, py, s=8+i*3, c=[CYAN, GREEN, RED, YELLOW][i % 4], alpha=0.7)
    return fig, ax


def gen_data_flow(seed, accent=CYAN):
    """Data streams - for UI/interface sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)

    for _ in range(12):
        x_start = np.random.uniform(0, WIDTH*0.7)
        y = np.random.uniform(20, HEIGHT-20)
        length = np.random.uniform(150, 400)
        x = np.linspace(x_start, x_start + length, 30)
        y_wave = y + 3 * np.sin(x * 0.03 + np.random.uniform(0, np.pi))
        color = np.random.choice([CYAN, GREEN, WHITE])
        ax.plot(x, y_wave, color=color, linewidth=0.8, alpha=0.4)
        for j in range(0, 30, 8):
            ax.scatter(x[j], y_wave[j], s=4, c=color, alpha=0.5)
    return fig, ax


def gen_grid_pattern(seed, accent=CYAN):
    """Technical grid - for design/blueprint sections."""
    fig, ax = setup_axes()

    for x in range(0, WIDTH+1, 25):
        alpha = 0.25 if x % 100 == 0 else 0.08
        ax.axvline(x, color=accent, linewidth=0.5, alpha=alpha)
    for y in range(0, HEIGHT+1, 25):
        alpha = 0.25 if y % 100 == 0 else 0.08
        ax.axhline(y, color=accent, linewidth=0.5, alpha=alpha)

    # Highlight points
    np.random.seed(seed)
    for _ in range(6):
        x = np.random.randint(2, WIDTH//25 - 2) * 25
        y = np.random.randint(1, HEIGHT//25 - 1) * 25
        ax.scatter(x, y, s=20, c=accent, alpha=0.6)
    return fig, ax


def gen_network_nodes(seed, accent=CYAN, num_nodes=8):
    """Connected nodes - for fleet/network sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, WIDTH, HEIGHT, 40, seed)

    nodes = [(np.random.uniform(80, WIDTH-80), np.random.uniform(30, HEIGHT-30)) for _ in range(num_nodes)]

    # Connections
    for i, (x1, y1) in enumerate(nodes):
        for j, (x2, y2) in enumerate(nodes[i+1:], i+1):
            if np.random.random() > 0.5:
                ax.plot([x1, x2], [y1, y2], color=accent, linewidth=0.6, alpha=0.25)

    # Nodes
    for x, y in nodes:
        ax.scatter(x, y, s=30, c=accent, alpha=0.15)
        ax.scatter(x, y, s=15, c=accent, alpha=0.6)
    return fig, ax


def gen_wave_pattern(seed, accent=CYAN):
    """Wave/signal pattern - for sensor/detection sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, WIDTH, HEIGHT, 30, seed)

    # Emanating waves from left
    cx, cy = 50, HEIGHT/2
    for r in range(3, 12):
        arc = Arc((cx, cy), r*40, r*25, theta1=-60, theta2=60,
                 color=accent, linewidth=1.2, alpha=0.5 - r*0.04)
        ax.add_patch(arc)

    ax.scatter(cx, cy, s=25, c=accent, alpha=0.8)

    # Detection blips
    for _ in range(5):
        x = np.random.uniform(200, WIDTH-50)
        y = np.random.uniform(30, HEIGHT-30)
        ax.scatter(x, y, s=12, c=np.random.choice([GREEN, YELLOW, RED]), alpha=0.6)
    return fig, ax


def gen_explosion_pattern(seed, accent=RED):
    """Explosion/combat pattern - for combat sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, WIDTH, HEIGHT, 40, seed)

    # Multiple small explosions
    for _ in range(4):
        ex = np.random.uniform(150, WIDTH-150)
        ey = np.random.uniform(40, HEIGHT-40)
        for r in [25, 15, 8]:
            ax.scatter(ex, ey, s=r*8, c=RED, alpha=0.15)
        ax.scatter(ex, ey, s=30, c=YELLOW, alpha=0.4)
        ax.scatter(ex, ey, s=10, c=WHITE, alpha=0.7)

    # Weapon traces
    for _ in range(6):
        x1 = np.random.uniform(0, 200)
        y1 = np.random.uniform(20, HEIGHT-20)
        x2 = np.random.uniform(400, WIDTH)
        y2 = np.random.uniform(20, HEIGHT-20)
        ax.plot([x1, x2], [y1, y2], color=CYAN, linewidth=1, alpha=0.3)
    return fig, ax


def gen_terrain_pattern(seed, accent=GREEN):
    """Terrain/ground - for ground forces sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)

    # Layered terrain
    x = np.linspace(0, WIDTH, 100)
    for i, (base_y, color, alpha) in enumerate([(20, DARK_GRAY, 0.9), (35, '#252542', 0.8), (50, '#2d2d44', 0.7)]):
        y = base_y + 15*np.sin(x*0.02 + i) + 8*np.sin(x*0.05 + i*2)
        ax.fill_between(x, 0, y, color=color, alpha=alpha)

    # Unit markers
    for _ in range(6):
        ux = np.random.uniform(100, WIDTH-100)
        uy = np.random.uniform(60, HEIGHT-30)
        ax.scatter(ux, uy, s=20, marker='s', c=np.random.choice([CYAN, RED]), alpha=0.7)
    return fig, ax


def gen_flow_arrows(seed, accent=GREEN):
    """Flow/logistics pattern - for logistics sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, WIDTH, HEIGHT, 30, seed)

    # Flow paths
    paths = [(100, HEIGHT/2), (350, HEIGHT/2-30), (350, HEIGHT/2+30),
             (600, HEIGHT/2), (850, HEIGHT/2-20), (850, HEIGHT/2+20)]

    for i in range(len(paths)-1):
        x1, y1 = paths[i]
        x2, y2 = paths[i+1]
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', color=accent, lw=1.5, alpha=0.5))

    for x, y in paths:
        ax.scatter(x, y, s=40, c=accent, alpha=0.3)
        ax.scatter(x, y, s=20, c=accent, alpha=0.7)
    return fig, ax


def gen_relationship_web(seed, accent=CYAN):
    """Relationship web - for diplomacy sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, WIDTH, HEIGHT, 30, seed)

    center = (WIDTH/2, HEIGHT/2)
    outer = [(200, HEIGHT/2-30), (200, HEIGHT/2+30), (800, HEIGHT/2-30), (800, HEIGHT/2+30)]

    for ox, oy in outer:
        color = np.random.choice([GREEN, YELLOW, RED, GRAY])
        ax.plot([center[0], ox], [center[1], oy], color=color, linewidth=1.5, alpha=0.4)
        ax.scatter(ox, oy, s=25, c=color, alpha=0.7)

    ax.scatter(*center, s=50, c=CYAN, alpha=0.3)
    ax.scatter(*center, s=25, c=CYAN, alpha=0.8)
    return fig, ax


def gen_rank_bars(seed, accent=CYAN):
    """Rank/progression bars - for commander sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)

    # Progression bars
    bar_y = HEIGHT/2
    for i in range(8):
        x = 80 + i * 110
        width = 80
        ax.add_patch(Rectangle((x, bar_y-15), width, 30, facecolor=DARK_GRAY,
                               edgecolor=accent, linewidth=1, alpha=0.6))
        fill = np.random.uniform(0.3, 1.0)
        ax.add_patch(Rectangle((x+2, bar_y-13), (width-4)*fill, 26,
                               facecolor=accent, alpha=0.5))
        # Stars
        num_stars = i // 2 + 1
        for j in range(min(num_stars, 4)):
            ax.scatter(x + 15 + j*15, bar_y+25, s=15, c=YELLOW, marker='*', alpha=0.8)
    return fig, ax


def gen_survey_spiral(seed, accent=CYAN):
    """Survey spiral - for exploration sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, WIDTH, HEIGHT, 100, seed)

    cx, cy = WIDTH/2, HEIGHT/2
    theta = np.linspace(0, 4*np.pi, 80)
    r = 15 + theta * 8
    x = cx + r * np.cos(theta) * 0.8
    y = cy + r * np.sin(theta) * 0.4

    ax.plot(x, y, color=accent, linewidth=1.2, alpha=0.5, linestyle='--')

    # Survey points
    for i in range(0, 80, 15):
        ax.scatter(x[i], y[i], s=15, c=GREEN if np.random.random() > 0.3 else GRAY, alpha=0.7)

    # Ship
    ax.scatter(x[60], y[60], s=25, c=CYAN, marker='>', alpha=0.9)
    return fig, ax


def gen_formula_blocks(seed, accent=CYAN):
    """Formula/calculation blocks - for advanced sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)

    # Formula boxes
    positions = [(150, HEIGHT/2), (400, HEIGHT/2), (650, HEIGHT/2), (900, HEIGHT/2)]
    for i, (x, y) in enumerate(positions):
        ax.add_patch(FancyBboxPatch((x-60, y-25), 120, 50,
                                    boxstyle="round,pad=0.02,rounding_size=5",
                                    facecolor=DARK_GRAY, edgecolor=accent,
                                    linewidth=1, alpha=0.7))
        # Connection
        if i < len(positions) - 1:
            ax.plot([x+60, positions[i+1][0]-60], [y, positions[i+1][1]],
                   color=accent, linewidth=1, alpha=0.3)
    return fig, ax


def gen_dome_structure(seed, accent=CYAN):
    """Colony domes - for colony sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, WIDTH, HEIGHT, 60, seed)

    # Ground
    ax.fill_between([0, WIDTH], [0, 0], [25, 25], color=DARK_GRAY, alpha=0.8)

    # Domes
    for dx in [200, 400, 600, 800]:
        size = np.random.uniform(35, 55)
        dome = Wedge((dx, 25), size, 0, 180, facecolor=accent, alpha=0.15)
        ax.add_patch(dome)
        arc = Arc((dx, 25), size*2, size*2, theta1=0, theta2=180,
                 color=accent, linewidth=1.5, alpha=0.6)
        ax.add_patch(arc)
        # Lights
        for _ in range(3):
            lx = dx + np.random.uniform(-size*0.5, size*0.5)
            ly = 25 + np.random.uniform(10, size*0.6)
            ax.scatter(lx, ly, s=3, c=YELLOW, alpha=0.7)
    return fig, ax


def gen_crystal_minerals(seed, accent=CYAN):
    """Mineral crystals - for mining/economy sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, WIDTH, HEIGHT, 30, seed)

    colors = [RED, CYAN, YELLOW, GREEN, GRAY]
    for _ in range(7):
        x = np.random.uniform(100, WIDTH-100)
        y = np.random.uniform(30, HEIGHT-30)
        size = np.random.uniform(12, 25)
        color = np.random.choice(colors)
        hex_patch = RegularPolygon((x, y), 6, radius=size, facecolor=color,
                                   edgecolor=WHITE, alpha=0.5, linewidth=0.8)
        ax.add_patch(hex_patch)
        ax.scatter(x, y, s=size*5, c=color, alpha=0.1)
    return fig, ax


def gen_tech_tree_branch(seed, accent=CYAN):
    """Tech tree branch - for research sections."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, WIDTH, HEIGHT, 30, seed)

    # Branching structure
    nodes = [(100, HEIGHT/2), (280, HEIGHT/2-35), (280, HEIGHT/2+35),
             (460, HEIGHT/2-50), (460, HEIGHT/2), (460, HEIGHT/2+50),
             (640, HEIGHT/2-35), (640, HEIGHT/2+35), (820, HEIGHT/2)]

    connections = [(0,1), (0,2), (1,3), (1,4), (2,4), (2,5), (3,6), (4,6), (4,7), (5,7), (6,8), (7,8)]

    for i, j in connections:
        ax.plot([nodes[i][0], nodes[j][0]], [nodes[i][1], nodes[j][1]],
               color=accent, linewidth=1, alpha=0.3)

    for x, y in nodes:
        ax.scatter(x, y, s=80, c=accent, alpha=0.15)
        ax.scatter(x, y, s=30, c=accent, alpha=0.7)
    return fig, ax


# ============================================================================
# SECTION MAPPING
# ============================================================================

SECTION_GENERATORS = {
    # Chapter 1: Introduction
    '1.1': ('stars_nebula', CYAN, "What is Aurora"),
    '1.2': ('grid_pattern', CYAN, "Installation"),
    '1.3': ('data_flow', CYAN, "First Launch"),

    # Chapter 2: Game Setup
    '2.1': ('grid_pattern', CYAN, "New Game Options"),
    '2.2': ('relationship_web', CYAN, "Race Creation"),
    '2.3': ('stars_nebula', YELLOW, "System Generation"),
    '2.4': ('rank_bars', GREEN, "Racial Traits"),
    '2.5': ('dome_structure', CYAN, "Starting Conditions"),

    # Chapter 3: User Interface
    '3.1': ('data_flow', CYAN, "Main Window"),
    '3.2': ('orbital_rings', CYAN, "System Map"),
    '3.3': ('grid_pattern', GREEN, "Common Controls"),
    '3.4': ('data_flow', YELLOW, "Event Log"),
    '3.5': ('network_nodes', CYAN, "Galactic Map"),

    # Chapter 4: Systems and Bodies
    '4.1': ('stars_nebula', YELLOW, "Star Systems"),
    '4.2': ('orbital_rings', CYAN, "Planets and Moons"),
    '4.3': ('stars_nebula', GRAY, "Asteroids and Comets"),
    '4.4': ('network_nodes', CYAN, "Jump Points"),

    # Chapter 5: Colonies
    '5.1': ('dome_structure', CYAN, "Establishing Colonies"),
    '5.2': ('dome_structure', GREEN, "Population"),
    '5.3': ('orbital_rings', GREEN, "Environment"),
    '5.4': ('grid_pattern', CYAN, "Infrastructure"),
    '5.5': ('orbital_rings', GREEN, "Terraforming"),

    # Chapter 6: Economy
    '6.1': ('crystal_minerals', CYAN, "Minerals"),
    '6.2': ('crystal_minerals', YELLOW, "Mining"),
    '6.3': ('grid_pattern', CYAN, "Construction"),
    '6.4': ('flow_arrows', YELLOW, "Wealth and Trade"),
    '6.5': ('network_nodes', GREEN, "Civilian Economy"),

    # Chapter 7: Research
    '7.1': ('tech_tree_branch', CYAN, "Technology Tree"),
    '7.2': ('rank_bars', GREEN, "Scientists"),
    '7.3': ('grid_pattern', CYAN, "Research Facilities"),
    '7.4': ('tech_tree_branch', YELLOW, "Tech Categories"),

    # Chapter 8: Ship Design
    '8.1': ('grid_pattern', CYAN, "Design Philosophy"),
    '8.2': ('grid_pattern', GRAY, "Hull and Armor"),
    '8.3': ('flow_arrows', YELLOW, "Engines"),
    '8.4': ('wave_pattern', CYAN, "Sensors"),
    '8.5': ('explosion_pattern', RED, "Weapons"),
    '8.6': ('grid_pattern', GREEN, "Other Components"),
    '8.7': ('grid_pattern', CYAN, "Design Examples"),

    # Chapter 9: Fleet Management
    '9.1': ('grid_pattern', CYAN, "Shipyards"),
    '9.2': ('grid_pattern', GREEN, "Construction and Refit"),
    '9.3': ('network_nodes', CYAN, "Task Groups"),
    '9.4': ('network_nodes', YELLOW, "Fleet Organization"),
    '9.5': ('data_flow', CYAN, "Orders"),
    '9.6': ('network_nodes', CYAN, "Light Naval Operations"),

    # Chapter 10: Navigation
    '10.1': ('orbital_rings', CYAN, "Movement Mechanics"),
    '10.2': ('network_nodes', CYAN, "Jump Transit"),
    '10.3': ('survey_spiral', GREEN, "Survey Operations"),
    '10.4': ('network_nodes', YELLOW, "Waypoints"),

    # Chapter 11: Sensors
    '11.0': ('wave_pattern', CYAN, "Sensor Overview"),
    '11.1': ('wave_pattern', RED, "Thermal/EM Signatures"),
    '11.2': ('wave_pattern', GREEN, "Passive Sensors"),
    '11.3': ('wave_pattern', YELLOW, "Active Sensors"),
    '11.4': ('wave_pattern', GRAY, "Stealth"),

    # Chapter 12: Combat
    '12.0': ('explosion_pattern', RED, "Combat Overview"),
    '12.1': ('grid_pattern', CYAN, "Fire Controls"),
    '12.2': ('explosion_pattern', CYAN, "Beam Weapons"),
    '12.3': ('explosion_pattern', YELLOW, "Missiles"),
    '12.4': ('explosion_pattern', GREEN, "Point Defense"),
    '12.5': ('wave_pattern', CYAN, "Electronic Warfare"),
    '12.6': ('grid_pattern', GRAY, "Damage and Armor"),
    '12.7': ('dome_structure', RED, "Planetary Defence"),

    # Chapter 13: Ground Forces
    '13.1': ('terrain_pattern', CYAN, "Unit Types"),
    '13.2': ('terrain_pattern', GREEN, "Training and Transport"),
    '13.3': ('terrain_pattern', RED, "Ground Combat"),

    # Chapter 14: Logistics
    '14.1': ('flow_arrows', YELLOW, "Fuel"),
    '14.2': ('flow_arrows', CYAN, "Maintenance"),
    '14.3': ('flow_arrows', GREEN, "Supply Ships"),
    '14.4': ('dome_structure', CYAN, "Orbital Habitats"),

    # Chapter 15: Diplomacy
    '15.1': ('relationship_web', RED, "Alien Races"),
    '15.2': ('relationship_web', CYAN, "Communications"),
    '15.3': ('relationship_web', GREEN, "Treaties"),
    '15.4': ('relationship_web', YELLOW, "Diplomacy"),
    '15.5': ('relationship_web', GRAY, "Intelligence"),

    # Chapter 16: Commanders
    '16.1': ('rank_bars', CYAN, "Officer Generation"),
    '16.2': ('rank_bars', YELLOW, "Skills and Bonuses"),
    '16.3': ('rank_bars', GREEN, "Assignments"),

    # Chapter 17: Exploration
    '17.1': ('survey_spiral', GREEN, "Geological Survey"),
    '17.2': ('survey_spiral', CYAN, "Gravitational Survey"),
    '17.3': ('survey_spiral', YELLOW, "Xenoarchaeology"),

    # Chapter 18: Advanced
    '18.1': ('formula_blocks', CYAN, "Game Mechanics"),
    '18.2': ('data_flow', CYAN, "Time Increments"),
    '18.3': ('relationship_web', RED, "Spoiler Races"),
    '18.4': ('network_nodes', YELLOW, "Late Game Strategy"),
    '18.5': ('grid_pattern', CYAN, "Spacemaster Mode"),
}

GENERATORS = {
    'stars_nebula': gen_stars_nebula,
    'orbital_rings': gen_orbital_rings,
    'data_flow': gen_data_flow,
    'grid_pattern': gen_grid_pattern,
    'network_nodes': gen_network_nodes,
    'wave_pattern': gen_wave_pattern,
    'explosion_pattern': gen_explosion_pattern,
    'terrain_pattern': gen_terrain_pattern,
    'flow_arrows': gen_flow_arrows,
    'relationship_web': gen_relationship_web,
    'rank_bars': gen_rank_bars,
    'survey_spiral': gen_survey_spiral,
    'formula_blocks': gen_formula_blocks,
    'dome_structure': gen_dome_structure,
    'crystal_minerals': gen_crystal_minerals,
    'tech_tree_branch': gen_tech_tree_branch,
}


def generate_section_art(section_id, output_dir='images/art/section-art'):
    """Generate art for a specific section."""
    if section_id not in SECTION_GENERATORS:
        print(f"  Warning: No generator defined for section {section_id}")
        return None

    gen_name, accent, title = SECTION_GENERATORS[section_id]
    gen_func = GENERATORS[gen_name]

    # Use section ID as seed for reproducibility
    seed = hash(section_id) % (2**31)

    fig, ax = gen_func(seed, accent)

    output_path = f'{output_dir}/{section_id}.png'
    save_figure(fig, output_path)
    print(f"Generated: {output_path}")
    return output_path


def main():
    """Generate section art based on command line args or all sections."""
    os.makedirs('images/art/section-art', exist_ok=True)

    if len(sys.argv) > 1:
        # Generate specific sections
        sections = sys.argv[1:]
    else:
        # Generate all sections
        sections = list(SECTION_GENERATORS.keys())

    for section_id in sections:
        try:
            generate_section_art(section_id)
        except Exception as e:
            print(f"  Error generating {section_id}: {e}")


if __name__ == '__main__':
    main()
