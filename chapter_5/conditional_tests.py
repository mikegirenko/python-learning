food = 'pizza'

if food == 'pizza':
    print('True')

print('\nIs food == pizza? I predict', food == 'pizza')
print('Is food == pasta? I predict', food == 'pasta')

if food != 'eggs':
    print(True)

car = 'Toyota'
if car.lower() == 'toyota':
    print(True)

number = 19
if number == 19:
    print(True)
if number != 21:
    print(True)
if number > 17:
    print(True)
if number < 23:
    print(True)
if number >= 19:
    print(True)
if number <= 19:
    print(True)

if number > 7 and number < 22:
    print(True)

if number == 19 or number < 2:
    print(True)

if 'p' in food:
    print(food, "includes letter p")

if 'm' not in food:
    print(food, 'does not include letter m')
