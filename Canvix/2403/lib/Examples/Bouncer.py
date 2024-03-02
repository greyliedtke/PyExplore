"""
Main Cave logic
"""

# bouncing ball game
import time
import lib.Tools.Matrix as mat
from Tools.Hardware import encoder_left, encoder_right, led_strip


# Define LED matrix dimensions
rows = 16
cols = 16


class Scene:
    def __init__(self):
        self.rate = g.refr
        # Rotating cube animation
        self.angle = 0

    def loop(self):

        cube_points = [
            (-1, -1, -1),
            (-1, -1, 1),
            (-1, 1, -1),
            (-1, 1, 1),
            (1, -1, -1),
            (1, -1, 1),
            (1, 1, -1),
            (1, 1, 1),
        ]

        rotated_cube = [rotate_point(x, y, z, self.angle) for x, y, z in cube_points]
        projected_cube = [project_point(x, y, z) for x, y, z in rotated_cube]

        self.angle += 0.1  # Adjust the rotation speed
        sq2 = [[p[0], p[1] + 4] for p in projected_cube]
        projected_cube += sq2
        return projected_cube


cm = Scene()
