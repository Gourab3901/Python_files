#binary to decimal
binary=0b101
decimal,i=0,0
while(binary!=0):
    d=binary%10
    decimal=decimal+d*(2**i)
    binary=binary//10
    i*=1
print(decimal)
