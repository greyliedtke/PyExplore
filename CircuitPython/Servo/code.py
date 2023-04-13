# imports
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
import time

# pwm signal to transitor for speed simulation
servo_pwm = pwmio.PWMOut(board.GP15, frequency=50, duty_cycle=0)

def send_servo_angle(theta):
    duty_percent = (theta/180)
    # duty_percent = int(theta/10 + 10)/100
    cycle = int(duty_percent*65535)
    # print(duty)
    # Cycles through the full PWM range from 0 to 65535
    servo_pwm.duty_cycle = cycle  # Cycles the LED pin duty cycle through the range of values
    # pi.set_PWM_frequency(servo_pin, freq)


while True:
    print('forward')
    for a in range(0,180, 5):
        send_servo_angle(a)
        time.sleep(.5)
    print('back')


