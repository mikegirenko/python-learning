"""
A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
Create a function that determines whether a number is a Disarium or not.
"""

def is_disarium(number):
    disarium_number = False
    number_to_string = str(number)
    list_of_digits = []
    for ch in number_to_string:
        list_of_digits.append(int(ch))
    position = 1
    sum = []
    for digit in list_of_digits:
        temp_sum = digit ** position
        sum.append(temp_sum)
        position += 1
    total = 0
    for item in sum:
        total = total + item
    if number == total:
        disarium_number = True

    return disarium_number


assert not is_disarium(75)
assert is_disarium(135)
assert not is_disarium(544)
assert is_disarium(518)
assert not is_disarium(466)
assert is_disarium(8)
