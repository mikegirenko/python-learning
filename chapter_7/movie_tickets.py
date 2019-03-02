prompt = 'What is your age? '

while True:
    age = input(prompt)
    if int(age) < 3:
        print('\nYou are ' + age + ' and your ticket is free!')
    if 3 < int(age) < 12:
        print('\nYou are ' + age + ' and your ticket is $10')
    if int(age) > 12:
        print('\nYou are ' + age + ' and your ticket is $15!')
    break
