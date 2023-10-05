"""
Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
"""


class FizzBuzz:
    def fizz_buzz(self, number) -> str:
        output = ""

        if number % 3 != 0 or number % 5 != 0:
            output = str(number)
        if number % 3 == 0:
            output = "Fizz"
        if number % 5 == 0:
            output = "Buzz"
        if number % 3 == 0 and number % 5 == 0:
            output = "FizzBuzz"

        return output


if __name__ == "__main__":
    number = 5
    obj = FizzBuzz()
    print(obj.fizz_buzz(number))


def test_fizz_buzz():
    assert obj.fizz_buzz(4) == "4"
    assert type(obj.fizz_buzz(4)) == str
    assert obj.fizz_buzz(3) == "Fizz"
    assert obj.fizz_buzz(5) == "Buzz"
    assert obj.fizz_buzz(15) == "FizzBuzz"


test_fizz_buzz()
