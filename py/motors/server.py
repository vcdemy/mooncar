# Imports go at the top
from microbit import *
import neopixel
import radio
radio.config(group=11)
radio.on()

# server

np = neopixel.NeoPixel(pin12, 8)

while True:
    message = radio.receive()
    if message=="b":
        pin8.write_analog(512)
        pin14.write_analog(0)
        np[1] = (100, 100, 0)
        np[4] = (0, 0, 0)
        np[5] = (0, 0, 0)
        np[8] = (100, 100, 0)
    elif message=="a":
        pin2.write_analog(512)
        pin13.write_analog(0)
        np[1] = (0, 0, 0)
        np[4] = (100, 100, 0)
        np[5] = (100, 100, 0)
        np[8] = (0, 0, 0)
    elif message=="a+b":
        pin8.write_analog(512)
        pin14.write_analog(0)
        pin2.write_analog(512)
        pin13.write_analog(0)
        np[1] = (0, 0, 0)
        np[4] = (0, 0, 0)
        np[5] = (0, 0, 0)
        np[8] = (0, 0, 0)
    elif message=='c':
        pin8.write_analog(0)
        pin14.write_analog(512)
        pin2.write_analog(0)
        pin13.write_analog(512)
        np[1] = (0, 0, 0)
        np[4] = (0, 0, 0)
        np[5] = (0, 0, 0)
        np[8] = (0, 0, 0)
    else:
        pin8.write_analog(0)
        pin14.write_analog(0)
        pin2.write_analog(0)
        pin13.write_analog(0)
        np[1] = (0, 0, 0)
        np[4] = (0, 0, 0)
        np[5] = (0, 0, 0)
        np[8] = (0, 0, 0)
    np.show()
    sleep(100)