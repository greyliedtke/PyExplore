"""
script to create sine plot
"""

import math
from MatMap.interp import point_make
import time
from MatMap.Mat import xy_mat

pi = True
if pi:
    from MatMap.led_strip import strip


def send_sine(amplitude, frequency, offset):
    # clear strip
    if pi:
        strip.fill([0, 0, 0])

    x = list(range(15))
    y = [8 + amplitude * math.sin(frequency * xr + offset) for xr in x]

    a_x, a_y = [], []
    for i in range(len(x)):
        eq_x, eq_y = point_make(x[i], y[i])
        a_x.append(eq_x[0])
        a_x.append(eq_x[1])
        a_x.append(eq_x[0])
        a_x.append(eq_x[1])
        a_y.append(eq_y[0])
        a_y.append(eq_y[1])
        a_y.append(eq_y[1])
        a_y.append(eq_y[0])

    # print(len(a_x))
    # print('x', a_x)
    # print('y', a_y)
    for i, p in enumerate(a_x):
        pix = xy_mat(a_x[i], a_y[i])
        if pi:
            strip[pix] = [94, 225, 235]

    if pi:
        strip.show()


ti = time.perf_counter()

while True:
    ts = time.perf_counter() - ti
    # send_sine(3, 0.7, ts * 2.5)
    send_sine(6, 0.45, ts * 3.14)
    # 6.5, .45
    # time.sleep(0.01)