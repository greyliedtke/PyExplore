"""
file to interpolate data to led matrix
"""

import math

def point_make(x, y):
    p1 = math.floor(x)
    p2 = math.ceil(x)
    if p2 == p1: p2+=1
    p3 = math.floor(y)
    p4 = math.ceil(y)
    if p3 == p4: p4+=1
    # print(p1, p2, p3, p4)
    return [p1, p2], [p3, p4]
