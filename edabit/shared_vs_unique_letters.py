"""
Create a function that takes in two words as input and returns a list of three elements, in the following order:
 1. Shared letters between two words.
 2. Letters unique to word 1.
 3. Letters unique to word 2.
Each element should have unique letters, and have each letter be alphabetically sorted.
"""


class SharedVsUniqueLetters:

    def letters(self, word_one, word_two) -> list:
        list_to_return = []
        shared_letters_list = []
        word_one_unique_letters_list = []
        word_two_unique_letters_list = []
        for letter in word_one:
            if letter in word_two:
                shared_letters_list.append(letter)
        shared_letters_set = set(shared_letters_list)
        shared_letters = "".join(sorted(shared_letters_set))

        for letter in word_one:
            if letter not in word_two:
                word_one_unique_letters_list.append(letter)
        word_one_unique_letters_set = set(word_one_unique_letters_list)
        word_one_unique_letters = "".join(sorted(word_one_unique_letters_set))

        for letter in word_two:
            if letter not in word_one:
                word_two_unique_letters_list.append(letter)
        word_two_unique_letters_set = set(word_two_unique_letters_list)
        word_two_unique_letters = "".join(sorted(word_two_unique_letters_set))

        list_to_return.append(shared_letters)
        list_to_return.append(word_one_unique_letters)
        list_to_return.append(word_two_unique_letters)

        return list_to_return


if __name__ == "__main__":
    obj = SharedVsUniqueLetters()
    assert obj.letters("sharp", "soap") == ["aps", "hr", "o"]
    assert obj.letters("board", "bored") == ["bdor", "a", "e"]
    assert obj.letters("happiness", "envelope") == ["enp", "ahis", "lov"]
    assert obj.letters("kerfuffle", "fluffy") == ["flu", "ekr", "y"]
    assert obj.letters("match", "ham") == ["ahm", "ct", ""]
