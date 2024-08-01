#1-1/2+1/3-1/4+...
n=int(input("enter n->"))
add=0
cnt=1
for i in range(1,n+1):
    if(cnt==1):
        add=1/i
    elif(cnt%2==0):
        add=add-(1/i)
    else:
        add=add+(1/i)
    cnt+=1

print(add)
