import random
"""
Take two lists, say for example these two:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that
are common between the lists (without duplicates).

Extra:
Randomly generate two lists to test this
Write this in one line of Python using at least one list comprehension
"""


def find_common_elements(list_a, list_b):
    list_of_common_elements = []
    for element in list_a:
        if element in list_b:
            if element not in list_of_common_elements:
                list_of_common_elements.append(element)
    return list_of_common_elements


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("Common elements in a and b", find_common_elements(a, b))

c = random.sample(range(100), 10)
print("List c", c)
d = random.sample(range(100), 12)
print("List d", d)

common_elements = [a for a in c if a in d]
print("Common elements in c and d using list comprehension", common_elements)
