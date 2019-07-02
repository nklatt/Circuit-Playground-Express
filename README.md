# Circuit Playground Express
Repository of notes and code exploring the Circuit Playground Express et al

## Steps I took to get off the ground:

### 1. Update the bootloader

[Update the Bootloader](https://learn.adafruit.com/adafruit-circuit-playground-express/updating-the-bootloader)

Specifically, I updated to update-bootloader-circuitplay_m0-v3.3.0-adafruit.10.uf2

### 2. Install CircuitPython

There are two parallel resources for this on the AdaFruit site.

[CircuitPython](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart)

[Installing CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)

[Download CircuitPython for Circuit Playground Express](https://circuitpython.org/board/circuitplayground_express/)

Specifically, I installed adafruit-circuitpython-circuitplayground_express-en_US-4.0.2.uf2

### 3. Install CircuitPython libraries

These must be installed as-needed as there is not enough space for them all.

[AdaFruit CircuitPython Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/tag/20190627)

Specifically, I grabbed adafruit-circuitpython-bundle-4.x-mpy-20190627

### 4. Set up your editing and monitoring environment

The easiest way to accomplish this is reportedly to use the [Mu editor](https://codewith.mu) which completely writes files upon save and comes with a built-in monitor. I am just using Emacs to edit (which also completely writes upon save) and `screen /dev/tty.usbmodem14401 115200` in a terminal to monitor.

### 5. Install a program

Code should be in code.py on the board's root directory. (Actually it checks, in order, for code.txt, code.py, main.txt, main.py and loads/runs the first one it finds.

In this repo I am storing programs by name with a number (in order that I wrote them) and then a descriptive name. To install one of them, copy it to your board and rename it to code.py.

## References

[CircuitPython documentation](https://circuitpython.readthedocs.io/en/3.x/docs)
