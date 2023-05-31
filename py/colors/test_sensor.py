# Imports go at the top
from microbit import *
import colors
import neopixel

sensors = colors.init_i2c()
sensor = sensors[0]
colors.setup(sensor)
np = neopixel.NeoPixel(pin12, 8)

np.fill((255, 0, 0))
np.show()

while True:
    colors.light_on()
    sleep(1000)
    color = colors.read_color(sensor)
    print(color)
    np.fill(color)
    np.show()
    colors.light_off()
    sleep(1000)