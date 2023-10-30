# imports
from digitalio import DigitalInOut, Direction, Pull
import board
import time
import countio
from oled import oled_text, oled_2_line, init_i2c

# Initializing display
time.sleep(2)
oled_display = init_i2c(board.GP17, board.GP16)
oled_text(oled_display, "N2 Reader")
pin_counter = countio.Counter(board.GP21, edge=countio.Edge.RISE, pull=Pull.UP)

def read_freq():
    tn = time.monotonic()
    ic = pin_counter.count
    time.sleep(2)
    ac = pin_counter.count
    et = time.monotonic() - tn
    freq = (ac - ic) / et
    freq = round(freq, 3)
    krpm = freq * (3600/1000)   # convert to krpm

    if pin_counter.count >= 10000:
        pin_counter.reset()

    return freq, krpm

print('Running Loop')
while True:

    time.sleep(.1)
    freq, krpm = read_freq()
    oled_2_line(oled_display, f"Frequency:{freq}" f"krpm: {krpm}")

