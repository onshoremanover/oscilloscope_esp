# Write your code here :-)

#dac.write values 0-255
from machine import DAC,Pin
import math
import time


dac1 = DAC(Pin(25))

dac2 = DAC(Pin(26))

time_interval = 0.0001



def sleep_m():
    time.sleep(0.000001)
    
def plot(x,y):
    dac1.write(y)
    dac2.write(x)
    time.sleep(time_interval)

def line_h(x,y,l):
    for i in range(l):
        xin = x + i
        if x<255:
            plot(xin,y)

def line_v(x,y,l):
    for i in range(l):
        yin = y + i
        if y<255:
            plot(x,yin)
            
def line(m):

    for x in range(0,100,1):
        y = math.tan(m*math.pi) * x
        
        xb = x + 128
        xb = round(xb)
        
        yb = y + 128
        yb = round(yb)
        
        if xb < 256:
            if yb < 256:
                if xb >= 0:
                    if yb >= 0:
                        plot(xb,yb)
        
def swoop():
    
    for m in range(0,-200,-1):
        m1 = m/100
        line(m1)
        circle()
        
    


def cross():
    i = 100
    j = 100
    
    i1 = 150
    j1 = 150
    
    

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
            
def square():
        
    dac1.write(1)
    dac2.write(1)
    sleep_m()
        
        
    dac1.write(1)
    dac2.write(255)
    sleep_m()
        
        
    dac1.write(255)
    dac2.write(1)
    sleep_m()
        
    dac1.write(255)
    dac2.write(255)
    sleep_m()
        
    dac1.write(1)
    dac2.write(1)
    sleep_m()
        
def circle():
    #(x-128)sq + (y-128)sq = Rsq
    #y = 128+ squareroot of (126sq - (x-128)sq)
    for x in range(2,255,1):
        in1 = math.pow(126,2)
        in22 = x - 128
        in2 = math.pow(in22,2)
        inner = in1-in2
        inner = round(inner)
        out = math.sqrt(inner)
        y1 = 128 - out
        y2 = 128 + out
        y1 = round(y1)
        y2 = round(y2)
        dac1.write(y1)
        dac2.write(x)
        dac1.write(y2)
        sleep_m()
    
while True:
    swoop()
        


        
        