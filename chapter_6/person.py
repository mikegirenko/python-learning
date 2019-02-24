person = {
    'first_name': 'mike',
    'last_name': 'spenser',
    'age': 34,
    'gender': 'male',
    'city': 'denver',
    'county': 'arapahoe'
}

print('This person is ' + str(person))
print('Persons first name is ' + person['first_name'].title())

for k, v in person.items():
    print('\tKey: ' + k)
    print('\tValue: ' + str(v))

for key in person.keys():
    print('Key: ' + key)

for value in person.values():
    print('\tValue: ' + str(value))
