result = 0

while True:
    first_number = input('Enter first number. Enter q to quit: ')
    if first_number == 'q':
        break
    second_number = input('Enter second number. Enter q to quit: ')
    if second_number == 'q':
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print('Letters not allowed')
    else:
        print(first_number, '+', second_number, 'equals', result)
