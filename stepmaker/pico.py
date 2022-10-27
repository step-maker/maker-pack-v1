from machine import Pin, ADC

class Temp(object):
    def __init__(self):
        self.raw_temp = ADC(4)
        self.conversion_factor = 3.44 / (65535)

    def measure(self):
        pico_temp = 27 - (self.raw_temp.read_u16() * self.conversion_factor - 0.706) / 0.001721
        return pico_temp

class Led(object):
    def __init__(self):
        self.pico_led = Pin(25, Pin.OUT)
        self.state = None

    def on(self):
        self.pico_led.high()
        self.state = True

    def off(self):
        self.pico_led.low()
        self.state = False