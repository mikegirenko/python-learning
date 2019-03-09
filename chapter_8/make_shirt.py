def make_shirt(size, message):
    print('\nT-shirt size is ' + size + ' and message is "' + message + '"')


make_shirt('Large', 'Python is great!')
make_shirt(size='Medium', message='How about them apples?!')


def make_shirt_large(size='Large', message='I love Python'):
    print('\nT-shirt size is ' + size + ' and message is "' + message + '"')


make_shirt_large()
make_shirt_large(size='Medium')
make_shirt_large(size='Extra Large', message='Go Broncos!')
