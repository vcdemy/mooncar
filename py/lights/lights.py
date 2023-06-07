from microbit import *
import neopixel

np = neopixel.NeoPixel(pin12, 8)

def left_on():
    np[3] = (255, 100, 0)
    np[4] = (255, 100, 0)
    np.show()

def left_off():
    np[3] = (0, 0, 0)
    np[4] = (0, 0, 0)
    np.show()

def right_on():
    np[0] = (255, 100, 0)
    np[7] = (255, 100, 0)
    np.show()

def right_off():
    np[0] = (0, 0, 0)
    np[7] = (0, 0, 0)
    np.show()

def front_on(v):
    np[1] = (v, v, v)
    np[2] = (v, v, v)
    np.show()

def front_off():
    np[1] = (0, 0, 0)
    np[2] = (0, 0, 0)
    np.show()

def back_on(v):
    np[5] = (v, 0, 0)
    np[6] = (v, 0, 0)
    np.show()

def back_off():
    np[5] = (0, 0, 0)
    np[6] = (0, 0, 0)
    np.show()

