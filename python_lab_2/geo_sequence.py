#print 6 no. starting with 2 and common ratio 3
def GP(a,r,n):
    for i in range(0,n):
        c=a*pow(r,i)
        print(c,end=" ")
a=2
r=3
n=6
GP(a,r,n)
