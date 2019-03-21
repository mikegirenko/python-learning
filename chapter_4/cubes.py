list_of_numbers = list(range(1, 11))
print('Original list', list_of_numbers)

cubes = []
for number in list_of_numbers:
    cubes.append(number**3)

for number in cubes:
    print('\t', number)
