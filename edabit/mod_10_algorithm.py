"""
Very hard
Create a function that takes a number and checks whethers the given number is a valid credit card number
using Luhn Algorithm. The return value is boolean.
"""


class ModTenAlgorithm:
    def valid_credit_card(self, given_number) -> bool:
        is_valid_card_number = False
        num_to_str = str(given_number)
        original_check_digit = num_to_str[-1]
        # Drop the check digit (last digit) of the number to validate. (e.g. 17893729974 → 1789372997)
        without_dropped_digit = num_to_str[:-1]
        #  Moving from right to left, double every second digit, starting from the last digit.
        #  If doubling a digit results in a value > 9, subtract 9 from it.
        doubled_numbers_as_list = []
        i = 1
        for digit in without_dropped_digit:
            if i % 2 != 0:
                doubled_numbers_as_list.append(int(digit))
            if i % 2 == 0:
                doubled_numbers_as_list.append(int(digit) * 2)
            i += 1
        #  Sum all the resulting digits (including the ones that were not doubled). If double from above is 14, then
        #  1+4 = 5
        sum_of_numbers_as_list = []
        for number in doubled_numbers_as_list:
            if number < 10:
                sum_of_numbers_as_list.append(number)
            if number >= 10:
                sum_of_digits = 0
                list_of_digits = [int(i) for i in str(number)]
                for digit in list_of_digits:
                    sum_of_digits = sum_of_digits + digit
                sum_of_numbers_as_list.append(sum_of_digits)
        sum_of_the_resulting_digits = 0
        for digit in sum_of_numbers_as_list:
            sum_of_the_resulting_digits = sum_of_the_resulting_digits + digit
        #  If the sum is evenly divisible by 10, then the sequence / card number is valid. ??
        final_check_digit = 10 - (sum_of_the_resulting_digits % 10) % 10
        if original_check_digit == final_check_digit:
            is_valid_card_number = True

        return is_valid_card_number


if __name__ == "__main__":
    obj = ModTenAlgorithm()
    print(obj.valid_credit_card(4111111111111111))
    print(obj.valid_credit_card(6451623895684318))
