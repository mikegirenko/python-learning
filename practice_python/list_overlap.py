"""
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that
are common between the lists (without duplicates). Make sure your program
works on two lists of different sizes.

Extras:
Randomly generate two lists to test this
"""
from random import randint

a = []
b = []
max = 20
common_elements = []

for i in range(1, max):
    a.append(randint(1, max))
    b.append(randint(1, max))

for element in a:
    if element in b:
        if element not in common_elements:
            common_elements.append(element)

print(common_elements)
