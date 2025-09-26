from random import randint
from time import sleep

from machine import Pin
from neopixel import NeoPixel

from brightness import adjust_brightness

N_LEDS = 36
LED_PIN = 29
BRIGHTNESS_PERCENT = 10
NO_COLOR = (0, 0, 0)  # Off

np = NeoPixel(Pin(LED_PIN), N_LEDS)

rainbow_colors = [
    (255, 0, 0),  # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (75, 0, 130),  # Indigo
    (148, 0, 211),  # Violet
]

order = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    17,
    18,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    24,
    23,
    12,
    11,
    10,
    9,
    8,
    7,
    16,
    19,
    28,
    27,
    26,
    25,
    22,
    13,
    14,
    15,
    20,
    21,
]

while True:
    for color in rainbow_colors:
        for led in order:
            np[led] = adjust_brightness(color, BRIGHTNESS_PERCENT)
            np.write()
            sleep(0.1)
        for led in range(N_LEDS):
            np[led] = adjust_brightness(color, BRIGHTNESS_PERCENT)
        np.write()
        sleep(0.1)
        for led in list(reversed(order)):
            np[led] = NO_COLOR
            np.write()
            sleep(0.1)
        for _ in range(N_LEDS):
            led = randint(0, N_LEDS - 1)
            np[led] = adjust_brightness(color, BRIGHTNESS_PERCENT)
            np.write()
            sleep(0.05)
        sleep(1)
