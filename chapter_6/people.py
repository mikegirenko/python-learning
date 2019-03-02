person_1 = {
    'first_name': 'mike',
    'last_name': 'spenser',
    'age': 34,
    'gender': 'male',
    'city': 'denver',
    'county': 'arapahoe'
}

person_2 = {
    'first_name': 'jim',
    'last_name': 'ship',
    'age': 23,
    'gender': 'male',
    'city': 'aurora',
    'county': 'arapahoe'
}

person_3 = {
    'first_name': 'courtney',
    'last_name': 'green',
    'age': 44,
    'gender': 'female',
    'city': 'santa fe',
    'county': 'adams'
}

list_of_people = [person_1, person_2, person_3]

print('There are ' + str(len(list_of_people)) + ' on the list. They are:')
for person in list_of_people:
    for k, v in person.items():
        print(str(k) + ' : ' + str(v))
    print(" ")
