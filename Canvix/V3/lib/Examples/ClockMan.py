"""
Main Cave logic
"""

# pygame tunnel run
import time
import lib.Tools.Matrix as mat
from Tools.Hardware import enc_1, enc_2, ns

class Scene:
    def __init__(self):
        self.init_time = time.time()

    def calc_time(self):
        # Get the current time
        t_now = time.time()
        delt = t_now - self.init_time

        # Extract hours, minutes, and seconds
        hours = delt // 3600
        minutes = delt % 3600 // 60
        seconds = delt % 60
        return [hours[0], hours[1], minutes[0], minutes[1], seconds[0], seconds[1]]

    def loop(self):

        # creating image of cave
        ts = [1,2,3,4, 5, 6, 7, 8]
        ts = [4]
        times = self.calc_time()

        cpp = []
        for i, t in enumerate(times):
            pp = mat.characters[i].char_matrix(t)
            cpp+=pp

        return [cpp, [0,0]]

clock = Scene()