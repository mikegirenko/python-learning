"""
Create a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list.
"""


def flip_list(list_to_flip) -> list:
    flipped_list = []

    if len(list_to_flip) == 0:
        pass
    elif type(list_to_flip[0]) is int:
        for item in list_to_flip:
            flipped_list.append(list(str(item)))
    elif type(list_to_flip[0]) is list:
        for item in list_to_flip:
            for s in item:
                flipped_list.append(int(s))

    return flipped_list


print(flip_list([1, 2, 3, 4]))
print(flip_list([[5], [6], [9]]))
print(flip_list([]))
