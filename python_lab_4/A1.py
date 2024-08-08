'''Write a program to enter a string. Calculate the length of the string. Find the substring country.
Count the occurences of each word in the given sentence.
If the String as input is India is my motherland. I love my country. Capital of India is New Delhi.'''
s=input("enter : ")
print()
print(s)
print()
print("length :",len(s))
print()
print("word country present?")
if "country" in s:
    print("yes")
else:
    print("no")
print()
c=dict()
words=s.split(" ")
for word in words:
    if word in c:
        c[word]+=1
    else:
        c[word]=1
print(c)
