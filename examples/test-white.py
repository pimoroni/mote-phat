import colorsys

import motephat

motephat.set_brightness(1)

offset = 0

while True:
    offset += 1
    for channel in range(4):
        for pixel in range(16):
            motephat.set_pixel(channel, pixel, 255, 255, 255)

    motephat.show()
