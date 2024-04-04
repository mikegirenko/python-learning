"""
Create a function that takes in n, a, b and returns the number of positive values raised to the nth power that lie in
the range [a, b], inclusive.
"""


class PowerRanger:

    def power_ranger(self, n, a, b):
        number_of_positive_values = 0
        for i in range(1, b):
            raised = i**n
            if a <= raised <= b:
                number_of_positive_values += 1

        return number_of_positive_values


if __name__ == "__main__":
    obj = PowerRanger()
    assert obj.power_ranger(2, 49, 65) == 2
    assert obj.power_ranger(3, 1, 27) == 3
    assert obj.power_ranger(10, 1, 5) == 1
    assert obj.power_ranger(5, 31, 33) == 1
    assert obj.power_ranger(4, 250, 1300) == 3
