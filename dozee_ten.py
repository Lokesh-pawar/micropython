from time import sleep

from machine import Pin
from neopixel import NeoPixel

from brightness import adjust_brightness

N_LEDS = 36
LED_PIN = 29
BRIGHTNESS_PERCENT = 5
NO_COLOR = (0, 0, 0)  # Off
DOZEE_BLUE = (0, int(85 / 10), int(210 / 10))
COLOR_ORDER = [0, 11, 12, 23, 24, 35, 4, 3, 9, 14, 21, 26, 32, 31, 29, 18, 17, 6]


np = NeoPixel(Pin(LED_PIN), N_LEDS)


while True:
    for n in COLOR_ORDER:
        np[n] = adjust_brightness(DOZEE_BLUE, BRIGHTNESS_PERCENT)
        np.write()
        sleep(0.1)
    for _ in range(3):
        for n in COLOR_ORDER:
            np[n] = NO_COLOR
        np.write()
        sleep(0.3)
        for n in COLOR_ORDER:
            np[n] = adjust_brightness(DOZEE_BLUE, BRIGHTNESS_PERCENT)
        np.write()
        sleep(0.3)
        for n in COLOR_ORDER:
            np[n] = NO_COLOR
        np.write()
        sleep(0.3)
