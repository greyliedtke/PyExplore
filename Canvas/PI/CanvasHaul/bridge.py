"""
control lights and more eventually...
"""

from MatMap.led_strip import strip

for p in range(256, 350):
    strip[p] = [210, 65, 0]
strip.show()
