"""
Read flowmeter for water cooling loop
"""


# imports
from digitalio import DigitalInOut, Direction, Pull
import board
import time
import rotaryio
import countio
from oled import oled_text, oled_2_line, init_i2c

# Initializing display
oled_display = init_i2c(board.GP15, board.GP14)
oled_text(oled_display, "Flowmeter!")

# initialize counter
pin_counter = countio.Counter(board.GP21, edge=countio.Edge.RISE, pull=Pull.DOWN)
flow_k = 21 # F = 21*Q



# ------------------- read frequency for flowrate -----------------------------------
def read_flow():
    # read frequency on pin and convert to lpmimport countio
    tn = time.monotonic()
    ic = pin_counter.count
    time.sleep(3)
    ac = pin_counter.count
    et = time.monotonic() - tn
    freq = (ac - ic) / et
    freq = round(freq, 3)
    
    l_min = freq / flow_k
    l_min = round(l_min, 3)

    if pin_counter.count >= 10000:
        pin_counter.reset()

    return freq, l_min

# ------------------- Run loop to control motors -----------------------------------------
print('Running Loop')
while True:

    time.sleep(.1)
    freq, flow = read_flow()
    oled_2_line(oled_display, f"Freq: {freq}", f"Flow: {flow}")



