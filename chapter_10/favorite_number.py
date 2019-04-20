import json

filename = 'favorite_number.json'

try:
    with open(filename) as file_object:
        number_from_file = json.load(file_object)
except FileNotFoundError:
    number = input('Enter your favorite number: ')
    with open(filename, 'w') as file_object:
        json.dump(int(number), file_object)
else:
    print("I know your favorite number! It’s", number_from_file)
