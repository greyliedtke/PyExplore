"""
script for making calling predefined colors easy

"""
import random

# ------------------------------------------------------
# Generate random color
def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return [red, green, blue]
# ------------------------------------------------------

# ------------------------------------------------------
# Scaling colors based on brightness
def scale_color(rgb_color, brightness):
    new_c = [int(rgb_color*brightness) for c in rgb_color]
    return new_c
# ------------------------------------------------------

# ------------------------------------------------------
# Color variables
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
sky_blue = [135, 206, 235]
mint_green = [152, 255, 100]
lavender = [230, 230, 250]
peach = [255, 218, 185]
goldenrod = [218, 165, 32]
nice_pink = [255, 192, 203]
silver = [192, 192, 192]
grey = [128, 128, 128]
off = [0, 0, 0]
yellow = [255, 200, 100]

# ------------------------------------------------------