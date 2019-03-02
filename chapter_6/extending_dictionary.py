students = {
    'tom': 'jones',
    'bobby': 'fisher',
    'mike': 'spenser'
}

print('Original list of students:')
print('\t', students)

print('First names only:')
for name in students.keys():
    print('\t', name.title())

print('Last names only')
for value in students.values():
    print('\t', value.title())

print('One more student added:')
students['julia'] = 'rodriguez'
for k, v in students.items():
    print('\t' + str(k.title()) + ' ' + str(v.title()))

print('Modified list:')
students['tom'] = 'douglas'
students['bobby'] = 'norris'
for k, v in students.items():
    print('\t' + str(k.title()) + ' ' + str(v.title()))

print('One student removed:')
del students['tom']
for k, v in students.items():
    print('\t' + str(k.title()) + ' ' + str(v.title()))

print('Slightly reformatted list')
for k, v in students.items():
    print('\t' + 'Student first name is ' + str(k.title(
    )) + ' and last name is ' + str(v.title()))
