import utime
import machine

class Pin(object):
    def __init__(self, pin):
        self.buzzer = machine.PWM(machine.Pin(pin))
        
    def beep(self, beat, power, duration):
        self.buzzer.freq(beat)
        self.buzzer.duty_u16((power*200))
        utime.sleep(duration)
        self.buzzer.duty_u16(0)
