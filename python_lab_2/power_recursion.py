#calculate power using recursion
def power(n,p):
    if p==0:
        return 1
    return(n*power(n,p-1))
n=5
p=2
print(power(n,p))
