"""
script for controlling xx motors
"""

import time
time.sleep(.5)

from hardware import p_w1, p_w2, encoder
from oled import oled_display, oled_text
oled_text("Motor Controller")


# # ------------------------------------------------------

# # ------------------------------------------------------
pump_i = 0
pumps = [p_w1, p_w2]
# Control loop
while True:
    pump_control = pumps[pump_i]

    # read encoder
    encoder.read()
    if encoder.delta:
        pump_control.set_speed(pump_control.speed + encoder.delta)

    if encoder.pushed:
        print("pushed")
        pump_i = (pump_i + 1) % 2
        time.sleep(.5)

    # set speed based on encoder position
    oled_text(f"{pump_control.desc}: {pump_control.speed}%")
# ------------------------------------------------------