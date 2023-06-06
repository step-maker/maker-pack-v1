from machine import Pin, PWM, I2C

def Find(i2c_num, i2c_sda, i2c_scl):
    i2c_info = I2C(i2c_num, sda = Pin(i2c_sda), scl = Pin(i2c_scl), freq = 400000)
        
    return I2C.scan(i2c_info)[0]
