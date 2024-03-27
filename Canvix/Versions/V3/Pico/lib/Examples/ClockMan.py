"""
Main Cave logic
"""

# pygame tunnel run
import time
import lib.Tools.Matrix as mat
from lib.Tools.Hardware import led_strip, enc_1

def format_2d(f):
    return f"{f:02d}"

class Scene:
    def __init__(self):
        self.t_correction = 1000000

    def calc_time(self):
        # Get the current time
        tn = time.time()
        delt = tn - self.t_correction
        days = delt // (24 * 3600)
        delt %= 24 * 3600
        hours = format_2d(delt // 3600)
        minutes = format_2d(delt % 3600 // 60)
        seconds = format_2d(delt % 60)
        ta = [hours[0], hours[1], minutes[0], minutes[1], seconds[0], seconds[1]]
        ta = [int(i) for i in ta]
        return ta

    def loop(self):
        self.t_correction += enc_1.read_delta()


        times = self.calc_time()
        cpp = []
        pa = []
        for i, t in enumerate(times):
            pp = mat.characters[i].char_matrix(t)
            for p in pp:
                pa.append(mat.xy_mat(p[0], p[1]))
            cpp+=pp
        led_strip.send_array(pa)
        time.sleep(1)
        
        return [cpp, [0,0]]

clock = Scene()