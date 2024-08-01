#slope 
def slope(x1,y1,x2,y2):
    if(x2-x1!=0):
        m1=y2-y1
        m2=x2-x1
        m=m1/m2
        return m
x1=3
x2=5
y1=3
y2=6
print("x1=",x1,"x2=",x2,"y1=",y1,"y2=",y2)
print("slope is :",slope(x1,y1,x2,y2))
