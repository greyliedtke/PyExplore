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
