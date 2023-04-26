# imports
from digitalio import DigitalInOut, Direction, Pull
import board
import time
import rotaryio
from oled import oled_text, oled_2_line, init_i2c
import pwmio


# Initializing display
gnd_oled = DigitalInOut(board.GP13)
gnd_oled.direction = Direction.OUTPUT
gnd_oled.value = False
v_oled = DigitalInOut(board.GP12)
v_oled.direction = Direction.OUTPUT
v_oled.value = True
time.sleep(2)
oled_display = init_i2c(board.GP11, board.GP10)
oled_text(oled_display, "GreyMan!")

# setting up rotary encoder
v_enc = DigitalInOut(board.GP9)
v_enc.direction = Direction.OUTPUT
v_enc.value = True
enc = rotaryio.IncrementalEncoder(board.GP7, board.GP6)
enc_push = DigitalInOut(board.GP8)
enc_push.direction = Direction.INPUT
enc_push.pull = Pull.UP

# setting up servo
# pwm signal to transitor for speed simulation
servo_pwm = pwmio.PWMOut(board.GP16, frequency=50, duty_cycle=0)

def send_angle(theta):
    


print('Running Loop')
while True:

    time.sleep(.1)
    oled_2_line(oled_display, f"encoder:{enc.position}", f"encoder:{enc.position}")

    if enc_push.value == False:
        oled_2_line(oled_display, f"encoder:{enc.position}", f"encoder:{enc.position}")
        print(f"okay")

            


