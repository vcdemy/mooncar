from microbit import *


def init_i2c():
    i2c.init()
    sensors = i2c.scan()
    return sensors


def setup(sensor):
    i2c.write(sensor, bytes([0x81, 0xfc]))
    i2c.write(sensor, bytes([0x80, 0x03]))


def light_on():
    # 打開補光燈
    pin11.set_pull(pin11.PULL_DOWN)


def light_off():
    pin11.set_pull(pin11.PULL_UP)


def read_color(sensor):
    i2c.write(sensor, bytes([178]))
    i2c.write(sensor, bytes([179]))
    i2c.write(sensor, bytes([182]), True)
    R = int.from_bytes(i2c.read(sensor, 2), 'big')
    R = int(R/65536*255)
    i2c.write(sensor, bytes([184]), True)
    G = int.from_bytes(i2c.read(sensor, 2), 'big')
    G = int(G/65536*255)
    i2c.write(sensor, bytes([186]), True)
    B = int.from_bytes(i2c.read(sensor, 2), 'big')
    B = int(B/65536*255)

    return R, G, B