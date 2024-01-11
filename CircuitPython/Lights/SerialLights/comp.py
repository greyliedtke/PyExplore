"""
file for writing commands over serial on computer
sudo chmod a+rw /dev/ttyACM0
"""

import SubProjects.Serial.read_serial as read_serial
import time

ser = read_serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Change the serial port as necessary

while True:
    # Prompt the user to enter an RGB color
    color_str = input('Enter an RGB color (comma-separated values between 0 and 255): ')
    color = color_str.split(',')
    if len(color) != 3:
        print('Invalid input. Please enter three comma-separated values between 0 and 255.')
        continue
    try:
        r = int(color[0])
        g = int(color[1])
        b = int(color[2])
    except ValueError:
        print('Invalid input. Please enter three comma-separated values between 0 and 255.')
        continue

    # Send the color over the serial connection
    ser.write(bytes([r, g, b]))
    time.sleep(0.1)
