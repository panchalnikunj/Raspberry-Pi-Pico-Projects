from machine import I2C, Pin
from urtc import DS1307
import utime
from pico_i2c_lcd import I2cLcd

i2c_lcd = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)

lcd = I2cLcd(i2c_lcd, 0x27, 2, 16)

i2c_rtc = I2C(0,scl = Pin(1),sda = Pin(0),freq = 400000)
result = I2C.scan(i2c_rtc)
rtc = DS1307(i2c_rtc)

while True:
    (year,month,date,day,hour,minute,second,p1)=rtc.datetime()
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Time:")
    lcd.move_to(6,0)
    lcd.putstr(str(hour) + ":" + str(minute) + ":" + str(second))
    lcd.move_to(0,1)
    lcd.putstr("Date:")
    lcd.move_to(6,1)
    lcd.putstr(str(date) + "/" + str(month) + "/" + str(year))
    utime.sleep(1)
