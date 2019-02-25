#!/usr/bin/env python3

import math
import time

import motephat as mote

print("""
Mote pHAT: Pulse White

Pulse all LEDs white from 0, 0, 0 to 255, 255, 255
using a sine wave.

Press Ctrl+C to exit!

""")

try:
    while True:
        br = (math.sin(time.time()) + 1) / 2
        br *= 255.0
        br = int(br)
        mote.set_all(br, br, br)
        mote.show()
        time.sleep(0.01)

except KeyboardInterrupt:
    mote.clear()
    mote.show()
