"""
Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence
is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
"""


def consecutive_combo(array_1, array_2) -> bool:
    is_consecutive_sequence = False
    sorted_array_1 = sorted(array_1)
    sorted_array_2 = sorted(array_2)
    start = 0
    if sorted_array_1[0] < sorted_array_2[0]:
        start = sorted_array_1[0]
    if sorted_array_2[0] < sorted_array_1[0]:
        start = sorted_array_2[0]
    if sorted_array_1[0] == sorted_array_2[0]:
        start = sorted_array_1[0]
    combined_array = sorted_array_1 + sorted_array_2
    combined_array_union = set().union(combined_array)
    counter = start
    truth_counter = []
    for item in combined_array_union:
        if counter == item:
            truth_counter.append(True)
        counter += 1
    if len(truth_counter) == len(combined_array_union):
        is_consecutive_sequence = True

    return is_consecutive_sequence


assert consecutive_combo([7, 4, 5, 1], [2, 3, 6])
assert not consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9])
assert not consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10])
assert consecutive_combo([44, 46], [45])
