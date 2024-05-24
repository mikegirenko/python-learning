"""
Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise, two
lines rhyme if the last word from each sentence contains the same vowels.
"""


class RhymeTime:

    def does_rhyme(self, line_one, line_two) -> bool:
        rhyme = False
        vowels = ["a", "e", "i", "o", "u"]

        line_one = line_one.lower()
        line_one_split = line_one.split(" ")
        line_one_last_word = line_one_split[-1]

        line_two = line_two.lower()
        line_two_split = line_two.split(" ")
        line_two_last_word = line_two_split[-1]

        line_one_last_word_vowels = []
        for vowel in vowels:
            if line_one_last_word.find(vowel) != -1:
                line_one_last_word_vowels.append(vowel)

        line_two_last_word_vowels = []
        for vowel in vowels:
            if line_two_last_word.find(vowel) != -1:
                line_two_last_word_vowels.append(vowel)

        if len(line_one_last_word_vowels) == len(line_two_last_word_vowels):
            if line_one_last_word_vowels == line_one_last_word_vowels:
                rhyme = True

        return rhyme


if __name__ == "__main__":
    obj = RhymeTime()
    assert obj.does_rhyme("Sam I am!", "Green eggs and ham.")
    assert obj.does_rhyme("Sam I am!", "Green eggs and HAM.")
    assert not obj.does_rhyme("You are off to the races", "a splendid day.")
    assert not obj.does_rhyme("and frequently do?", "you gotta move.")
