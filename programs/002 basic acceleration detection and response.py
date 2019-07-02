import board
import time

from adafruit_circuitplayground.express import cpx

cpx.pixels.fill(0x000000)

while True:

    x, y, z = cpx.acceleration

#    print((x, y, z))

    cpx.pixels[0] = (0, 0x20, 0) if x > 2 else (0x20, 0, 0) if x < -2 else (0, 0, 0)
    cpx.pixels[1] = (0, 0x20, 0) if y > 2 else (0x20, 0, 0) if y < -2 else (0, 0, 0)
    cpx.pixels[2] = (0, 0x20, 0) if z > 2 else (0x20, 0, 0) if z < -2 else (0, 0, 0)

    time.sleep(0.1)
