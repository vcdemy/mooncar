from microbit import *

def left(v):
    pin2.write_analog(v)
    pin13.write_analog(0)
    pin8.write_analog(0)
    pin14.write_analog(0)

def right(v):
    pin2.write_analog(0)
    pin13.write_analog(0)
    pin8.write_analog(v)
    pin14.write_analog(0)

def forward(v):
    pin2.write_analog(v)
    pin13.write_analog(0)
    pin8.write_analog(v)
    pin14.write_analog(0)

def backward(v):
    pin2.write_analog(0)
    pin13.write_analog(v)
    pin8.write_analog(0)
    pin14.write_analog(v)


def stop():
    pin2.write_analog(0)
    pin13.write_analog(0)
    pin8.write_analog(0)
    pin14.write_analog(0)
