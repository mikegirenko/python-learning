"""
Working with if statement, conditional tests, and comparing
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

age = 4

if age < 4:
    price = 0
elif age == 4:
    price = 5
else:
    price = 7

print('\nFor age ' + str(age) + ', price is $' + str(price))

pizza_toppings = ['cheese', 'pepperoni']
if 'cheese' in pizza_toppings:
    print('\nAdding cheeze')
if 'pepper' in pizza_toppings:
    print('Adding pepper')
if 'pepperoni' in pizza_toppings:
    print('Adding pepperoni')
print('Pizza is ready!')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    print('\tAdding ', topping)
print('\tPizza is ready!')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    if topping == 'green peppers':
        print('Sorry, we out of green pappers now')
    else:
        print('Adding ', topping)
print('Pizza without green peppers is ready!')

requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print('\tAdding ', topping)
    print('\tPizza is ready')
else:
    print('\tMaking pizza without toppings')

available_toppings = ['olives', 'mushrooms', 'green peppers', 'extra cheese']
requested_toppings = ['green peppers', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print('Adding', topping)
    else:
        print('Sorry, we do not have', topping)
print('Pizza is done')

