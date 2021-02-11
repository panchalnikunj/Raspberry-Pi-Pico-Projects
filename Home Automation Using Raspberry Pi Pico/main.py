from machine import UART, Pin

bt = UART(0,9600)

L1 = Pin(2,Pin.OUT)
L2 = Pin(3,Pin.OUT)
L3 = Pin(4,Pin.OUT)
L4 = Pin(5,Pin.OUT)

while True:
    
    br = bt.readline()
    
    if "ON1" in br:
        L1.value(0)
    elif "OFF1" in br:
        L1.value(1)
        
    elif "ON2" in br:
        L2.value(0)
    elif "OFF2" in br:
        L2.value(1)
        
    elif "ON3" in br:
        L3.value(0)
    elif "OFF3" in br:
        L3.value(1)
        
    elif "ON4" in br:
        L4.value(0)
    elif "OFF4" in br:
        L4.value(1)
