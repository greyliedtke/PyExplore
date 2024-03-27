"""
simulate a sine wave
"""

import math

l = 64

# create larger point out of single point...
def zoom_bound(x,y, w):
    xa = []
    ya = []
    wr = list(range(int(-w),int(w+1)))

    for xs in wr:
        for ys in wr:
            xa.append(x+xs)
            ya.append(y+ys)
    return xa, ya


def send_sine(amp, frequency, x_off):
    
    xa = list(range(l))
    ya = [amp+amp*math.sin(frequency*x+x_off) for x in xa]

    a_x, a_y = [], []
    for i,x in enumerate(xa):
        pp = zoom_bound(xa[i], ya[i], 0)
        a_x.append(pp[0])
        a_y.append(pp[1])
        
    return a_x, a_y