"""
functions for simulator meant to work without pico
"""

# fake speed response. Come up with legit equation...

def krpm_freq(krpm, scale):
    if krpm < 1:
        krpm = 0
        hz = 1
    else:
        hz = int(krpm * 1000 * scale / 60)
    return hz

def bound(position):
    upper_bound, lower_bound = 12, 0
    position = max(lower_bound, min(upper_bound, position))
    return position
