"""
script for handling hardware specific code
"""


# ------------------------------------------------------
# Imports
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
import rotaryio
from oled import oled_display, oled_text
oled_text("Motor Controller")
# ------------------------------------------------------

# ------------------------------------------------------
# encoder setups
class Encoder:
    def __init__(self, desc, pin1, pin2, pin_push):
        self.desc = desc
        self.enc = rotaryio.IncrementalEncoder(pin1, pin2)
        self.enc.position = 0
        self.push = DigitalInOut(pin_push)
        self.push.direction = Direction.INPUT
        self.push.pull = Pull.UP
        self.value = 0
        self.delta = 0
        self.pushed = False

    def read(self):
        # push button pressed
        if not self.push.value:
            self.pushed = True
        else:
            self.pushed = False
        if self.enc.position != self.value:
            print(f"{self.desc}: {self.enc.position}")
            self.delta = self.value - self.enc.position
            self.value = self.enc.position
        else:
            self.delta = 0

encoder = Encoder("Left", board.GP2, board.GP1, board.GP0)


# ------------------------------------------------------

# ------------------------------------------------------
# Motor controller class
class PWM_Motor:
    def __init__(self, desc, pin):
        self.desc = desc
        self.pwm = pwmio.PWMOut(pin, frequency=1000, duty_cycle=0)
        self.speed = 0

    def set_speed(self, speed):
        self.pwm.duty_cycle = int(65535 * speed/10)
        self.speed = speed

p_w1 = PWM_Motor("Water Pump 1", board.GP14)
p_w2 = PWM_Motor("Water Pump 2", board.GP13)