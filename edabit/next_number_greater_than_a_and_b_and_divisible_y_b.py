"""
You are given two numbers a and b. Create a function that returns the next number greater than a and b and
divisible by b.
"""

class NextNumber:

    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def get_next_number(self):
        a_or_b_bigger = 0
        this_flag = False
        if self.first_number > self.second_number:
            a_or_b_bigger = self.first_number
        if self.first_number < self.second_number:
            a_or_b_bigger = self.second_number
        next_number = a_or_b_bigger + 1
        while not this_flag:
            if next_number % self.second_number == 0:
                this_flag = True
            else:
                next_number += 1

        return next_number


if __name__ == "__main__":
    obj = NextNumber(17, 8)
    assert obj.get_next_number() == 24
    obj = NextNumber(98, 3)
    assert obj.get_next_number() == 99
    obj = NextNumber(14, 11)
    assert obj.get_next_number() == 22
