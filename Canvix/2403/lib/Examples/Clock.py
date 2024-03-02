"""
Main Cave logic
"""

# pygame tunnel run
import time
import lib.Tools.Matrix as mat
from Tools.Hardware import encoder_left, encoder_right, led_strip

def format_2d(f):
    return f"{f:02d}"


class Scene:
    def __init__(self):
        self.t_correction = 1000000
        self.time_set = False
        self.time_color = 'Sky_Blue'

        self.offsets = [
            [-1, 11],
            [2, 11],
            [8, 11],
            [12, 11],
            [8, 5],
            [12, 5],
        ]

    def clear_time_vals(self):
        # clear time characters
        clear_array = []
        for c in range(16):
            for r in range(11,16):
                clear_array.append(mat.xy_mat(c, r))
        led_strip.send_array(clear_array, 'off', show=False)
        

    def calc_time(self):
        # Get the current time as integers
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

        if encoder_left.held():
            self.time_set = not self.time_set
            time.sleep(.5)

        if self.time_set:
            # setting time mode
            self.time_color = 'Red'
            self.t_correction += encoder_left.read_delta()*3600 # correct hours
            self.t_correction += encoder_right.read_delta()* 60 # correct minutes
        else:
            self.time_color = 'Sky_Blue'

        # updating time
        times = self.calc_time()
        cpp = []
        pa = [mat.xy_mat(6, 12), mat.xy_mat(6, 14)]  # initiate with time dots

        for i, t in enumerate(times):
            if i == 0:
                if t == 0:
                    continue
            pp = mat.char_matrix(t, self.offsets[i])
            for p in pp:
                pa.append(mat.xy_mat(p[0], p[1]))
            cpp += pp
        self.clear_time_vals()
        led_strip.send_array(pa, self.time_color)
        # time.sleep(.1)
        

        return [cpp, [0, 0]]


clock_mode = Scene()
