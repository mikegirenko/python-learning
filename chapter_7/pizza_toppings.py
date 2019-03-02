prompt = 'Enter your favorite pizza topping: '
prompt += '\nEnter "quit" to exit. '
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print('You entered ' + topping)
