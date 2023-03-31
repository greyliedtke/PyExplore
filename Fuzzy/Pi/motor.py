from gpiozero import Motor
from time import sleep

# pins...


motor = Motor(forward=20, backward=21)

def motor_cmd(dir, speed):
    if dir == "FWD":
        motor.forward(speed=speed)
    elif dir == "BWD":
        motor.backward(speed=speed)
    else:
        motor.stop()