"""
script for storing color values
"""

import random


rgb_colors = {
    "light_yellow": (255, 200, 100),
    "Sky_Blue": (135, 206, 235),
    "Mint_Green": (152, 255, 100),
    "Lavender": (230, 230, 250),
    "Peach": (255, 218, 185),
    "Goldenrod": (218, 165, 32),
    "nice_pink": (255, 192, 203),
    "silver": (192, 192, 192),
    "grey": (128, 128, 128),
    "Red": (255, 0, 0),
    "off": (0, 0, 0)
}
colors = list(rgb_colors.keys())


def random_color():
    """
    Generate a random color represented as an RGB tuple.
    """
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return [red, green, blue]
