import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

CLR = ((0xFFFFFF), (0xFF0000), (0xFF6200), (0xFFFF00), (0x00FF00), (0x0000FF), (0x8800FF), (0xFF0088))
clr_selector = 0

pixels.brightness = .04

d4 = DigitalInOut(board.D4)
d5 = DigitalInOut(board.D5)
d4.switch_to_input(pull = Pull.DOWN)
d5.switch_to_input(pull = Pull.DOWN)

d4_read_old = d4.value
d5_read_old = d5.value

on = False

d4_timer = 0
d5_timer = 0

timer_threshold = 40

while True:
    d4_read = d4.value
    d5_read = d5.value

    if d4_read:
        d4_timer += 1
        if d4_timer > timer_threshold and on:
            if pixels.brightness < .08:
                pixels.brightness += .001

    if not d4_read:
        if d4_timer < timer_threshold:
            if d4_read_old:
                on = not on
        d4_timer = 0

    if on:
        pixels.fill(CLR[clr_selector])
    else:
        pixels.fill(0)

    if d5_read:
        d5_timer += 1
        if d5_timer > timer_threshold and on:
            if pixels.brightness > .008:
                pixels.brightness -= .001

    if not d5_read:
        if d5_timer < timer_threshold and on:
            if d5_read_old:
                if clr_selector < len(CLR) - 1:
                    clr_selector += 1
                else:
                    clr_selector = 0
        d5_timer = 0

    d4_read_old = d4_read
    d5_read_old = d5_read

    print("on state is", on)
    print("d4_timer is", d4_timer)
    print("d5_timer is", d5_timer)

    time.sleep(0.01)
