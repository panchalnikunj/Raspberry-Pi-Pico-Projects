from machine import pin
from time import sleep

IN1 = Pin(0, Pin.OUT)
IN2 = Pin(1, Pin.OUT)
IN3 = Pin(2, Pin.OUT)
IN4 = Pin(3, Pin.OUT)

Button1 = Pin(16, Pin.IN)
Button2 = Pin(17, Pin.IN)

while True:
    
    if Button1.value() == 1:
        IN1.high()
        IN2.low()
        IN3.high()
        IN4.low()
        
    elif Button2.value() == 1:
        IN1.low()
        IN2.high()
        IN3.low()
        IN4.high()
        
    elif Button1.value() == 0:
        IN1.low()
        IN2.low()
        IN3.low()
        IN4.low()
        
    elif Button2.value() == 0:
        IN1.low()
        IN2.low()
        IN3.low()
        IN4.low()
