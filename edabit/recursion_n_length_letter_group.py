"""
Very hard
Write a function that returns an array of strings populated from the slices of n-length characters of the given word
(a slice after another while n-length applies onto the word).
You are expected to solve this challenge via a recursive approach.
"""


class LetterGroups:
    def collect(self, given_word, characters_count) -> list:
        if len(given_word) < characters_count:
            array_of_strings = []
        else:
            array_of_strings = [
                given_word[i : i + characters_count]
                for i in range(0, len(given_word), characters_count)
            ]
            array_of_strings.sort()
            for item in array_of_strings:
                l = len(item)
                if len(item) < characters_count:
                    ind = array_of_strings.index(item)
                    array_of_strings.pop(ind)

        return array_of_strings


if __name__ == "__main__":
    letter_groups_object = LetterGroups()
    assert letter_groups_object.collect("intercontinentalisationalism", 6) == [
        "ationa",
        "interc",
        "ntalis",
        "ontine",
    ]
    assert letter_groups_object.collect("strengths", 3) == ["eng", "str", "ths"]
    assert letter_groups_object.collect(
        "pneumonoultramicroscopicsilicovolcanoconiosis", 15
    ) == ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"]
    assert letter_groups_object.collect("strengths", 30) == []
