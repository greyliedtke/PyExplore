"""
script for support functions
"""

def bound(position):
    if position < 0:
        position = 0
    elif position > 10:
        position = 10
    return position

def big_delta(v, mmax, mmin):
    nmax = max(mmax, v)
    nmin = min(mmin, v)
    return nmax, nmin