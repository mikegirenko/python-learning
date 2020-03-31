"""
Implement a function that takes as input three variables, and returns the largest of the three.
Do this without using the Python max() function!

"""


def max_of_three(one, two, three):
    if (one >= two) and (one >= three):
        largest = one
    elif (two >= one) and (two >= three):
        largest = two
    else:
        largest = three

    return largest


print(max_of_three(5, 7, 11))
