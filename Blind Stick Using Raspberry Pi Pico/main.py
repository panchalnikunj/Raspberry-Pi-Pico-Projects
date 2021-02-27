from machine import Pin
import time

trig = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
buzz = Pin(17, Pin.OUT)

def ultra():
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
   
    if distance < 10:
        buzz.high()
    else:
        buzz.low()
     
while True:
    ultra()
    time.sleep(0.3)
