#sum of digits
n=12345
s=0
while n>0:
    d=n%10
    s=s+d
    n=n//10
print(s)
