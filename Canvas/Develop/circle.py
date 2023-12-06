"""
script to create hombre from one color to another as circle function
"""


import matplotlib.pyplot as plt
import numpy as np


# ------------------------------------------------------
# Creating rings
center = [8, 8]


# ------------------------------------------------------
# Define the starting and ending colors in RGB format (0-255 range)
start_color = (255, 17, 23)  # Red
end_color = (156, 247, 255)    # Blue
# ------------------------------------------------------

# ------------------------------------------------------
# comment
# ------------------------------------------------------

# Define the number of steps in the gradient
num_lights = 256
num_rings = 8

# Create an array of colors transitioning from start_color to end_color
colors = []

for i in range(num_rings):
    # Interpolate between start_color and end_color
    r = start_color[0] + int((end_color[0] - start_color[0]) * (i / num_rings))
    g = start_color[1] + int((end_color[1] - start_color[1]) * (i / num_rings))
    b = start_color[2] + int((end_color[2] - start_color[2]) * (i / num_rings))
    
    # Append the RGB tuple to the colors list
    colors.append((r, g, b))

# Create a color map with the defined gradient
cmap = plt.cm.colors.ListedColormap(colors)

# Create a sample image with the gradient as a 16x16 matrix
image = np.linspace(0, 1, 16 * 16).reshape(16, 16)
plt.imshow(image, cmap=cmap, aspect='auto')
plt.axis('off')

# Show the gradient as a 16x16 matrix
plt.show()