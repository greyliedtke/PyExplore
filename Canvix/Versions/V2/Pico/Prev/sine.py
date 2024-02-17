"""
function for sine wave
"""
import math
from Mat import xy_mat
from Strip import s

def send_sine(amp, frequency, offset):
    
    x = list(range(15))
    y = [8+amp*math.sin(frequency*xr+offset) for xr in x]

    a_x, a_y = [], []
    for i in range(len(x)):
        eq_x, eq_y = xy_mat(x[i], y[i])
        a_x.append(eq_x[0])
        a_x.append(eq_x[1])
        a_x.append(eq_x[0])
        a_x.append(eq_x[1])
        a_y.append(eq_y[0])
        a_y.append(eq_y[1])
        a_y.append(eq_y[1])
        a_y.append(eq_y[0])

    for i,p in enumerate(a_x):
        pix = xy_mat(a_x[i], a_y[i])
        s[pix] = [0, 2, 2.1]

    s.show()