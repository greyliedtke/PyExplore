"""
simulate N2 and N1 with regards to load bank to test controls
"""

import board
import pwmio
import rotaryio
import analogio
import time
from digitalio import DigitalInOut, Direction, Pull
from simulator_funcs import speed_response, krpm_freq, bound
from oled import oled_display, oled_text, oled_2_line
oled_text("Turbo Sim!")




# Initialize board pins
fuel_ai = analogio.AnalogIn(board.A0)  # fuel analog input
n1_sig = pwmio.PWMOut(
    board.GP9, frequency=1, duty_cycle=int(65535 / 2), variable_frequency=True
)
n2_sig = pwmio.PWMOut(
    board.GP15, frequency=1, duty_cycle=int(65535 / 2), variable_frequency=True
)
load_enc = rotaryio.IncrementalEncoder(board.GP10, board.GP11)


load_level = 0 # 0-12
fuel_ao = 0 # percentage read


while True:
    fuel_percentage = round(fuel_ai.value / 65535 * (2/3.3), 3)  # read fuel input signal as percentage of 2 volts
    load_enc.position = bound(load_enc.position)
    n1, n2 = speed_response(fuel_percentage, load_enc.position)
    n1_sig.frequency = krpm_freq(n1, 1.25)
    n2_sig.frequency = krpm_freq(n2, 1)
    # print(n2_sig.frequency)
    oled_2_line(f"load:{load_enc.position}", f"n1:{n1}, n2:{n2}")

    time.sleep(.1)
