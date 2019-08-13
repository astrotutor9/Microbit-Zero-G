from microbit import *
from math import sqrt
import radio

radio.config(channel=7)
radio.on()
display.scroll("Go")

while True:
    message = radio.receive()
    if message:
        message = (int(message))
        print((message,))