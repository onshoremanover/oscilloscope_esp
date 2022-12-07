# Write your code here :-)

#dac.write values 0-255
from machine import DAC,Pin
import sys
import math
import time
import random



dac1 = DAC(Pin(25))

dac2 = DAC(Pin(26))

time_interval = 0.0000001



def sleep_m():
    time.sleep(0.0000001)
    
def plot(x,y):
    if (0 < x <= 255) and (0 < y <= 255):
        dac1.write(y)
        dac2.write(x)
        sleep_m()

def line_h(x,y,l):
    for i in range(l):
        xin = x + i
        plot(xin,y)

def line_v(x,y,l):
    for i in range(l):
        yin = y + i
        plot(x,yin)


def line(b,h,v,l):
    for i in range(l):
        y = math.tan(m*math.pi) * x
            
def line_r(m):
    for x in range(0,100,1):
        y = math.tan(m*math.pi) * x
        
        xb = x + 128
        xb = round(xb)
        
        yb = y + 128
        yb = round(yb)

        plot(xb,yb)

def line_l(m):
    for x in range(0,100,1):
        y = math.tan(m*math.pi) * x
        
        xb = -x + 128
        xb = round(xb)
        
        yb = -y + 128
        yb = round(yb)
        
        plot(xb,yb)


        
def swoop():
    
    for m in range(-50,-150,-2):
        m1 = m/100
        line_l(m1)
        #line_h(180,160,20)
        #line_v(190,150,20)
        
        circle()
        
        plane(220,60,7.2)
        plane(200,180,7.2)   
        
    for m in range(-150,-250,-2):
        m1 = m/100
        line_r(m1)
        #line_h(180,160,20)
        #line_v(190,150,20)
        circle()
        
        plane(120,40,2.2)
        plane(140,240,7.2)
    
def cross_old():
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
            
def square_old():
        
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

def cross(x,y,m):
    
    xh=round(x-(m/2))
    
    yv=round(y-(m/2))
    
    line_h(xh,y,m)
    line_v(x,yv,m)

def square(x,y,m):
    xmin = round(x-(m/2))
    ymin = round(y-(m/2))
    yplu = round(y+(m/2))
    xplu = round(x+(m/2))
    
    line_h(xmin,ymin,m)
    line_h(xmin,yplu,m)
    line_v(xmin,ymin,m)
    line_v(xplu,ymin,m)
    
def vector(b,h,r,phi):
    for i in range(r):
        x = round(i * math.cos(phi*math.pi)+b)
        y = round(i * math.sin(phi*math.pi)+h)

        plot(x,y)
        
    
def plane(b,h,phi):
    vector(b,h,10,phi)
    square(b,h,8)
    
def randplane():
    y = random.randrange(1,255,1)
    x = random.randrange(1,255,1)
    phi = random.randrange(0,400,1)/100
    vector(x,y,10,phi)
    square(x,y,8)

#function to write letters
def write_letter():



def A(x,y):
    line_h(x+0,y+4,6)
    line_h(x+0,y+8,6)
    line_v(x+0,y,8)
    line_v(x+6,y,8)

def B(x,y):
    line_h(x+0,y+0,6)
    line_h(x+0,y+4,6)
    line_h(x+0,y+8,4)
    line_v(x+0,y,8)
    line_v(x+6,y,4)
    line_v(x+4,y+4,4)

def C(x,y):
    line_h(x+0,y+0,6)
    line_h(x+0,y+8,6)
    line_v(x+0,y,8)

def D(x,y):
    line_h(x,y+0,6)
    line_h(x,y+4,6)
    line_v(x,y,4)
    line_v(x+6,y,8)

def E(x,y):
    line_h(x,y+0,6)
    line_h(x,y+4,6)
    line_h(x,y+8,6)
    line_v(x,y,8)

def F(x,y):
    line_h(x,y+4,4)
    line_h(x,y+8,6)
    line_v(x,y,8)

def G(x,y):
    line_h(x,y+0,6)
    line_h(x,y+8,6)
    line_v(x,y,8)
    line_v(x+6,y,4)

def H(x,y):
    line_h(x,y+4,6)
    line_v(x,y,8)
    line_v(x+6,y,8)

def I(x,y):
    line_h(x,y+0,6)
    line_h(x,y+8,6)
    line_v(x+3,y,8)

def J(x,y):
    line_h(x,y+0,6)
    line_v(x+6,y,8)
    line_h(x+4,y+8,2)

def K(x,y):
    line_v(x,y,8)
    line_v(x+6,y+2,4)
    line_h(x,y+4,6)

def L(x,y):
    line_h(x,y+0,6)
    line_v(x,y,8)

def M(x,y):
    line_h(x,y+8,6)
    line_v(x,y,8)
    line_v(x+6,y,8)
    line_v(x+3,y+4,4)

def N(x,y):
    line_h(x,y+8,3)
    line_h(x+3,y,3)
    line_v(x,y,8)
    line_v(x+6,y,8)
    line_v(x+3,y,8)

def O(x,y):
    line_h(x,y+0,6)
    line_h(x,y+8,6)
    line_v(x,y,8)
    line_v(x+6,y,8)

def P(x,y):
    line_h(x,y+4,4)
    line_h(x,y+8,4)
    line_v(x,y,8)
    line_v(x+6,y+4,4)

def Q(x,y):
    line_h(x,y+0,6)
    line_h(x,y+8,6)
    line_v(x,y,8)
    line_v(x+6,y,8)
    line_h(x+3,y+4,3)
    line_v(x+3,y,4)

def R(x,y):
    line_h(x,y+8,6)
    line_h(x+3,y+4,3)
    line_v(x,y,8)
    line_v(x+6,y+4,4)
    line_v(x+3,y,4)

def S(x,y):
    line_h(x,y+0,6)
    line_h(x,y+4,6)
    line_h(x,y+8,6)
    line_v(x+6,y,4)
    line_v(x,y+4,4)

def T(x,y):
    line_h(x,y+8,6)
    line_v(x+3,y,8)

def U(x,y):
    line_h(x,y+0,6)
    line_v(x,y,8)
    line_v(x+6,y,8)

def V(x,y):
    line_h(x,y+4,2)
    line_h(x+2,y,2)
    line_h(x+4,y+4,2)
    line_v(x,y+4,4)
    line_v(x+6,y+4,4)
    line_v(x+2,y,4)
    line_v(x+4,y,4)

def W(x,y):
    line_h(x,y+0,2)
    line_h(x+4,y,2)
    line_h(x+2,y+4,2)
    line_v(x,y,8)
    line_v(x+6,y,8)

def X(x,y):
    line_h(x,y+2,6)
    line_h(x,y+6,6)
    line_v(x,y,2)
    line_v(x+6,y,2)
    line_v(x,y+6,2)
    line_v(x+6,y+6,2)
    line_v(x+3,y+2,4)

def Y(x,y):
    line_h(x,y+4,6)
    line_v(x+3,y,4)
    line_v(x+6,y+4,4)
    line_v(x,y+4,4)

def Z(x,y):
    line_h(x,y+0,6)
    line_h(x,y+8,6)
    line_h(x,y+4,6)
    line_v(x+6,y+4,4)
    line_v(x,y,4)

def one(x,y):
    line_h(x,y+0,6)
    line_h(x+1,y+8,2)
    line_v(x+3,y,8)

def two(x,y):
    line_h(x,y+0,6)
    line_h(x,y+4,6)
    line_h(x,y+8,6)
    line_v(x,y,4)
    line_v(x+6,y+4,4)

def three(x,y):
    line_h(x+0,y+0,6)
    line_h(x+0,y+4,6)
    line_h(x+0,y+8,6)
    line_v(x+6,y,8)

def four(x,y):
    line_h(x,y+4,6)
    line_v(x,y+4,4)
    line_v(x+6,y,8)

def five(x,y):
    line_h(x,y+0,6)
    line_h(x,y+4,6)
    line_h(x,y+8,6)
    line_v(x+6,y,4)
    line_v(x,y+4,4)

def six(x,y):
    line_h(x,y+0,6)
    line_h(x,y+4,6)
    line_h(x,y+8,6)
    line_v(x,y,8)
    line_v(x+6,y,4)

def seven(x,y):
    line_h(x,y+8,6)
    line_h(x+3,y+4,3)
    line_v(x+6,y,8)

def eight(x,y):
    line_h(x,y+0,6)
    line_h(x,y+4,6)
    line_h(x,y+8,6)
    line_v(x,y,8)
    line_v(x+6,y,8)

def nine(x,y):
    line_h(x,y+0,6)
    line_h(x,y+4,6)
    line_h(x,y+8,6)
    line_v(x,y+4,4)
    line_v(x+6,y,8)

def zero(x,y):
    line_h(x,y+0,6)
    line_h(x,y+8,6)
    line_v(x,y,8)
    line_v(x+6,y,8)


    
while True:
    swoop()


    
