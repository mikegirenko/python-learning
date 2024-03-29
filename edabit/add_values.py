"""
Write a function that takes a list of lists and returns the value of all of the symbols in it
"""


def check_score(list_of_symbols):
    total_score = 0
    symbol_values = {"#": 5, "O": 3, "X": 1, "!": -1, "!!": -3, "!!!": -5}
    for list in list_of_symbols:
        for item in list:
            for k, v in symbol_values.items():
                if item == k:
                    total_score = total_score + v
    if total_score < 0:
        total_score = 0

    return total_score


assert check_score([["#", "!"], ["!!", "X"]]) == 2
assert check_score([["!!!", "O", "!"], ["X", "#", "!!!"], ["!!", "X", "O"]]) == 0
assert (
    check_score(
        [
            ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
            [
                "!!!",
                "!!!",
                "!!",
                "!!",
                "!",
                "!",
                "X",
                "!",
                "!!!",
                "O",
                "!",
                "!!!",
                "X",
                "#",
            ],
            [
                "#",
                "X",
                "#",
                "!!!",
                "!",
                "!!",
                "#",
                "#",
                "!!",
                "X",
                "!!",
                "!!!",
                "X",
                "O",
            ],
            [
                "!!",
                "X",
                "!!",
                "!!",
                "!!!",
                "#",
                "O",
                "O",
                "!!!",
                "#",
                "O",
                "O",
                "#",
                "!!",
            ],
            ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
            [
                "!!",
                "!!!",
                "X",
                "!!!",
                "!!",
                "!!",
                "!!!",
                "X",
                "O",
                "!",
                "#",
                "!!",
                "!!",
                "!!!",
            ],
            [
                "!!",
                "!!",
                "#",
                "O",
                "!",
                "!!",
                "!",
                "!!!",
                "#",
                "O",
                "#",
                "!",
                "#",
                "!!",
            ],
            [
                "X",
                "X",
                "O",
                "X",
                "!!!",
                "#",
                "!!!",
                "!!!",
                "X",
                "X",
                "X",
                "!",
                "#",
                "!!",
            ],
            ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
            ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
            [
                "!",
                "!!",
                "!!",
                "O",
                "!!",
                "!!",
                "#",
                "#",
                "!",
                "!!!",
                "O",
                "!",
                "#",
                "#",
            ],
            [
                "!",
                "!!!",
                "!!",
                "X",
                "!!",
                "!!",
                "#",
                "!!!",
                "O",
                "!!",
                "!!!",
                "!",
                "!",
                "!",
            ],
            [
                "!!!",
                "!!!",
                "!!",
                "O",
                "!",
                "!",
                "!!!",
                "!!!",
                "!!",
                "!!",
                "X",
                "!",
                "#",
                "#",
            ],
            ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"],
        ]
    )
    == 12
)
