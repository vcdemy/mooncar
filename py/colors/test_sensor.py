# Imports go at the top
from microbit import *
import colors

sensors = colors.init_i2c()
sensor = sensors[0]
colors.setup(sensor)

while True:
    colors.light_on()
    sleep(1000)
    print(colors.read_color(sensor))
    colors.light_off()
    sleep(1000)