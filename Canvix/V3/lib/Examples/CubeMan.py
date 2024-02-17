"""
Main Cave logic
"""

# pygame tunnel run
import time
import lib.Tools.Matrix as mat
import time
import math

# Define LED matrix dimensions
rows = 16
cols = 16

# Function to rotate a point (x, y, z) around the origin
def rotate_point(x, y, z, angle):
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    new_x = x * cos_a + y * sin_a
    new_y = x * sin_a - y * cos_a
    return new_x, new_y, z


# Function to project 3D point (x, y, z) onto 2D plane
def project_point(x, y, z):
    scale_factor = 3  # Adjust this for the cube size
    return int(x * scale_factor + cols / 2), int(y * scale_factor + rows / 2)


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
