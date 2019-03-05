prompt = 'If you could visit one place in the world, where would you go? '
prompt += '\nEnter "quit" to exit the program '

active_polling = True
places = []
while active_polling:
    user_response = input(prompt)
    if user_response == 'quit':
        active_polling = False
    else:
        places.append(user_response)

print('\nUsers want to visit:')
for item in places:
    print('\t' + item.title())
