#!/usr/bin/python3
""" Example of the Wargames' WOPR 8x8 LED matrix dispplay class """

from threading import Lock

from Adafruit_Python_LED_Backpack.Adafruit_LED_Backpack import BicolorMatrix8x8

from led8x8controller.led8x8controller import Led8x8Controller

if __name__ == '__main__':
    LOCK = Lock()
    CONTROLLER = Led8x8Controller(LOCK)
    CONTROLLER.run()
    while True:
        choice = raw_input("> ")
        if choice == 'x' :
            print("exiting")
            break