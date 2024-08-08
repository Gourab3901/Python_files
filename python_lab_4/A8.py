'''Write a program that accepts a string
I. 1.reverses it.
II. 2.checks whether it is a palindrome.
III. 3.checks whether it ends with a specific substring.
IV. 4.capitalize the first letter of each word in a string
V. 5.check if a string is anagram of another string
VI. 6.remove vowels from string
VII. 7.find length of the longest word in a sentence'''
import re
s=input("enter :")
print()
r=s[::-1]
print("reverse :",r)
print()
if r==s:
    print("palindrome")
else:
    print("palindrome not")
print()
print("endwith")
sub=s.endswith("hello")
print(sub)
print()
print("first letter capital")
cap=s.title()
print(cap)
print()
print("remove vowel ")
v=re.sub("[aeiouAEIOU]","",s)
print(v)
print()
print("longest word length")
long=max(s.split(),key=len)
print("longest word :",long)
print("length :",len(long))
