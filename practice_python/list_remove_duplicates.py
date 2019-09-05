"""
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Extras:
Write two different functions to do this - one using a loop and constructing a
list, and another using sets.
"""

a = [1, 1, 3, 7, 0, 1, 7]
b = [55, 1, 1, 0, 3, 7, 0, 1, 7]


def return_new_list_using_loop(old_list):
    new_list = []
    for i in old_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


def return_new_list_using_set(old_list):
    new_list = []
    new_list = set(old_list)
    new_list = list(new_list)
    return new_list


print(return_new_list_using_loop(a))
print(return_new_list_using_set(b))
