#!/usr/bin/env python3
"""Generate geometric ship silhouettes."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle, FancyBboxPatch
from matplotlib.collections import PatchCollection

# Dark theme colors
BG_COLOR = '#1a1a2e'
CYAN = '#4ecdc4'
YELLOW = '#ffe66d'
RED = '#ff6b6b'
GREEN = '#95d5b2'
WHITE = '#ffffff'
GRAY = '#888888'
DARK_GRAY = '#2d2d44'

def generate_ship_silhouette(ship_type='cruiser', size=100, color=CYAN):
    """Generate a geometric ship silhouette.

    Ship types: fighter, corvette, frigate, destroyer, cruiser, battleship, carrier, freighter
    """
    patches = []

    if ship_type == 'fighter':
        # Small, angular, fast
        hull = Polygon([
            (0.5, 0), (0.15, 0.3), (0, 0.25), (0, -0.25), (0.15, -0.3), (0.5, 0)
        ], closed=True)
        patches.append(hull)
        # Wings
        wing1 = Polygon([(0.1, 0.2), (0.3, 0.5), (0.35, 0.45), (0.2, 0.15)])
        wing2 = Polygon([(0.1, -0.2), (0.3, -0.5), (0.35, -0.45), (0.2, -0.15)])
        patches.extend([wing1, wing2])

    elif ship_type == 'corvette':
        # Compact, versatile
        hull = Polygon([
            (0.6, 0), (0.4, 0.15), (0.1, 0.18), (-0.1, 0.12), (-0.1, -0.12), (0.1, -0.18), (0.4, -0.15)
        ], closed=True)
        patches.append(hull)
        # Engine pods
        pod1 = Polygon([(-0.15, 0.1), (-0.25, 0.15), (-0.25, 0.05), (-0.15, 0.05)])
        pod2 = Polygon([(-0.15, -0.1), (-0.25, -0.15), (-0.25, -0.05), (-0.15, -0.05)])
        patches.extend([pod1, pod2])

    elif ship_type == 'frigate':
        # Balanced, medium
        hull = Polygon([
            (0.7, 0), (0.5, 0.12), (0.2, 0.15), (-0.1, 0.15), (-0.2, 0.1), (-0.2, -0.1), (-0.1, -0.15), (0.2, -0.15), (0.5, -0.12)
        ], closed=True)
        patches.append(hull)
        # Weapon mounts
        mount1 = Polygon([(0.3, 0.15), (0.35, 0.22), (0.4, 0.22), (0.4, 0.15)])
        mount2 = Polygon([(0.3, -0.15), (0.35, -0.22), (0.4, -0.22), (0.4, -0.15)])
        patches.extend([mount1, mount2])

    elif ship_type == 'destroyer':
        # Aggressive, weapons-focused
        hull = Polygon([
            (0.8, 0), (0.6, 0.1), (0.3, 0.14), (0, 0.16), (-0.2, 0.12), (-0.25, 0), (-0.2, -0.12), (0, -0.16), (0.3, -0.14), (0.6, -0.1)
        ], closed=True)
        patches.append(hull)
        # Spinal mount
        spine = Polygon([(0.8, 0.02), (0.3, 0.04), (0.3, -0.04), (0.8, -0.02)])
        patches.append(spine)

    elif ship_type == 'cruiser':
        # Heavy, armored
        hull = Polygon([
            (0.9, 0), (0.7, 0.15), (0.3, 0.2), (-0.1, 0.2), (-0.3, 0.15), (-0.35, 0), (-0.3, -0.15), (-0.1, -0.2), (0.3, -0.2), (0.7, -0.15)
        ], closed=True)
        patches.append(hull)
        # Broadside turrets
        for y in [0.22, -0.22]:
            for x in [0.1, 0.3, 0.5]:
                turret = Circle((x, y * (1 if y > 0 else 1)), 0.04)
                patches.append(turret)

    elif ship_type == 'battleship':
        # Massive, imposing
        hull = Polygon([
            (1.0, 0), (0.8, 0.18), (0.4, 0.25), (0, 0.25), (-0.3, 0.2), (-0.4, 0.1), (-0.4, -0.1), (-0.3, -0.2), (0, -0.25), (0.4, -0.25), (0.8, -0.18)
        ], closed=True)
        patches.append(hull)
        # Command tower
        tower = Polygon([(0.2, 0.25), (0.15, 0.35), (0.3, 0.35), (0.35, 0.25)])
        patches.append(tower)
        # Heavy turrets
        for x in [0.5, 0.7]:
            turret = Circle((x, 0), 0.06)
            patches.append(turret)

    elif ship_type == 'carrier':
        # Long, flat deck
        hull = Polygon([
            (1.1, 0.05), (0.9, 0.12), (0.3, 0.15), (-0.3, 0.15), (-0.4, 0.1), (-0.4, -0.15), (-0.3, -0.2), (0.3, -0.2), (0.9, -0.15), (1.1, -0.05)
        ], closed=True)
        patches.append(hull)
        # Flight deck markings
        deck = Polygon([(0.8, 0.1), (-0.2, 0.1), (-0.2, 0.05), (0.8, 0.05)])
        patches.append(deck)

    elif ship_type == 'freighter':
        # Bulky, cargo-focused
        hull = Polygon([
            (0.7, 0), (0.5, 0.2), (0.2, 0.3), (-0.3, 0.3), (-0.5, 0.2), (-0.5, -0.2), (-0.3, -0.3), (0.2, -0.3), (0.5, -0.2)
        ], closed=True)
        patches.append(hull)
        # Cargo pods
        pod1 = Polygon([(-0.1, 0.32), (-0.1, 0.4), (0.1, 0.4), (0.1, 0.32)])
        pod2 = Polygon([(-0.1, -0.32), (-0.1, -0.4), (0.1, -0.4), (0.1, -0.32)])
        patches.extend([pod1, pod2])

    return patches


def render_ship_set(output_path, ships=None):
    """Render a set of ship silhouettes."""
    if ships is None:
        ships = ['fighter', 'corvette', 'frigate', 'destroyer', 'cruiser', 'battleship', 'carrier', 'freighter']

    colors = [CYAN, GREEN, WHITE, YELLOW, CYAN, RED, GREEN, GRAY]

    fig, axes = plt.subplots(2, 4, figsize=(16, 6), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)

    for ax, ship_type, color in zip(axes.flat, ships, colors):
        ax.set_facecolor(BG_COLOR)
        ax.set_xlim(-0.7, 1.3)
        ax.set_ylim(-0.6, 0.6)
        ax.set_aspect('equal')
        ax.axis('off')

        patches = generate_ship_silhouette(ship_type, color=color)

        for patch in patches:
            patch.set_facecolor(color)
            patch.set_edgecolor(WHITE)
            patch.set_linewidth(0.5)
            patch.set_alpha(0.8)
            ax.add_patch(patch)

        # Glow effect
        for patch in generate_ship_silhouette(ship_type):
            patch.set_facecolor(color)
            patch.set_edgecolor('none')
            patch.set_alpha(0.15)
            patch.set_transform(ax.transData)
            # Slight offset for glow
            ax.add_patch(patch)

        # Label
        ax.text(0.3, -0.5, ship_type.upper(), fontsize=10, color=WHITE,
                ha='center', va='top', fontfamily='sans-serif', alpha=0.7)

    plt.tight_layout(pad=1)
    fig.savefig(
        output_path,
        facecolor=BG_COLOR,
        edgecolor='none',
        bbox_inches='tight',
        dpi=150
    )
    plt.close()


def render_single_ship(output_path, ship_type, color=CYAN, size=(200, 150)):
    """Render a single ship silhouette."""
    fig, ax = plt.subplots(figsize=(size[0]/100, size[1]/100), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)
    ax.set_xlim(-0.7, 1.3)
    ax.set_ylim(-0.6, 0.6)
    ax.set_aspect('equal')
    ax.axis('off')

    patches = generate_ship_silhouette(ship_type, color=color)

    for patch in patches:
        patch.set_facecolor(color)
        patch.set_edgecolor(WHITE)
        patch.set_linewidth(0.8)
        patch.set_alpha(0.85)
        ax.add_patch(patch)

    plt.tight_layout(pad=0)
    fig.savefig(
        output_path,
        facecolor=BG_COLOR,
        edgecolor='none',
        bbox_inches='tight',
        pad_inches=0.1,
        dpi=150
    )
    plt.close()


def main():
    # Full ship set
    render_ship_set('images/art/silhouettes/ship-silhouettes-set.png')
    print("Generated: images/art/silhouettes/ship-silhouettes-set.png")

    # Individual ships
    ships = ['fighter', 'corvette', 'frigate', 'destroyer', 'cruiser', 'battleship', 'carrier', 'freighter']
    colors = [CYAN, GREEN, WHITE, YELLOW, CYAN, RED, GREEN, GRAY]

    for ship, color in zip(ships, colors):
        render_single_ship(f'images/art/silhouettes/{ship}.png', ship, color)
        print(f"Generated: images/art/silhouettes/{ship}.png")


if __name__ == '__main__':
    main()
