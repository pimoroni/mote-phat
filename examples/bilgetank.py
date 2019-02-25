#!/usr/bin/env python

import math
import time
from colorsys import hsv_to_rgb

import motephat


print("""#BilgeTank

This is the lighting script we use to run the shelves in BilgeTank.

It uses a simple Sine wave to sweep gently between greeny blue
and blue, giving a nice oceanic effect!

This is achieved by moving around a portion of a hue wheel,
defined by hue_start and hue_range.

Press Ctrl+C to clear and exit.
""")

# The hue wheel is 360 degrees around, with;
# 0 = Red
# 40ish = Orange
# 120 = Green
# 180 = Teal
# 240 = Blue
# 300 = Purple

hue_start = 160
hue_range = 80
speed = 1

motephat.configure_channel(1, 16, False)
motephat.configure_channel(2, 16, False)
motephat.configure_channel(3, 16, False)
motephat.configure_channel(4, 16, False)

try:
    while True:
        phase = 0
        for channel in [1, 2, 3, 4]:
            for pixel in range(motephat.get_pixel_count(channel)):
                h = (time.time() * speed) + (phase / 10.0)
                h = math.sin(h) * (hue_range / 2)
                hue = hue_start + (hue_range / 2) + h
                hue %= 360
                hue /= 360.0

                r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]
                motephat.set_pixel(channel, pixel, r, g, b)

                phase += 1

        motephat.show()
        time.sleep(0.01)

except KeyboardInterrupt:
    motephat.clear()
    motephat.show()
