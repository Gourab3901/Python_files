'''Create fruits, vegetables and animal products tuples.
I. Join the three tuples and assign it to a variable called food_stuff_tp.
II. Change the about food_stuff_tp tuple to a food_stuff_lt list
III. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
IV. Slice out the first three items and the last three items from food_staff_lt list
V. Delete the food_staff_tp tuple completely'''
fruits=('apple','mango','orange')
vegetables=('carrot','potato','cabbage')
animal_products=('milk','butter','cheese')
#i
food_stuff_tp=fruits+vegetables+animal_products
print("all items ",food_stuff_tp)
#ii
food_stuff_lt=list(food_stuff_tp)
#iii
l=len(food_stuff_tp)
m=l//2
print("middle item ",food_stuff_tp[m])
#iv
print("remove first 3 and last 3 item ",food_stuff_lt[3:-3])
#v
del food_stuff_tp
