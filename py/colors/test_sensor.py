# Imports go at the top
from microbit import *
import colors
import neopixel

sensors = colors.init_i2c()
sensor = sensors[0]
colors.setup(sensor)
np = neopixel.NeoPixel(pin12, 8)

while True:
    colors.light_on()
    sleep(1000)
    color = colors.read_color(sensor)
    print(color)
    if (54 < color[0] < 74) and (48 < color[1] < 68) and (89 < color[2] < 109):
        np.fill((27, 8, 31))
    elif (140 < color[0] < 160) and (208 < color[1] < 228) and (80 < color[2] < 100):
        np.fill((200, 200, 0))
    elif (72 < color[0] < 92) and (28 < color[1] < 48) and (27 < color[2] < 47):
        np.fill((200, 0, 0))
    elif (143 < color[0] < 163) and (0 < color[1] < 20) and (0 < color[2] < 20):
        np.fill((100, 100, 100))
    else:
        np.fill(color)
    np.show()
    colors.light_off()
    sleep(1000)
