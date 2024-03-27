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
        self.time_set = False

    def set_time():
        pass

    def clear_bottom(self):
        # clear top rows
        clear_array = []
        for c in range(16):
            for r in range(11,16):
                clear_array.append(mat.xy_mat(c, r))
        led_strip.send_array(clear_array, 'off', show=False)
        

    def calc_time(self):
        # Get the current time
        tn = time.time()
        delt = tn - self.t_correction
        days = delt // (24 * 3600)
        # delt %= 24 * 3600
        delt %= 12 * 3600
        hours = format_2d(delt // 3600)
        minutes = format_2d(delt % 3600 // 60)
        seconds = format_2d(delt % 60)
        ta = [hours[0], hours[1], minutes[0], minutes[1], seconds[0], seconds[1]]
        ta = [hours[0], hours[1], minutes[0], minutes[1]]
        ta = [int(i) for i in ta]
        return ta

    def loop(self):
        self.t_correction += enc_1.read_delta()

        if self.time_set:
            self.set_time()

        times = self.calc_time()
        cpp = []
        pa = []  # initiate with time dots
        pa.append(mat.xy_mat(6, 12))
        pa.append(mat.xy_mat(6, 14))

        offsets = [
            [-1, 11],
            [2, 11],
            [8, 11],
            [12, 11],
            [8, 5],
            [12, 5],
        ]

        for i, t in enumerate(times):
            if i == 0:
                if t == 0:
                    continue
            pp = mat.char_matrix(t, offsets[i])
            for p in pp:
                pa.append(mat.xy_mat(p[0], p[1]))
            cpp += pp
        self.clear_bottom()
        led_strip.send_array(pa)
        time.sleep(.1)
        

        return [cpp, [0, 0]]


clock = Scene()
