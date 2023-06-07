from microbit import *
import lights
import cars
import radio

radio.config(group=100)
radio.on()

while True:    
    message = radio.receive()
    if message=='A':
        lights.right_off()
        lights.left_on()
        cars.left(500)
    elif message=='B':
        lights.left_off()
        lights.right_on()
        cars.right(500)
    else:
        lights.left_off()
        lights.right_off()
        cars.stop()