"""
used for reading analog input of microphone...
-3v3-->10k-->A0--->1/50k-->GND
scale this value to light brightness?

"""
import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.A0)


def get_voltage():
    # get voltage out of 100
    voltage = (analog_in.value * 100) / 65536
    voltage = round(voltage, 2)
    print(voltage)
    return voltage 

while True:
    get_voltage()
    time.sleep(1)