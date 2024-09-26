"""
Very Hard
Write two functions:
One that returns the maximum product of three numbers in a list.
One that returns the minimum product of three numbers in a list.
The triplet of an array is a tuple of three elements of different indices, represented by (i, j, k)
"""
import math


def max_product(input_list) -> int:
    # Find triplets
    list_of_triplets = []
    n = len(input_list)
    # Fix the first element as arr[i]
    for i in range(n - 2): # The range() function returns a sequence of numbers, so, 0, 1, 2
        # Fix the second element as arr[j]
        for j in range(i + 1, n - 1):
            # Now look for the third number
            for k in range(j + 1, n):
                list_of_triplets.append([input_list[i], input_list[j], input_list[k]])

    # Find max from list of triplets:
    triplet_sum = 0
    temp_triplet_sum = 0
    for triplet in list_of_triplets:
        triplet_sum = math.prod(triplet)
        if temp_triplet_sum < triplet_sum:
            temp_triplet_sum = triplet_sum
        else:
            triplet_sum = temp_triplet_sum
    product = triplet_sum

    return product



def min_product(input_list) -> int:
    # Find triplets
    list_of_triplets = []
    n = len(input_list)
    # Fix the first element as arr[i]
    for i in range(n - 2):
        # Fix the second element as arr[j]
        for j in range(i + 1, n - 1):
            # Now look for the third number
            for k in range(j + 1, n):
                list_of_triplets.append([input_list[i], input_list[j], input_list[k]])

    # Find max from list of triplets:
    triplet_sum = 0
    temp_triplet_sum = 0
    for triplet in list_of_triplets:
        triplet_sum = math.prod(triplet)
        if temp_triplet_sum > triplet_sum:
            temp_triplet_sum = triplet_sum
        else:
            triplet_sum = temp_triplet_sum
    product = triplet_sum

    return product


assert max_product([-8, -9, 1, 2, 7]) == 504
# assert max_product([-8, 1, 2, 7, 9]) == 126
# assert min_product([1, -1, 1, 1]) == -1
# assert min_product([-5, -3, -1, 0, 4]) == -15
