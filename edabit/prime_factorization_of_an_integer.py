"""
Very Hard
Create a function that returns a list containing the prime factors of whatever integer is passed to it.
"""
import math


def prime_factors(integer_in) -> list:
    list_containing_prime_factors = []

    # Print the number of two's that divide n
    while integer_in % 2 == 0:
        list_containing_prime_factors.append(2)
        integer_in = integer_in / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(integer_in)) + 1, 2):
        # while i divides n, print i and divide n
        while integer_in % i == 0:
            list_containing_prime_factors.append(i)
            integer_in = integer_in / i

    # Condition if n is a prime
    # number greater than 2
    if integer_in > 2:
        list_containing_prime_factors.append(int(integer_in))

    return list_containing_prime_factors


print(prime_factors(20))  # [2, 2, 5]
print(prime_factors(100))  # [2, 2, 5, 5]
print(prime_factors(8912234))  # [2, 47, 94811]
