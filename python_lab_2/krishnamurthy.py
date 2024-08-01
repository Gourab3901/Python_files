#krishnamurthy number
n=145
temp=n
s=0
while n>0:
    f=1
    i=1
    rem=n%10
    f=math.factorial(rem)
    s=s+f
    n=n//10
if s==temp:
    print("yes")
else:
    print("no")
