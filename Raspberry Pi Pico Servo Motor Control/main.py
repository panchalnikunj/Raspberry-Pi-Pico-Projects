from machine import Pin, PWM

analogvalue = machine.ADC(28)

pwm = PWM(Pin(0))
pwm.freq(50)

while True:
    reading = analogvalue.read_u16() 
    pwm.duty_u16(int(reading/6))
