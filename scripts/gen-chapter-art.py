#!/usr/bin/env python3
"""Generate thematic chapter header art for Aurora 4X Manual."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Polygon, Circle, Ellipse, Rectangle, FancyBboxPatch,
    Wedge, Arc, PathPatch, RegularPolygon
)
from matplotlib.path import Path
from matplotlib.collections import PatchCollection, LineCollection
import matplotlib.colors as mcolors

# Dark theme colors
BG_COLOR = '#1a1a2e'
CYAN = '#4ecdc4'
YELLOW = '#ffe66d'
RED = '#ff6b6b'
GREEN = '#95d5b2'
WHITE = '#ffffff'
GRAY = '#888888'
DARK_GRAY = '#2d2d44'

# Standard dimensions
WIDTH = 1200
HEIGHT = 250


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


def add_stars(ax, width, height, num_stars=200, num_bright=15):
    """Add background stars."""
    np.random.seed(hash(f"{width}{height}") % 2**32)

    # Dim stars
    x = np.random.uniform(0, width, num_stars)
    y = np.random.uniform(0, height, num_stars)
    sizes = np.random.uniform(0.2, 1.5, num_stars)
    alphas = np.random.uniform(0.1, 0.4, num_stars)

    for xi, yi, s, a in zip(x, y, sizes, alphas):
        ax.scatter(xi, yi, s=s, c=WHITE, alpha=a, edgecolors='none', zorder=1)

    # Bright stars
    x = np.random.uniform(0, width, num_bright)
    y = np.random.uniform(0, height, num_bright)
    sizes = np.random.uniform(3, 8, num_bright)

    for xi, yi, s in zip(x, y, sizes):
        color = np.random.choice([WHITE, CYAN, YELLOW])
        ax.scatter(xi, yi, s=s*2, c=color, alpha=0.15, edgecolors='none', zorder=1)
        ax.scatter(xi, yi, s=s, c=color, alpha=0.7, edgecolors='none', zorder=1)


def save_figure(fig, filename):
    """Save figure with standard settings."""
    fig.savefig(
        f'images/art/chapter-art/{filename}',
        facecolor=BG_COLOR,
        edgecolor='none',
        bbox_inches='tight',
        pad_inches=0,
        dpi=150
    )
    plt.close()
    print(f"Generated: images/art/chapter-art/{filename}")


# ============================================================================
# CHAPTER 1: INTRODUCTION - Galaxy panorama
# ============================================================================
def gen_ch1_introduction():
    """Galaxy spiral with discovery theme."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=300, num_bright=20)

    cx, cy = WIDTH/2, HEIGHT/2

    # Spiral galaxy arms
    for arm in range(4):
        theta_offset = arm * np.pi/2
        theta = np.linspace(0.2, 3, 100)
        r = 20 + theta * 35

        x = cx + r * np.cos(theta + theta_offset + 0.3*np.sin(theta*3))
        y = cy + r * np.sin(theta + theta_offset + 0.3*np.sin(theta*3)) * 0.4

        sizes = np.linspace(4, 0.5, 100)
        alphas = np.linspace(0.6, 0.1, 100)
        colors = [CYAN if i % 3 == 0 else WHITE for i in range(100)]

        for i in range(len(x)-1):
            ax.scatter(x[i], y[i], s=sizes[i], c=colors[i], alpha=alphas[i], edgecolors='none')

    # Central bulge
    for i in range(50):
        r = np.random.uniform(0, 25)
        theta = np.random.uniform(0, 2*np.pi)
        ax.scatter(cx + r*np.cos(theta), cy + r*np.sin(theta)*0.4,
                  s=np.random.uniform(1, 4), c=YELLOW,
                  alpha=np.random.uniform(0.3, 0.7), edgecolors='none')

    # Core glow
    ax.scatter(cx, cy, s=300, c=YELLOW, alpha=0.1, edgecolors='none')
    ax.scatter(cx, cy, s=150, c=YELLOW, alpha=0.2, edgecolors='none')
    ax.scatter(cx, cy, s=50, c=WHITE, alpha=0.5, edgecolors='none')

    save_figure(fig, '01-introduction.png')


# ============================================================================
# CHAPTER 2: GAME SETUP - Configuration grid
# ============================================================================
def gen_ch2_game_setup():
    """Configuration dials and parameter grid."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=100, num_bright=5)

    # Draw configuration panels
    panel_positions = [(150, HEIGHT/2), (400, HEIGHT/2), (650, HEIGHT/2),
                       (900, HEIGHT/2), (1100, HEIGHT/2)]

    for i, (px, py) in enumerate(panel_positions):
        # Panel background
        panel = FancyBboxPatch(
            (px-60, py-80), 120, 160,
            boxstyle="round,pad=0.02,rounding_size=5",
            facecolor=DARK_GRAY, edgecolor=CYAN, linewidth=1, alpha=0.6
        )
        ax.add_patch(panel)

        # Dial/gauge
        angle = 45 + i * 30  # Different positions
        wedge = Wedge((px, py+20), 35, -135, angle, facecolor=CYAN, alpha=0.4)
        ax.add_patch(wedge)
        arc = Arc((px, py+20), 70, 70, angle=0, theta1=-135, theta2=135,
                 color=WHITE, linewidth=2, alpha=0.8)
        ax.add_patch(arc)

        # Dial indicator
        rad = np.radians(angle)
        ax.plot([px, px + 30*np.cos(rad)], [py+20, py+20 + 30*np.sin(rad)],
               color=WHITE, linewidth=2, alpha=0.9)

        # Parameter bars below
        for j in range(3):
            bar_width = np.random.uniform(40, 100)
            bar = Rectangle((px-50, py-70+j*18), bar_width, 12,
                           facecolor=[GREEN, CYAN, YELLOW][j], alpha=0.5)
            ax.add_patch(bar)

    # Connecting lines
    for i in range(len(panel_positions)-1):
        x1, y1 = panel_positions[i]
        x2, y2 = panel_positions[i+1]
        ax.plot([x1+65, x2-65], [y1, y2], color=CYAN, linewidth=1, alpha=0.3, linestyle='--')

    save_figure(fig, '02-game-setup.png')


# ============================================================================
# CHAPTER 3: USER INTERFACE - Data streams and windows
# ============================================================================
def gen_ch3_user_interface():
    """Abstract UI elements and data flow."""
    fig, ax = setup_axes()

    # Data stream lines
    np.random.seed(303)
    for _ in range(15):
        x_start = np.random.uniform(0, WIDTH)
        y = np.random.uniform(20, HEIGHT-20)
        length = np.random.uniform(100, 400)

        x = np.linspace(x_start, x_start + length, 50)
        y_wave = y + 5 * np.sin(x * 0.05)

        color = np.random.choice([CYAN, GREEN, WHITE])
        ax.plot(x, y_wave, color=color, linewidth=1, alpha=0.4)

        # Data points along stream
        for j in range(0, 50, 10):
            if j < len(x):
                ax.scatter(x[j], y_wave[j], s=8, c=color, alpha=0.6)

    # Window frames
    windows = [(100, 50, 200, 150), (450, 30, 250, 180), (850, 60, 220, 140)]
    for x, y, w, h in windows:
        # Window border
        rect = Rectangle((x, y), w, h, facecolor='none',
                         edgecolor=CYAN, linewidth=2, alpha=0.6)
        ax.add_patch(rect)
        # Title bar
        title = Rectangle((x, y+h-20), w, 20, facecolor=CYAN, alpha=0.3)
        ax.add_patch(title)
        # Content lines
        for i in range(4):
            line_y = y + 20 + i * 25
            line_w = np.random.uniform(0.4, 0.9) * w
            ax.plot([x+10, x+10+line_w], [line_y, line_y],
                   color=WHITE, linewidth=1, alpha=0.3)

    save_figure(fig, '03-user-interface.png')


# ============================================================================
# CHAPTER 4: SYSTEMS AND BODIES - Solar system
# ============================================================================
def gen_ch4_systems_bodies():
    """Solar system with orbits and planets."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=200, num_bright=10)

    cx, cy = WIDTH/2, HEIGHT/2

    # Star
    ax.scatter(cx, cy, s=400, c=YELLOW, alpha=0.15, edgecolors='none')
    ax.scatter(cx, cy, s=200, c=YELLOW, alpha=0.3, edgecolors='none')
    ax.scatter(cx, cy, s=80, c=WHITE, alpha=0.9, edgecolors='none')

    # Orbits and planets
    orbit_radii = [50, 80, 110, 150, 200, 280, 380, 500]
    planet_colors = [GRAY, YELLOW, CYAN, RED, YELLOW, CYAN, GREEN, CYAN]
    planet_sizes = [8, 12, 14, 10, 30, 25, 20, 18]

    for r, color, size in zip(orbit_radii, planet_colors, planet_sizes):
        # Orbit ellipse
        ellipse = Ellipse((cx, cy), r*2, r*0.6, facecolor='none',
                         edgecolor=WHITE, linewidth=0.5, alpha=0.3)
        ax.add_patch(ellipse)

        # Planet at random position
        theta = np.random.uniform(0, 2*np.pi)
        px = cx + r * np.cos(theta)
        py = cy + r * np.sin(theta) * 0.3

        ax.scatter(px, py, s=size*3, c=color, alpha=0.2, edgecolors='none')
        ax.scatter(px, py, s=size, c=color, alpha=0.8, edgecolors='none')

    # Asteroid belt hint
    for _ in range(40):
        r = np.random.uniform(175, 185)
        theta = np.random.uniform(0, 2*np.pi)
        ax.scatter(cx + r*np.cos(theta), cy + r*np.sin(theta)*0.3,
                  s=1, c=GRAY, alpha=0.5)

    save_figure(fig, '04-systems-bodies.png')


# ============================================================================
# CHAPTER 5: COLONIES - Dome structures
# ============================================================================
def gen_ch5_colonies():
    """Colony domes and habitation structures."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=150, num_bright=8)

    # Ground line
    ground_y = 40
    ax.fill_between([0, WIDTH], [0, 0], [ground_y, ground_y],
                   color=DARK_GRAY, alpha=0.8)

    # Dome structures
    dome_positions = [(200, 80), (400, 100), (600, 120), (800, 90), (1000, 85)]
    dome_sizes = [60, 80, 100, 70, 55]

    for (dx, dy), size in zip(dome_positions, dome_sizes):
        # Main dome
        dome = Wedge((dx, ground_y), size, 0, 180, facecolor=CYAN, alpha=0.2)
        ax.add_patch(dome)
        dome_outline = Arc((dx, ground_y), size*2, size*2, theta1=0, theta2=180,
                          color=CYAN, linewidth=2, alpha=0.7)
        ax.add_patch(dome_outline)

        # Internal structure lines
        for angle in [30, 60, 90, 120, 150]:
            rad = np.radians(angle)
            ax.plot([dx, dx + size*0.9*np.cos(rad)],
                   [ground_y, ground_y + size*0.9*np.sin(rad)],
                   color=CYAN, linewidth=0.5, alpha=0.3)

        # Lights
        for _ in range(5):
            lx = dx + np.random.uniform(-size*0.6, size*0.6)
            ly = ground_y + np.random.uniform(10, size*0.7)
            if (lx-dx)**2 + (ly-ground_y)**2 < (size*0.85)**2:
                ax.scatter(lx, ly, s=3, c=YELLOW, alpha=0.8)

    # Connecting tubes
    for i in range(len(dome_positions)-1):
        x1, _ = dome_positions[i]
        x2, _ = dome_positions[i+1]
        ax.plot([x1 + dome_sizes[i]*0.8, x2 - dome_sizes[i+1]*0.8],
               [ground_y + 15, ground_y + 15],
               color=CYAN, linewidth=3, alpha=0.4)

    save_figure(fig, '05-colonies.png')


# ============================================================================
# CHAPTER 6: ECONOMY AND INDUSTRY - Mining and factories
# ============================================================================
def gen_ch6_economy():
    """Mining operations and industrial networks."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=100, num_bright=5)

    # Resource nodes (minerals)
    np.random.seed(606)
    mineral_colors = {'D': '#ff6b6b', 'N': '#4ecdc4', 'C': '#ffe66d',
                     'V': '#95d5b2', 'B': '#888888'}

    nodes = []
    for _ in range(12):
        x = np.random.uniform(100, WIDTH-100)
        y = np.random.uniform(50, HEIGHT-50)
        mineral = np.random.choice(list(mineral_colors.keys()))
        nodes.append((x, y, mineral))

        # Crystal shape
        color = mineral_colors[mineral]
        size = np.random.uniform(15, 30)
        hex_patch = RegularPolygon((x, y), 6, radius=size, facecolor=color,
                                   edgecolor=WHITE, alpha=0.6, linewidth=1)
        ax.add_patch(hex_patch)

        # Glow
        ax.scatter(x, y, s=size*8, c=color, alpha=0.15, edgecolors='none')

    # Factory nodes
    factories = [(200, HEIGHT/2), (600, HEIGHT/2), (1000, HEIGHT/2)]
    for fx, fy in factories:
        # Factory building
        rect = Rectangle((fx-40, fy-30), 80, 60, facecolor=DARK_GRAY,
                         edgecolor=CYAN, linewidth=2, alpha=0.8)
        ax.add_patch(rect)
        # Smokestacks
        for offset in [-20, 0, 20]:
            ax.add_patch(Rectangle((fx+offset-5, fy+30), 10, 25,
                                   facecolor=DARK_GRAY, edgecolor=CYAN, linewidth=1))
        # Activity indicator
        ax.scatter(fx, fy, s=100, c=GREEN, alpha=0.3)

    # Supply lines between nodes and factories
    for node in nodes:
        nx, ny, _ = node
        # Find nearest factory
        nearest = min(factories, key=lambda f: (f[0]-nx)**2 + (f[1]-ny)**2)
        ax.plot([nx, nearest[0]], [ny, nearest[1]],
               color=WHITE, linewidth=0.5, alpha=0.2, linestyle=':')

    save_figure(fig, '06-economy.png')


# ============================================================================
# CHAPTER 7: RESEARCH - Tech tree branches
# ============================================================================
def gen_ch7_research():
    """Branching technology tree."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=80, num_bright=3)

    # Tree structure from left to right
    levels = [
        [(100, HEIGHT/2)],
        [(250, HEIGHT/2-60), (250, HEIGHT/2+60)],
        [(400, HEIGHT/2-90), (400, HEIGHT/2-30), (400, HEIGHT/2+30), (400, HEIGHT/2+90)],
        [(550, HEIGHT/2-100), (550, HEIGHT/2-50), (550, HEIGHT/2), (550, HEIGHT/2+50), (550, HEIGHT/2+100)],
        [(700, HEIGHT/2-80), (700, HEIGHT/2-20), (700, HEIGHT/2+40), (700, HEIGHT/2+100)],
        [(850, HEIGHT/2-50), (850, HEIGHT/2+30)],
        [(1000, HEIGHT/2-20), (1000, HEIGHT/2+20)],
        [(1100, HEIGHT/2)]
    ]

    colors = [CYAN, GREEN, YELLOW, WHITE, CYAN, GREEN, YELLOW, RED]

    # Draw connections first
    for i in range(len(levels)-1):
        for node1 in levels[i]:
            for node2 in levels[i+1]:
                # Curved connection
                x1, y1 = node1
                x2, y2 = node2
                mid_x = (x1 + x2) / 2

                t = np.linspace(0, 1, 20)
                x = x1 + (x2-x1)*t
                y = y1 + (y2-y1)*t + 10*np.sin(t*np.pi)

                ax.plot(x, y, color=colors[i], linewidth=1, alpha=0.3)

    # Draw nodes
    for level_idx, level in enumerate(levels):
        for x, y in level:
            # Node glow
            ax.scatter(x, y, s=200, c=colors[level_idx % len(colors)],
                      alpha=0.15, edgecolors='none')
            # Node
            circle = Circle((x, y), 12, facecolor=colors[level_idx % len(colors)],
                           edgecolor=WHITE, linewidth=1.5, alpha=0.8)
            ax.add_patch(circle)
            # Inner highlight
            ax.scatter(x-3, y+3, s=15, c=WHITE, alpha=0.5)

    # Discovery sparks
    for _ in range(20):
        x = np.random.uniform(50, WIDTH-50)
        y = np.random.uniform(20, HEIGHT-20)
        ax.scatter(x, y, s=np.random.uniform(1, 5), c=YELLOW,
                  alpha=np.random.uniform(0.2, 0.6), marker='*')

    save_figure(fig, '07-research.png')


# ============================================================================
# CHAPTER 8: SHIP DESIGN - Blueprint grid
# ============================================================================
def gen_ch8_ship_design():
    """Technical blueprint with ship outline."""
    fig, ax = setup_axes()

    # Blueprint grid
    for x in range(0, WIDTH+1, 30):
        alpha = 0.3 if x % 150 == 0 else 0.1
        ax.axvline(x, color=CYAN, linewidth=0.5, alpha=alpha)
    for y in range(0, HEIGHT+1, 30):
        alpha = 0.3 if y % 150 == 0 else 0.1
        ax.axhline(y, color=CYAN, linewidth=0.5, alpha=alpha)

    # Ship outline (cruiser-style)
    cx, cy = WIDTH/2, HEIGHT/2
    ship_points = np.array([
        [300, 0], [200, 30], [100, 45], [-50, 50], [-100, 40],
        [-120, 20], [-120, -20], [-100, -40], [-50, -50],
        [100, -45], [200, -30], [300, 0]
    ], dtype=float)
    ship_points[:, 0] += cx - 100
    ship_points[:, 1] += cy

    # Ship hull
    ship = Polygon(ship_points, facecolor='none', edgecolor=CYAN,
                  linewidth=2, alpha=0.8)
    ax.add_patch(ship)

    # Internal structure lines
    ax.plot([cx-100, cx+200], [cy, cy], color=CYAN, linewidth=1, alpha=0.4)
    ax.plot([cx, cx], [cy-40, cy+40], color=CYAN, linewidth=1, alpha=0.4)
    ax.plot([cx+100, cx+100], [cy-35, cy+35], color=CYAN, linewidth=1, alpha=0.4)

    # Component callouts
    callouts = [
        (cx+150, cy, "BRIDGE", 50),
        (cx-50, cy+35, "ENGINE", -40),
        (cx+50, cy-30, "WEAPONS", 40),
        (cx-80, cy, "FUEL", -50)
    ]

    for x, y, label, offset in callouts:
        # Callout line
        ax.plot([x, x + offset*0.5], [y, y + offset],
               color=WHITE, linewidth=0.5, alpha=0.6)
        # Callout circle
        ax.scatter(x, y, s=20, facecolor='none', edgecolor=WHITE, linewidth=1, alpha=0.6)

    # Dimension lines
    ax.annotate('', xy=(float(cx-120), float(cy-70)), xytext=(float(cx+200), float(cy-70)),
               arrowprops=dict(arrowstyle='<->', color=YELLOW, lw=1))

    save_figure(fig, '08-ship-design.png')


# ============================================================================
# CHAPTER 9: FLEET MANAGEMENT - Formation patterns
# ============================================================================
def gen_ch9_fleet_management():
    """Fleet formations and command structure."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=150, num_bright=8)

    # Main fleet formation (center)
    cx, cy = WIDTH/2, HEIGHT/2

    # Command ship
    ax.scatter(cx, cy, s=150, c=YELLOW, alpha=0.2, edgecolors='none')
    ax.scatter(cx, cy, s=60, c=YELLOW, alpha=0.8, edgecolors='none')

    # Escort formation
    escort_positions = [
        (cx-80, cy+40), (cx-80, cy-40),
        (cx+80, cy+40), (cx+80, cy-40),
        (cx-40, cy+60), (cx+40, cy+60),
        (cx-40, cy-60), (cx+40, cy-60)
    ]

    for ex, ey in escort_positions:
        ax.scatter(ex, ey, s=25, c=CYAN, alpha=0.7, edgecolors='none')
        # Formation line to command
        ax.plot([ex, cx], [ey, cy], color=CYAN, linewidth=0.5, alpha=0.2, linestyle=':')

    # Secondary formations
    for offset_x in [-350, 350]:
        scx = cx + offset_x
        ax.scatter(scx, cy, s=80, c=GREEN, alpha=0.2, edgecolors='none')
        ax.scatter(scx, cy, s=35, c=GREEN, alpha=0.8, edgecolors='none')

        for angle in [60, 120, 240, 300]:
            rad = np.radians(angle)
            sx = scx + 50*np.cos(rad)
            sy = cy + 50*np.sin(rad)
            ax.scatter(sx, sy, s=15, c=CYAN, alpha=0.6)

        # Link to main fleet
        ax.plot([scx + (-60 if offset_x < 0 else 60), cx + (60 if offset_x < 0 else -60)],
               [cy, cy], color=WHITE, linewidth=1, alpha=0.3, linestyle='--')

    # Movement arrows
    arrow_x = [cx-200, cx, cx+200]
    for ax_pos in arrow_x:
        ax.annotate('', xy=(ax_pos+80, cy), xytext=(ax_pos+30, cy),
                   arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5, alpha=0.4))

    save_figure(fig, '09-fleet-management.png')


# ============================================================================
# CHAPTER 10: NAVIGATION - Jump point network
# ============================================================================
def gen_ch10_navigation():
    """Jump point network and travel paths."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=200, num_bright=10)

    # System nodes
    np.random.seed(1010)
    systems = []
    for _ in range(8):
        x = np.random.uniform(100, WIDTH-100)
        y = np.random.uniform(50, HEIGHT-50)
        systems.append((x, y))

    # Add Sol at center
    systems.append((WIDTH/2, HEIGHT/2))

    # Jump connections
    connections = [
        (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7),
        (8, 0), (8, 2), (8, 4), (8, 6), (1, 3), (5, 7)
    ]

    for i, j in connections:
        x1, y1 = systems[i]
        x2, y2 = systems[j]

        # Jump lane
        ax.plot([x1, x2], [y1, y2], color=CYAN, linewidth=1.5, alpha=0.3)

        # Jump point markers at ends
        for t in [0.15, 0.85]:
            px = x1 + t*(x2-x1)
            py = y1 + t*(y2-y1)
            ax.scatter(px, py, s=15, c=CYAN, alpha=0.5, marker='o')

    # System stars
    for i, (sx, sy) in enumerate(systems):
        if i == 8:  # Sol
            color, size = YELLOW, 60
        else:
            color = np.random.choice([YELLOW, WHITE, '#ffaa77', '#aaaaff'])
            size = np.random.uniform(20, 40)

        ax.scatter(sx, sy, s=size*2, c=color, alpha=0.2, edgecolors='none')
        ax.scatter(sx, sy, s=size, c=color, alpha=0.8, edgecolors='none')

    # Active travel path
    path_systems = [systems[8], systems[2], systems[3], systems[4]]
    path_x = [s[0] for s in path_systems]
    path_y = [s[1] for s in path_systems]
    ax.plot(path_x, path_y, color=GREEN, linewidth=2, alpha=0.6, linestyle='-')

    # Ship on path
    ax.scatter(path_x[1] + 30, path_y[1] + 10, s=30, c=WHITE, marker='>')

    save_figure(fig, '10-navigation.png')


# ============================================================================
# CHAPTER 11: SENSORS AND DETECTION - Radar sweeps
# ============================================================================
def gen_ch11_sensors():
    """Sensor sweeps and detection rings."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=100, num_bright=5)

    cx, cy = WIDTH/2, HEIGHT/2

    # Sensor origin
    ax.scatter(cx, cy, s=50, c=CYAN, alpha=0.8)

    # Detection rings (expanding)
    for r in [40, 80, 120, 180, 250, 350]:
        alpha = 0.4 - r/1000
        ring = Circle((cx, cy), r, facecolor='none', edgecolor=CYAN,
                     linewidth=1, alpha=max(alpha, 0.1))
        ax.add_patch(ring)

    # Active sensor sweep wedge
    sweep_angle = 45  # degrees
    wedge = Wedge((cx, cy), 300, sweep_angle-30, sweep_angle+30,
                 facecolor=GREEN, alpha=0.15)
    ax.add_patch(wedge)

    # Sweep edge lines
    for angle in [sweep_angle-30, sweep_angle+30]:
        rad = np.radians(angle)
        ax.plot([cx, cx + 320*np.cos(rad)], [cy, cy + 320*np.sin(rad)],
               color=GREEN, linewidth=1, alpha=0.4)

    # Detected contacts
    contacts = [
        (cx+150, cy+80, 'friendly'),
        (cx-200, cy+30, 'unknown'),
        (cx+100, cy-60, 'hostile'),
        (cx-80, cy-90, 'friendly')
    ]

    for x, y, status in contacts:
        color = {'friendly': GREEN, 'unknown': YELLOW, 'hostile': RED}[status]
        marker = {'friendly': 'o', 'unknown': 's', 'hostile': '^'}[status]
        ax.scatter(x, y, s=40, c=color, marker=marker, alpha=0.8)
        # Detection line
        ax.plot([cx, x], [cy, y], color=color, linewidth=0.5, alpha=0.3, linestyle=':')

    # Range scale
    for r, label in [(100, '10M km'), (200, '20M km')]:
        ax.text(cx + r + 10, cy - 5, label, fontsize=7, color=WHITE, alpha=0.5)

    save_figure(fig, '11-sensors.png')


# ============================================================================
# CHAPTER 12: COMBAT - Weapon fire patterns
# ============================================================================
def gen_ch12_combat():
    """Weapon fire, explosions, and engagement."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=100, num_bright=5)

    # Friendly ships (left side)
    friendly_ships = [(200, HEIGHT/2), (150, HEIGHT/2+50), (150, HEIGHT/2-50)]
    for fx, fy in friendly_ships:
        ax.scatter(fx, fy, s=40, c=CYAN, alpha=0.8)

    # Enemy ships (right side)
    enemy_ships = [(1000, HEIGHT/2+20), (1050, HEIGHT/2-30), (950, HEIGHT/2+70)]
    for ex, ey in enemy_ships:
        ax.scatter(ex, ey, s=35, c=RED, alpha=0.8)

    # Beam weapon fire
    for i, (fx, fy) in enumerate(friendly_ships):
        target = enemy_ships[i % len(enemy_ships)]
        # Beam line with taper
        for width in [3, 2, 1]:
            ax.plot([fx+20, target[0]-20], [fy, target[1]],
                   color=CYAN, linewidth=width, alpha=0.3/width)

    # Missiles in flight
    np.random.seed(1212)
    for _ in range(8):
        mx = np.random.uniform(400, 800)
        my = np.random.uniform(50, HEIGHT-50)
        ax.scatter(mx, my, s=10, c=YELLOW, marker='>')
        # Missile trail
        trail_x = [mx - 20 - i*5 for i in range(5)]
        trail_y = [my + np.random.uniform(-2, 2) for _ in range(5)]
        ax.plot(trail_x, trail_y, color=YELLOW, linewidth=1, alpha=0.3)

    # Explosions
    explosions = [(850, HEIGHT/2-40), (920, HEIGHT/2+60)]
    for ex, ey in explosions:
        for r in [30, 20, 10]:
            ax.scatter(ex, ey, s=r*10, c=RED, alpha=0.2, edgecolors='none')
        ax.scatter(ex, ey, s=50, c=YELLOW, alpha=0.6, edgecolors='none')
        ax.scatter(ex, ey, s=20, c=WHITE, alpha=0.9, edgecolors='none')

    # Engagement range indicator
    ax.add_patch(Arc((200, HEIGHT/2), 500, 500, theta1=-60, theta2=60,
                    color=WHITE, linewidth=1, alpha=0.2, linestyle='--'))

    save_figure(fig, '12-combat.png')


# ============================================================================
# CHAPTER 13: GROUND FORCES - Terrain and formations
# ============================================================================
def gen_ch13_ground_forces():
    """Ground combat terrain and unit formations."""
    fig, ax = setup_axes()

    # Terrain (layered hills)
    terrain_layers = [
        (20, 0.3, DARK_GRAY),
        (40, 0.4, '#252542'),
        (60, 0.5, '#2d2d44')
    ]

    np.random.seed(1313)
    x_terrain = np.linspace(0, WIDTH, 100)

    for base_y, amp_mult, color in terrain_layers:
        y_terrain = base_y + 30*amp_mult*np.sin(x_terrain*0.02) + 20*amp_mult*np.sin(x_terrain*0.05)
        ax.fill_between(x_terrain, 0, y_terrain, color=color, alpha=0.8)

    # Unit formations
    # Friendly (left)
    friendly_units = [(150, 80), (200, 90), (180, 70), (250, 85), (220, 95)]
    for ux, uy in friendly_units:
        ax.scatter(ux, uy, s=30, c=CYAN, marker='s', alpha=0.8)

    # Defensive line
    ax.plot([100, 300], [75, 75], color=CYAN, linewidth=2, alpha=0.4)

    # Enemy (right)
    enemy_units = [(900, 90), (950, 85), (1000, 95), (1050, 80), (980, 70)]
    for ux, uy in enemy_units:
        ax.scatter(ux, uy, s=30, c=RED, marker='^', alpha=0.8)

    # Battle line
    ax.plot([850, 1100], [85, 85], color=RED, linewidth=2, alpha=0.4)

    # Fortification
    fort_x = 550
    ax.add_patch(Rectangle((fort_x-40, 50), 80, 50, facecolor=GRAY,
                           edgecolor=WHITE, linewidth=2, alpha=0.7))
    ax.scatter(fort_x, 75, s=40, c=GREEN, marker='P', alpha=0.8)

    # Artillery fire arcs
    for start_x in [200, 950]:
        direction = 1 if start_x < WIDTH/2 else -1
        t = np.linspace(0, 1, 30)
        arc_x = start_x + direction * 200 * t
        arc_y = 90 + 80*t - 80*t**2
        ax.plot(arc_x, arc_y, color=YELLOW, linewidth=1, alpha=0.4, linestyle='--')

    save_figure(fig, '13-ground-forces.png')


# ============================================================================
# CHAPTER 14: LOGISTICS - Supply networks
# ============================================================================
def gen_ch14_logistics():
    """Supply chains and fuel flow."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=80, num_bright=4)

    # Supply depot (center)
    depot_x, depot_y = WIDTH/2, HEIGHT/2
    ax.add_patch(Rectangle((depot_x-50, depot_y-30), 100, 60,
                           facecolor=DARK_GRAY, edgecolor=GREEN, linewidth=2, alpha=0.8))
    ax.text(depot_x, depot_y, 'DEPOT', ha='center', va='center',
           fontsize=8, color=WHITE, alpha=0.7)

    # Supply sources (left)
    sources = [(100, HEIGHT/2-50), (100, HEIGHT/2+50), (150, HEIGHT/2)]
    for sx, sy in sources:
        ax.add_patch(Circle((sx, sy), 20, facecolor=CYAN, edgecolor=WHITE,
                           linewidth=1, alpha=0.6))
        # Flow to depot
        ax.annotate('', xy=(depot_x-55, depot_y), xytext=(sx+25, sy),
                   arrowprops=dict(arrowstyle='->', color=CYAN, lw=1.5, alpha=0.5))

    # Destinations (right)
    destinations = [
        (1000, HEIGHT/2-60, 'FLEET A'),
        (1000, HEIGHT/2, 'FLEET B'),
        (1000, HEIGHT/2+60, 'COLONY')
    ]

    for dx, dy, label in destinations:
        ax.scatter(dx, dy, s=60, c=YELLOW, alpha=0.7)
        ax.text(dx+30, dy, label, fontsize=7, color=WHITE, alpha=0.6, va='center')
        # Flow from depot
        ax.annotate('', xy=(dx-15, dy), xytext=(depot_x+55, depot_y),
                   arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5, alpha=0.5))

    # Fuel level indicators
    for i, (_, dy, _) in enumerate(destinations):
        fuel_level = [0.8, 0.5, 0.3][i]
        bar_x = 1080
        ax.add_patch(Rectangle((bar_x, dy-10), 40, 20, facecolor='none',
                               edgecolor=WHITE, linewidth=1, alpha=0.5))
        ax.add_patch(Rectangle((bar_x, dy-10), 40*fuel_level, 20,
                               facecolor=[GREEN, YELLOW, RED][i], alpha=0.6))

    # Tanker ship in transit
    ax.scatter(750, HEIGHT/2+20, s=40, c=GREEN, marker='D', alpha=0.8)
    ax.plot([depot_x+60, 740], [depot_y+10, HEIGHT/2+20],
           color=GREEN, linewidth=1, alpha=0.3, linestyle=':')

    save_figure(fig, '14-logistics.png')


# ============================================================================
# CHAPTER 15: DIPLOMACY - Relationship web
# ============================================================================
def gen_ch15_diplomacy():
    """Diplomatic relationships and faction web."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=80, num_bright=3)

    # Faction nodes
    factions = [
        (WIDTH/2, HEIGHT/2, 'PLAYER', CYAN, 40),
        (200, HEIGHT/2-40, 'ALLY', GREEN, 30),
        (200, HEIGHT/2+60, 'NEUTRAL', GRAY, 25),
        (800, HEIGHT/2-50, 'RIVAL', YELLOW, 30),
        (900, HEIGHT/2+40, 'HOSTILE', RED, 35),
        (500, HEIGHT/2+80, 'TRADE', GREEN, 25),
        (700, HEIGHT/2-80, 'UNKNOWN', GRAY, 20)
    ]

    # Relationship lines
    relationships = [
        (0, 1, GREEN, 'ALLIED'),
        (0, 2, GRAY, 'NEUTRAL'),
        (0, 3, YELLOW, 'TENSE'),
        (0, 4, RED, 'WAR'),
        (0, 5, GREEN, 'TRADE'),
        (1, 5, GREEN, None),
        (3, 4, YELLOW, None),
        (2, 6, GRAY, None)
    ]

    for i, j, color, label in relationships:
        x1, y1 = factions[i][0], factions[i][1]
        x2, y2 = factions[j][0], factions[j][1]

        ax.plot([x1, x2], [y1, y2], color=color, linewidth=2, alpha=0.4)

        if label:
            mid_x, mid_y = (x1+x2)/2, (y1+y2)/2
            ax.text(mid_x, mid_y, label, fontsize=6, color=color,
                   alpha=0.7, ha='center', va='center',
                   bbox=dict(boxstyle='round', facecolor=BG_COLOR, alpha=0.8))

    # Draw faction nodes
    for fx, fy, name, color, size in factions:
        ax.scatter(fx, fy, s=size*4, c=color, alpha=0.2, edgecolors='none')
        ax.scatter(fx, fy, s=size*2, c=color, alpha=0.6, edgecolors='none')
        ax.text(fx, fy-size/2-15, name, fontsize=7, color=WHITE,
               alpha=0.8, ha='center')

    save_figure(fig, '15-diplomacy.png')


# ============================================================================
# CHAPTER 16: COMMANDERS - Rank insignia and hierarchy
# ============================================================================
def gen_ch16_commanders():
    """Officer ranks and command structure."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=60, num_bright=2)

    # Rank progression (left to right)
    ranks = [
        (100, 'LT', 1),
        (250, 'LCDR', 2),
        (400, 'CDR', 3),
        (550, 'CAPT', 4),
        (700, 'RADM', 5),
        (850, 'VADM', 6),
        (1000, 'ADM', 7),
        (1100, 'FADM', 8)
    ]

    cy = HEIGHT/2

    for rx, rank, level in ranks:
        # Rank badge
        badge_size = 25 + level * 3
        ax.add_patch(RegularPolygon((rx, cy), 6, radius=badge_size,
                                    facecolor=DARK_GRAY, edgecolor=CYAN,
                                    linewidth=2, alpha=0.7))

        # Stars based on rank
        num_stars = min(level, 5)
        for i in range(num_stars):
            star_x = rx + (i - num_stars/2 + 0.5) * 10
            ax.scatter(star_x, cy, s=20, c=YELLOW, marker='*', alpha=0.9)

        # Rank label
        ax.text(rx, cy - badge_size - 15, rank, fontsize=8, color=WHITE,
               ha='center', alpha=0.8)

        # Skill bars
        skills = np.random.uniform(0.3, 1.0, 3)
        colors = [CYAN, GREEN, YELLOW]
        for i, (skill, color) in enumerate(zip(skills, colors)):
            bar_y = cy + badge_size + 10 + i * 12
            ax.add_patch(Rectangle((rx-20, bar_y), 40*skill, 8,
                                   facecolor=color, alpha=0.5))

    # Progression arrows
    for i in range(len(ranks)-1):
        x1 = ranks[i][0] + 40
        x2 = ranks[i+1][0] - 40
        ax.annotate('', xy=(x2, cy), xytext=(x1, cy),
                   arrowprops=dict(arrowstyle='->', color=WHITE, lw=1, alpha=0.3))

    save_figure(fig, '16-commanders.png')


# ============================================================================
# CHAPTER 17: EXPLORATION - Survey patterns
# ============================================================================
def gen_ch17_exploration():
    """Survey grids and exploration patterns."""
    fig, ax = setup_axes()
    add_stars(ax, WIDTH, HEIGHT, num_stars=200, num_bright=12)

    # Surveyed system (center)
    cx, cy = WIDTH/2, HEIGHT/2

    # Survey grid overlay
    grid_size = 50
    for x in range(int(cx-200), int(cx+201), grid_size):
        for y in range(int(cy-100), int(cy+101), grid_size):
            # Survey status
            surveyed = np.random.random() > 0.3
            color = GREEN if surveyed else GRAY
            alpha = 0.3 if surveyed else 0.1

            ax.add_patch(Rectangle((x, y), grid_size-2, grid_size-2,
                                   facecolor=color, alpha=alpha, edgecolor='none'))

    # Central star
    ax.scatter(cx, cy, s=100, c=YELLOW, alpha=0.8)

    # Surveyed bodies
    bodies = [
        (cx-150, cy+30, 'SURVEYED', GREEN),
        (cx+100, cy-50, 'SURVEYED', GREEN),
        (cx-80, cy-60, 'PARTIAL', YELLOW),
        (cx+180, cy+40, 'UNSURVEYED', GRAY)
    ]

    for bx, by, status, color in bodies:
        ax.scatter(bx, by, s=30, c=color, alpha=0.7)
        ax.text(bx, by-20, status, fontsize=6, color=color, alpha=0.7, ha='center')

    # Survey ship path (spiral outward)
    theta = np.linspace(0, 4*np.pi, 100)
    r = 30 + theta * 8
    path_x = cx - 200 + r * np.cos(theta) * 0.5
    path_y = cy + r * np.sin(theta) * 0.3

    ax.plot(path_x, path_y, color=CYAN, linewidth=1.5, alpha=0.5, linestyle='--')

    # Survey ship
    ship_idx = 70
    ax.scatter(path_x[ship_idx], path_y[ship_idx], s=40, c=CYAN, marker='>', alpha=0.9)

    # Unknown region (right side)
    ax.text(WIDTH-100, cy, '?', fontsize=48, color=GRAY, alpha=0.3, ha='center', va='center')

    save_figure(fig, '17-exploration.png')


# ============================================================================
# CHAPTER 18: ADVANCED TOPICS - Formula visualization
# ============================================================================
def gen_ch18_advanced():
    """Complex formulas and interconnected systems."""
    fig, ax = setup_axes()

    # Formula boxes
    formulas = [
        (150, HEIGHT/2, 'DMG = PWR × RNG'),
        (450, HEIGHT/2-60, 'HIT% = BASE × MOD'),
        (450, HEIGHT/2+60, 'FUEL = MASS × V²'),
        (750, HEIGHT/2, 'EFF = OUT / IN'),
        (1050, HEIGHT/2-40, 'FINAL'),
        (1050, HEIGHT/2+40, 'RESULT')
    ]

    for fx, fy, text in formulas:
        # Box
        box_width = 120
        ax.add_patch(FancyBboxPatch(
            (fx-box_width/2, fy-20), box_width, 40,
            boxstyle="round,pad=0.02,rounding_size=5",
            facecolor=DARK_GRAY, edgecolor=CYAN, linewidth=1.5, alpha=0.8
        ))
        ax.text(fx, fy, text, fontsize=8, color=WHITE, ha='center', va='center',
               fontfamily='monospace')

    # Connection flows
    connections = [
        (0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (3, 5)
    ]

    for i, j in connections:
        x1, y1, _ = formulas[i]
        x2, y2, _ = formulas[j]

        # Bezier-like curve
        mid_x = (x1 + x2) / 2
        ax.plot([x1+60, mid_x, x2-60], [y1, (y1+y2)/2, y2],
               color=CYAN, linewidth=1, alpha=0.4)

    # Data flow particles
    np.random.seed(1818)
    for _ in range(30):
        x = np.random.uniform(100, WIDTH-100)
        y = np.random.uniform(30, HEIGHT-30)
        ax.scatter(x, y, s=3, c=CYAN, alpha=0.4)

    # Variable nodes
    variables = ['α', 'β', 'γ', 'δ', 'ε']
    for i, var in enumerate(variables):
        vx = 100 + i * 250
        vy = 30
        ax.text(vx, vy, var, fontsize=14, color=YELLOW, alpha=0.6,
               ha='center', fontfamily='serif')
        vy2 = HEIGHT - 30
        ax.text(vx, vy2, var, fontsize=14, color=YELLOW, alpha=0.6,
               ha='center', fontfamily='serif')

    save_figure(fig, '18-advanced.png')


# ============================================================================
# APPENDICES - Reference patterns
# ============================================================================
def gen_appendices():
    """Reference tables and data patterns."""
    fig, ax = setup_axes()

    # Data table grid
    rows, cols = 6, 8
    cell_width = WIDTH / (cols + 1)
    cell_height = HEIGHT / (rows + 1)

    for r in range(rows):
        for c in range(cols):
            x = (c + 0.5) * cell_width + 50
            y = HEIGHT - (r + 1) * cell_height

            # Cell
            alpha = 0.3 if (r + c) % 2 == 0 else 0.15
            ax.add_patch(Rectangle((x, y), cell_width-4, cell_height-4,
                                   facecolor=DARK_GRAY, alpha=alpha))

            # Random data visualization
            if r > 0 and c > 0:
                val = np.random.random()
                bar_color = GREEN if val > 0.6 else YELLOW if val > 0.3 else RED
                ax.add_patch(Rectangle((x+5, y+5), (cell_width-14)*val, cell_height-14,
                                       facecolor=bar_color, alpha=0.5))

    # Header row
    headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for c, header in enumerate(headers):
        x = (c + 1) * cell_width + 50
        y = HEIGHT - cell_height/2
        ax.text(x, y, header, fontsize=10, color=CYAN, ha='center', va='center')

    # Header column
    for r in range(1, rows):
        x = cell_width/2 + 20
        y = HEIGHT - (r + 0.5) * cell_height
        ax.text(x, y, str(r), fontsize=10, color=CYAN, ha='center', va='center')

    save_figure(fig, 'appendices.png')


# ============================================================================
# MAIN
# ============================================================================
def main():
    """Generate all chapter art."""
    import os
    os.makedirs('images/art/chapter-art', exist_ok=True)

    generators = [
        gen_ch1_introduction,
        gen_ch2_game_setup,
        gen_ch3_user_interface,
        gen_ch4_systems_bodies,
        gen_ch5_colonies,
        gen_ch6_economy,
        gen_ch7_research,
        gen_ch8_ship_design,
        gen_ch9_fleet_management,
        gen_ch10_navigation,
        gen_ch11_sensors,
        gen_ch12_combat,
        gen_ch13_ground_forces,
        gen_ch14_logistics,
        gen_ch15_diplomacy,
        gen_ch16_commanders,
        gen_ch17_exploration,
        gen_ch18_advanced,
        gen_appendices
    ]

    for gen_func in generators:
        try:
            gen_func()
        except Exception as e:
            print(f"Error in {gen_func.__name__}: {e}")


if __name__ == '__main__':
    main()
