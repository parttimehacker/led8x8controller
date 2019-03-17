#!/usr/bin/python3
""" Control the display of an Adafruit 8x8 LED backpack """

import led8x8idle.Led8x8Idle
import led8x8flash.Led8x8Flash

IDLE_MODE = 0
FIRE_MODE = 1
PANIC_MODE = 2
FIBINACCI_MODE = 3
WOPR_MODE = 4
PRIME_MODE = 5

class Led8x8Controller:
    """ Idle or sleep pattern """

    def __init__(self, lock):
        """ create initial conditions and saving display and I2C lock """
        self.bus_lock = lock
        self.bus_lock.acquire(True)
        self.idle = Led8x8Idle()
        self.fire = Led8x8Flash(RED)
        self.panic = LED8x8Flash(YELLOW)
        self.bus_lock.release()

    def reset(self,):
        """ initialize to starting state and set brightness """
        self.bus_lock.acquire(True)
        self.bus_lock.release()

    def display_thread(self,):
        """ display the series as a 64 bit image with alternating colored pixels """
        while True:
            if self.mode == IDLE_MODE:
                self.idle.display()
            elif self.mode == FIRE_MODE:
            	self.fire.display()
            elif self.mode == PANIC_MODE:
            	self.panic.display()

    def setMode(self, mode):
        self.busLock.acquire(True)
        self.lastMode = self.mode
        self.busLock.release()

    def restoreMode(self,):
        self.busLock.acquire(True)
        self.mode = self.lastMode
        self.busLock.release()

    def run(self):
        display = Thread(target=self.display_thread )
        display.start()

if __name__ == '__main__':
    exit()
