from machine import Pin

PIR = Pin(28,Pin.IN)
Buz = Pin(15,Pin.OUT)

while True:
    if PIR.value() == 1:
        Buz.high()
        
    else:
        Buz.low()
