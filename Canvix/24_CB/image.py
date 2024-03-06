"""
sending image to matrix
"""

import pixel_frame

# ------------------------------------------------------
# sending image to matrix
def matrix_input(matrix, show=True):
    for pixel in matrix:
        x, y, color = pixel[0][0], pixel[0][1], pixel[1]
        pixel_frame.pixel(x, y, color)
    if show:
        pixel_frame.display()
# ------------------------------------------------------
