"""
Very Hard
Create a function that takes a number num and returns each place value in the number.
"""

def num_split(number_to_split) -> list:
    to_return = []
    if number_to_split > 0:
        list_of_numbers = [int(n) for n in str(number_to_split)]
        number_of_places = len(list_of_numbers)
        if number_of_places == 1:
            to_return.append(list_of_numbers[0])
        if number_of_places == 2:
            to_return.append(list_of_numbers[0] * 10)
            to_return.append(list_of_numbers[1])
        if number_of_places == 3:
            to_return.append(list_of_numbers[0] * 100)
            to_return.append(list_of_numbers[1] * 10)
            to_return.append(list_of_numbers[2])
    if number_to_split < 0:
        list_of_numbers = [int(n) for n in str(abs(number_to_split))]
        number_of_places = len(list_of_numbers)
        if number_of_places == 1:
            to_return.append(list_of_numbers[0] * -1)
        if number_of_places == 2:
            to_return.append(list_of_numbers[0] * -10)
            to_return.append(list_of_numbers[1] * -1)
        if number_of_places == 3:
            to_return.append(list_of_numbers[0] * -100)
            to_return.append(list_of_numbers[1] * -10)
            to_return.append(list_of_numbers[2] * -1)

    return to_return

print(num_split(3))  # [3]
print(num_split(39))  # [30, 9]
print(num_split(100))  # [[100, 0, 0]
print(num_split(-434))  # [-400, -30, -4]
