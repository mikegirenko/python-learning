"""
Create a function that takes a number (num) and returns its length
"""


class NumberLength:
    def number_length(self, number) -> int:
        length = 0
        number_to_string = str(number)
        length = len(number_to_string)

        return length


if __name__ == "__main__":
    obj = NumberLength()
    number = 5000
    number_length = obj.number_length(number)
    print(f"Number length is {number_length}")

    assert number_length == 4
