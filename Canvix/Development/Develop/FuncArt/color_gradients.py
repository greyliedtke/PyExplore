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

import matplotlib.pyplot as plt
import numpy as np

# Define the starting and ending colors in RGB format (0-255 range)
start_color = (255, 23, 23)  # Red
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
    colors.append((r / 255, g / 255, b / 255))

# Create a color map with the defined gradient
cmap = plt.cm.colors.ListedColormap(colors)

# Create a color bar for reference
norm = plt.cm.colors.Normalize(vmin=0, vmax=num_steps - 1)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

# Display the color bar
plt.colorbar(sm, label='Gradient (Start Color to End Color)')

# Create a sample image with the gradient
image = np.linspace(0, 1, 256).reshape(1, -1)
plt.imshow(image, cmap=cmap, aspect='auto')
plt.axis('off')

# Show the gradient
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define the size of the matrix
matrix_size = 16

# Create an empty matrix to hold RGB values
colors = np.zeros((matrix_size, matrix_size, 3))

# Define start and end colors
start_color = [255, 0, 0]  # Red
end_color = [0, 0, 255]     # Blue

# Generate gradual color change along the diagonal
for i in range(matrix_size):
    # Calculate interpolation factor
    t = i / (matrix_size - 1)
    
    # Interpolate between start and end colors
    interpolated_color = [int(start + (end - start) * t) for start, end in zip(start_color, end_color)]
    
    # Fill the diagonal with interpolated color
    colors[i, i, :] = interpolated_color

# Display the color matrix
plt.imshow(colors)
plt.axis('off')
plt.show()
