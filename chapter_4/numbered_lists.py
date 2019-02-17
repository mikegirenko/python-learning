for number in range(1, 9):
    print(number, end=' ')

list_of_numbers = []
for number in range(1, 21):
    list_of_numbers.append(number)
print('\nList of numbers', list_of_numbers)
print('Min is ', min(list_of_numbers))
print('Max is ', max(list_of_numbers))
print('Sum is ', sum(list_of_numbers))

list_of_odd_numbers = []
for number in range(1, 20, 2):
    list_of_odd_numbers.append(number)
print('List of odd numbers', list_of_odd_numbers)

list_of_multiples_by_three = []
for number in range(3, 31):
    list_of_multiples_by_three.append(number*3)
print('List of multiples by three', list_of_multiples_by_three)

list_of_cubes = []
for integer in range(1, 11):
    list_of_cubes.append(integer**3)
print('List of cubes', list_of_cubes)

cube_comprehension = [integer**3 for integer in range(1, 11)]
print('Cube comprehension ', cube_comprehension)
