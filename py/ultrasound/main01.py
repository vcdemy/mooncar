# Imports go at the top
from microbit import *
import machine

display.off()

pin15.set_pull(pin15.NO_PULL)
pin16.set_pull(pin16.NO_PULL)

def distance():
    pin3.write_digital(1)
    pin3.write_digital(0)

    # 計算回傳時間 (us)
    micros = machine.time_pulse_us(pin9, 1)

    # 計算聲波打到障礙物的時間 (s)
    secs = micros / 2000000

    dist = 343 * 100 * secs
    return dist

# Code in a 'while True:' loop repeats forever
while True:
    p15 = pin15.read_digital()
    p16 = pin16.read_digital()

    if distance() < 10:
        pin2.write_analog(0)
        pin8.write_analog(0)
        sleep(1000)
        pin2.write_analog(200)
        pin8.write_analog(200)
    elif p15 and p16:
        pin8.write_analog(200)
        pin2.write_analog(200)
    elif p15:
        pin2.write_analog(200)
        pin8.write_analog(0)
    elif p16:
        pin2.write_analog(0)
        pin8.write_analog(200)
