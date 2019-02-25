#!/usr/bin/env python

import sys
import time

import motephat


motephat.set_brightness(1)
motephat.set_clear_on_exit(True)


def usage():
    print("Usage: {} <r> <g> <b>".format(sys.argv[0]))
    sys.exit(1)


if len(sys.argv) != 4:
    usage()

# Exit if non integer value. int() will raise a ValueError
try:
    r, g, b = [int(x) for x in sys.argv[1:]]
except ValueError:
    usage()

# Exit if any of r, g, b are greater than 255
if max(r, g, b) > 255:
    usage()

print("""
Mote pHAT: RGB

Setting Mote to {r},{g},{b}"

Press Ctrl+C to exit!

""".format(r=r, g=g, b=b))

while True:

    for channel in range(4):
        for pixel in range(16):
            motephat.set_pixel(channel + 1, pixel, r, g, b)
        time.sleep(0.01)

    motephat.show()
