guest = input('Please enter guest name:')

filename = 'guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(guest)

with open(filename) as file_object:
    print('File has', file_object.read())

guest_list = []
filename = 'guest_book.txt'
while True:
    if guest == 'quit':
        break
    else:
        guest = input('Please enter guest name:')
        if guest != 'quit':
            print('Hi', guest)
            with open(filename, 'a') as file_object:
                file_object.write(guest + '\n')

with open(filename) as file_object:
    print(filename, 'file has', file_object.read())
