my_favorite_pizzas = ['pepperoni', 'double cheese', 'chicken']

for pizza in my_favorite_pizzas:
    print(pizza)

for pizza in my_favorite_pizzas:
    print('\tI like ' + pizza)

for pizza in my_favorite_pizzas:
    print('I like ' + pizza)
print('Pizza is my favorite food')

animals_list = ['dog', 'cat']
for animal in animals_list:
    print('\tA ' + animal + ' would make a great pet')
print('\tAny of these animals would make a great pet!')

for value in range(1, 5):
    print(value)

numbers = list(range(1, 5))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(2, 12):
    squares.append(value**2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares_using_list_comprehension = [value**2 for value in range(1, 11)]
print(squares_using_list_comprehension)
