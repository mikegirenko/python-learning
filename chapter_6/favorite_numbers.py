favorite_numbers = {
    'jen': 1,
    'peter': 22,
    'sam': 9,
    'danny': 67,
    'sal': 0
}
print("Jen's favorite number is " + str(favorite_numbers['jen']))
print("Peter's favorite number is " + str(favorite_numbers['peter']))
print("Sam's favorite number is " + str(favorite_numbers['sam']))
print("Danny's favorite number is " + str(favorite_numbers['danny']))
print("Sal's favorite number is " + str(favorite_numbers['sal']))

multiple_favorite_numbers = {
    'jen': {1, 2, 3},
    'peter': {4, 5, 6},
    'sam': {7, 8, 9},
    'danny': {10, 11, 12},
    'sal': {13, 14, 15}
}
for k, v in multiple_favorite_numbers.items():
    print('\n' + str(k.title()) + ':')
    for number in v:
        print(number)
    print(" ")
