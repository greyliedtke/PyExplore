"""
reading 0-10V signal from PLC and using v divider to get max 3.17v reading on pico
v_max = 10  # volts
r1 = 2200
r2 = 1000
Vo = v_max * r2 / (r1 + r2)

"""

# imports
import board
import pwmio
import rotaryio
import analogio
import time
from digitalio import DigitalInOut, Direction, Pull

from oled import oled_display, oled_text

oled_text("Turbo Sim!")

fuel_ai = analogio.AnalogIn(board.A0)  # fuel analog input

# rotary encoder do nothing for now...
enc_switch = DigitalInOut(board.GP13)
enc_switch.direction = Direction.INPUT
enc_switch.pull = Pull.UP
# enc = rotaryio.IncrementalEncoder(board.GP0, board.GP1)
prev_position = 0

# pwm signal to transitor for speed simulation
krpm_sig = pwmio.PWMOut(
    board.GP16, frequency=1, duty_cycle=int(65535 / 2), variable_frequency=True
)


def sig_to_speed():
    # read signal from plc ao and convert to dummy speed signal

    # 0 to 65535. # raw v value # read ai26, A0
    v_read = fuel_ai.value
    v_read = v_read * 3.3 / 65535
    v_read = round(v_read, 2)
    krpm = v_read * (50 / 2)  # convert to max 50 krpm at 2 volt signal
    krpm = round(krpm, 2)

    if krpm < 1:
        krpm = 0
        hz = 1
    elif krpm > 130:
        krpm = 130
        hz = krpm * 1000 / (60)
    else:
        hz = krpm * 1000 / (60)

    # print(f"hz: {int(hz)}")
    krpm_sig.frequency = int(hz)
    oled_text(f"v: {v_read}, n2:{krpm}")


while True:

    sig_to_speed()
    time.sleep(1)
