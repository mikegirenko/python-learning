prompt = 'What is your age? '

while True:
    age = input(prompt)
    if int(age) < 3:
        print('\nYou are ' + age + ' and your ticket is free!')
        break
    if 3 < int(age) < 12:
        print('\nYou are ' + age + ' and your ticket is $10')
        break
    if int(age) > 12:
        print('\nYou are ' + age + ' and your ticket is $15!')
        break

prompt = 'What is your age? '

active = True
while active:
    age = input(prompt)
    if int(age) < 3:
        print('\nYou are ' + age + ' and your ticket is free!')
        active = False
    if 3 < int(age) < 12:
        print('\nYou are ' + age + ' and your ticket is $10')
        active = False
    if int(age) > 12:
        print('\nYou are ' + age + ' and your ticket is $15!')
        active = False

prompt = 'What is your age? '
prompt += '\nEnter quit to exit '

while True:
    age = input(prompt)
    if age == 'quit':
        break
    if int(age) < 3:
        print('\nYou are ' + age + ' and your ticket is free!')
        break
    if 3 < int(age) < 12:
        print('\nYou are ' + age + ' and your ticket is $10')
        break
    if int(age) > 12:
        print('\nYou are ' + age + ' and your ticket is $15!')
        break
