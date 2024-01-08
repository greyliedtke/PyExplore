"""
script for managing the 7 sergment servos
"""

# imports
import pwmio
import board

# ------------------------------------------------------
# Servo Class setup
class ServoClass:
    def __init__(self, pin, on, off):
        self.pwm = pwmio.PWMOut(pin, frequency=50, duty_cycle=0)
        self.on = on
        self.off = off
        self.pos = 0
        self.target = 0
        self.rate = 0

    def send_angle(self, angle):
        # turn angle from 0-180 into pwm duty cycle...
        # duty range from .5 to 2.5 ms. since 50 hz... duty = pulse_width/period = 
        # 50hz = 20ms
        norm = (angle/180)*100
        duty = norm*.1+0.25
        self.pwm.duty_cycle = int(duty*65535/100)

    def send_bin(self, on=False):
        if on:
            self.send_angle(self.on)
        else:
            self.send_angle(self.off)

    def update(self):
        if self.pos != self.target:
            self.pos = self.pos + self.rate
            self.send_angle(self.pos)

    def new_target(self, target):
        self.target = target
        self.rate = (self.target - self.pos)/10

s0 = ServoClass(board.GP0, 0, 1)
s1 = ServoClass(board.GP17, 0, 1)
s2 = ServoClass(board.GP18, 0, 1)
s3 = ServoClass(board.GP19, 0, 1)
s4 = ServoClass(board.GP20, 0, 1)
s5 = ServoClass(board.GP21, 0, 1)
s6 = ServoClass(board.GP22, 0, 1)
servos = [s0, s1, s2, s3, s4, s5, s6]
# ------------------------------------------------------

# ------------------------------------------------------
# Seven segment display matrix
digits = [
    [1,1,1,1,1,0,1],   # 0
    [0,1,0,1,0,0,0],    # 1
    [0,1,1,0,1,1,1],    # 2
    [0,1,0,1,1,1,1],    # 3
    [1,1,0,1,0,1,0],    # 4
    [1,0,1,0,1,1,1],    # 5
    [1,0,1,1,1,1,1],    # 6
    [0,1,0,1,1,0,0],    # 7
    [1,1,1,1,1,1,1],    # 8
    [1,1,0,1,1,1,0]     # 9
]
# ------------------------------------------------------

# ------------------------------------------------------
# send servo digits
def send_servo_digits(number):
    sc = digits[number]
    for i, s in enumerate(servos):
        s.send_bin(sc[i])
# ------------------------------------------------------

