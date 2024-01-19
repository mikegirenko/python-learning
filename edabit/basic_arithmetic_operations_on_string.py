"""
Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and
division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
"""


def arithmetic_operation(string_to_calculate) -> int:
    calculated_number = 0
    split_string_to_calculate = string_to_calculate.split()
    first_number = int(split_string_to_calculate[0])
    operator = split_string_to_calculate[1]
    second_number = int(split_string_to_calculate[2])

    if operator == "+":
        calculated_number = first_number + second_number
    if operator == "-":
        calculated_number = first_number - second_number
    if operator == "*":
        calculated_number = first_number * second_number
    if operator == "/":
        if second_number == 0:
            calculated_number = -1
        else:
            calculated_number = int(first_number) / int(second_number)

    return int(calculated_number)


assert arithmetic_operation("12 + 12") == 24
assert arithmetic_operation("12 - 12") == 0
assert arithmetic_operation("12 * 12") == 144
assert arithmetic_operation("24 / 2") == 12
assert arithmetic_operation("12 / 0") == -1
