"""
Working with if statement
"""

cars = ['audi', 'bmw', 'honda', 'opel', 'toyote']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# car = 'Audi'
# assert(car == 'audi')

car = 'Audi'
assert(car.lower() == 'audi')

requested_topping = 'cheese'
if requested_topping != 'anchovies':
    print('\nHold the anchovies!')

age = 19
if age != 23:
    print('\nThe age is incorrect')
if age < 43:
    print('Way too young')
if age > 14 and age == 19:
    print('Age just right')
if age == 19 or age > 23:
    print('Still just right')

if 'audi' in cars:
    print('\naudi in in the list of cars')

if 'ford' not in cars:
    print('\nford is not in the list')

game_ended = True
if game_ended:
    print('\nPlayers, stop playing')
