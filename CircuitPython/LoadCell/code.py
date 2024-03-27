# SPDX-FileCopyrightText: 2022 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# code load cell

from hx711_cp import HX711
import board
import digitalio
#from hx711_spi import *
#from hx711 import *

#i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
# scan for I2C addresses
#I2C_ADDR = i2c.scan()[0]
#creaet an lcd object, 2 rows, 16 columns
#lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

import time
#import ticks_ms, ticks_diff, sleep, sleep_ms

pin_OUT = digitalio.DigitalInOut(board.GP16)
#pin_OUT.direction = digitalio.Direction.OUTPUT

pin_SCK = digitalio.DigitalInOut(board.GP17)
pin_SCK.direction = digitalio.Direction.OUTPUT

hx = HX711(pin_SCK, pin_OUT)
hx.OFFSET = 0 # -150000
hx.set_gain(128)
time.sleep(0.050)
scale = 25000.0

def getdata():
    while True:
        data = hx.read()/scale
        print(data) 
        time.sleep(.5)
       # lcd.putstr("Strain Gauge " +"\n")
       # lcd.putstr(str(data)+"\n")

        
if __name__=="__main__":
    print("NOT CALIBRATED!")
    getdata()
    