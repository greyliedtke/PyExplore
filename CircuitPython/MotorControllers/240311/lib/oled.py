import board, busio, displayio, terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import time

displayio.release_displays()
time.sleep(.5)
print('init')
i2c = busio.I2C (scl=board.GP15, sda=board.GP14) # This RPi Pico way to call I2C<br>
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
WIDTH, HEIGHT, BORDER= 128, 32, 5
oled_display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
splash = displayio.Group()
oled_display.show(splash)


def oled_text(text):
    newt = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1)
    oled_display.show(newt)
    oled_display.refresh() 