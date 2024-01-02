"""
Create a function that takes a number (step) as an argument and returns the amount of boxes in that step of the
sequence. Step (the input) is always a positive integer (or zero). For an odd step add 3, for an even step subtract 1
"""


def return_boxes(steps_count: int) -> int:  # return count of boxes, do not print
    boxes_count = 0
    if not isinstance(steps_count, int):
        boxes_count = "Error"
    elif steps_count == 0:
        boxes_count = 0
    elif steps_count % 2 == 0:
        boxes_count = boxes_count - 1
    elif steps_count % 2 != 0:
        boxes_count = boxes_count + 3

    return boxes_count


print("not integer:", return_boxes(0))
print("0:", return_boxes(0))
print("2:", return_boxes(2))
print("3:", return_boxes(3))
