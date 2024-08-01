# sin x=x-x^3/3!+x^5/51!x^7/7!+x^9/9!
import math
def value(x,n):
    sine=0
    for i in range(n):
        sign=(-1)**i
        pi=3.14
        y=x*(pi/180)
        m=math.factorial(2*i+1)*sign
        p=(y**(2*i+1))
        sine+=((p)/m)
    return sine
x=30
n=10
print(round(value(x,n),2))
