"""
used for reading analog input of microphone...

"""
import time
import board
from analogio import AnalogIn
import neopixel

analog_in = AnalogIn(board.A0)


def get_voltage():
    # get voltage out of 100
    return (analog_in.value * 100) / 65536


def delta_loop():
    # read xx samples and return max difference "magnitude"
    max_s = 0
    min_s = 0
    for l in range(1000):
        sound_v = get_voltage()

        max_s = max(sound_v, max_s)
        min_s = min(sound_v, min_s)
    delta = max_s - min_s
    print(delta)


while True:
    delta_loop()
    time.sleep(0.1)