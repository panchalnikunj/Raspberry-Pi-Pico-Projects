from machine import Pin
import time
import ssd1306

oled = ssd1306.SSD1306_I2C(128, 64, machine.I2C(0))

trig = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def find():
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(5)
    trig.low()
    
    while echo.value() == 0:
        signaloff = time.ticks_us()
    
    while echo.value() == 1:
        signalon = time.ticks_us()
        
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    
    print("Distance is: ", distance, "cm")
    
    oled.text("Distance is : ", 0, 0)
    oled.text(str(distance) + " cm", 0, 10)
    oled.show()
    oled.fill(0)
    
while True:
    find()
    time.sleep(1)
