#!/usr/bin/env python

import time
from colorsys import hsv_to_rgb

import motephat as mote


print("""Rainbow

Press Ctrl+C to exit.
""")

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

try:
    while True:
        h = time.time() * 50
        for channel in range(4):
            for pixel in range(16):
                hue = (h + (channel * 64) + (pixel * 4))
                hue = hue % 360
                hue = hue / 360.0
                r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]
                mote.set_pixel(channel + 1, pixel, r, g, b)
        mote.show()
        time.sleep(0.01)

except KeyboardInterrupt:
    mote.clear()
    mote.show()
