# Write your code here :-)

#dac.write values 0-255
from machine import DAC,Pin
import math
import time

dac1 = DAC(Pin(25))
dac1.write(64)

dac2 = DAC(Pin(26))
dac2.write(64)


def graph():
    i = 0
    while True:
        time.sleep(0.0001)
        dac1.write(i)
        dac2.write(i)
        i += 1
        if i > 255:
            i = 0

def cross():
    i = 100
    j = 100
    
    i1 = 150
    j1 = 150
    
    
    while True:
        time.sleep(0.0001)
        dac1.write(i)
        dac1.write(i1)
        
        dac1.write(j)
        dac1.write(j1)
        
        dac2.write(i)
        dac2.write(i1)
        
        dac2.write(j)
        dac2.write(j1)
        
        i += 1
        j += 1

        if i > 200:
            i = 100
        if j > 200:
            j = 100

          
            
cross()

        
        