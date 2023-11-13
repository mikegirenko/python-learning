"""
Create a function that takes two number strings and returns their sum as a string.
"""


class AddNumbers:
    def adding_numbers(self, number_one, number_two) -> str:
        if number_one == "" or number_two == "":
            this_sum = "Invalid Operation"
        else:
            this_sum = int(number_one) + int(number_two)
        return str(this_sum)


if __name__ == "__main__":
    obj = AddNumbers()
    assert obj.adding_numbers("111", "111") == "222"
    assert obj.adding_numbers("10", "80") == "90"
    assert obj.adding_numbers("", "20") == "Invalid Operation"
    assert obj.adding_numbers("20", "") == "Invalid Operation"
