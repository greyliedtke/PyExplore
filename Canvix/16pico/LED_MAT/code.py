# from CaveMan import cm, game_l
# from PingMan import pm
# from ClockMan import clock
from Mat import characters
import time
print("greyma")

import board
import neopixel
from adafruit_pixel_framebuf import PixelFramebuffer

pixels = neopixel.NeoPixel(board.GP2, 256, auto_write=False, brightness=.1)

pixels.fill([255,0,0])
pixels.show()

time.sleep(10)
pixel_framebuf = PixelFramebuffer(
    pixels,
    16,
    16,
    reverse_x=True,
)

for r in range(16):
    for p in range(8):
        pixel_framebuf.pixel(r, p, 0xFF0000)

pixel_framebuf.display()

pixel_framebuf.text("22:", 0, 0, 0x00FF00)
pixel_framebuf.display()

cx,cy = characters[6].char_matrix(6)
for i,c in enumerate(cx):
    pixel_framebuf.pixel(c, cy[i], 0x00FF00)
pixel_framebuf.display()


# game mode
game_mode = "Clock"
game_mode = "Char"

# Function to update the scatter plot
# def update():
#     

#     # if game_mode == "Clock":
#     #     clock.loop()
        
# while True:
#     update()
#     time.sleep(1)