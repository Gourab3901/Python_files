'''From the above sets A and B
I. Join A and B
II. Find A intersection B
III. Is A subset of B
IV. Are A and B disjoint sets
V. Join A with B and B with A
VI. What is the symmetric difference between A and B
VII. Delete the sets completely'''
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print('A = ',A)
print('B = ',B)
join=A.union(B)
print("join : ",join)
inter=A.intersection(B)
print('intersection ',inter)
sub=A.issubset(B)
print('subset ',sub)
dis=A.isdisjoint(B)
print('disjoint ',dis)
sym=A.symmetric_difference(B)
print('symmetric ',sym)
del A
del B

