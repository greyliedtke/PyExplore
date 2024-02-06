"""
Main Cave logic
"""

# pygame tunnel run
import random
from collections import deque
import keyboard
import time
import lib.globe as g
import lib.matop as mo

class Scene:
    def __init__(self):
        self.rate = g.refr

    def loop(self):

        # creating image of cave
        ts = [1,2,3,4, 5, 6, 7, 8]
        ts = 


        cpp = []
        for i, t in enumerate(ts):
            pp = mo.characters[i].char_matrix(t)
            cpp+=pp

        return [cpp, [0,0]]

cm = Scene()