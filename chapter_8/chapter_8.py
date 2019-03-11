def display_message():
    print('I am learning functions!')


display_message()


def greet_user(username):
    """Display a simple greeting."""
    print('\nHello, ' + username.title() + '!')


greet_user('mike')


def favorite_book_and_author(book, author):
    print('\nMy favorite book is ' + book + ' and author is ' + author)


favorite_book_and_author('Alice in Wonderland', 'Charles Lutwidge')


def pet(animal_type, pet_name):
    print('\nI have ' + animal_type + ' named ' + pet_name)


pet(animal_type='dog', pet_name='Willie')
pet(pet_name='Burney', animal_type='dog')


def describe_pet(pet_name, animal_type='dog'):
    print('\nI have ' + animal_type + ' named ' + pet_name)


describe_pet('Harry')
describe_pet(pet_name='Oy')
describe_pet('Harry', 'hamster')
describe_pet('Chip', animal_type='cat')


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name


formatted_name = get_formatted_name('Jimmy', 'Burnes')
print('\nFormatted name is ' + formatted_name)


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        this_full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        this_full_name = first_name + ' ' + last_name
    return this_full_name


formatted_name = get_formatted_name('Jimmy', 'Burnes', 'Jay')
print('\nFormatted name is ' + formatted_name)


def build_person(first_name, last_name, age=''):
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = '27'
    return person


full_name = build_person('Mike', 'Jones', '27')
print('\t', full_name)


def greet_users(user_list):
    for user in user_list:
        message = 'Hello, ' + user.title() + '!'
        print(message)


users = ['mike', 'tom', 'sammy']
greet_users(users)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_designs = []


def print_models(unprinted, completed):
    while unprinted:
        current_design = unprinted.pop()
        print('\tPrinting ' + current_design)
        completed.append(current_design)


def completed_models(completed):
    print('\nPrinting finished designs:')
    for design in completed:
        print('\t', design)


print_models(unprinted_designs, completed_designs)
completed_models(completed_designs)
