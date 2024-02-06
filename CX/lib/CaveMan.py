"""
Main Cave logic
"""

# pygame tunnel run
import numpy as np
import random
from collections import deque
import keyboard
import time
import lib.globe as g


# constants
wall_t = 3
cave_w = 2 # size of cave hole
middle = int(g.pw/2)  # middle of canvas
og_cave = [middle for i in range(g.pw)]

class Scene:
    def __init__(self):
        self.rate = g.refr
        self.cave_top = middle
        self.target = middle
        self.playing = False
        self.body = middle
        self.cave_center_queue = deque(og_cave, maxlen=g.pw)

    def init_game(self):
        self.rate = .25
        self.cave_top = middle
        self.target = middle
        self.body = middle
        self.cave_center_queue = deque(og_cave, maxlen=g.pw)

    def cave_row(self, row, center):
        # thinner walls
        wl = max(0, center-cave_w-wall_t)
        cave_l = list(range(wl, center-cave_w))
        wr = min(g.pw, center+cave_w+wall_t)
        cave_r = list(range(center+cave_w, wr))

        cave_row = cave_l + cave_r
        cr = [[c,row] for c in cave_row]
        return cr
    
    def cave_matrix(self):
        pts = []
        for i in range(0, len(self.cave_center_queue)):
            cr = self.cave_row(i, self.cave_center_queue[i])
            pts += cr
        return pts

    def loop(self):
        # updating cave setpoint
        if self.cave_top == self.target:
            self.target = random.randint(0,g.pw-1)

        # rate limiting cave centerpoint
        else:
            if self.cave_top < self.target:
                self.cave_top += self.rate
            else:
                self.cave_top -= self.rate
        self.cave_center_queue.append(int(round(self.cave_top, 0)))

        # creating image of cave
        pts_cave = self.cave_matrix()

        # controlling game
        self.body = [g.move_delta(), 1]

        # # logic to end game if hits wall
        # if self.body in cave_plot[0][1]:
        #     self.cave_center_queue = deque(og_cave, maxlen=g.pw)
        #     print(f'Game Over: xx')
        #     self.init_game()
        #     time.sleep(1.5)

        # cavex = [item for sublist in cave_plot[0] for item in sublist]
        # cavey = [item for sublist in cave_plot[1] for item in sublist]
        # cave_map = [cavex, cavey]

        return [pts_cave, self.body]

cm = Scene()