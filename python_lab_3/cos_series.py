#cos x=1-x^2/2!+x^4/4!-x^6/6!+...
import math
def value(x,n):
    cos=0
    for i in range(n):
        sign=(-1)**i
        pi=3.14
        y=x*(pi/180)
        m=math.factorial(2*i)*sign
        p=(y**(2*i))
        cos+=((p)/m)
    return cos
x=45
n=5
print(round(value(x,n),2))
