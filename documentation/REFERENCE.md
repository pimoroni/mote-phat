# Mote pHAT Function Reference

## Clear All Channels
```python
motephat.clear()[source]
```
Clear the pixel buffer.

## Clear A Single Channel
```python
motephat.clear_channel(c)[source]
```
Clear a single channel.

Parameters:  
c – Channel to clear: 0 to 3

## Set A Pixel
```python
motephat.set_pixel(c, x, r, g, b, brightness=None)[source]
```
Set the RGB value, and optionally brightness, of a single pixel. If you don’t supply a brightness value, the last value will be kept.

Parameters:  
x – The horizontal position of the pixel: 0 to 7  
r – Amount of red: 0 to 255  
g – Amount of green: 0 to 255  
b – Amount of blue: 0 to 255  
brightness – Brightness: 0.0 to 1.0 (default around 0.2)  

## Set All Pixels
```python
motephat.set_all(r, g, b, brightness=None)[source]
```
Set the RGB value and optionally brightness of all pixels. If you don’t supply a brightness value, the last value set for each pixel be kept.

Parameters:  
r – Amount of red: 0 to 255  
g – Amount of green: 0 to 255  
b – Amount of blue: 0 to 255  
brightness – Brightness: 0.0 to 1.0 (default around 0.2)  

## Set Brightness
```python
motephat.set_brightness(brightness)[source]
```
Set the brightness of all pixels.

Parameters:  
brightness – Brightness: 0.0 to 1.0  

## Set Clear On Exit
```python
motephat.set_clear_on_exit(value=True)[source]
```
Set whether Mote pHAT should be cleared upon exit.

By default Mote pHAT will turn off the pixels on exit, but calling `blinkt.set_clear_on_exit(False)` will ensure that it does not.

Parameters:  
value – True or False (default True)  

## Show Buffer
```python
motephat.show()[source]
```
Output the buffer to Mote pHAT.
