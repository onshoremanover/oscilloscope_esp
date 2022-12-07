# Write your code here :-)

#dac.write values 0-255
from machine import DAC,Pin
import math
import time

dac1 = DAC(Pin(25))
dac1.write(64)

dac2 = DAC(Pin(26))
dac2.write(64)


i = 100

while True:
    time.sleep(0.0001)
    dac1.write(i)
    dac2.write(i)
    i += 1
    if i > 255:
        i = 100
        

        
        
        

 