"""
Given a function that accepts unlimited arguments, check and count how many data types are in those arguments.
Finally return the total in a list.
"""


def count_datatypes(*args) -> list:
    totals_list = []  # [int, str, bool, list, tuple, dictionary]
    int_count = 0
    str_count = 0
    bool_count = 0
    list_count = 0
    tuple_count = 0
    dictionary_count = 0
    for item in args:
        if isinstance(item, int) and type(item) != bool:
            int_count += 1
        if isinstance(item, str):
            str_count += 1
        if type(item) == bool:
            bool_count += 1
        if isinstance(item, list):
            list_count += 1
        if isinstance(item, tuple):
            tuple_count += 1
        if isinstance(item, dict):
            dictionary_count += 1
    totals_list.append(int_count)
    totals_list.append(str_count)
    totals_list.append(bool_count)
    totals_list.append(list_count)
    totals_list.append(tuple_count)
    totals_list.append(dictionary_count)

    return totals_list


print(count_datatypes(1, 45, "Hi", False))
print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))
print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23))
print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]))

