from machine import Pin
from time import sleep
from neopixel import NeoPixel

from brightness import adjust_brightness

N_LEDS = 36
LED_PIN = 29
BRIGHTNESS_PERCENT = 10
DARK_GREY = (0, 0, 153)
NO_COLOR = (0, 0, 0)  # Off
DARK_GREEN = (0, 204, 0)

FACE_COLOR_ORDER = [10, 7, 14, 15, 22, 21, 20, 19, 25, 26, 27, 28, 34, 31]

np = NeoPixel(Pin(LED_PIN), N_LEDS)

def face_on():
    for n in range(N_LEDS):
        if n in FACE_COLOR_ORDER:
            np[n] = adjust_brightness(DARK_GREY, BRIGHTNESS_PERCENT)
        else:
            np[n] = DARK_GREEN
    np.write()
    sleep(0.5)

def face_off():
    for n in range(N_LEDS):
        np[n] = NO_COLOR
    np.write()
    sleep(0.5)

if __name__ == "__main__":
    while True:
        face_on()
        sleep(2)
        face_off()
        sleep(2)