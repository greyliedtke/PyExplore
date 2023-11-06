# import serial
import board
import neopixel
import time

# Configure the serial connection ------chat answer
# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

import board
import busio
import digitalio

# For most CircuitPython boards:
led = digitalio.DigitalInOut(board.LED)
# For QT Py M0:
# led = digitalio.DigitalInOut(board.SCK)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.TX, board.RX, baudrate=9600)



# Configure the RGB LED
pixel_pin = board.GP0
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

while True:
    # Read an RGB color from the serial connection
    try:
        color = ser.read(3)
        print(color)
    except serial.serialutil.SerialException:
        continue
    if not color:
        continue

    # Display the color on the RGB LED
    pixels.fill(color)
    pixels.show()
    time.sleep(0.1)
