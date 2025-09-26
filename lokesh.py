from time import sleep

from machine import Pin
from neopixel import NeoPixel

from brightness import adjust_brightness

N_LEDS = 36
LED_PIN = 29
BRIGHTNESS_PERCENT = 10
COLOR = (0, 0, 255)  # Blue color
NO_COLOR = (0, 0, 0)  # Off


np = NeoPixel(Pin(LED_PIN), N_LEDS)

lokesh = [
    [1, 10, 13, 22, 25, 26, 27],  # L
    [1, 2, 3, 8, 15, 20, 27, 26, 25, 22, 13, 10],  # O
    [1, 10, 13, 22, 25, 9, 3, 21, 27],  # K
    [3, 2, 1, 10, 13, 22, 25, 26, 27, 14],  # E
    [3, 2, 1, 10, 13, 14, 15, 20, 27, 26, 25],  # S
    [1, 10, 13, 22, 25, 14, 15, 3, 8, 20, 27],  # H
]

while True:
    for pattern in lokesh:
        for led in pattern:
            np[led] = adjust_brightness(COLOR, BRIGHTNESS_PERCENT)
            np.write()
            sleep(0.2)
        for led in pattern:
            np[led] = adjust_brightness(COLOR, BRIGHTNESS_PERCENT)
        np.write()
        sleep(0.2)
        for led in list(reversed(pattern)):
            np[led] = adjust_brightness(NO_COLOR, BRIGHTNESS_PERCENT)
            np.write()
            sleep(0.2)
