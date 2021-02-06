from pico_i2c_lcd import I2cLcd
from machine import I2C
from machine import Pin
import utime as time

i2c = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16) # LCD 16x2

lcd.putstr('Hello World')
