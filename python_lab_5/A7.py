'''Create a student dictionary and add first_name, last_name, gender, age, marital status, skills,
country, city and address as keys for the dictionary
I. Get the length of the student dictionary
II. Get the value of skills and check the data type, it should be a list
III. Modify the skills values by adding one or two skills
IV. Get the dictionary keys as a list
V. Get the dictionary values as a list
VI. Change the dictionary to a list of tuples using _items()_ method
VII. Delete one of the items in the dictionary
VIII. Delete one of the dictionaries'''
student={
    'first_name':'Gourab',
    'last_name':'Nandi',
    'gender':'Male',
    'age': 22,
    'marital_status':'single',
    'skills':['c','java'],
    'country':'India',
    'city':'Kolkata',
    'address':'169/8 N N Road'
    }
l=len(student)
print("length : ",l)
print()
skills = student["skills"]
print("Skills:", skills)
print("Data type of skills:", type(skills))

print()
student["skills"].extend(["Python", "Web"])
print("Updated Skills:", student["skills"])

print()
keys_list = list(student.keys())
print("Keys :", keys_list)

print()
values_list = list(student.values())
print("Values :", values_list)

print()
items_list = list(student.items())
print("List of Tuples:", items_list)

print()
del student["marital_status"]
print("after deletion:", student)

del student
