"""
functions for simulator meant to work without pico
"""

# fake speed response. Come up with legit equation...
def speed_response(fuel_percent, load_level):
    n2_max_sim = 60
    n2_speed = n2_max_sim * fuel_percent / ((1+load_level)/10)
    n1_speed = n2_speed * 1.8
    return round(n1_speed, 1), round(n2_speed, 1)

def krpm_freq(krpm, scale):
    if krpm < 1:
        krpm = 0
        hz = 1
    else:
        hz = int(krpm * 1000 * scale / 60)
    return hz

def bound(position):
    if position < 0:
        position = 0
    elif position > 12:
        position = 12
    return position
