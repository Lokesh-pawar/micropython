from time import sleep

from machine import Pin
from neopixel import NeoPixel

from brightness import adjust_brightness

N_LEDS = 36
LED_PIN = 29
BRIGHTNESS_PERCENT = 10

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

while True:
    for color in rainbow_colors:
        for led in range(N_LEDS):
            np[led] = adjust_brightness(color, BRIGHTNESS_PERCENT)
            np.write()
            sleep(0.1)
        for led in range(N_LEDS):
            np[led] = (0, 0, 0)
        np.write()
        sleep(0.5)
