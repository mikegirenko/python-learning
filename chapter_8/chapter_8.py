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
