"""
Create a function that finds the highest integer in the list using recursion.
"""
import random


class Highest_Integer:

    def highest_integer(self, integers_list):
        hi = 0
        for i in range(0, len(integers_list) - 1):
            if hi < integers_list[i]:
                hi = integers_list[i]

        return hi

    def generate_random_list(self):
        random_list = []
        for i in range (0, 100):
            random_list.append(random.randint(0, 100))

        return random_list


if __name__ == "__main__":
    obj = Highest_Integer()
    this_list = obj.generate_random_list()
    print("List is", this_list)
    highest_integer = obj.highest_integer(this_list)
    print("Highest integer is", highest_integer)
