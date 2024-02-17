# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import keyboard


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 300

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.7, auto_write=False, pixel_order=ORDER
)

i = -1

pixels.fill((0, 0, 0))
pixels.show()    

while True:
    if keyboard.read_key() == "n":
        i = i + 1
        pixels[i - 1] = (0,0,0)
        pixels[i] = (255,255,255)
        print("i = {i}".format(i=i))
        pixels.show()
    if keyboard.read_key() == "p":
        i = i - 1
        pixels[i + 1] = (0,0,0)
        pixels[i] = (255,255,255)
        print("i = {i}".format(i=i))
        pixels.show()
    

