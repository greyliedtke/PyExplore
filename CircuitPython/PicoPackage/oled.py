import board, busio, displayio, terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
WIDTH, HEIGHT, BORDER= 128, 32, 5

def init_i2c(scl_pin, sda_pin):
    displayio.release_displays()
    i2c = busio.I2C(scl=scl_pin, sda=sda_pin) # This RPi Pico way to call I2C<br>
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    oled_display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
    splash = displayio.Group()
    oled_display.show(splash)
    return oled_display


def oled_text(oled_display, text):
    newt = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1)
    oled_display.show(newt)
    oled_display.refresh() 

def oled_2_line(oled_display, l1, l2):
    line_1 = label.Label(terminalio.FONT, text=l1, color=0xFFFFFF, x=7, y=8)
    line_2 = label.Label(terminalio.FONT, text=l2, color=0xFFFFFF, x=7, y=16)
    line_1.append(line_2)
    oled_display.show(line_1)
    oled_display.refresh()