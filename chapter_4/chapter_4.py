"""
More working with lists. Working with tuple
"""

food = ['spam', 'eggs', 'chees']
for item in food:
    print(item)

# names = ['Tom', 'Mike']
# for name in names
#     print(name)

list_of_names = ['charles', 'tony', 'mike', 'joe']
print('First two names', list_of_names[0:2])
print('Last two names', list_of_names[2:4])
for name in list_of_names[:2]:
    print('Name', name)

print('My favorite foods are', food)
my_friend_foods = food[:]
print("My friend's favorite foods are", my_friend_foods)
food.append('bacon')
my_friend_foods.append('ice cream')
print('My latest favorite foods are', food)
print("My latest friend's favorite foods are", my_friend_foods)

for value in range(1, 5):
    print('\t', value)

list_of_numbers = list(range(1, 10))
print('List of numbers', list_of_numbers)

list_of_even_numbers = list(range(2, 21, 2))
print('List of even numbers', list_of_even_numbers)

print('\tMin', min(list_of_numbers))
print('\tMax', max(list_of_numbers))
print('\tSum', sum(list_of_numbers))

squares = []
for value in range(1, 7):
    squares.append(value**2)
print('List populated with squares', squares)

bigger_squares = [value**2 for value in range(11, 15)]
print('Another list populated with squares', bigger_squares)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 231

for dimension in dimensions:
    print('Original tuple', dimension)

dimensions = (187, 3)

for dimension in dimensions:
    print('Updated tuple', dimension)
