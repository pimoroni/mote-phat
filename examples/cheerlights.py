#!/usr/bin/env python

import time
from sys import exit

try:
    import requests
except ImportError:
    exit("""This script requires the requests module.
Install with: sudo pip install requests""")

import motephat


print("""
Mote pHAT: Cheerlights

Display colours from the cheerlights API.

Press Ctrl+C to exit!

""")


motephat.set_brightness(1)

num_pixels = 16

motephat.configure_channel(1, num_pixels, False)
motephat.configure_channel(2, num_pixels, False)
motephat.configure_channel(3, num_pixels, False)
motephat.configure_channel(4, num_pixels, False)


try:
    while True:
        r = requests.get('http://api.thingspeak.com/channels/1417/feed.json')
        j = r.json()
        f = j['feeds'][-8:]

        f = [element for index, element in enumerate(f) if index % 2 == 0]

        print(f)

        channel = 1
        for col in f:
            col = col['field2']
            r, g, b = tuple(ord(c) for c in col[1:].lower().decode('hex'))
            for pixel in range(motephat.get_pixel_count(channel)):
                motephat.set_pixel(channel, pixel, r, g, b)
            channel += 1

        motephat.show()

        time.sleep(5)

except KeyboardInterrupt:
    motephat.clear()
    motephat.show()
    time.sleep(0.1)
