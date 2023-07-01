# imports
from digitalio import DigitalInOut, Direction, Pull
import board
import time
import rotaryio
from oled import oled_text, oled_2_line, init_i2c

# Initializing display
oled_display = init_i2c(board.GP15, board.GP14)
oled_text(oled_display, "GreyMan!")

# setting up rotary encoder
enc = rotaryio.IncrementalEncoder(board.GP7, board.GP6)
enc_push = DigitalInOut(board.GP8)
enc_push.direction = Direction.INPUT
enc_push.pull = Pull.UP

# setting up motor pwm's
pwm_m1 = 0
pwm_m2 = 0
pwm_m3 = 0
pwm_m4 = 0
pwm_ms = [0, pwm_m1, pwm_m2, pwm_m3, pwm_m4]


# read pwm settings from file
def read_params():
    pass
    # read


# update pwm settings
def send_motors():
    # write pwm signals, write to file
    pass


# loop through motors
def next_motor(motor_i):
    motor_i += 1
    if motor_i > 4:
        motor_i == 0
    return motor_i



motor_i = 0
enc.position = 0
enc_p = enc.position


# ------------------- Run loop to control motors -----------------------------------------
print('Running Loop')
while True:

    time.sleep(.1)
    oled_2_line(oled_display, f"M1: {pwm_m1}, M2: {pwm_m2}, adj:{motor_i}", f"M3: {pwm_m3}, M4: {pwm_m4}, enc:{enc.position}")

    # pushing button...
    if enc_push.value == False:
        time.sleep(1)
        if enc_push.value == False:
            motor_i = next_motor(motor_i)
            enc.position = pwm_ms[motor_i]
            enc_p = enc.position

    # check for changes in enc position
    if enc_p != enc.position:
        enc_p = enc.position
        send_motors()

