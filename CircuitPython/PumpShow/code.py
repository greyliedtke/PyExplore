# imports
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
import time
import rotaryio

from oled import oled_display, oled_text

oled_text("hey grey!")

# initialize buttons and outputs
p1_b = DigitalInOut(board.GP0)
p1_b.direction = Direction.INPUT
p1_b.pull = Pull.UP
p2_b = DigitalInOut(board.GP1)
p2_b.direction = Direction.INPUT
p2_b.pull = Pull.UP

# rotary encoder and screen...
# pwm output
# pwm signal to transitor for speed simulation
pump_pwm = pwmio.PWMOut(board.GP14, frequency=1000, duty_cycle=0)


enc = rotaryio.IncrementalEncoder(board.GP20, board.GP21)


while True:
    time.sleep(1)
    if 0 > enc.position:
        enc.position = 0
    elif enc.position > 10:
        enc.position = 10

    # set speed based on encoder position
    ss = enc.position
    oled_text(f"speed%: {ss}0")
    pump_pwm.duty_cycle = int(65535 * ss/10)
    




