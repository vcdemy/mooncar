from microbit import *

pin15.set_pull(pin15.NO_PULL)
pin16.set_pull(pin16.NO_PULL)


def is_left_off():
    return pin15.read_digital()


def is_right_off():
    return pin16.read_digital()
