"""
Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every
alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.
"""


def loves_me(petals_count) -> str:
    string_to_return = []
    phrase_one = "Loves me"
    phrase_two = "Loves me not"

    for i in range(1, petals_count + 1):
        if i % 2 != 0:
            string_to_return.append(phrase_one)
        if i % 2 == 0:
            string_to_return.append(phrase_two)
        if i == petals_count:
            string_to_return[-1] = string_to_return[-1].upper()

    s = ", ".join(string_to_return)

    return s


assert loves_me(3) == "Loves me, Loves me not, LOVES ME"
assert (
    loves_me(6)
    == "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"
)
assert loves_me(1) == "LOVES ME"
