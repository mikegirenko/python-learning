magicians_names = ['edgar', 'ben', 'tom', 'majestic']

print('Original list: ')


def show_magicians(list_of_magicians):
    for name in list_of_magicians:
        print('\t', name.title())


show_magicians(magicians_names)


def make_great(list_of_magicians):
    list_of_great_magicians = []
    while list_of_magicians:
        current_magician = list_of_magicians.pop()
        list_of_great_magicians.append('The Great ' + current_magician.title())

    while list_of_great_magicians:
        current_magician = list_of_great_magicians.pop()
        list_of_magicians.append(current_magician)
    return list_of_magicians


print('\nModified list:')
show_magicians(make_great(magicians_names))

print('\nNew original list: ')
new_magicians_names = ['sam', 'paul', 'jimmy']


def make_great(list_of_magicians):
    updated_list_of_magicians = []
    while list_of_magicians:
        current_magician = list_of_magicians.pop()
        updated_list_of_magicians.append('The Great ' + current_magician)
    return updated_list_of_magicians


show_magicians(new_magicians_names)
print('\nNew list: ')
show_magicians(make_great(new_magicians_names[:]))
print('\nUnchanged original list:')
show_magicians(new_magicians_names)
