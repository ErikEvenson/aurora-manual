#!/usr/bin/env python3
"""Generate orbital mechanics section dividers."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, FancyArrowPatch
from matplotlib.lines import Line2D

# Dark theme colors
BG_COLOR = '#1a1a2e'
CYAN = '#4ecdc4'
YELLOW = '#ffe66d'
RED = '#ff6b6b'
GREEN = '#95d5b2'
WHITE = '#ffffff'
GRAY = '#888888'

def draw_orbit(ax, a, e, angle=0, color=CYAN, alpha=0.6, linewidth=1.5):
    """Draw an elliptical orbit.

    a: semi-major axis
    e: eccentricity
    angle: rotation angle in degrees
    """
    b = a * np.sqrt(1 - e**2)  # semi-minor axis
    c = a * e  # focus distance

    # Create ellipse centered at focus (star position)
    ellipse = Ellipse(
        (c, 0),  # offset so star is at focus
        width=2*a,
        height=2*b,
        angle=angle,
        facecolor='none',
        edgecolor=color,
        alpha=alpha,
        linewidth=linewidth,
        linestyle='-'
    )
    ax.add_patch(ellipse)
    return ellipse


def generate_orbital_divider(
    width=1200,
    height=100,
    num_orbits=5,
    seed=None,
    style='centered'
):
    """Generate an orbital mechanics divider."""
    if seed is not None:
        np.random.seed(seed)

    fig, ax = plt.subplots(figsize=(width/100, height/100), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')
    ax.set_aspect('equal')

    center_x = width / 2
    center_y = height / 2

    if style == 'centered':
        # Central star
        ax.scatter(center_x, center_y, s=80, c=YELLOW, alpha=0.9, edgecolors='none', zorder=10)
        ax.scatter(center_x, center_y, s=200, c=YELLOW, alpha=0.2, edgecolors='none', zorder=9)

        # Concentric orbits
        colors = [CYAN, GREEN, WHITE, YELLOW, RED]
        for i in range(num_orbits):
            a = 30 + i * 25  # increasing semi-major axis
            e = np.random.uniform(0.1, 0.4)  # eccentricity
            angle = np.random.uniform(-15, 15)  # slight tilt
            color = colors[i % len(colors)]
            alpha = 0.7 - i * 0.1

            draw_orbit(ax, a, e, angle, color=color, alpha=alpha, linewidth=1.2)

            # Add planet on orbit
            theta = np.random.uniform(0, 2*np.pi)
            b = a * np.sqrt(1 - e**2)
            px = center_x + a * np.cos(theta) * np.cos(np.radians(angle)) - b * np.sin(theta) * np.sin(np.radians(angle))
            py = center_y + a * np.cos(theta) * np.sin(np.radians(angle)) + b * np.sin(theta) * np.cos(np.radians(angle))

            planet_size = np.random.uniform(8, 20)
            ax.scatter(px, py, s=planet_size, c=color, alpha=0.8, edgecolors='none', zorder=11)

        # Transform to center
        ax.set_xlim(center_x - width/2, center_x + width/2)
        ax.set_ylim(center_y - height/2, center_y + height/2)

    elif style == 'horizontal':
        # Stretched ellipses as horizontal divider
        y_center = height / 2

        for i in range(3):
            y_offset = (i - 1) * 15

            # Draw dashed orbital path
            x_points = np.linspace(50, width-50, 200)
            y_points = y_center + y_offset + 8 * np.sin(x_points * np.pi / 300)

            color = [CYAN, WHITE, GREEN][i]
            alpha = [0.6, 0.4, 0.5][i]

            ax.plot(x_points, y_points, color=color, alpha=alpha, linewidth=1.5, linestyle='-')

            # Add small bodies along path
            for j in range(5):
                idx = int(len(x_points) * (j + 0.5) / 5)
                ax.scatter(x_points[idx], y_points[idx], s=10, c=color, alpha=0.8)

    plt.tight_layout(pad=0)
    return fig, ax


def main():
    # Centered orbital system
    fig, ax = generate_orbital_divider(seed=42, style='centered')
    fig.savefig(
        'images/art/dividers/orbital-centered.png',
        facecolor=BG_COLOR,
        edgecolor='none',
        bbox_inches='tight',
        pad_inches=0,
        dpi=150
    )
    plt.close()
    print("Generated: images/art/dividers/orbital-centered.png")

    # Horizontal wave divider
    fig, ax = generate_orbital_divider(seed=42, style='horizontal')
    fig.savefig(
        'images/art/dividers/orbital-horizontal.png',
        facecolor=BG_COLOR,
        edgecolor='none',
        bbox_inches='tight',
        pad_inches=0,
        dpi=150
    )
    plt.close()
    print("Generated: images/art/dividers/orbital-horizontal.png")


if __name__ == '__main__':
    main()
