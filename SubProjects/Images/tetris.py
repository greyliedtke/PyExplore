import curses
import random

# Initialize the curses screen
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = stdscr.subwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Create the Tetris grid
grid = [[' ' for _ in range(sw)] for _ in range(sh)]

# Define Tetris shapes and their rotations
tetrominos = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]]
]

# Define colors for Tetris shapes
tetromino_colors = [curses.COLOR_WHITE, curses.COLOR_CYAN, curses.COLOR_BLUE, curses.COLOR_GREEN, curses.COLOR_RED]

# Define the starting position for the tetromino
current_tetromino = random.choice(tetrominos)
current_tetromino_color = random.randint(1, len(tetromino_colors))
tetromino_x = sw // 2 - 2
tetromino_y = 0

# Function to draw the Tetris grid
def draw_grid():
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            w.addch(y, x * 2, cell)
    w.refresh()

# Function to draw a Tetris shape
def draw_tetromino():
    for y, row in enumerate(current_tetromino):
        for x, cell in enumerate(row):
            if cell:
                w.addch(tetromino_y + y, (tetromino_x + x) * 2, ' ', curses.color_pair(current_tetromino_color))
    w.refresh()

# Function to move the tetromino
def move(direction):
    global tetromino_x, tetromino_y
    if direction == 'left':
        tetromino_x -= 1
    elif direction == 'right':
        tetromino_x += 1
    elif direction == 'down':
        tetromino_y += 1

# Function to rotate the tetromino
def rotate():
    global current_tetromino
    current_tetromino = list(zip(*current_tetromino[::-1]))

# Function to check for collisions
def check_collision():
    for y, row in enumerate(current_tetromino):
        for x, cell in enumerate(row):
            if cell:
                if (
                    tetromino_y + y >= sh or
                    tetromino_x + x < 0 or
                    tetromino_x + x >= sw or
                    grid[tetromino_y + y][tetromino_x + x] != ' '
                ):
                    return True
    return False

# Main game loop
while True:
    draw_grid()
    draw_tetromino()
    action = w.getch()

    if action == ord('q'):
        break
    elif action == curses.KEY_RIGHT:
        move('right')
        if check_collision():
            move('left')
    elif action == curses.KEY_LEFT:
        move('left')
        if check_collision():
            move('right')
    elif action == curses.KEY_DOWN:
        move('down')
        if check_collision():
            move('up')
            for y, row in enumerate(current_tetromino):
                for x, cell in enumerate(row):
                    if cell:
                        grid[tetromino_y + y][tetromino_x + x] = ' '
            tetromino_x = sw // 2 - 2
            tetromino_y = 0
            current_tetromino = random.choice(tetrominos)
            current_tetromino_color = random.randint(1, len(tetromino_colors))
            if check_collision():
                break
    elif action == ord('r'):
        rotate()
        if check_collision():
            for _ in range(3):
                rotate()
    elif action == ord(' '):
        while not check_collision():
            move('down')
        move('up')
        for y, row in enumerate(current_tetromino):
            for x, cell in enumerate(row):
                if cell:
                    grid[tetromino_y + y][tetromino_x + x] = ' '
        tetromino_x = sw // 2 - 2
        tetromino_y = 0
        current_tetromino = random.choice(tetrominos)
        current_tetromino_color = random.randint(1, len(tetromino_colors))
        if check_collision():
            break

# Clean up and exit
curses.endwin()
