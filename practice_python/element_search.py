import random
"""
Write a function that takes an ordered list of numbers (a list where the
elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list
and returns (then prints) an appropriate boolean.

Extras:
Use binary search.
"""


def generate_list():
    random_list = []
    for i in range(1, 10):
        random_list.append(random.randint(1, 10))
    return sorted(random_list)


def check_if_inside(generated_list, number_to_find):
    list_to_check = generated_list
    print('Generated list is', list_to_check)
    print('Number to search for is', number_to_find)
    if number_to_find in list_to_check:
        return True
    else:
        return False


def check_if_inside_using_binary_search(generated_list, number_to_find):
    list_to_check = generated_list
    print('Generated list is', list_to_check)
    print('Number to search for is', number_to_find)
    middle = int(len(list_to_check) / 2)
    first_half = list_to_check[0:middle]
    second_half = list_to_check[middle:-1]
    if number_to_find in first_half:
        return True
    elif number_to_find in second_half:
        return True
    else:
        return False


if __name__ == "__main__":
    generated_list = generate_list()
    print(check_if_inside(generated_list, 5))
    print(check_if_inside_using_binary_search(generated_list, 3))
