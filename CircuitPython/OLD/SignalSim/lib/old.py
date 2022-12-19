"""
reading 0-10V signal from PLC and using v divider to get max 3.17v reading on pico
v_max = 10  # volts
r1 = 2200
r2 = 1000
Vo = v_max * r2 / (r1 + r2)

"""
class SimState:
    def __init__(self):
        self.ao = 0
        self.krpm = 0

sim_state = SimState()

# RC circuit to simulate analog output
ao_sig = pwmio.PWMOut(board.GP0, frequency=1000, duty_cycle=0)


def change_ao():
    if sim_state.ao < 0:
        sim_state.ao = 0
    if sim_state.ao > 3.3 / 2:
        sim_state.ao = 3.3 / 2
    ap = 100 * sim_state.ao * 2 / 3.3
    ao_sig.duty_cycle = int(65535 * ap / 100)


# pwm signal to transitor for speed simulation
krpm_sig = pwmio.PWMOut(board.GP5, frequency=1, duty_cycle=50, variable_frequency=True)


def change_speed():
    if sim_state.krpm < 1:
        sim_state.krpm = 1
    if sim_state.krpm > 130:
        sim_state.krpm = 130
    hz = sim_state.krpm * 1000 / (60)
    # print(f"hz: {int(hz)}")
    krpm_sig.duty_cycle = int(65535 / 2)
    krpm_sig.frequency = int(hz)
    

# imports
import board
import pwmio
import rotaryio
import analogio
from oled import oled_display, oled_text

oled_text("hey grey!")

fuel_ai = analogio.AnalogIn(board.A0)

def read_fuel_s():
    # 0 to 65535. # raw v value # read ai26, A0
    v_read = fuel_ai.value
    v_read = (v_read * 3.3 / 65535)
    speed_sim = v_read * (50000/3.3)    # convert to max 50 krpm


import time
from board import *
from digitalio import DigitalInOut, Direction, Pull

enc_switch = DigitalInOut(board.GP13)
enc_switch.direction = Direction.INPUT
enc_switch.pull = Pull.UP

enc = rotaryio.IncrementalEncoder(board.GP14, board.GP15)
prev_position = 0

modes = ["PWM O", "AO"]
mode_i = 0

# pwm signal to transitor for speed simulation
krpm_sig = pwmio.PWMOut(board.GP5, frequency=1, duty_cycle=int(65535 / 2), variable_frequency=True)


def change_speed(krpm):
    if krpm < 1:
        krpm = 1
    if krpm > 130:
        krpm = 130
    hz = krpm * 1000 / (60)
    
    # print(f"hz: {int(hz)}")
    krpm_sig.frequency = int(hz)

while True:

    # pressing encoder switch button...
    if enc_switch.value is False:
        mode_i += 1
        if mode_i > (len(modes) - 1):
            mode_i = 0
        oled_text(f"MODE: {modes[mode_i]}")
        time.sleep(0.5)

    position = enc.position
    if position != prev_position:
        if position > prev_position:
            prev_position = position
            if mode_i == 0:
                sim_state.krpm += 1
            if mode_i == 1:
                sim_state.ao += 0.1

        elif position < prev_position:
            prev_position = position
            if mode_i == 0:
                sim_state.krpm -= 1
            if mode_i == 1:
                sim_state.ao -= 0.1

        if mode_i == 0:
            change_speed()
            oled_text(f"KRPM: {sim_state.krpm}")
        if mode_i == 1:
            change_ao()
            oled_text(f"V: {sim_state.ao}")
