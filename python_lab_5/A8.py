'''I. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
II. Check if the person dictionary has skills key, if so check if the person has &#39;Python&#39; skill and
print out the result.
III. If a person skills has only JavaScript and React, print(&#39;He is a front end developer&#39;), if the
person skills has Node, Python, MongoDB, print(&#39;He is a backend developer&#39;), if the person
skills has React, Node and MongoDB, Print(&#39;He is a fullstack developer&#39;), else print(&#39;unknown
title&#39;) - for more accurate results more conditions can be nested!
IV. If the person is married and if he lives in Finland, print the information in the following
format:

```py
Asabeneh Yetayeh lives in Finland. He is married.'''

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# i
if 'skills' in person:
    skills_list = person['skills']
    middle_index = len(skills_list) // 2
    middle_skill = skills_list[middle_index]
    print("Middle skill:", middle_skill)

# ii
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

# iii
if 'skills' in person:
    skills = person['skills']
    
    if set(['JavaScript', 'React']).issubset(skills):
        print('He is a front end developer')
    elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
        print('He is a backend developer')
    elif set(['React', 'Node', 'MongoDB']).issubset(skills):
        print('He is a fullstack developer')
    else:
        print('unknown title')

# iv
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
