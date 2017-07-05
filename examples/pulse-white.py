#!/usr/bin/env python

import colorsys
import math
import time

import motephat


motephat.set_brightness(1)

while True:
    br = (math.sin(time.time()) + 1) / 2
    br *= 255.0
    br = int(br)

    for channel in range(1,5):
        for pixel in range(16):
            motephat.set_pixel(channel, pixel, br, br, br)

    motephat.show()
