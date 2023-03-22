# Imports go at the top
from microbit import *
import machine

display.off()

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
    if distance() < 15:
        pin2.write_analog(0)
        pin8.write_analog(0)
        sleep(100)
        pin13.write_analog(200)
        pin14.write_analog(200)
        sleep(500)
        pin2.write_analog(500)
        pin8.write_analog(0)
        pin13.write_analog(0)
        pin14.write_analog(00)
        sleep(1000)
        pin2.write_analog(500)
        pin8.write_analog(500)
    else:
        pin2.write_analog(500)
        pin8.write_analog(500)