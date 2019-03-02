message = input('Tell me something and I will repeat it back to you: ')
print(message)

prompt = 'Who are you?'
prompt += '\nAre you Mike? '

message = input(prompt)
print(message)

age = input('How old are you? ')
age = int(age)
if age > 21:
    print('You are ' + str(age) + ' and you are an adult!')
else:
    print('You are ' + str(age) + ' and you are NOT an adult!')

number = input('Enter number and I will tell you if it is even or odd: ')
number = int(number)
if number % 2 == 0:
    print('The number ' + str(number) + ' is even')
else:
    print('The number ' + str(number) + ' is odd')
