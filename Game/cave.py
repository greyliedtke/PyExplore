import pygame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame with Matplotlib")

# Create a Matplotlib figure
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 5, 20, 15])

# Create a Matplotlib canvas
canvas = FigureCanvasAgg(fig)
canvas.draw()

# Convert the Matplotlib canvas to a Pygame surface
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()
size = canvas.get_width_height()
surf = pygame.image.fromstring(raw_data, size, "RGB")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Blit the Matplotlib surface onto the Pygame screen
    screen.blit(surf, (0, 0))

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
