#decimal to binary
def DtoB(n):
    if n>=1:
        DtoB(n//2)
    print(n%2,end='')
n=8
print("binary :")
print(DtoB(n))
