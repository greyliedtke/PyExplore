"""
Main Cave logic
"""

# pygame tunnel run
import random
from Tools.Hardware import encoder_left, encoder_right, led_strip
import time

# constants
wall_t = 3
cave_w = 2 # size of cave hole
cube_l = 16
middle = int(cube_l/2)  # middle of canvas
og_cave = [middle for i in range(cube_l)]

class Scene:
    def __init__(self):
        self.rate = .25
        self.cave_top = middle
        self.target = middle
        self.playing = False
        self.body = middle
        self.cave_center_queue = og_cave

    def init_game(self):
        self.rate = .25
        self.cave_top = middle
        self.target = middle
        self.body = middle
        self.cave_center_queue = og_cave

    def cave_row(self, row, center):
        # thinner walls
        wl = max(0, center-cave_w-wall_t)
        cave_l = list(range(wl, center-cave_w))
        wr = min(cube_l, center+cave_w+wall_t)
        cave_r = list(range(center+cave_w, wr))

        cave_row = cave_l + cave_r
        cr = [[c,row] for c in cave_row]
        return cr
    
    def cave_matrix(self):
        pts = []
        for i in range(0, min(len(self.cave_center_queue), 15)):
            cr = self.cave_row(i, self.cave_center_queue[i])
            pts += cr
        return pts

    def loop(self):
        # updating cave setpoint
        if self.cave_top == self.target:
            self.target = random.randint(0,cube_l-1)

        # rate limiting cave centerpoint
        else:
            if self.cave_top < self.target:
                self.cave_top += self.rate
            else:
                self.cave_top -= self.rate
        self.cave_center_queue.insert(0,int(round(self.cave_top, 0)))

        # creating image of cave
        pts_cave = self.cave_matrix()

        # controlling game
        self.body += encoder_left.delta

        # # logic to end game if hits wall
        if self.body in [pts_cave[0][1]]:
            print(f'Game Over: xx')
            time.sleep(2)
            self.init_game()

        led_strip.strip.fill([0,0,0])
        led_strip.send_matrix(pts_cave, show=False)
        led_strip.send_matrix([[self.body, 1]], color="Red")


cave_man = Scene()