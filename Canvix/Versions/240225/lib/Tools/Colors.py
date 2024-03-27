"""
script for storing color values
"""
import random

def random_color():
    """
    Generate a random color represented as an RGB tuple.
    """
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return [red, green, blue]

# color values
color_dict = {
    "Red": [255, 0, 0],
    "Green": [0, 255, 0],
    "Blue": [0, 0, 255],
}

colors = list(color_dict.keys())