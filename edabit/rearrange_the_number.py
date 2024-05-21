"""
Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are
rearranged.
"""


class RearrangeTheNumber:

    def rearranged_difference(self, number_to_rearrange):
        max_number = self.rearranger(number_to_rearrange, "desc")
        min_number = self.rearranger(number_to_rearrange, "asc")
        difference = max_number - min_number

        return difference

    def rearranger(self, number_to_rearrange, sort_order):
        list_of_numbers = [int(x) for x in str(number_to_rearrange)]
        sorted_list_of_numbers = 0
        if sort_order == "asc":
            sorted_list_of_numbers = sorted(list_of_numbers)
        if sort_order == "desc":
            sorted_list_of_numbers = sorted(list_of_numbers, reverse=True)
        sorted_numbers = int("".join(map(str, sorted_list_of_numbers)))

        return sorted_numbers


if __name__ == "__main__":
    obj = RearrangeTheNumber()

    assert obj.rearranger(972882, "asc") == 227889
    assert obj.rearranger(972882, "desc") == 988722

    result = obj.rearranged_difference(972882)
    assert result == 760833, f"Function returned {result}"

    result = obj.rearranged_difference(3320707)
    assert result == 7709823, f"Function returned {result}"

    result = obj.rearranged_difference(90010)
    assert result == 90981, f"Function returned {result}"
