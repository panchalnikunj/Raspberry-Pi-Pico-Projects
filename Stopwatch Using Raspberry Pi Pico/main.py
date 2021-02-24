from machine import Pin
import time
import tm1637

tm = tm1637.TM1637(clk=Pin(1), dio=Pin(0))
Button = Pin(2, Pin.IN)

a = 0
b = 0

tm.numbers(a,b)

while True:
    if Button.value() == 1:
        while True:
            tm.numbers(a,b)
            b = b+1
            if b > 59:
                b = 0
                a = a+1
            time.sleep(1)
