


def line_h(x,y,l):
    for i in range(l):
        xin = x + i
        plot(xin,y)

def line_v(x,y,l):
    for i in range(l):
        yin = y + i
        plot(x,yin)

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
    line_v(x+6,y,8)

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

def S(x,y):
    line_h(x,y+0,6)
    line_h(x,y+4,6)
    line_h(x,y+8,6)
    line_v(x+3,y,4)
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