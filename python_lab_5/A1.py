'''1.The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
I. Sort the list and find the min and max age
II. Add the min age and the max age again to the list
III. Find the median age (one middle item or two middle items divided by two)
IV. Find the average age (sum of all items divided by their number )
V. Find the range of the ages (max minus min)
VI. Compare the value of (min - average) and (max - average), use _abs()_ method'''
import statistics as s
ages=[19,22,19,24,20,25,26,24,25,24]
#i
ages.sort()
print(ages)
b=min(ages)
c=max(ages)
print("min age",b,"max age",c)
#ii
ages.append(b)
ages.append(c)
print(ages)
#iii
ages.sort()
print("median",s.median(ages))
#iv
avg=sum(ages)/len(ages)
print("average ",avg)
#v
print("difference ",c-b)
#vi
