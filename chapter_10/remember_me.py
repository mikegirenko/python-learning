import json

filename = 'username.json'


def get_stored_username():
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    user_input = input('Enter your name: ')
    with open(filename, 'w') as file_object:
        json.dump(user_input, file_object)
    return user_input


def greet_user():
    username = get_stored_username()
    if username:
        print(username, 'is the username. Is this correct?')
        user_response = input('Enter Yes ot No: ')
        if user_response == 'Yes':
            print('Welcome back,', username.title())
        else:
            username = get_new_username()
            print('I will remember you next time,', username.title())


greet_user()
