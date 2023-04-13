"""
used for reading analog input of microphone...

"""
import time
import board
from analogio import AnalogIn

# analog_in = AnalogIn(board.A0)


# def get_voltage(pin):
#     return (pin.value * 100) / 65536


# while True:
#     print((get_voltage(analog_in),))
#     time.sleep(0.1)

#     import time


import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP16, echo_pin=board.GP17)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)