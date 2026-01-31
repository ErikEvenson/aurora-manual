#!/usr/bin/env python3
"""Generate procedural star field chapter headers."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse
import matplotlib.colors as mcolors

# Dark theme colors
BG_COLOR = '#1a1a2e'
CYAN = '#4ecdc4'
YELLOW = '#ffe66d'
RED = '#ff6b6b'
GREEN = '#95d5b2'
WHITE = '#ffffff'

def generate_starfield(
    width=1200,
    height=300,
    num_stars=800,
    num_bright=50,
    num_nebula_points=15,
    seed=None,
    title=None,
    accent_color=CYAN
):
    """Generate a procedural star field with nebula hints."""
    if seed is not None:
        np.random.seed(seed)

    fig, ax = plt.subplots(figsize=(width/100, height/100), dpi=100)
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    # Remove axes
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')
    ax.set_aspect('equal')

    # Generate nebula background (subtle color clouds)
    for _ in range(num_nebula_points):
        x = np.random.uniform(0, width)
        y = np.random.uniform(0, height)
        size = np.random.uniform(50, 150)
        alpha = np.random.uniform(0.02, 0.08)
        color = np.random.choice([accent_color, '#2d2d44', '#3d3d5c'])

        nebula = Ellipse(
            (x, y),
            width=size * np.random.uniform(1, 2),
            height=size * np.random.uniform(1, 2),
            angle=np.random.uniform(0, 360),
            facecolor=color,
            alpha=alpha,
            edgecolor='none'
        )
        ax.add_patch(nebula)

    # Dim background stars
    x_dim = np.random.uniform(0, width, num_stars)
    y_dim = np.random.uniform(0, height, num_stars)
    sizes_dim = np.random.uniform(0.1, 1.5, num_stars)
    alphas_dim = np.random.uniform(0.2, 0.6, num_stars)

    for x, y, s, a in zip(x_dim, y_dim, sizes_dim, alphas_dim):
        ax.scatter(x, y, s=s, c=WHITE, alpha=a, edgecolors='none')

    # Bright stars with color variation
    x_bright = np.random.uniform(0, width, num_bright)
    y_bright = np.random.uniform(0, height, num_bright)
    sizes_bright = np.random.uniform(3, 12, num_bright)

    star_colors = [WHITE, CYAN, YELLOW, '#aaaaff', '#ffaaaa']

    for x, y, s in zip(x_bright, y_bright, sizes_bright):
        color = np.random.choice(star_colors, p=[0.5, 0.2, 0.15, 0.1, 0.05])
        # Glow effect
        ax.scatter(x, y, s=s*4, c=color, alpha=0.1, edgecolors='none')
        ax.scatter(x, y, s=s*2, c=color, alpha=0.2, edgecolors='none')
        ax.scatter(x, y, s=s, c=color, alpha=0.9, edgecolors='none')

    # Add title if provided
    if title:
        ax.text(
            width/2, height/2,
            title.upper(),
            fontsize=36,
            fontweight='bold',
            color=WHITE,
            alpha=0.9,
            ha='center',
            va='center',
            fontfamily='sans-serif'
        )

    # Subtle vignette effect (darker edges)
    gradient = np.linspace(0, 1, 100)
    for i, g in enumerate(gradient[:30]):
        alpha = 0.3 * (1 - g/0.3)
        ax.axvline(i * width/100, color=BG_COLOR, alpha=alpha, linewidth=width/50)
        ax.axvline(width - i * width/100, color=BG_COLOR, alpha=alpha, linewidth=width/50)

    plt.tight_layout(pad=0)
    return fig, ax


def main():
    # Generate sample header
    fig, ax = generate_starfield(
        seed=42,
        title="Aurora",
        accent_color=CYAN
    )
    fig.savefig(
        'images/art/headers/starfield-sample.png',
        facecolor=BG_COLOR,
        edgecolor='none',
        bbox_inches='tight',
        pad_inches=0,
        dpi=150
    )
    plt.close()
    print("Generated: images/art/headers/starfield-sample.png")


if __name__ == '__main__':
    main()
