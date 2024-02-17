"""
Main Cave logic
"""

# pygame tunnel run
import numpy as np
import random
from collections import deque
import keyboard
import time


# constants
game_l = 16
wall_t = 3
cave_w = 2 # size of cave hole
middle = int(game_l/2)  # middle of canvas
og_cave = [middle for i in range(game_l)]

class Scene:
    def __init__(self):
        self.rate = .25
        self.cave_top = middle
        self.target = middle
        self.playing = False
        self.body = middle
        self.cave_center_queue = deque(og_cave, maxlen=game_l)

    def init_game(self):
        self.rate = .25
        self.cave_top = middle
        self.target = middle
        self.body = middle
        self.cave_center_queue = deque(og_cave, maxlen=game_l)

    def cave_row(self, row, center):
        # full walls
        cave_l = list(range(0, center-cave_w))
        cave_r = list(range(center+cave_w+1, game_l))

        # thinner walls
        wl = max(0, center-cave_w-wall_t)
        cave_l = list(range(wl, center-cave_w))
        wr = min(game_l, center+cave_w+wall_t)
        cave_r = list(range(center+cave_w+1, wr))

        cave_row = cave_l + cave_r
        cave_y = np.full(len(cave_row), row)
        return cave_row, cave_y
    
    def cave_matrix(self):
        cave_x, cave_y = [], []
        for i in range(0, len(self.cave_center_queue)):
            x, y = self.cave_row(i, self.cave_center_queue[i])
            cave_x.append(x)
            cave_y.append(y)
        return [cave_x, cave_y]

    def loop(self):
        # updating cave setpoint
        if self.cave_top == self.target:
            self.target = random.randint(0,game_l-1)

        # rate limiting cave centerpoint
        else:
            if self.cave_top < self.target:
                self.cave_top += self.rate
            else:
                self.cave_top -= self.rate
        self.cave_center_queue.append(int(round(self.cave_top, 0)))

        # creating image of cave
        cave_plot = self.cave_matrix()

        # controlling game
        if keyboard.is_pressed('left'):
            self.body -= 1
        elif keyboard.is_pressed('right'):
            self.body += 1

        # logic to end game if hits wall
        if self.body in cave_plot[0][1]:
            self.cave_center_queue = deque(og_cave, maxlen=game_l)
            print(f'Game Over: xx')
            self.init_game()
            time.sleep(1.5)

        cavex = [item for sublist in cave_plot[0] for item in sublist]
        cavey = [item for sublist in cave_plot[1] for item in sublist]
        cave_map = [cavex, cavey]

        return cave_map

cm = Scene()