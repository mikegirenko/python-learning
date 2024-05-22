"""
You are given three inputs: a string, one letter, and a second letter. Write a function that returns True if every
instance of the first letter occurs before every instance of the second letter.
"""


class FirstBeforeSecondLetter:

    def first_before_second(self, a_string, first_letter, second_letter) -> bool:
        value_to_return = False

        count_a = a_string.count(first_letter)
        count_b = a_string.count(second_letter)

        stop = 0
        if count_a > count_b:
            stop = count_b
        if count_a < count_b:
            stop = count_a
        if count_a == count_b:
            stop = count_a

        first_letter_indexes = []
        for i in range(0, len(a_string)):
            if a_string[i] == first_letter:
                first_letter_indexes.append(i)

        second_letter_indexes = []
        for i in range(0, len(a_string)):
            if a_string[i] == second_letter:
                second_letter_indexes.append(i)

        for i in range(0, stop):
            if first_letter_indexes[i] < second_letter_indexes[i]:
                value_to_return = True

        return value_to_return


if __name__ == "__main__":

    obj = FirstBeforeSecondLetter()
    print(obj.first_before_second("a rabbit jumps joyfully", "a", "j"))
    print(obj.first_before_second("knaves knew about waterfalls", "k", "w"))
    print(obj.first_before_second("happy birthday", "a", "y"))
    print(obj.first_before_second("precarious kangaroos", "k", "a"))
