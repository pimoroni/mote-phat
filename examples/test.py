import colorsys

import motephat

offset = 0

while True:
    offset += 1
    for channel in range(4):
        for pixel in range(16):
            hue = offset + (10 * (channel * 16) + pixel)
            hue %= 360
            hue /= 360.0

            r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
            motephat.set_pixel(channel+1, pixel, r, g, b)

    motephat.show()
