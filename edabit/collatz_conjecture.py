"""
Create a function that, when given two positive integers a b, returns the string "a" if integer a took fewer steps to
reach 1 than b when passed through the Collatz sequence, or "b" if integer b took fewer steps to reach 1 than a.
"""

class CollatzConjecture:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def collatz(self) -> str:
        reached_one = ""
        a_number_of_attempts = self.calculate_attempts(self.a)
        b_number_of_attempts = self.calculate_attempts(self.b)
        if a_number_of_attempts < b_number_of_attempts:
            reached_one = "a"
        if a_number_of_attempts > b_number_of_attempts:
            reached_one = "b"

        return reached_one

    def calculate_attempts(self, this_number) -> int:
        attempt_counter = 0
        keep_checking = True
        while keep_checking:
            if this_number % 2 == 0:
                this_number = this_number / 2
                attempt_counter += 1
            if this_number % 2 != 0 and this_number != 1:
                this_number = (this_number * 3) + 1
                attempt_counter += 1
            if this_number == 1:
                keep_checking = False

        return attempt_counter


if __name__ == "__main__":
    obj = CollatzConjecture(10, 15)
    print(obj.collatz())

    obj = CollatzConjecture(13, 16)
    print(obj.collatz())

    obj = CollatzConjecture(53782, 72534)
    print(obj.collatz())
