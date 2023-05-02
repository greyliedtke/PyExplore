"""
Script for controlling servo and with pi
"""

# imports
from gpiozero import AngularServo
from time import sleep

servo = AngularServo(12, min_angle=0, max_angle=180)

# 


# set pins

# pi = pigpio.pi()

# pi.set_mode(servo_pin, pigpio.OUTPUT)
# pi.set_PWM_frequency(servo_pin, 0)



def send_servo_angle(theta):
    # send pi servo to angle theta between 0 and 180
    servo.angle = theta
    # pi.set_PWM_frequency(servo_pin, freq)

# for a in range(0,100):
#     send_servo_angle(a)
#     time.sleep(.05)

