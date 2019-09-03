"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no
divisors.). You can (and should!) use your answer to Exercise 4 to help you.
"""

user_input = input("Enter a number: ")


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if is_prime(int(user_input)):
    print(user_input, "is a Prime number")
else:
    print(user_input, "is not a Prime number")
