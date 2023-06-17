from microbit import *
import neopixel

np = neopixel.NeoPixel(pin12, 8)


def all_on(b):
    front_on(b)
    rear_on(b)
    left_on()
    right_on()
    np.show()


def all_on(v):
    np.clear()
    np.show()


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

def front_on(b):
    np[1] = (b, b, b)
    np[2] = (b, b, b)
    np.show()

def front_off():
    np[1] = (0, 0, 0)
    np[2] = (0, 0, 0)
    np.show()

def rear_on(b):
    np[5] = (b, 0, 0)
    np[6] = (b, 0, 0)
    np.show()

def rear_off():
    np[5] = (0, 0, 0)
    np[6] = (0, 0, 0)
    np.show()