# script for solar charger
print('Solar Project')

# imports
import board
import displayio
import analogio
import terminalio
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import time

# init OLED
def init_display():
    displayio.release_displays()
    i2c = busio.I2C (scl=board.GP17, sda=board.GP16) # This RPi Pico way to call I2C<br>
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    WIDTH, HEIGHT, BORDER= 128, 32, 5
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
    splash = displayio.Group()
    display.show(splash)
    return display
oled_disp = init_display()

def oled_text(text):
    newt = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1)
    # splash.append(text_area)
    oled_disp.show(newt)
    oled_disp.refresh() 

sensor = analogio.AnalogIn(board.A0)
r1, r2 = 220000, 147000

def read_v():
    # 0 to 65535. # raw v value # read ai26, A0
    v_read = sensor.value
    v_read = (v_read * 3.3 / 65535)
    # converting to 5 volt from voltage divider equation...
    v_batt = v_read * (r1+r2) / r2
    v_batt = round(v_batt, 2) - .15 # accounting for offset
    return v_batt

while True:
    time.sleep(1)
    v_read = read_v()
    oled_text(f"voltage: {v_read}")