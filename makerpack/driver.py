import utime
from micropython import const
import machine

class Pin(object):
    def __init__(self, InA, InB, PWM1):
        self.state = False
        self.InA = machine.Pin(InA, machine.Pin.OUT)
        self.InB = machine.Pin(InB, machine.Pin.OUT)
        self.EN = machine.PWM(machine.Pin(PWM1))
        self.EN.freq(30000)

    def on(self, power):
        self.InA.high()
        self.InB.low()
        self.EN.duty_u16(int(power*655.35))
        self.state = True

    def off(self):
        self.InA.low()
        self.InB.low()
        self.state = False

    def slow_on(self, power):
        for power in range(0, power+1, 5):
            self.InA.high()
            self.InB.low()
            self.EN.duty_u16(int(power*655.35))
            utime.sleep_ms(25)
            self.state = True
    
    def slow_off(self):
        for power in range(100, -1, -5):
            self.InA.high()
            self.InB.low()
            self.EN.duty_u16(int(power*655.35))
            utime.sleep_ms(25)
            self.state = False
