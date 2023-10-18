"""
Write a function that takes a list of numbers and returns a list with two elements:
The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
"""


class SumOfOddAndEvenNumbers:
    def sum_of_odd_and_even_numbers(self, list_of_numbers) -> list:
        list_with_two_elements = [0, 0]
        even_numbers = []
        odd_numbers = []

        for number in list_of_numbers:
            if number % 2 == 0:
                even_numbers.append(number)
            if number % 2 != 0:
                odd_numbers.append(number)

        list_with_two_elements[0] = sum(even_numbers)
        list_with_two_elements[1] = sum(odd_numbers)

        return list_with_two_elements


if __name__ == "__main__":
    obj = SumOfOddAndEvenNumbers()
    list_of_numbers = [1, 2, 3, 4, 5, 6]
    print(f"list with two elements, {obj.sum_of_odd_and_even_numbers(list_of_numbers)}")
    list_of_numbers = [0, 0]
    print(f"list with two elements, {obj.sum_of_odd_and_even_numbers(list_of_numbers)}")


def test_sum_of_odd_and_even_numbers():
    obj = SumOfOddAndEvenNumbers()
    list_of_numbers = [0, 0]
    assert obj.sum_of_odd_and_even_numbers(list_of_numbers)
    list_of_numbers = [1, 2, 3, 4, 5, 6]
    assert obj.sum_of_odd_and_even_numbers(list_of_numbers) == [12, 9]
