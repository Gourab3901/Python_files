#lcm
import math
def Lcm(a,b):
    gcd=math.gcd(a,b)
    lcm=(a*b)//gcd
    return lcm
a=12
b=15
print(Lcm(a,b))
