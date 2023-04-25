# imports
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
import time
import rotaryio

# pwm signal to transitor for speed simulation
servo_pwm = pwmio.PWMOut(board.GP15, frequency=50, duty_cycle=0)

# setting up rotary encoder
v_enc = DigitalInOut(board.GP9)
v_enc.direction = Direction.OUTPUT
v_enc.value = True
enc = rotaryio.IncrementalEncoder(board.GP7, board.GP6)
enc_push = DigitalInOut(board.GP8)
enc_push.direction = Direction.INPUT
enc_push.pull = Pull.UP


def send_servo_angle(theta):
    duty_percent = (theta/180)
    # duty_percent = int(theta/10 + 10)/100
    cycle = int(duty_percent*65535)
    # print(duty)
    # Cycles through the full PWM range from 0 to 65535
    servo_pwm.duty_cycle = cycle  # Cycles the LED pin duty cycle through the range of values
    # pi.set_PWM_frequency(servo_pin, freq)
    v_enc.value = theta


while True:

    # check if button pressed
    if enc_push:
        if v_enc.value <= 90:
            send_servo_angle(0)
        else:
            send_servo_angle(180)



