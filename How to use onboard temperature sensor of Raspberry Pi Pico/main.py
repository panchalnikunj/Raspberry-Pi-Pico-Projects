from pico_i2c_lcd import I2cLcd
from machine import I2C,Pin
import time

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

i2c = I2C(id=0,scl=Pin(1),sda=Pin(0),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    lcd.move_to(0,0)
    lcd.putstr('Temp:')
    lcd.move_to(6,0)
    lcd.putstr(str(temperature)+" C")
    time.sleep(1)
    lcd.clear()