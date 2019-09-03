"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

a = [1, 5, 10, 15, 20, 25, 100]


def new_list(original_list):

    return [original_list[0], original_list[-1]]


print(new_list(a))
