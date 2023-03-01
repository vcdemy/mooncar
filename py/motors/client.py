# Imports go at the top
from microbit import *
import radio
radio.config(group=11)
radio.on()

# client
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send('a+b')
    elif button_a.is_pressed():
        radio.send('a')
    elif button_b.is_pressed():
        radio.send('b')
    elif pin_logo.is_touched():
        radio.send('c')
    sleep(100)