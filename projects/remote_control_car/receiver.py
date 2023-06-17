from microbit import *
import lights
import car
import radio

radio.config(group=100)
radio.on()

lights.front_on(100)
lights.rear_on(100)

while True:    
    message = radio.receive()
    if message=='A':
        lights.right_off()
        lights.left_on()
        car.left(500)
    elif message=='B':
        lights.left_off()
        lights.right_on()
        car.right(500)
    else:
        lights.left_off()
        lights.right_off()
        car.stop()