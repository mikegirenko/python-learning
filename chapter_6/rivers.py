rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'amazon': 'brazil'
}

for k, v in rivers.items():
    print('The ' + k.title() + ' runs through ' + v.title())

for key in rivers.keys():
    print('\tThe river is ' + key.title())

for value in rivers.values():
    print('The country is ' + value.title())
