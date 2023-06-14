from microbit import *
import machine

display.off()

def distance():
    # Trigger Ultrasound Wave
    pin3.write_digital(1)
    pin3.write_digital(0)

    micros = machine.time_pulse_us(pin9, 1)
    v = 340 * 100 / 1000000  # cm/us
    d = micros / 2 * v       # distance in cm
    return d