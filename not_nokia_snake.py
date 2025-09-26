from random import randint
from time import sleep

from machine import Pin
from neopixel import NeoPixel

from brightness import adjust_brightness

N_LEDS = 36
N_COLUMNS = 6
LED_PIN = 29
BRIGHTNESS_PERCENT = 5  # It's overridden in the function
NO_COLOR = (0, 0, 0)  # Off
START = (0, 255, 0)  # Green color
END = (255, 0, 0)  # Red color
PATH = (0, 0, 255)  # Blue color

LED_MATRIX = [
    [0, 1, 2, 3, 4, 5],
    [11, 10, 9, 8, 7, 6],
    [12, 13, 14, 15, 16, 17],
    [23, 22, 21, 20, 19, 18],
    [24, 25, 26, 27, 28, 29],
    [35, 34, 33, 32, 31, 30],
]

np = NeoPixel(Pin(LED_PIN), N_LEDS)


def determine_path(start: list[int], goal: list[int]) -> list[int]:
    if start[0] == goal[0]:
        if start[1] < goal[1]:
            return LED_MATRIX[start[0]][start[1] : goal[1] + 1]
        else:
            return list(reversed(LED_MATRIX[start[0]][goal[1] : start[1] + 1]))
    elif start[1] == goal[1]:
        if start[0] < goal[0]:
            return [LED_MATRIX[i][start[1]] for i in range(start[0], goal[0] + 1)]
        else:
            return list(
                reversed(
                    [LED_MATRIX[i][start[1]] for i in range(goal[0], start[0] + 1)]
                )
            )
    else:
        if start[0] < goal[0]:
            vertical_path = [
                LED_MATRIX[i][start[1]] for i in range(start[0], goal[0] + 1)
            ]
        else:
            vertical_path = list(
                reversed(
                    [LED_MATRIX[i][start[1]] for i in range(goal[0], start[0] + 1)]
                )
            )
        if start[1] < goal[1]:
            horizontal_path = LED_MATRIX[goal[0]][start[1] : goal[1] + 1]
        else:
            horizontal_path = list(
                reversed(LED_MATRIX[goal[0]][goal[1] : start[1] + 1])
            )
        return vertical_path + horizontal_path[1:]


def let_snake_move():
    BRIGHTNESS_PERCENT = 5
    start = [randint(0, N_COLUMNS - 1), randint(0, N_COLUMNS - 1)]
    destination = [randint(0, N_COLUMNS - 1), randint(0, N_COLUMNS - 1)]
    led_trail = determine_path(start, destination)
    while True:
        while start == destination:
            destination = [randint(0, N_COLUMNS - 1), randint(0, N_COLUMNS - 1)]
        np[led_trail[0]] = adjust_brightness(START, BRIGHTNESS_PERCENT)
        np[led_trail[-1]] = adjust_brightness(END, BRIGHTNESS_PERCENT)
        np.write()
        sleep(0.2)
        print(f"From {start} to {destination}: {led_trail}")
        for led in led_trail[1:]:
            BRIGHTNESS_PERCENT += 9  # LONGEST PATH INCLUDES 10 LEDS
            np[led] = adjust_brightness(PATH, BRIGHTNESS_PERCENT)
            np.write()
            sleep(0.2)
        sleep(0.6)
        start = destination
        destination = [randint(0, N_COLUMNS - 1), randint(0, N_COLUMNS - 1)]
        led_trail = determine_path(start, destination)
        for led in range(N_LEDS):
            if led not in [led_trail[0], led_trail[-1]]:
                np[led] = adjust_brightness(NO_COLOR, BRIGHTNESS_PERCENT)
                np.write()
            else:
                np[led_trail[-1]] = adjust_brightness(END, BRIGHTNESS_PERCENT)
                np[led_trail[0]] = adjust_brightness(START, BRIGHTNESS_PERCENT)
                np.write()
        BRIGHTNESS_PERCENT = 5
        sleep(0.2)


let_snake_move()
