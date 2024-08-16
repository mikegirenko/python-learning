"""
Very Hard
Create a function that returns the simplified version of a fraction.
"""

class SimplifiedFractions:
    def __init__(self, fraction):
        self.fraction = fraction

    def simplify(self):
        simplified_fraction = ""
        split_numbers = self.fraction.split("/")
        first_number = int(split_numbers[0])
        second_number = int(split_numbers[1])
        i = 1
        first_number_modulos = []
        while i < first_number:
            if i % 2 == 0:
                first_number_modulos.append(i)
            i += 1
        print(first_number_modulos)

        second_number_modulos = []
        for m in first_number_modulos:
            if second_number % m == 0:
                second_number_modulos.append(second_number / m)
        print(second_number_modulos)

        return simplified_fraction


if __name__ == "__main__":
    obj = SimplifiedFractions("100/400")
    obj.simplify()

