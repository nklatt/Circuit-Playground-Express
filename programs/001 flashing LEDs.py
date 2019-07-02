import board
import digitalio
import time
import random
import neopixel

led13 = digitalio.DigitalInOut(board.D13)
led13.direction = digitalio.Direction.OUTPUT

buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)
pixels.fill((0, 0, 0))
pixels.show()

a = True
b = True

led13_value = False

neopixel_OFF = 0x000000
neopixel_ON = (0, 0x09, 0x09)

neopixel8_value = neopixel_OFF

while True:

    if buttonA.value:
        a = not(a)

    if buttonB.value:
        b = not(b)

    if a:
        neopixel8_value = neopixel_ON if neopixel8_value == neopixel_OFF else neopixel_OFF
    else:
        neopixel8_value = neopixel_OFF
    pixels[8] = neopixel8_value

    if b:
        led13_value = not(led13_value)
    else:
        led13_value = False
    led13.value = led13_value

    time.sleep(0.5)
