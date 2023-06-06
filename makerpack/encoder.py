import utime
import machine

class Pin(object):
    def __init__(self, CLK, DT, SW):
        self.CLK = machine.Pin(CLK, machine.Pin.IN, machine.Pin.PULL_UP)
        self.DT = machine.Pin(DT, machine.Pin.IN, machine.Pin.PULL_UP)
        self.SW = machine.Pin(SW, machine.Pin.IN, machine.Pin.PULL_UP)
        
        self.value = 0
        self.click_value = 0
        self.direction = None
        self.previousValue = self.CLK.value()
        self.state = False
        
    def rotate(self):
        if self.previousValue != self.CLK.value():
            if self.DT.value() != self.CLK.value():

                self.value = (self.value + .5)
                self.direction = "right"
          
            else:
                self.value = (self.value - .5)
                self.direction = "left"

                
        self.previousValue = self.CLK.value()
        return int(round(self.value))
    
    def direction(self):
        if self.previousValue != self.CLK.value():
            if self.DT.value() != self.CLK.value():

                return "right"
          
            else:
                return "left"

                
        self.previousValue = self.CLK.value()
        
        
        
        
        
        
    def rotate2(self):
        if self.previousValue != self.CLK.value():
            if self.CLK.value() == 0:
                if self.DT.value() == 0:
                    self.value = self.value - 1
                else:
                    self.value = self.value + 1               
            self.previousValue = self.CLK.value()       
        return self.value
    
    
    def direction2(self):
        if self.previousValue != self.CLK.value():
            if self.CLK.value() == 0:
                if self.DT.value() == 0:
              
                    return "right"
                    
                else:
            
                    
                    return "left"
                                    
            self.previousValue = self.CLK.value()
        
        
        
        
        
        
    def click(self, interval):
        if self.SW.value() == 0:
            if self.state == False:
                self.start_time = utime.ticks_ms()
                self.state = True
                
            elif utime.ticks_ms() >= self.start_time + interval:
                self.click_value = self.click_value + 1
                self.value = 0
                self.state = False
                return True
        else:
            self.state = False
            
            
    def remove_rotate_value(self):
        self.value = 0
        
    def remove_click_value(self):
        self.click_value = 0