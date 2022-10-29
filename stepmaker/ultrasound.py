import machine
import utime
from micropython import const

class Pin(object):
    def __init__(self, echo, trig):
        self.echo = machine.Pin(echo, machine.Pin.IN)
        self.trig = machine.Pin(trig, machine.Pin.OUT)

    def measure(self):
        self.trig.low()
        utime.sleep_us(2)
        self.trig.high()
        utime.sleep_us(5)
        self.trig.low()
        while self.echo.value() == 0:
            signaloff = utime.ticks_us()
        while self.echo.value() == 1:
            signalon = utime.ticks_us()
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2 * 10

        filter_distance = distance
        filter_distance = filter_distance * (1-0.5) + distance * 0.5
        
        return filter_distance

