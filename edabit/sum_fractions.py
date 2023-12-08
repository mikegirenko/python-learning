import math

"""
Create a function that takes a list containing nested lists as an argument. Each sublist has 2 elements. 
The first element is the numerator and the second element is the denominator. Return the sum of the fractions 
rounded to the nearest whole number.
"""


def sum_fractions(list_in):
    sum_of_fractions = 0
    fract = 0
    for sublist in list_in:
        fract = sublist[0] / sublist[1]
        sum_of_fractions = sum_of_fractions + fract

    return math.floor(sum_of_fractions)


assert sum_fractions([[18, 13], [4, 5]]) == 2
assert sum_fractions([[36, 4], [22, 60]]) == 9
assert sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]) == 11
