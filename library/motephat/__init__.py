import atexit
import RPi.GPIO as GPIO


DAT_PIN = 10
CLK_PIN = 11

CHANNEL_PINS = [8,7,25,24]

NUM_PIXELS_PER_CHANNEL = 16
NUM_CHANNELS = 4
BRIGHTNESS = 15
MAX_BRIGHTNESS = 0b01111


pixels = [
    [[0,0,0,BRIGHTNESS]] * NUM_PIXELS_PER_CHANNEL,
    [[0,0,0,BRIGHTNESS]] * NUM_PIXELS_PER_CHANNEL,
    [[0,0,0,BRIGHTNESS]] * NUM_PIXELS_PER_CHANNEL,
    [[0,0,0,BRIGHTNESS]] * NUM_PIXELS_PER_CHANNEL
]

channels = [(16, False) for c in range(NUM_CHANNELS)]

_gpio_setup = False
_clear_on_exit = True

def _exit():
    if _clear_on_exit:
        clear()
        show()
    GPIO.cleanup()

def configure_channel(channel, num_pixels, gamma_correction=False):
    global channels
    channels[channel - 1] = (num_pixels, False)

def get_pixel_count(channel):
    return channels[channel - 1][0]

def set_brightness(brightness):
    """Set the brightness of all pixels

    :param brightness: Brightness: 0.0 to 1.0
    """
    for c in range(NUM_CHANNELS):
        for x in range(NUM_PIXELS_PER_CHANNEL):
            pixels[c][x][3] = int(MAX_BRIGHTNESS * brightness) & MAX_BRIGHTNESS

def clear_channel(c):
    """Clear a single channel

    :param c: Channel to clear: 0 to 3
    """
    for x in range(NUM_PIXELS_PER_CHANNEL):
        pixels[c-1][x][0:3] = [0,0,0]

def clear():
    """Clear the pixel buffer"""
    for c in range(1, NUM_CHANNELS+1):
        clear_channel(c)

def _select_channel(c):
    for x in range(NUM_CHANNELS):
        GPIO.output(CHANNEL_PINS[x], GPIO.LOW if x==c else GPIO.HIGH)

def _write_byte(byte):
    for x in range(8):
        GPIO.output(DAT_PIN, byte & 0b10000000)
        GPIO.output(CLK_PIN, 1)
        byte <<= 1
        GPIO.output(CLK_PIN, 0)

# Emit exactly enough clock pulses to latch the small dark die APA102s which are weird
# for some reason it takes 36 clocks, the other IC takes just 4 (number of pixels/2)
def _eof():
    GPIO.output(DAT_PIN, 0)
    for x in range(36):
        GPIO.output(CLK_PIN, 1)
        GPIO.output(CLK_PIN, 0)

def _sof():
    GPIO.output(DAT_PIN,0)
    for x in range(32):
        GPIO.output(CLK_PIN, 1)
        GPIO.output(CLK_PIN, 0)

def show():
    """Output the buffer to Mote pHAT"""
    global _gpio_setup

    if not _gpio_setup:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup([DAT_PIN,CLK_PIN],GPIO.OUT)
        GPIO.setup(CHANNEL_PINS,GPIO.OUT)
        _gpio_setup = True

    for index, channel in enumerate(pixels):
        _select_channel(index)
        _sof()
        for pixel in channel:
            r, g, b, brightness = pixel
            _write_byte(0b11100000 | brightness)
            _write_byte(b)
            _write_byte(g)
            _write_byte(r)

        _eof()

def set_all(r, g, b, brightness=None):
    """Set the RGB value and optionally brightness of all pixels

    If you don't supply a brightness value, the last value set for each pixel be kept.

    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
    for c in range(1, NUM_CHANNELS+1):
        for x in range(NUM_PIXELS_PER_CHANNEL):
            set_pixel(c, x, r, g, b, brightness)

def get_pixel(c, x):
    return tuple(pixels[c-1][x])

def set_pixel(c, x, r, g, b, brightness=None):
    """Set the RGB value, and optionally brightness, of a single pixel
    
    If you don't supply a brightness value, the last value will be kept.

    :param x: The horizontal position of the pixel: 0 to 7
    :param r: Amount of red: 0 to 255
    :param g: Amount of green: 0 to 255
    :param b: Amount of blue: 0 to 255
    :param brightness: Brightness: 0.0 to 1.0 (default around 0.2)
    """
    c -= 1
    c %= NUM_CHANNELS
    x %= NUM_PIXELS_PER_CHANNEL

    if brightness is None:
        brightness = pixels[c][x][3]
    else:
        brightness = int(MAX_BRIGHTNESS * brightness) & MAX_BRIGHTNESS

    pixels[c][x] = [int(r) & 0xff,int(g) & 0xff,int(b) & 0xff,brightness]

def set_clear_on_exit(value=True):
    """Set whether Mote pHAT should be cleared upon exit

    By default Mote pHAT will turn off the pixels on exit, but calling::

        blinkt.set_clear_on_exit(False)

    Will ensure that it does not.

    :param value: True or False (default True)
    """
    global _clear_on_exit
    _clear_on_exit = value

atexit.register(_exit)

