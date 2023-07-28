# imports
from digitalio import DigitalInOut, Direction, Pull
import board
import time
import countio
from oled import oled_text, oled_2_line, init_i2c

# Initializing display
oled_display = init_i2c(board.GP15, board.GP14)
oled_text(oled_display, "GreyMan!")

# setting up pump buttons
sw_high = DigitalInOut(board.GP8)
sw_high.direction = Direction.INPUT
sw_high.pull = Pull.UP
sw_low = DigitalInOut(board.GP9)
sw_low.direction = Direction.INPUT
sw_low.pull = Pull.UP

# ------------------- read frequency for flowrate -----------------------------------
# initialize counter
pin_counter = countio.Counter(board.GP21, edge=countio.Edge.RISE, pull=Pull.DOWN)
flow_k = 15 # 15 counts / ml/min... frequency / value = flowrate
def read_flow():
    # read frequency on pin and convert to lpmimport countio
    tn = time.monotonic()
    ic = pin_counter.count
    time.sleep(.25)
    ac = pin_counter.count
    et = time.monotonic() - tn
    freq = (ac - ic) / et
    freq = round(freq, 3)
    
    ml_min = freq / flow_k
    ml_min = round(ml_min, 3)

    if pin_counter.count >= 10000:
        pin_counter.reset()

    return ml_min



# ------------------- Run loop to control motors -----------------------------------------
print('Running Loop')
react_time = .25
while True:

    time.sleep(.1)

    # pushing button...
    if sw_high.value == False:
        time.sleep(react_time)
        if sw_high.value == False:
            print("high speed")

    flow = read_flow()
    oled_2_line(oled_display, "Flowrate:", flow)
        
