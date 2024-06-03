"""
Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in your
function. The target number will be from 2 through 97. If the target is prime then return "yes" else return "no".
"""

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def is_prime(list_of_primes, target_number) -> str:
    prime_number = "no"
    if target_number in list_of_primes:
        prime_number = "yes"

    return prime_number


print(is_prime(PRIMES, 3))
print(is_prime(PRIMES, 4))


def is_prime_v1(list_of_primes, target_number) -> str:
    prime_number = "no"
    for prime in list_of_primes:
        if target_number == prime:
            prime_number = "yes"

    return prime_number


print(is_prime_v1(PRIMES, 3))
print(is_prime_v1(PRIMES, 4))


def is_prime_v2(list_of_primes, target_number) -> str:
    prime_number = ""

    def binary_search(arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0

        while low <= high:
            m = (high + low) / 2
            mid = int(m)
            # If x is greater, ignore left half
            if arr[mid] < x:
                low = mid + 1
            # If x is smaller, ignore right half
            elif arr[mid] > x:
                high = mid - 1
            # means x is present at mid
            else:
                return mid
        # If we reach here, then the element was not present
        return -1

    result = binary_search(list_of_primes, target_number)

    if result != -1:
        prime_number = "yes"
    else:
        prime_number = "no"

    return prime_number


print(is_prime_v2(PRIMES, 3))
print(is_prime(PRIMES, 4))
