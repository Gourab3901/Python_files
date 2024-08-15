'''Create a set given below
it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
I. Find the length of the set it_companies
II. Add 'Twitter' to it_companies
III. Insert multiple IT companies at once to the set it_companies
IV. Remove one of the companies from the set it_companies
V. What is the difference between remove and discard'''
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM','Oracle','Amazon'}
#i
print("length ",len(it_companies))
#ii
it_companies.add('twitter')
print("single add ",it_companies)
#iii
it_companies.update(['TCS','Accenture','Cognizent'])
print("multiple add ", it_companies)
#iv
it_companies.remove('TCS')
print("remove a item ",it_companies)
