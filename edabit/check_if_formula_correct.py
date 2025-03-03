"""
Very hard
Create a function that takes a string and returns True or False depending on whether or not the given formula is
correct.
"""


class Formula:
    def formula(self, formula_as_string) -> bool:
        formula_correct = False
        if formula_as_string == "":
            formula_correct = None
        else:
            formula_without_spaces = formula_as_string.replace(" ", "")
            operand = ""
            for ch in formula_without_spaces:
                if ch in ("*", "/"):
                    operand = ch
            first_split = formula_without_spaces.split(operand)
            first_number = int(first_split[0])
            second_split = first_split[1].split("=")
            second_number = int(second_split[0])
            total = int(second_split[1])
            if operand == "*":
                calculated_total = first_number * second_number
                if calculated_total == total:
                    formula_correct = True
            if operand == "/":
                calculated_total = first_number / second_number
                if calculated_total == total:
                    formula_correct = True

        return formula_correct


if __name__ == "__main__":
    obj = Formula()
    print(obj.formula("6 * 4 = 24"))
    print(obj.formula("18 / 17 = 2"))
    print(obj.formula(""))
