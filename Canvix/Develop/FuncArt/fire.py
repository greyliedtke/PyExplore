import pygame
import random

# Constants
WIDTH, HEIGHT = 200, 200
FIRE_WIDTH = 64
FIRE_HEIGHT = 64
FIRE_COLOR = [(255, 0, 0), (255, 69, 0), (255, 140, 0), (255, 215, 0), (255, 255, 0)]
FIRE_SPARKLE_PROBABILITY = 0.02
FIRE_SPARKLE_COLOR = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Fireplace")

# Generate fire pixels
fire_pixels = []
for y in range(FIRE_HEIGHT):
    fire_row = []
    for x in range(FIRE_WIDTH):
        fire_row.append(random.choice(FIRE_COLOR))
    fire_pixels.append(fire_row)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update fire pixels
    for y in range(1, FIRE_HEIGHT):
        for x in range(FIRE_WIDTH):
            # Calculate the average color of neighboring pixels
            neighbors = fire_pixels[y - 1][max(x - 1, 0):min(x + 2, FIRE_WIDTH)]
            color_sum = [sum(component) for component in zip(*neighbors)]
            color = tuple(component // len(neighbors) for component in color_sum)
            # Introduce randomness to simulate flickering
            color = [min(max(c + random.randint(-10, 10), 0), 255) for c in color]
            fire_pixels[y][x] = tuple(color)

            # Add occasional sparkles
            if random.random() < FIRE_SPARKLE_PROBABILITY:
                fire_pixels[y][x] = FIRE_SPARKLE_COLOR\
        

    # Draw fire pixels to screen
    for y in range(FIRE_HEIGHT):
        for x in range(FIRE_WIDTH):
            pygame.draw.rect(screen, fire_pixels[y][x], (x + 100, y + 100, 1, 1))

    pygame.display.flip()

    # Cap frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
