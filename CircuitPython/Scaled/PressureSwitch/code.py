"""
script to create pressure witch for air tank
- display pressure reading
- set pressure
- states: OFF, Charging
if OFF and button hold. Charge until pressure
else nothing
"""


# imports
from digitalio import DigitalInOut, Direction, Pull
import board
import time
import rotaryio
from oled import oled_text, oled_2_line, init_i2c
from analogio import AnalogIn

analog_in = AnalogIn(board.A0)
v_10 = .33
v_90 = 2.97
v_scale = 300/(v_90-v_10)

def get_pressure():
    # get voltage out of 100
    voltage = analog_in.value/65536
    press = (voltage-v_10)*v_scale
    psi = round(press, 0)
    return psi

# Initializing display
time.sleep(1)
oled_display = init_i2c(board.GP15, board.GP14)
oled_text(oled_display, "GreyMan!")

b_push = DigitalInOut(board.GP17)
b_push.direction = Direction.INPUT
b_push.pull = Pull.UP

relay = DigitalInOut(board.GP1)
relay.direction = Direction.OUTPUT

state = "OFF"
psi_limit = 20
relay.value = False

while True:

    time.sleep(.1)
    psi = get_pressure()
    
    if psi > psi_limit or psi < 0:
        state = "OFF"
        relay.value = False

    if state == "Charging":

        # if button held for 1 second, turn off
        if b_push.value is False:
            time.sleep(1)
            if b_push.value:
                state = "OFF"

    if state == "OFF":
        relay.value = False
        
        if psi < psi_limit:

            # if button held for over 1 second, start charging
            if b_push.value is False:
                time.sleep(1)
                if b_push.value is False:
                    state = "Charging"
                    relay.value = True

    oled_2_line(oled_display, f"PSI: {psi}", f"State: {state}")

            


