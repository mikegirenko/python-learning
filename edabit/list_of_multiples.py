"""
Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until
the list length reaches length.
"""


def list_of_multiples(num, length) -> list:
    list_of_multiples = []
    multiple = 0
    for i in range(1, length + 1):
        multiple = num * i
        list_of_multiples.append(multiple)

    return list_of_multiples


assert list_of_multiples(7, 5) == [7, 14, 21, 28, 35]
assert list_of_multiples(12, 10) == [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
assert list_of_multiples(17, 6) == [17, 34, 51, 68, 85, 102]
