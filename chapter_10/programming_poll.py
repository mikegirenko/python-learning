flag = True
reason = ''
filename = 'reasons.txt'

while flag:
    if reason == 'quit':
        flag = False
    else:
        reason = input('Why do you like programming? Enter quit to exit: ')
        if reason != 'quit':
            with open(filename, 'a') as file_object:
                file_object.write(reason + '\n')

print('File has the below:')
with open(filename) as file_object:
    print(file_object.read())
