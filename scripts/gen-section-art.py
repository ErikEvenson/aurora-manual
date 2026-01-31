#!/usr/bin/env python3
"""Generate thematic section art for Aurora 4X Manual - V2 with representational imagery."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Polygon, Circle, Ellipse, Rectangle, FancyBboxPatch,
    Wedge, Arc, RegularPolygon, PathPatch, FancyArrow
)
from matplotlib.path import Path
from pathlib import Path as FilePath
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

WIDTH = 1000
HEIGHT = 150


def setup_axes():
    """Create figure with standard dark theme setup."""
    fig, ax = plt.subplots(figsize=(WIDTH/100, HEIGHT/100), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.axis('off')
    ax.set_aspect('equal')
    return fig, ax


def add_stars(ax, num_stars=50, seed=None):
    """Add subtle background stars."""
    if seed:
        np.random.seed(seed + 999)
    x = np.random.uniform(0, WIDTH, num_stars)
    y = np.random.uniform(0, HEIGHT, num_stars)
    sizes = np.random.uniform(0.3, 1.5, num_stars)
    for xi, yi, s in zip(x, y, sizes):
        ax.scatter(xi, yi, s=s, c=WHITE, alpha=0.2, edgecolors='none')


def save_figure(fig, filepath):
    """Save figure with standard settings."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fig.savefig(filepath, facecolor=BG_COLOR, edgecolor='none',
                bbox_inches='tight', pad_inches=0, dpi=150)
    plt.close()


def draw_ship(ax, x, y, size=20, angle=0, color=CYAN, style='fighter'):
    """Draw a spaceship silhouette."""
    if style == 'fighter':
        # Pointed fighter shape
        pts = np.array([[1, 0], [-.5, .4], [-.3, 0], [-.5, -.4]]) * size
    elif style == 'cruiser':
        # Elongated cruiser
        pts = np.array([[1, 0], [.6, .25], [-.8, .2], [-1, 0], [-.8, -.2], [.6, -.25]]) * size
    elif style == 'freighter':
        # Boxy freighter
        pts = np.array([[.6, .15], [.6, .3], [-.6, .3], [-.8, 0], [-.6, -.3], [.6, -.3], [.6, -.15]]) * size
    elif style == 'station':
        # Circular station
        circle = Circle((x, y), size*0.8, facecolor=color, alpha=0.4, edgecolor=color, linewidth=1)
        ax.add_patch(circle)
        return
    else:
        pts = np.array([[1, 0], [-.5, .3], [-.5, -.3]]) * size

    # Rotate
    c, s = np.cos(np.radians(angle)), np.sin(np.radians(angle))
    rot = np.array([[c, -s], [s, c]])
    pts = pts @ rot.T + [x, y]

    ship = Polygon(pts, facecolor=color, alpha=0.6, edgecolor=color, linewidth=1)
    ax.add_patch(ship)
    # Engine glow
    ax.scatter(x - size*0.6*np.cos(np.radians(angle)),
               y - size*0.6*np.sin(np.radians(angle)),
               s=size*2, c=YELLOW, alpha=0.3)


def draw_planet(ax, x, y, radius, color=CYAN, rings=False, moons=0):
    """Draw a planet with optional rings and moons."""
    # Planet body
    planet = Circle((x, y), radius, facecolor=color, alpha=0.5, edgecolor=color, linewidth=1.5)
    ax.add_patch(planet)
    # Highlight
    ax.scatter(x - radius*0.3, y + radius*0.3, s=radius*3, c=WHITE, alpha=0.15)

    if rings:
        ring = Ellipse((x, y), radius*3, radius*0.6, facecolor='none',
                       edgecolor=color, linewidth=1, alpha=0.5)
        ax.add_patch(ring)

    for i in range(moons):
        angle = (i + 0.5) * (2 * np.pi / max(moons, 1))
        mx = x + radius * 2 * np.cos(angle)
        my = y + radius * 0.8 * np.sin(angle)
        moon = Circle((mx, my), radius*0.2, facecolor=GRAY, alpha=0.6)
        ax.add_patch(moon)


def draw_missile(ax, x, y, size=15, angle=0, color=RED):
    """Draw a missile silhouette with exhaust."""
    # Body
    pts = np.array([[1, 0], [.7, .15], [-.6, .12], [-.8, .2], [-1, 0],
                    [-.8, -.2], [-.6, -.12], [.7, -.15]]) * size
    c, s = np.cos(np.radians(angle)), np.sin(np.radians(angle))
    rot = np.array([[c, -s], [s, c]])
    pts = pts @ rot.T + [x, y]
    missile = Polygon(pts, facecolor=color, alpha=0.7, edgecolor=color, linewidth=0.8)
    ax.add_patch(missile)
    # Exhaust
    ex = x - size * np.cos(np.radians(angle))
    ey = y - size * np.sin(np.radians(angle))
    ax.scatter(ex, ey, s=size*4, c=YELLOW, alpha=0.4)


def draw_beam(ax, x1, y1, x2, y2, color=CYAN, width=2):
    """Draw a beam weapon effect."""
    ax.plot([x1, x2], [y1, y2], color=color, linewidth=width, alpha=0.8)
    ax.plot([x1, x2], [y1, y2], color=WHITE, linewidth=width*0.3, alpha=0.5)
    # Impact flash
    ax.scatter(x2, y2, s=50, c=WHITE, alpha=0.6)
    ax.scatter(x2, y2, s=100, c=color, alpha=0.3)


# ============================================================================
# REPRESENTATIONAL GENERATORS
# ============================================================================

def gen_intro_aurora(seed, accent=CYAN):
    """Aurora title scene - ships approaching star."""
    fig, ax = setup_axes()
    np.random.seed(seed)
    add_stars(ax, 80, seed)

    # Central star
    ax.scatter(500, 75, s=800, c=YELLOW, alpha=0.3)
    ax.scatter(500, 75, s=400, c=YELLOW, alpha=0.5)
    ax.scatter(500, 75, s=150, c=WHITE, alpha=0.8)

    # Fleet approaching
    for i, (x, y) in enumerate([(150, 90), (180, 50), (220, 75), (120, 65)]):
        draw_ship(ax, x, y, 12 + i*2, angle=15, color=accent, style='cruiser' if i == 0 else 'fighter')

    return fig, ax


def gen_installation(seed, accent=CYAN):
    """Installation/setup - computer terminal style."""
    fig, ax = setup_axes()

    # Terminal frame
    ax.add_patch(Rectangle((100, 20), 800, 110, facecolor=DARK_GRAY,
                           edgecolor=accent, linewidth=2, alpha=0.8))

    # Code/text lines
    np.random.seed(seed)
    for i in range(6):
        y = 110 - i * 15
        width = np.random.uniform(100, 600)
        ax.plot([130, 130 + width], [y, y], color=accent, linewidth=2, alpha=0.4 + i*0.05)
        if np.random.random() > 0.6:
            ax.scatter(130 + width + 10, y, s=20, c=GREEN, alpha=0.8)

    # Cursor
    ax.add_patch(Rectangle((130, 30), 10, 12, facecolor=accent, alpha=0.8))

    return fig, ax


def gen_main_window(seed, accent=CYAN):
    """UI window representation."""
    fig, ax = setup_axes()

    # Window frame
    ax.add_patch(Rectangle((50, 15), 400, 120, facecolor=DARK_GRAY,
                           edgecolor=accent, linewidth=1.5, alpha=0.7))
    # Title bar
    ax.add_patch(Rectangle((50, 115), 400, 20, facecolor=accent, alpha=0.3))

    # Second window (overlapping)
    ax.add_patch(Rectangle((500, 25), 450, 110, facecolor=DARK_GRAY,
                           edgecolor=GREEN, linewidth=1.5, alpha=0.7))
    ax.add_patch(Rectangle((500, 115), 450, 20, facecolor=GREEN, alpha=0.3))

    # Data elements
    for i in range(4):
        ax.plot([70, 200], [95 - i*18, 95 - i*18], color=GRAY, linewidth=1, alpha=0.5)
        ax.scatter(220, 95 - i*18, s=15, c=accent, alpha=0.6)

    for i in range(3):
        ax.add_patch(Rectangle((520, 90 - i*25), 100, 18, facecolor=accent, alpha=0.2))

    return fig, ax


def gen_system_map(seed, accent=CYAN):
    """System map with star, planets, orbits."""
    fig, ax = setup_axes()
    add_stars(ax, 40, seed)

    # Central star
    ax.scatter(150, 75, s=200, c=YELLOW, alpha=0.8)
    ax.scatter(150, 75, s=400, c=YELLOW, alpha=0.2)

    # Orbital paths and planets
    planets = [(250, 20, GRAY), (400, 25, CYAN), (600, 18, RED), (800, 30, GREEN)]
    for dist, size, color in [(100, 8, GRAY), (250, 15, CYAN), (450, 12, RED), (650, 20, GREEN)]:
        # Orbit
        orbit = Ellipse((150, 75), dist*2, dist*0.5, facecolor='none',
                       edgecolor=GRAY, linewidth=0.5, alpha=0.3, linestyle='--')
        ax.add_patch(orbit)

    # Planets at positions
    np.random.seed(seed)
    draw_planet(ax, 250, 65, 8, GRAY)
    draw_planet(ax, 450, 95, 15, CYAN, moons=1)
    draw_planet(ax, 650, 55, 12, RED)
    draw_planet(ax, 850, 80, 20, GREEN, rings=True)

    return fig, ax


def gen_galactic_map(seed, accent=CYAN):
    """Connected star systems."""
    fig, ax = setup_axes()
    add_stars(ax, 100, seed)

    np.random.seed(seed)
    # Star systems as nodes
    systems = [(100, 75), (250, 45), (250, 105), (400, 75), (550, 35),
               (550, 115), (700, 75), (850, 55), (850, 95)]

    # Jump lanes
    connections = [(0,1), (0,2), (1,3), (2,3), (3,4), (3,5), (4,6), (5,6), (6,7), (6,8)]
    for i, j in connections:
        ax.plot([systems[i][0], systems[j][0]], [systems[i][1], systems[j][1]],
               color=accent, linewidth=1, alpha=0.3, linestyle='--')

    # Systems
    colors = [YELLOW, CYAN, GREEN, YELLOW, RED, CYAN, YELLOW, GREEN, RED]
    for (x, y), c in zip(systems, colors):
        ax.scatter(x, y, s=80, c=c, alpha=0.6)
        ax.scatter(x, y, s=30, c=WHITE, alpha=0.8)

    return fig, ax


def gen_star_system(seed, accent=YELLOW):
    """Star types visualization."""
    fig, ax = setup_axes()
    add_stars(ax, 60, seed)

    # Different star types
    stars = [(150, 75, 40, '#ff6b6b', 'M'), (350, 75, 50, YELLOW, 'G'),
             (550, 75, 35, '#87ceeb', 'A'), (750, 75, 60, '#ffffff', 'O'),
             (900, 75, 25, '#ffa500', 'K')]

    for x, y, size, color, label in stars:
        ax.scatter(x, y, s=size*20, c=color, alpha=0.3)
        ax.scatter(x, y, s=size*10, c=color, alpha=0.6)
        ax.scatter(x, y, s=size*3, c=WHITE, alpha=0.8)

    return fig, ax


def gen_planets(seed, accent=CYAN):
    """Planet types lineup."""
    fig, ax = setup_axes()
    add_stars(ax, 40, seed)

    # Various planet types
    draw_planet(ax, 100, 75, 25, '#8b4513')  # Rocky
    draw_planet(ax, 250, 75, 35, CYAN, moons=2)  # Terrestrial
    draw_planet(ax, 450, 75, 45, '#ffa500', rings=True)  # Gas giant
    draw_planet(ax, 650, 75, 30, '#87ceeb')  # Ice giant
    draw_planet(ax, 850, 75, 20, GRAY)  # Barren

    return fig, ax


def gen_asteroids(seed, accent=GRAY):
    """Asteroid field."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)
    np.random.seed(seed)

    for _ in range(40):
        x = np.random.uniform(50, 950)
        y = np.random.uniform(20, 130)
        size = np.random.uniform(3, 15)
        pts = []
        for angle in np.linspace(0, 2*np.pi, 6):
            r = size * (0.7 + 0.3 * np.random.random())
            pts.append([x + r*np.cos(angle), y + r*np.sin(angle)])
        asteroid = Polygon(pts, facecolor=GRAY, alpha=0.5, edgecolor=DARK_GRAY)
        ax.add_patch(asteroid)

    return fig, ax


def gen_jump_point(seed, accent=CYAN):
    """Jump point visualization."""
    fig, ax = setup_axes()
    add_stars(ax, 50, seed)

    # Jump point as swirling portal
    cx, cy = 500, 75
    for r in range(5, 50, 5):
        circle = Circle((cx, cy), r, facecolor='none', edgecolor=accent,
                        linewidth=2 - r/30, alpha=0.6 - r/100)
        ax.add_patch(circle)

    ax.scatter(cx, cy, s=100, c=WHITE, alpha=0.8)

    # Ships entering/exiting
    draw_ship(ax, 300, 80, 15, angle=10, color=CYAN, style='cruiser')
    draw_ship(ax, 700, 70, 15, angle=170, color=GREEN, style='cruiser')

    return fig, ax


def gen_colony_establish(seed, accent=CYAN):
    """Colony ship landing on planet."""
    fig, ax = setup_axes()
    add_stars(ax, 40, seed)

    # Planet surface
    ax.fill_between([0, WIDTH], [0, 0], [40, 40], color='#3d3d5c', alpha=0.8)
    ax.fill_between([0, WIDTH], [0, 0], [30, 30], color='#4d4d6d', alpha=0.6)

    # Colony ship descending
    draw_ship(ax, 500, 90, 35, angle=-90, color=accent, style='freighter')

    # Landing pad/beacon
    ax.plot([450, 550], [35, 35], color=YELLOW, linewidth=2, alpha=0.8)
    ax.scatter(500, 35, s=50, c=YELLOW, alpha=0.6)

    # Existing domes
    for dx in [150, 300, 700, 850]:
        size = np.random.uniform(20, 35)
        dome = Wedge((dx, 30), size, 0, 180, facecolor=accent, alpha=0.2)
        ax.add_patch(dome)
        arc = Arc((dx, 30), size*2, size*2, theta1=0, theta2=180,
                 color=accent, linewidth=1.5, alpha=0.6)
        ax.add_patch(arc)

    return fig, ax


def gen_population(seed, accent=GREEN):
    """Population growth visualization."""
    fig, ax = setup_axes()

    # Growth chart
    x = np.linspace(100, 900, 50)
    y = 30 + 80 * (1 - np.exp(-x/400))
    ax.fill_between(x, 20, y, color=accent, alpha=0.3)
    ax.plot(x, y, color=accent, linewidth=2, alpha=0.8)

    # Population icons
    for px in [200, 400, 600, 800]:
        idx = int((px - 100) / 16)
        py = y[min(idx, len(y)-1)]
        ax.scatter(px, py, s=40, c=WHITE, alpha=0.8)

    return fig, ax


def gen_environment(seed, accent=GREEN):
    """Atmospheric/environment."""
    fig, ax = setup_axes()

    # Planet with atmosphere layers
    cx, cy = 500, 75

    # Atmosphere layers
    for r, alpha in [(70, 0.1), (60, 0.15), (50, 0.2)]:
        atmo = Circle((cx, cy), r, facecolor=accent, alpha=alpha)
        ax.add_patch(atmo)

    # Planet core
    planet = Circle((cx, cy), 40, facecolor='#2d5a3d', alpha=0.8,
                    edgecolor=accent, linewidth=1)
    ax.add_patch(planet)

    # Atmospheric indicators
    for angle in [30, 90, 150, 210, 270, 330]:
        x = cx + 55 * np.cos(np.radians(angle))
        y = cy + 55 * np.sin(np.radians(angle))
        ax.scatter(x, y, s=15, c=WHITE, alpha=0.5)

    add_stars(ax, 30, seed)
    return fig, ax


def gen_infrastructure(seed, accent=CYAN):
    """Industrial infrastructure."""
    fig, ax = setup_axes()

    # Ground
    ax.fill_between([0, WIDTH], [0, 0], [35, 35], color=DARK_GRAY, alpha=0.8)

    # Buildings/installations
    buildings = [(100, 50), (200, 70), (350, 45), (500, 80), (650, 55), (800, 65), (900, 40)]
    for bx, height in buildings:
        ax.add_patch(Rectangle((bx-20, 35), 40, height, facecolor='#3a3a5a',
                               edgecolor=accent, linewidth=1, alpha=0.7))
        # Windows
        for wy in range(45, 35 + int(height) - 5, 12):
            ax.scatter(bx, wy, s=8, c=YELLOW, alpha=0.6)

    # Connecting lines (power/transport)
    for i in range(len(buildings) - 1):
        ax.plot([buildings[i][0], buildings[i+1][0]], [35, 35],
               color=accent, linewidth=1, alpha=0.3)

    return fig, ax


def gen_terraforming(seed, accent=GREEN):
    """Planet transformation."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Before planet (left, barren)
    draw_planet(ax, 200, 75, 40, GRAY)

    # Arrow
    ax.annotate('', xy=(450, 75), xytext=(300, 75),
               arrowprops=dict(arrowstyle='->', color=accent, lw=2))

    # After planet (right, terraformed)
    draw_planet(ax, 700, 75, 40, GREEN)
    # Add blue water patches
    ax.scatter(685, 85, s=80, c=CYAN, alpha=0.4)
    ax.scatter(715, 65, s=60, c=CYAN, alpha=0.4)

    return fig, ax


def gen_minerals(seed, accent=CYAN):
    """Mineral crystals and deposits."""
    fig, ax = setup_axes()
    add_stars(ax, 20, seed)
    np.random.seed(seed)

    colors = [RED, CYAN, YELLOW, GREEN, '#ff69b4', '#9370db', GRAY]
    for i in range(9):
        x = 80 + i * 100
        y = 75 + np.random.uniform(-20, 20)
        color = colors[i % len(colors)]
        # Crystal shape
        size = np.random.uniform(15, 30)
        pts = [[x, y + size], [x + size*0.4, y + size*0.3], [x + size*0.3, y - size*0.5],
               [x - size*0.3, y - size*0.5], [x - size*0.4, y + size*0.3]]
        crystal = Polygon(pts, facecolor=color, alpha=0.6, edgecolor=WHITE, linewidth=0.8)
        ax.add_patch(crystal)
        ax.scatter(x, y + size*0.7, s=20, c=WHITE, alpha=0.5)

    return fig, ax


def gen_mining(seed, accent=YELLOW):
    """Mining operation."""
    fig, ax = setup_axes()

    # Asteroid/planet surface
    ax.fill_between([0, WIDTH], [0, 0], [50, 50], color='#4a4a5a', alpha=0.8)
    np.random.seed(seed)

    # Mining installations
    for mx in [200, 500, 800]:
        # Drill structure
        ax.add_patch(Rectangle((mx-15, 50), 30, 50, facecolor=GRAY, edgecolor=accent, linewidth=1))
        ax.plot([mx, mx], [100, 50], color=accent, linewidth=3, alpha=0.8)
        # Mineral deposits below
        for _ in range(3):
            dx = mx + np.random.uniform(-40, 40)
            dy = np.random.uniform(10, 40)
            color = np.random.choice([RED, CYAN, YELLOW, GREEN])
            ax.scatter(dx, dy, s=np.random.uniform(30, 80), c=color, alpha=0.5)

    return fig, ax


def gen_construction(seed, accent=CYAN):
    """Factory/construction."""
    fig, ax = setup_axes()

    # Factory building
    ax.add_patch(Rectangle((300, 30), 400, 90, facecolor=DARK_GRAY,
                           edgecolor=accent, linewidth=2, alpha=0.8))

    # Conveyor belt input
    ax.plot([50, 300], [50, 50], color=GRAY, linewidth=4, alpha=0.6)
    for x in range(80, 280, 40):
        ax.add_patch(Rectangle((x, 45), 20, 10, facecolor=accent, alpha=0.5))

    # Conveyor belt output
    ax.plot([700, 950], [70, 70], color=GRAY, linewidth=4, alpha=0.6)
    for x in range(720, 930, 40):
        ax.scatter(x + 10, 70, s=80, marker='s', c=GREEN, alpha=0.6)

    # Smokestacks
    for sx in [350, 450, 550, 650]:
        ax.add_patch(Rectangle((sx, 120), 15, 25, facecolor=GRAY, alpha=0.7))

    return fig, ax


def gen_trade(seed, accent=YELLOW):
    """Trade routes and freighters."""
    fig, ax = setup_axes()
    add_stars(ax, 40, seed)

    # Trade route
    x = np.linspace(100, 900, 50)
    y = 75 + 20 * np.sin(x * 0.01)
    ax.plot(x, y, color=accent, linewidth=1, alpha=0.4, linestyle='--')

    # Freighters along route
    for i, fx in enumerate([200, 400, 600, 800]):
        fy = 75 + 20 * np.sin(fx * 0.01)
        draw_ship(ax, fx, fy, 18, angle=5 + i*3, color=CYAN, style='freighter')

    # Stations at endpoints
    draw_ship(ax, 100, 75, 25, color=GREEN, style='station')
    draw_ship(ax, 900, 75, 25, color=GREEN, style='station')

    return fig, ax


def gen_civilian(seed, accent=GREEN):
    """Civilian shipping."""
    fig, ax = setup_axes()
    add_stars(ax, 50, seed)

    np.random.seed(seed)
    # Multiple civilian ships
    for _ in range(8):
        x = np.random.uniform(100, 900)
        y = np.random.uniform(30, 120)
        angle = np.random.uniform(-30, 30)
        draw_ship(ax, x, y, np.random.uniform(10, 20), angle=angle,
                 color=np.random.choice([CYAN, GREEN, GRAY]), style='freighter')

    return fig, ax


def gen_tech_tree(seed, accent=CYAN):
    """Technology tree branches."""
    fig, ax = setup_axes()
    np.random.seed(seed)

    # Tree structure
    nodes = [(100, 75), (250, 45), (250, 105), (400, 30), (400, 75), (400, 120),
             (550, 45), (550, 105), (700, 75), (850, 60), (850, 90)]

    # Connections
    conns = [(0,1), (0,2), (1,3), (1,4), (2,4), (2,5), (3,6), (4,6), (4,7), (5,7), (6,8), (7,8), (8,9), (8,10)]
    for i, j in conns:
        ax.plot([nodes[i][0], nodes[j][0]], [nodes[i][1], nodes[j][1]],
               color=accent, linewidth=1.5, alpha=0.4)

    # Nodes with icons
    for i, (x, y) in enumerate(nodes):
        researched = i < 6
        color = GREEN if researched else GRAY
        ax.scatter(x, y, s=150, c=color, alpha=0.3)
        ax.scatter(x, y, s=60, c=color, alpha=0.7)
        if researched:
            ax.scatter(x, y, s=20, c=WHITE, alpha=0.8)

    return fig, ax


def gen_scientists(seed, accent=GREEN):
    """Research scientists."""
    fig, ax = setup_axes()

    # Lab setting
    ax.add_patch(Rectangle((100, 20), 800, 110, facecolor=DARK_GRAY, alpha=0.5))

    # Scientist icons (simplified figures)
    positions = [200, 350, 500, 650, 800]
    for i, px in enumerate(positions):
        # Head
        ax.scatter(px, 90, s=100, c=WHITE, alpha=0.6)
        # Body
        ax.plot([px, px], [75, 50], color=WHITE, linewidth=3, alpha=0.5)
        # Lab coat
        color = [CYAN, GREEN, YELLOW, RED, CYAN][i]
        ax.add_patch(Rectangle((px-15, 40), 30, 35, facecolor=color, alpha=0.3))
        # Research bar below
        fill = 0.3 + i * 0.15
        ax.add_patch(Rectangle((px-25, 25), 50*fill, 8, facecolor=color, alpha=0.6))

    return fig, ax


def gen_research_lab(seed, accent=CYAN):
    """Research facilities."""
    fig, ax = setup_axes()

    # Multiple lab buildings
    for i, lx in enumerate([150, 400, 650, 900]):
        size = 60 + i * 10
        ax.add_patch(Rectangle((lx-40, 30), 80, size, facecolor=DARK_GRAY,
                               edgecolor=accent, linewidth=1.5, alpha=0.7))
        # Dome top
        dome = Arc((lx, 30 + size), 80, 40, theta1=0, theta2=180,
                  color=accent, linewidth=1.5, alpha=0.7)
        ax.add_patch(dome)
        # Windows
        ax.scatter(lx, 30 + size*0.6, s=50, c=CYAN, alpha=0.5)

    return fig, ax


def gen_ship_blueprint(seed, accent=CYAN):
    """Ship design blueprint."""
    fig, ax = setup_axes()

    # Grid
    for x in range(0, WIDTH+1, 25):
        ax.axvline(x, color=accent, linewidth=0.3, alpha=0.2)
    for y in range(0, HEIGHT+1, 25):
        ax.axhline(y, color=accent, linewidth=0.3, alpha=0.2)

    # Ship outline (large cruiser)
    pts = np.array([[400, 75], [350, 95], [200, 90], [150, 75], [200, 60], [350, 55]])
    ship = Polygon(pts, facecolor='none', edgecolor=accent, linewidth=2, alpha=0.8)
    ax.add_patch(ship)

    # Component boxes
    components = [(300, 75, 40, 'Engine'), (250, 85, 25, 'Fuel'), (250, 65, 25, 'Fuel'),
                  (350, 75, 30, 'Bridge')]
    for cx, cy, size, _ in components:
        ax.add_patch(Rectangle((cx-size/2, cy-size/3), size, size*0.6,
                               facecolor=accent, alpha=0.2, edgecolor=accent, linewidth=1))

    # Dimension lines
    ax.annotate('', xy=(400, 40), xytext=(150, 40),
               arrowprops=dict(arrowstyle='<->', color=GRAY, lw=1))

    return fig, ax


def gen_armor(seed, accent=GRAY):
    """Hull and armor layers."""
    fig, ax = setup_axes()

    # Cross-section of ship hull
    cx, cy = 500, 75

    # Armor layers
    for r, color, label in [(60, '#3a3a5a', 'Outer'), (50, '#4a4a6a', 'Mid'), (40, DARK_GRAY, 'Inner')]:
        layer = Ellipse((cx, cy), r*3, r*1.5, facecolor=color, alpha=0.6, edgecolor=accent, linewidth=1)
        ax.add_patch(layer)

    # Internal components
    ax.scatter(cx, cy, s=200, c=CYAN, alpha=0.3)
    ax.scatter(cx, cy, s=80, c=CYAN, alpha=0.6)

    # Damage indicators
    for angle in [45, 120, 200, 300]:
        x = cx + 50 * np.cos(np.radians(angle))
        y = cy + 25 * np.sin(np.radians(angle))
        ax.scatter(x, y, s=30, c=RED, alpha=0.6, marker='x')

    return fig, ax


def gen_engines(seed, accent=YELLOW):
    """Engine systems."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Ship with prominent engine
    ship_pts = np.array([[700, 75], [650, 95], [400, 90], [350, 75], [400, 60], [650, 55]])
    ship = Polygon(ship_pts, facecolor=DARK_GRAY, edgecolor=CYAN, linewidth=1.5, alpha=0.7)
    ax.add_patch(ship)

    # Engine glow/exhaust
    for i, (size, alpha) in enumerate([(200, 0.1), (150, 0.2), (100, 0.3), (50, 0.5)]):
        ax.scatter(350 - i*30, 75, s=size*10, c=accent, alpha=alpha)

    # Exhaust trail
    x = np.linspace(350, 100, 30)
    for i, xi in enumerate(x):
        ax.scatter(xi, 75 + np.random.uniform(-5, 5), s=20-i*0.5, c=accent, alpha=0.3-i*0.01)

    return fig, ax


def gen_sensors(seed, accent=CYAN):
    """Sensor systems - radar waves."""
    fig, ax = setup_axes()
    add_stars(ax, 40, seed)

    # Ship with sensor dish
    draw_ship(ax, 150, 75, 25, angle=0, color=GRAY, style='cruiser')

    # Sensor waves emanating
    for r in range(1, 10):
        arc = Arc((180, 75), r*80, r*40, theta1=-45, theta2=45,
                 color=accent, linewidth=2-r*0.15, alpha=0.6-r*0.05)
        ax.add_patch(arc)

    # Detected contacts
    contacts = [(600, 95, GREEN, 'friendly'), (750, 50, RED, 'hostile'), (850, 80, YELLOW, 'unknown')]
    for cx, cy, color, _ in contacts:
        ax.scatter(cx, cy, s=80, c=color, alpha=0.3)
        ax.scatter(cx, cy, s=30, c=color, alpha=0.7)

    return fig, ax


def gen_weapons(seed, accent=RED):
    """Weapons - beams and missiles."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Attacking ship
    draw_ship(ax, 150, 75, 25, angle=10, color=CYAN, style='cruiser')

    # Beam weapons
    draw_beam(ax, 175, 80, 600, 90, CYAN, 2)
    draw_beam(ax, 175, 70, 620, 60, CYAN, 2)

    # Target ship (damaged)
    draw_ship(ax, 700, 75, 20, angle=180, color=RED, style='cruiser')
    ax.scatter(680, 75, s=150, c=YELLOW, alpha=0.4)
    ax.scatter(680, 75, s=50, c=WHITE, alpha=0.6)

    # Missiles
    draw_missile(ax, 300, 100, 12, angle=20, color=RED)
    draw_missile(ax, 350, 50, 12, angle=-15, color=RED)

    return fig, ax


def gen_fire_control(seed, accent=CYAN):
    """Fire control targeting."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Targeting reticle
    cx, cy = 500, 75
    for r in [50, 35, 20]:
        circle = Circle((cx, cy), r, facecolor='none', edgecolor=accent,
                        linewidth=1.5, alpha=0.6)
        ax.add_patch(circle)

    # Crosshairs
    ax.plot([cx-60, cx+60], [cy, cy], color=accent, linewidth=1, alpha=0.5)
    ax.plot([cx, cx], [cy-60, cy+60], color=accent, linewidth=1, alpha=0.5)

    # Target
    draw_ship(ax, cx, cy, 15, angle=45, color=RED, style='fighter')

    # Range indicators
    for x in [200, 350, 650, 800]:
        ax.plot([x, x], [30, 40], color=GRAY, linewidth=1, alpha=0.5)

    return fig, ax


def gen_missiles(seed, accent=RED):
    """Missile systems."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Missile salvo
    for i in range(6):
        x = 150 + i * 100
        y = 75 + 15 * np.sin(i * 0.5)
        draw_missile(ax, x, y, 15, angle=10 + i*2, color=accent)

    # Target ahead
    draw_ship(ax, 900, 75, 20, angle=180, color=GRAY, style='cruiser')

    return fig, ax


def gen_point_defense(seed, accent=GREEN):
    """Point defense systems."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Defending ship
    draw_ship(ax, 800, 75, 30, angle=180, color=CYAN, style='cruiser')

    # Incoming missiles being shot down
    missiles = [(200, 90), (300, 50), (400, 100), (350, 65)]
    for mx, my in missiles:
        draw_missile(ax, mx, my, 10, angle=np.degrees(np.arctan2(75-my, 800-mx)), color=RED)
        # PD beam
        draw_beam(ax, 770, 75, mx+30, my, GREEN, 1)
        # Explosion
        ax.scatter(mx+30, my, s=50, c=YELLOW, alpha=0.5)

    return fig, ax


def gen_electronic_warfare(seed, accent=CYAN):
    """ECM/ECCM visualization."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Two ships with interference between them
    draw_ship(ax, 200, 75, 20, color=CYAN, style='cruiser')
    draw_ship(ax, 800, 75, 20, angle=180, color=RED, style='cruiser')

    # ECM waves (jagged)
    x = np.linspace(250, 750, 100)
    np.random.seed(seed)
    y = 75 + 15 * np.sin(x * 0.1) + np.random.uniform(-5, 5, 100)
    ax.plot(x, y, color=accent, linewidth=1, alpha=0.5)
    ax.plot(x, y + 10, color=RED, linewidth=1, alpha=0.3)
    ax.plot(x, y - 10, color=RED, linewidth=1, alpha=0.3)

    return fig, ax


def gen_damage(seed, accent=RED):
    """Damage and armor penetration."""
    fig, ax = setup_axes()

    # Armor grid
    for x in range(100, 900, 40):
        for y in range(25, 130, 35):
            damaged = np.random.random() < 0.3
            color = RED if damaged else GRAY
            alpha = 0.6 if damaged else 0.3
            ax.add_patch(Rectangle((x, y), 35, 30, facecolor=color, alpha=alpha,
                                   edgecolor=DARK_GRAY, linewidth=1))
            if damaged:
                ax.scatter(x+17, y+15, s=20, c=YELLOW, alpha=0.5)

    return fig, ax


def gen_pdc(seed, accent=RED):
    """Planetary Defense Centers."""
    fig, ax = setup_axes()
    add_stars(ax, 40, seed)

    # Planet surface
    ax.fill_between([0, WIDTH], [0, 0], [40, 40], color='#3d5a3d', alpha=0.8)

    # PDC installations
    for px in [200, 500, 800]:
        # Bunker
        ax.add_patch(Rectangle((px-30, 40), 60, 30, facecolor=GRAY, alpha=0.7))
        # Turret
        ax.add_patch(Wedge((px, 70), 20, 30, 150, facecolor=DARK_GRAY, edgecolor=accent))

    # Missiles launching
    draw_missile(ax, 220, 100, 12, angle=60, color=RED)
    draw_missile(ax, 500, 110, 12, angle=80, color=RED)

    # Incoming threat
    draw_ship(ax, 850, 130, 15, angle=200, color=CYAN, style='fighter')

    return fig, ax


def gen_ground_units(seed, accent=CYAN):
    """Ground force units."""
    fig, ax = setup_axes()

    # Terrain
    x = np.linspace(0, WIDTH, 100)
    np.random.seed(seed)
    y = 40 + 10*np.sin(x*0.02) + 5*np.sin(x*0.05)
    ax.fill_between(x, 0, y, color='#4a5a4a', alpha=0.8)

    # Units
    unit_types = [('Infantry', 's', 15, CYAN), ('Vehicle', 'D', 25, GREEN),
                  ('Artillery', '^', 20, YELLOW), ('Armor', 'H', 30, RED)]
    for i, (_, marker, size, color) in enumerate(unit_types):
        for j in range(3):
            ux = 150 + i*200 + j*40
            uy = 70 + np.random.uniform(-10, 20)
            ax.scatter(ux, uy, s=size*10, marker=marker, c=color, alpha=0.7)

    return fig, ax


def gen_training(seed, accent=GREEN):
    """Training and transport."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Training bars (experience levels)
    for i in range(5):
        x = 150 + i * 160
        fill = 0.2 + i * 0.2
        ax.add_patch(Rectangle((x, 50), 100, 50, facecolor=DARK_GRAY,
                               edgecolor=accent, linewidth=1, alpha=0.6))
        ax.add_patch(Rectangle((x+5, 55), 90*fill, 40, facecolor=accent, alpha=0.5))
        # Rank indicator
        for j in range(i+1):
            ax.scatter(x + 20 + j*15, 110, s=20, c=YELLOW, marker='*', alpha=0.8)

    return fig, ax


def gen_ground_combat(seed, accent=RED):
    """Ground combat scene."""
    fig, ax = setup_axes()

    # Terrain
    ax.fill_between([0, WIDTH], [0, 0], [35, 35], color='#3a4a3a', alpha=0.8)

    # Two forces facing each other
    # Blue force (left)
    for ux in [100, 150, 200]:
        ax.scatter(ux, 60 + np.random.uniform(-10, 10), s=150, marker='s', c=CYAN, alpha=0.6)

    # Red force (right)
    for ux in [800, 850, 900]:
        ax.scatter(ux, 60 + np.random.uniform(-10, 10), s=150, marker='s', c=RED, alpha=0.6)

    # Fire exchange
    for _ in range(4):
        y = 55 + np.random.uniform(0, 30)
        ax.plot([220, 780], [y, y + np.random.uniform(-10, 10)],
               color=YELLOW, linewidth=1, alpha=0.4)

    # Explosions in middle
    for _ in range(3):
        ex = np.random.uniform(400, 600)
        ey = np.random.uniform(50, 100)
        ax.scatter(ex, ey, s=100, c=YELLOW, alpha=0.4)
        ax.scatter(ex, ey, s=40, c=WHITE, alpha=0.6)

    return fig, ax


def gen_fuel(seed, accent=YELLOW):
    """Fuel logistics."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Tanker ship
    draw_ship(ax, 300, 75, 30, angle=0, color=accent, style='freighter')

    # Fuel transfer beam
    ax.plot([340, 550], [75, 75], color=accent, linewidth=3, alpha=0.5, linestyle=':')

    # Receiving ship
    draw_ship(ax, 600, 75, 25, angle=0, color=CYAN, style='cruiser')

    # Fuel gauge
    ax.add_patch(Rectangle((800, 40), 30, 70, facecolor=DARK_GRAY, edgecolor=accent, linewidth=1))
    ax.add_patch(Rectangle((805, 45), 20, 40, facecolor=accent, alpha=0.6))

    return fig, ax


def gen_maintenance(seed, accent=CYAN):
    """Maintenance operations."""
    fig, ax = setup_axes()

    # Ship in drydock/maintenance
    ship_pts = np.array([[600, 75], [550, 95], [300, 90], [250, 75], [300, 60], [550, 55]])
    ship = Polygon(ship_pts, facecolor=DARK_GRAY, edgecolor=GRAY, linewidth=1.5, alpha=0.6)
    ax.add_patch(ship)

    # Scaffolding/support structures
    for sx in [280, 350, 450, 550]:
        ax.plot([sx, sx], [20, 55], color=accent, linewidth=2, alpha=0.5)
        ax.plot([sx, sx], [95, 130], color=accent, linewidth=2, alpha=0.5)

    # Work indicators
    ax.scatter(400, 85, s=30, c=YELLOW, alpha=0.8)  # Welding spark
    ax.scatter(500, 65, s=30, c=YELLOW, alpha=0.8)

    # Maintenance bar
    ax.add_patch(Rectangle((700, 60), 200, 30, facecolor=DARK_GRAY, edgecolor=accent))
    ax.add_patch(Rectangle((705, 65), 140, 20, facecolor=GREEN, alpha=0.6))

    return fig, ax


def gen_supply(seed, accent=GREEN):
    """Supply ships."""
    fig, ax = setup_axes()
    add_stars(ax, 40, seed)

    # Supply convoy
    for i, x in enumerate([150, 350, 550, 750]):
        draw_ship(ax, x, 75 + (i%2)*20 - 10, 20, angle=5, color=accent, style='freighter')
        # Cargo indicators
        for j in range(3):
            ax.add_patch(Rectangle((x-15+j*10, 55), 8, 8, facecolor=CYAN, alpha=0.4))

    return fig, ax


def gen_orbital_habitat(seed, accent=CYAN):
    """Orbital habitats/stations."""
    fig, ax = setup_axes()
    add_stars(ax, 50, seed)

    # Large station
    cx, cy = 500, 75

    # Central hub
    ax.add_patch(Circle((cx, cy), 30, facecolor=DARK_GRAY, edgecolor=accent, linewidth=2, alpha=0.7))

    # Rotating ring
    ring = Ellipse((cx, cy), 120, 40, facecolor='none', edgecolor=accent, linewidth=2, alpha=0.6)
    ax.add_patch(ring)

    # Spokes
    for angle in [0, 60, 120, 180, 240, 300]:
        x2 = cx + 45 * np.cos(np.radians(angle))
        y2 = cy + 15 * np.sin(np.radians(angle))
        ax.plot([cx, x2], [cy, y2], color=accent, linewidth=1, alpha=0.5)

    # Docked ships
    draw_ship(ax, 350, 80, 12, angle=0, color=GREEN, style='freighter')
    draw_ship(ax, 650, 70, 12, angle=180, color=GREEN, style='freighter')

    return fig, ax


def gen_aliens(seed, accent=RED):
    """Alien races."""
    fig, ax = setup_axes()
    add_stars(ax, 60, seed)

    # Human ship
    draw_ship(ax, 300, 75, 20, color=CYAN, style='cruiser')

    # Unknown alien ship (different design)
    alien_pts = np.array([[700, 75], [650, 60], [600, 75], [650, 90]])
    alien = Polygon(alien_pts, facecolor=accent, alpha=0.5, edgecolor=accent, linewidth=1.5)
    ax.add_patch(alien)
    ax.scatter(650, 75, s=100, c=accent, alpha=0.3)

    # Question marks / unknown
    ax.scatter(500, 75, s=200, c=YELLOW, alpha=0.2)
    ax.text(490, 65, '?', fontsize=20, color=YELLOW, alpha=0.6, fontweight='bold')

    return fig, ax


def gen_communications(seed, accent=CYAN):
    """Communications."""
    fig, ax = setup_axes()
    add_stars(ax, 40, seed)

    # Two ships communicating
    draw_ship(ax, 200, 75, 20, color=CYAN, style='cruiser')
    draw_ship(ax, 800, 75, 20, angle=180, color=GREEN, style='cruiser')

    # Communication waves
    for i in range(5):
        x = 300 + i * 80
        wave_y = 75 + 10 * np.sin(np.linspace(0, 2*np.pi, 20))
        ax.plot(np.linspace(x, x+60, 20), wave_y, color=accent, linewidth=1.5, alpha=0.5-i*0.08)

    return fig, ax


def gen_treaties(seed, accent=GREEN):
    """Treaties/agreements."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Two faction symbols connected
    ax.scatter(250, 75, s=400, c=CYAN, alpha=0.3)
    ax.scatter(250, 75, s=150, c=CYAN, alpha=0.6)

    ax.scatter(750, 75, s=400, c=GREEN, alpha=0.3)
    ax.scatter(750, 75, s=150, c=GREEN, alpha=0.6)

    # Connection/treaty line
    ax.plot([300, 700], [75, 75], color=accent, linewidth=3, alpha=0.6)

    # Handshake symbol in middle
    ax.add_patch(Rectangle((470, 55), 60, 40, facecolor=DARK_GRAY, edgecolor=accent,
                           linewidth=2, alpha=0.7))

    return fig, ax


def gen_diplomacy(seed, accent=YELLOW):
    """Diplomatic relations web."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Central player
    cx, cy = 500, 75
    ax.scatter(cx, cy, s=200, c=CYAN, alpha=0.5)

    # Connected factions
    factions = [(200, 45, GREEN), (200, 105, YELLOW), (800, 45, RED), (800, 105, GRAY)]
    for fx, fy, color in factions:
        ax.scatter(fx, fy, s=100, c=color, alpha=0.5)
        ax.plot([cx, fx], [cy, fy], color=color, linewidth=2, alpha=0.4)

    return fig, ax


def gen_intelligence(seed, accent=GRAY):
    """Intelligence gathering."""
    fig, ax = setup_axes()
    add_stars(ax, 40, seed)

    # Stealth ship
    ship_pts = np.array([[300, 75], [270, 85], [200, 80], [180, 75], [200, 70], [270, 65]])
    ship = Polygon(ship_pts, facecolor=DARK_GRAY, edgecolor=accent, linewidth=1, alpha=0.4)
    ax.add_patch(ship)

    # Target being observed
    draw_ship(ax, 700, 75, 25, angle=45, color=RED, style='cruiser')

    # Observation line (dashed)
    ax.plot([320, 680], [75, 75], color=accent, linewidth=1, alpha=0.3, linestyle=':')

    # Data collection indicators
    for i in range(4):
        ax.scatter(400 + i*60, 75, s=15, c=accent, alpha=0.4 + i*0.1)

    return fig, ax


def gen_officers(seed, accent=CYAN):
    """Officer generation."""
    fig, ax = setup_axes()

    # Academy building
    ax.add_patch(Rectangle((350, 30), 300, 90, facecolor=DARK_GRAY, edgecolor=accent, linewidth=2))
    # Columns
    for cx in [380, 450, 550, 620]:
        ax.add_patch(Rectangle((cx, 30), 15, 70, facecolor='#4a4a6a', alpha=0.7))
    # Roof
    pts = [[340, 120], [500, 140], [660, 120]]
    ax.add_patch(Polygon(pts, facecolor=DARK_GRAY, edgecolor=accent, linewidth=1.5))

    # Graduating officers (silhouettes)
    for ox in [150, 200, 750, 800, 850]:
        ax.scatter(ox, 50, s=60, c=WHITE, alpha=0.5)
        ax.plot([ox, ox], [35, 20], color=WHITE, linewidth=2, alpha=0.4)

    return fig, ax


def gen_skills(seed, accent=YELLOW):
    """Skills and bonuses."""
    fig, ax = setup_axes()

    # Skill bars
    skills = [('Combat', 0.8, RED), ('Navigation', 0.6, CYAN), ('Engineering', 0.9, GREEN),
              ('Science', 0.5, YELLOW), ('Leadership', 0.7, WHITE)]

    for i, (name, level, color) in enumerate(skills):
        y = 120 - i * 22
        ax.add_patch(Rectangle((200, y), 600, 18, facecolor=DARK_GRAY, edgecolor=GRAY, linewidth=1))
        ax.add_patch(Rectangle((202, y+2), 596*level, 14, facecolor=color, alpha=0.6))
        # Star rating
        stars = int(level * 5)
        for j in range(stars):
            ax.scatter(820 + j*20, y+9, s=25, c=YELLOW, marker='*', alpha=0.8)

    return fig, ax


def gen_assignments(seed, accent=GREEN):
    """Officer assignments."""
    fig, ax = setup_axes()
    add_stars(ax, 30, seed)

    # Ships with officer indicators
    ships = [(200, 75, 'cruiser'), (500, 75, 'cruiser'), (800, 75, 'station')]
    for sx, sy, style in ships:
        draw_ship(ax, sx, sy, 25, color=CYAN, style=style)
        # Officer icon
        ax.scatter(sx, sy + 35, s=40, c=YELLOW, alpha=0.8)
        # Connection line
        ax.plot([sx, sx], [sy + 15, sy + 30], color=accent, linewidth=1, alpha=0.5)

    return fig, ax


def gen_geological_survey(seed, accent=GREEN):
    """Geological survey."""
    fig, ax = setup_axes()
    add_stars(ax, 50, seed)

    # Survey ship with scan beam
    draw_ship(ax, 300, 100, 20, angle=-45, color=CYAN, style='cruiser')

    # Planet being surveyed
    draw_planet(ax, 600, 60, 40, '#8b4513')

    # Scan beam
    ax.fill([320, 560, 640, 320], [90, 20, 100, 90], color=accent, alpha=0.1)
    ax.plot([320, 560], [90, 20], color=accent, linewidth=1, alpha=0.5)
    ax.plot([320, 640], [90, 100], color=accent, linewidth=1, alpha=0.5)

    # Mineral indicators on planet
    for angle in [30, 120, 200]:
        mx = 600 + 30 * np.cos(np.radians(angle))
        my = 60 + 30 * np.sin(np.radians(angle))
        ax.scatter(mx, my, s=20, c=np.random.choice([RED, YELLOW, CYAN]), alpha=0.7)

    return fig, ax


def gen_gravitational_survey(seed, accent=CYAN):
    """Gravitational survey - finding jump points."""
    fig, ax = setup_axes()
    add_stars(ax, 60, seed)

    # Survey ship
    draw_ship(ax, 200, 75, 20, color=CYAN, style='cruiser')

    # Search pattern (spiral)
    theta = np.linspace(0, 4*np.pi, 100)
    r = 10 + theta * 15
    x = 500 + r * np.cos(theta) * 0.6
    y = 75 + r * np.sin(theta) * 0.3
    ax.plot(x, y, color=accent, linewidth=1, alpha=0.4, linestyle='--')

    # Discovered jump point
    cx, cy = 750, 60
    for r in range(5, 30, 5):
        circle = Circle((cx, cy), r, facecolor='none', edgecolor=accent, alpha=0.5-r/60)
        ax.add_patch(circle)
    ax.scatter(cx, cy, s=50, c=WHITE, alpha=0.8)

    return fig, ax


def gen_xenoarch(seed, accent=YELLOW):
    """Xenoarchaeology."""
    fig, ax = setup_axes()
    add_stars(ax, 40, seed)

    # Ancient ruins/artifact
    cx, cy = 500, 60

    # Mysterious structure
    pts = [[cx-60, 30], [cx-40, 90], [cx, 110], [cx+40, 90], [cx+60, 30]]
    structure = Polygon(pts, facecolor=DARK_GRAY, edgecolor=accent, linewidth=2, alpha=0.6)
    ax.add_patch(structure)

    # Glowing elements
    ax.scatter(cx, 70, s=100, c=accent, alpha=0.5)
    ax.scatter(cx, 70, s=40, c=WHITE, alpha=0.8)

    # Survey ship nearby
    draw_ship(ax, 200, 100, 15, angle=-20, color=CYAN, style='cruiser')

    # Mystery symbols
    for sx in [cx-30, cx, cx+30]:
        ax.scatter(sx, 50, s=15, c=accent, alpha=0.6)

    return fig, ax


def gen_mechanics(seed, accent=CYAN):
    """Game mechanics - formulas."""
    fig, ax = setup_axes()

    # Formula boxes connected
    boxes = [(150, 75), (400, 75), (650, 75), (900, 75)]
    for i, (bx, by) in enumerate(boxes):
        ax.add_patch(FancyBboxPatch((bx-60, by-30), 120, 60,
                                    boxstyle="round,pad=0.02", facecolor=DARK_GRAY,
                                    edgecolor=accent, linewidth=1.5, alpha=0.7))
        # Pseudo-formula lines
        for j in range(3):
            ax.plot([bx-40, bx+40], [by+15-j*12, by+15-j*12], color=accent, linewidth=1, alpha=0.4)

    # Connecting arrows
    for i in range(len(boxes)-1):
        ax.annotate('', xy=(boxes[i+1][0]-70, boxes[i+1][1]),
                   xytext=(boxes[i][0]+70, boxes[i][1]),
                   arrowprops=dict(arrowstyle='->', color=accent, lw=1.5, alpha=0.5))

    return fig, ax


def gen_time(seed, accent=CYAN):
    """Time increments."""
    fig, ax = setup_axes()

    # Timeline
    ax.plot([100, 900], [75, 75], color=GRAY, linewidth=2, alpha=0.5)

    # Time markers
    markers = [(150, '5s'), (300, '30s'), (450, '5m'), (600, '1h'), (750, '1d'), (900, '30d')]
    for mx, label in markers:
        ax.plot([mx, mx], [65, 85], color=accent, linewidth=2, alpha=0.7)
        ax.scatter(mx, 75, s=50, c=accent, alpha=0.6)

    # Current position indicator
    ax.scatter(450, 75, s=100, c=YELLOW, alpha=0.8)
    ax.annotate('', xy=(470, 75), xytext=(450, 95),
               arrowprops=dict(arrowstyle='->', color=YELLOW, lw=2))

    return fig, ax


def gen_spoilers(seed, accent=RED):
    """Spoiler races - mysterious threats."""
    fig, ax = setup_axes()
    add_stars(ax, 50, seed)

    # Ominous shapes
    for i in range(3):
        x = 300 + i * 200
        # Shadow/silhouette
        pts = np.array([[0, 0], [-30, -20], [-20, -40], [20, -40], [30, -20]]) + [x, 80]
        shadow = Polygon(pts, facecolor=accent, alpha=0.3 + i*0.1, edgecolor=accent, linewidth=1)
        ax.add_patch(shadow)
        # Glowing eyes
        ax.scatter(x-8, 65, s=15, c=WHITE, alpha=0.8)
        ax.scatter(x+8, 65, s=15, c=WHITE, alpha=0.8)

    # Warning indicators
    for wx in [100, 900]:
        ax.scatter(wx, 75, s=80, c=YELLOW, marker='^', alpha=0.6)

    return fig, ax


def gen_late_game(seed, accent=YELLOW):
    """Late game strategy - large fleet."""
    fig, ax = setup_axes()
    add_stars(ax, 40, seed)

    # Large fleet formation
    positions = [(100, 75), (150, 55), (150, 95), (200, 40), (200, 75), (200, 110),
                 (250, 55), (250, 95), (300, 75)]
    for i, (px, py) in enumerate(positions):
        style = 'cruiser' if i == 0 else 'fighter'
        size = 20 if i == 0 else 12
        draw_ship(ax, px, py, size, angle=0, color=CYAN, style=style)

    # Target system
    ax.scatter(800, 75, s=150, c=RED, alpha=0.5)
    draw_planet(ax, 800, 75, 25, RED)

    # Movement arrow
    ax.annotate('', xy=(700, 75), xytext=(350, 75),
               arrowprops=dict(arrowstyle='->', color=accent, lw=2, alpha=0.5))

    return fig, ax


def gen_spacemaster(seed, accent=CYAN):
    """SpaceMaster mode - god view."""
    fig, ax = setup_axes()
    add_stars(ax, 60, seed)

    # Overview grid
    for x in range(100, 900, 100):
        ax.axvline(x, color=accent, linewidth=0.5, alpha=0.2)
    for y in range(25, 150, 25):
        ax.axhline(y, color=accent, linewidth=0.5, alpha=0.2)

    # Multiple systems visible
    systems = [(200, 50), (400, 100), (600, 60), (800, 90)]
    for sx, sy in systems:
        ax.scatter(sx, sy, s=80, c=YELLOW, alpha=0.5)
        # Planets around each
        for angle in [0, 120, 240]:
            px = sx + 30 * np.cos(np.radians(angle))
            py = sy + 15 * np.sin(np.radians(angle))
            ax.scatter(px, py, s=15, c=CYAN, alpha=0.5)

    # Control panel overlay
    ax.add_patch(Rectangle((50, 110), 150, 30, facecolor=DARK_GRAY, alpha=0.7, edgecolor=accent))

    return fig, ax


# ============================================================================
# SECTION MAPPING - Now with representational generators
# ============================================================================

SECTION_GENERATORS = {
    # Chapter 1: Introduction
    '1.1': ('intro_aurora', CYAN),
    '1.2': ('installation', CYAN),
    '1.3': ('main_window', CYAN),

    # Chapter 2: Game Setup
    '2.1': ('main_window', GREEN),
    '2.2': ('aliens', CYAN),
    '2.3': ('star_system', YELLOW),
    '2.4': ('skills', GREEN),
    '2.5': ('colony_establish', CYAN),

    # Chapter 3: User Interface
    '3.1': ('main_window', CYAN),
    '3.2': ('system_map', CYAN),
    '3.3': ('installation', GREEN),
    '3.4': ('main_window', YELLOW),
    '3.5': ('galactic_map', CYAN),

    # Chapter 4: Systems and Bodies
    '4.1': ('star_system', YELLOW),
    '4.2': ('planets', CYAN),
    '4.3': ('asteroids', GRAY),
    '4.4': ('jump_point', CYAN),

    # Chapter 5: Colonies
    '5.1': ('colony_establish', CYAN),
    '5.2': ('population', GREEN),
    '5.3': ('environment', GREEN),
    '5.4': ('infrastructure', CYAN),
    '5.5': ('terraforming', GREEN),

    # Chapter 6: Economy
    '6.1': ('minerals', CYAN),
    '6.2': ('mining', YELLOW),
    '6.3': ('construction', CYAN),
    '6.4': ('trade', YELLOW),
    '6.5': ('civilian', GREEN),

    # Chapter 7: Research
    '7.1': ('tech_tree', CYAN),
    '7.2': ('scientists', GREEN),
    '7.3': ('research_lab', CYAN),
    '7.4': ('tech_tree', YELLOW),

    # Chapter 8: Ship Design
    '8.1': ('ship_blueprint', CYAN),
    '8.2': ('armor', GRAY),
    '8.3': ('engines', YELLOW),
    '8.4': ('sensors', CYAN),
    '8.5': ('weapons', RED),
    '8.6': ('ship_blueprint', GREEN),
    '8.7': ('ship_blueprint', CYAN),

    # Chapter 9: Fleet Management
    '9.1': ('maintenance', CYAN),
    '9.2': ('construction', GREEN),
    '9.3': ('galactic_map', CYAN),
    '9.4': ('galactic_map', YELLOW),
    '9.5': ('main_window', CYAN),
    '9.6': ('galactic_map', CYAN),

    # Chapter 10: Navigation
    '10.1': ('engines', CYAN),
    '10.2': ('jump_point', CYAN),
    '10.3': ('geological_survey', GREEN),
    '10.4': ('galactic_map', YELLOW),

    # Chapter 11: Sensors
    '11.0': ('sensors', CYAN),
    '11.1': ('sensors', RED),
    '11.2': ('sensors', GREEN),
    '11.3': ('sensors', YELLOW),
    '11.4': ('intelligence', GRAY),

    # Chapter 12: Combat
    '12.0': ('weapons', RED),
    '12.1': ('fire_control', CYAN),
    '12.2': ('weapons', CYAN),
    '12.3': ('missiles', RED),
    '12.4': ('point_defense', GREEN),
    '12.5': ('electronic_warfare', CYAN),
    '12.6': ('damage', RED),
    '12.7': ('pdc', RED),

    # Chapter 13: Ground Forces
    '13.1': ('ground_units', CYAN),
    '13.2': ('training', GREEN),
    '13.3': ('ground_combat', RED),

    # Chapter 14: Logistics
    '14.1': ('fuel', YELLOW),
    '14.2': ('maintenance', CYAN),
    '14.3': ('supply', GREEN),
    '14.4': ('orbital_habitat', CYAN),

    # Chapter 15: Diplomacy
    '15.1': ('aliens', RED),
    '15.2': ('communications', CYAN),
    '15.3': ('treaties', GREEN),
    '15.4': ('diplomacy', YELLOW),
    '15.5': ('intelligence', GRAY),

    # Chapter 16: Commanders
    '16.1': ('officers', CYAN),
    '16.2': ('skills', YELLOW),
    '16.3': ('assignments', GREEN),

    # Chapter 17: Exploration
    '17.1': ('geological_survey', GREEN),
    '17.2': ('gravitational_survey', CYAN),
    '17.3': ('xenoarch', YELLOW),

    # Chapter 18: Advanced
    '18.1': ('mechanics', CYAN),
    '18.2': ('time', CYAN),
    '18.3': ('spoilers', RED),
    '18.4': ('late_game', YELLOW),
    '18.5': ('spacemaster', CYAN),
}

GENERATORS = {
    'intro_aurora': gen_intro_aurora,
    'installation': gen_installation,
    'main_window': gen_main_window,
    'system_map': gen_system_map,
    'galactic_map': gen_galactic_map,
    'star_system': gen_star_system,
    'planets': gen_planets,
    'asteroids': gen_asteroids,
    'jump_point': gen_jump_point,
    'colony_establish': gen_colony_establish,
    'population': gen_population,
    'environment': gen_environment,
    'infrastructure': gen_infrastructure,
    'terraforming': gen_terraforming,
    'minerals': gen_minerals,
    'mining': gen_mining,
    'construction': gen_construction,
    'trade': gen_trade,
    'civilian': gen_civilian,
    'tech_tree': gen_tech_tree,
    'scientists': gen_scientists,
    'research_lab': gen_research_lab,
    'ship_blueprint': gen_ship_blueprint,
    'armor': gen_armor,
    'engines': gen_engines,
    'sensors': gen_sensors,
    'weapons': gen_weapons,
    'fire_control': gen_fire_control,
    'missiles': gen_missiles,
    'point_defense': gen_point_defense,
    'electronic_warfare': gen_electronic_warfare,
    'damage': gen_damage,
    'pdc': gen_pdc,
    'ground_units': gen_ground_units,
    'training': gen_training,
    'ground_combat': gen_ground_combat,
    'fuel': gen_fuel,
    'maintenance': gen_maintenance,
    'supply': gen_supply,
    'orbital_habitat': gen_orbital_habitat,
    'aliens': gen_aliens,
    'communications': gen_communications,
    'treaties': gen_treaties,
    'diplomacy': gen_diplomacy,
    'intelligence': gen_intelligence,
    'officers': gen_officers,
    'skills': gen_skills,
    'assignments': gen_assignments,
    'geological_survey': gen_geological_survey,
    'gravitational_survey': gen_gravitational_survey,
    'xenoarch': gen_xenoarch,
    'mechanics': gen_mechanics,
    'time': gen_time,
    'spoilers': gen_spoilers,
    'late_game': gen_late_game,
    'spacemaster': gen_spacemaster,
}


def generate_section_art(section_id, output_dir='images/art/section-art'):
    """Generate art for a specific section."""
    if section_id not in SECTION_GENERATORS:
        print(f"  Warning: No generator defined for section {section_id}")
        return None

    gen_name, accent = SECTION_GENERATORS[section_id]
    gen_func = GENERATORS[gen_name]

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
        sections = sys.argv[1:]
    else:
        sections = list(SECTION_GENERATORS.keys())

    for section_id in sections:
        try:
            generate_section_art(section_id)
        except Exception as e:
            print(f"  Error generating {section_id}: {e}")


if __name__ == '__main__':
    main()
