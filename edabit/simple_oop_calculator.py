"""
Create methods for the Calculator class that can do the following:
Add two numbers.
Subtract two numbers.
Multiply two numbers.
Divide two numbers.
"""


class OopCalculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def add_numbers(self) -> int:
        result = self.first_number + self.second_number

        return result

    def subtract_numbers(self) -> int:
        result = self.first_number - self.second_number

        return result

    def multiply_numbers(self) -> int:
        result = self.first_number * self.second_number

        return result

    def divide_numbers(self) -> int:
        result = self.first_number / self.second_number

        return result


if __name__ == "__main__":
    calculator = OopCalculator(10, 5)
    assert calculator.add_numbers() == 15
    assert calculator.subtract_numbers() == 5
    assert calculator.multiply_numbers() == 50
    assert calculator.divide_numbers() == 2
