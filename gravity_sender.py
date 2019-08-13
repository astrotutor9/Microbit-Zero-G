from microbit import *
from math import sqrt
import radio

radio.config(channel=7)
radio.on()

while True:
    x, y, z = accelerometer.get_values()
    gravity = round(sqrt((x**2)+(y**2)+(z**2)))
    radio.send(str(gravity))
    sleep(5)