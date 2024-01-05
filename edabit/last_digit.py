"""
Your job is to create a function, that takes 3 numbers: a, b, c and returns True if the last digit
of a * b = the last digit of c. Check the examples below for an explanation.
"""


class LastDigit:
    def find_last_digit(self, a, b, c) -> bool:
        last_digit = False
        a_last_digit = a % 10
        b_last_digit = b % 10
        c_last_digit = c % 10
        a_times_b = a_last_digit * b_last_digit
        if a_times_b < 10:
            if a_times_b == c_last_digit:
                last_digit = True
        if a_times_b > 9:
            a_times_b_last_digit = a_times_b % 10
            if a_times_b_last_digit == c_last_digit:
                last_digit = True

        return last_digit


if __name__ == "__main__":
    last_digit_obj = LastDigit()
    assert last_digit_obj.find_last_digit(25, 21, 125)
    assert last_digit_obj.find_last_digit(55, 226, 5190)
    assert not last_digit_obj.find_last_digit(12, 215, 214)
