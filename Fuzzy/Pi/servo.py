import RPi.GPIO as GPIO
import time

from gpiozero import Servo
from time import sleep

servo = Servo(21)

while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)

# set pins

# pi = pigpio.pi()

# pi.set_mode(servo_pin, pigpio.OUTPUT)
# pi.set_PWM_frequency(servo_pin, 0)



def send_servo_angle(theta):
    # duty = (theta/180) * 100 * (1/10) + 10
    duty = int(theta/10 + 10)
    # print(duty)
    pi_pwm.ChangeDutyCycle(duty)
    # pi.set_PWM_frequency(servo_pin, freq)

for a in range(0,100):
    send_servo_angle(a)
    time.sleep(.05)

