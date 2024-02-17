"""
script to create hombre from one color to another
"""


import matplotlib.pyplot as plt
import numpy as np

# Define the starting and ending colors in RGB format (0-255 range)
start_color = (255, 17, 23)  # Red
end_color = (156, 247, 255)    # Blue

# Define the number of steps in the gradient
num_steps = 256

# Create an array of colors transitioning from start_color to end_color
colors = []

for i in range(num_steps):
    # Interpolate between start_color and end_color
    r = start_color[0] + int((end_color[0] - start_color[0]) * (i / num_steps))
    g = start_color[1] + int((end_color[1] - start_color[1]) * (i / num_steps))
    b = start_color[2] + int((end_color[2] - start_color[2]) * (i / num_steps))
    
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