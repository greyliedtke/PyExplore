"""
script for controlling xx motors
"""

# ------------------------------------------------------
# Imports
from hardware import p_w1, p_w2, encoder
from oled import oled_display, oled_text
oled_text("Motor Controller")
# ------------------------------------------------------

# ------------------------------------------------------
pump_i = 0
pumps = [p_w1, p_w2]
# Control loop
while True:
    pump_control = pumps[pump_i]

    # read encoder
    if encoder.delta:
        pump_control.set_speed(pump_control.speed + encoder.delta)

    # set speed based on encoder position
    oled_text(f"{pump_control.desc}: {pump_control.speed}%")
# ------------------------------------------------------