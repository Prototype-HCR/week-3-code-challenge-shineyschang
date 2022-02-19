import board
import time
import neopixel
import touchio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

pixels.brightness = .04

a1 = touchio.TouchIn(board.A1)
a2 = touchio.TouchIn(board.A2)
a3 = touchio.TouchIn(board.A3)
a4 = touchio.TouchIn(board.A4)
a5 = touchio.TouchIn(board.A5)
a6 = touchio.TouchIn(board.A6)
tx = touchio.TouchIn(board.TX)

a1_read_old = a1.value

on = False

red = 255
green = 255
blue = 255

while True:
    a1_read = a1.value
    a2_read = a2.value
    a3_read = a3.value
    a4_read = a4.value
    a5_read = a5.value
    a6_read = a6.value
    tx_read = tx.value

    if a1_read:
        if not a1_read_old:
            on = not on

    a1_read_old = a1_read

    if on:
        pixels.fill((red, green, blue))

        if a2_read:
            if red > 10:
                red -= 4
        if a3_read:
            if red < 250:
                red += 4

        if a4_read:
            if green > 10:
                green -= 4
        if a5_read:
            if green < 250:
                green += 4

        if a6_read:
            if blue > 10:
                blue -= 4
        if tx_read:
            if blue < 250:
                blue += 4
    else:
        pixels.fill(0)

    print("on is", on)
    print("red is", red)
    print("green is", green)
    print("blue is", blue)

    time.sleep(0.01)
