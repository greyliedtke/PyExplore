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
middle = int(game_l/2)  # middle of canvas
ping_w = 4 # size of cave hole
og_cave = [middle for i in range(game_l)]


class Scene:
    def __init__(self):
        self.rate = 0
        self.vx = 0
        self.vy = 0
        self.ping = [0, 0]
        self.paddle_m = 0
        self.paddle = [0, 0, 0]
        self.init_game()

    def init_game(self):
        self.rate = .25
        self.vx = 1
        self.vy = 1
        self.ping = [middle, 1]
        self.paddle_m = middle
        self.pp = [[],[]]

    def loop(self):
        self.paddle = [self.paddle_m-1, self.paddle_m, self.paddle_m+1]

        # hitting paddle on bottom
        if self.ping[1] == game_l: self.vy = -self.vy
        if self.ping[0] in [0,game_l]: self.vx = -self.vx

        if self.ping[1] == 0:
            if self.ping[0] in self.paddle:
                self.vy = -self.vy
            else:
                print("game over")
                time.sleep(1.5)
                self.init_game()

        self.ping[0] = self.ping[0]+self.vx
        self.ping[1] = self.ping[1]+self.vy
            
        # controlling game
        if keyboard.is_pressed('left'):
            self.paddle_m -= 1
        elif keyboard.is_pressed('right'):
            self.paddle_m += 1
        self.pp = [self.paddle, [0,0,0]]
        return

pm = Scene()