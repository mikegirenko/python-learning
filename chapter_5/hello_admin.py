username = ['mike', 'admin', 'sam', 'tom', 'peter']
for name in username:
    if name == 'admin':
        print('Hello ' + name.title() + ', would you like to see report?')
    else:
        print('Hello ' + name.title() + ', thank you logging in')

username = []
if username:
    for name in username:
        if name == 'admin':
            print('Hello ' + name.title() + ', would you like to see report?')
        else:
            print('Hello ' + name.title() + ', thank you logging in')
else:
    print('\nWe need to find some users')
