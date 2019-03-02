# """
# User input and while loops
# """

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

current_number = 1
while current_number <= 5:
    print(current_number, end=', ')
    current_number += 1

prompt = '\nTell me something and I will repeat it back to you:'
prompt += '\nType "quit" to end it. '
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nType something and I will repeat it back to you: "
prompt += '\nType quit to exit '

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)

current_number = 0
end = 10
while current_number < end:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number, 'is odd number below', end)
