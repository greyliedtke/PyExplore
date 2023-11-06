"""
Characterize Hall effect sensor for magnetization purposes

initial measurements

- Magnetize compressor spacer
After measurements

- speed and counting...


"""
import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
import countio

# ------------------------------------------------------
# Analog magnet reading
analog_in = AnalogIn(board.A0)

def get_voltage():
    # get voltage out of 100
    voltage = (analog_in.value * 100) / 65536
    voltage = round(voltage, 2)
    # print(voltage)
    return voltage 
# ------------------------------------------------------


# ------------------------------------------------------
# Digital magnet reading
di_mag = DigitalInOut(board.GP15)
di_mag.direction = Direction.INPUT
di_mag.pull = Pull.UP
def get_din():
    print(di_mag.value)
    if not di_mag.value:
        mv = "low"
    else:
        mv = "high"
        return mv

# pin_counter = countio.Counter(board.GP21, edge=countio.Edge.RISE, pull=Pull.UP)
# ------------------------------------------------------


while True:
    mav = get_voltage()
    mdv = get_din()
    print(mav, mdv)
    time.sleep(1)