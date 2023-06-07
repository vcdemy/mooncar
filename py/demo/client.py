from microbit import *
import lights
import cars
import radio

radio.config(group=100)
radio.on()

while True:
    if button_a.is_pressed():
        radio.send('A')
    if button_b.is_pressed():
        radio.send('B')
    