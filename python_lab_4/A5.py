'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''
s=input("enter :")
print()
print(s)
l=0
d=0
for i in s:
    if i>='a' and i<='z':
        l+=1
    elif i>='0' and i<='9':
        d+=1
    else:
        print("error")
print("letter : ",l,"digit :",d)
