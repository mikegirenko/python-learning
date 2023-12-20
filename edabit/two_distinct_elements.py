"""
In each input list, every number repeats at least once, except for two. Write a function that returns the two unique
numbers.
"""


def return_unique(input_list) -> list:
    output_list = []
    for number in input_list:
        if input_list.count(number) == 1:  # if number repeated once, add to output_list
            output_list.append(number)

    return output_list


assert return_unique([1, 9, 8, 8, 7, 6, 1, 6]) == [9, 7]
assert return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) == [2, 1]
assert return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) == [5, 6]
