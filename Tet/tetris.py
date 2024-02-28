import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Shapes
shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3],
     [3, 3]],

    [[4, 4, 0],
     [0, 4, 4]],

    [[0, 5, 0, 0],
     [0, 5, 0, 0],
     [0, 5, 0, 0],
     [0, 5, 0, 0]],

    [[6, 0, 0],
     [6, 6, 6]],

    [[0, 0, 7],
     [7, 7, 7]]
]

# Tetris class
class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_piece = self.new_piece()
        self.game_over = False

    def new_piece(self):
        piece = random.choice(shapes)
        x = (len(self.grid[0]) - len(piece[0])) // 2
        y = 0
        return {'piece': piece, 'x': x, 'y': y}

    def draw_grid(self):
        for y, row in enumerate(self.grid):
            for x, color in enumerate(row):
                if color:
                    pygame.draw.rect(self.screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(self.screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def draw_piece(self, piece):
        shape = piece['piece']
        x, y = piece['x'], piece['y']
        for row_index, row in enumerate(shape):
            for col_index, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, COLORS[cell], ((x + col_index) * BLOCK_SIZE, (y + row_index) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, GRAY, ((x + col_index) * BLOCK_SIZE, (y + row_index) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def check_collision(self, piece, offset):
        shape = piece['piece']
        x, y = piece['x'] + offset[0], piece['y'] + offset[1]
        for row_index, row in enumerate(shape):
            for col_index, cell in enumerate(row):
                if cell and (x + col_index < 0 or x + col_index >= len(self.grid[0]) or y + row_index >= len(self.grid) or self.grid[y + row_index][x + col_index]):
                    return True
        return False

    def merge_piece(self, piece):
        shape = piece['piece']
        x, y = piece['x'], piece['y']
        for row_index, row in enumerate(shape):
            for col_index, cell in enumerate(row):
                if cell:
                    self.grid[y + row_index][x + col_index] = cell

    def clear_lines(self):
        lines_cleared = 0
        for i, row in enumerate(self.grid):
            if all(row):
                del self.grid[i]
                self.grid.insert(0, [0] * (SCREEN_WIDTH // BLOCK_SIZE))
                lines_cleared += 1
        return lines_cleared

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def run(self):
        while not self.game_over:
            self.screen.fill(WHITE)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if not self.check_collision(self.current_piece, (-1, 0)):
                            self.current_piece['x'] -= 1
                    elif event.key == pygame.K_RIGHT:
                        if not self.check_collision(self.current_piece, (1, 0)):
                            self.current_piece['x'] += 1
                    elif event.key == pygame.K_DOWN:
                        if not self.check_collision(self.current_piece, (0, 1)):
                            self.current_piece['y'] += 1
                    elif event.key == pygame.K_SPACE:
                        while not self.check_collision(self.current_piece, (0, 1)):
                            self.current_piece['y'] += 1

            # Move piece down automatically
            if not self.check_collision(self.current_piece, (0, 1)):
                self.current_piece['y'] += 1
            else:
                self.merge_piece(self.current_piece)
                lines_cleared = self.clear_lines()
                if lines_cleared:
                    print("Lines cleared:", lines_cleared)
                self.current_piece = self.new_piece()
                if self.check_collision(self.current_piece, (0, 0)):
                    self.game_over = True

            # Draw everything
            self.draw_grid()
            self.draw_piece(self.current_piece)
            if self.game_over:
                self.draw_text("Game Over", 36, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()

# Colors
COLORS = [BLACK, RED, BLUE, GREEN, (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Run the game
if __name__ == "__main__":
    Tetris().run()
