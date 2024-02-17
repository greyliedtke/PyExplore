"""
script to create sine plot
"""

import math
from MatMap.interp import point_make
from MatMap.led_strip import strip
from MatMap.Mat import xy_mat

def send_sine(amplitude, frequency, offset):
    # clear strip
    strip.fill([0,0,0])

    x = list(range(15))
    y = [8+amplitude*math.sin(frequency*xr+offset) for xr in x]

    a_x, a_y = [], []
    for i in range(len(x)):
        eq_x, eq_y = point_make(x[i], y[i])
        a_x.append(eq_x[0])
        a_x.append(eq_x[1])
        a_x.append(eq_x[0])
        a_x.append(eq_x[0])
        a_y.append(eq_y[0])
        a_y.append(eq_y[1])
        a_y.append(eq_y[1])
        a_y.append(eq_y[0])

    for i,p in enumerate(a_x):
        pix = xy_mat(a_x[i], a_y[i])
        strip[pix] = [255, 0, 0]

    strip.show()
