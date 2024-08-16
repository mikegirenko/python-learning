"""
Very Hard
Given a sentence, create a function which shifts the first letter of each word to the next word in the sentence
(shifting right).
"""


class FirstLetterShift:
    def shift_sentence(self, sentence_in) -> str:
        sentence_out = ""
        list_of_lists = []
        list_of_words = sentence_in.split(" ")
        for i in list_of_words:
            list_of_lists.append(list(i))
        i = 0
        if len(list_of_lists) == 1:
            sentence_out = sentence_in
        else:
            while i < len(list_of_lists):
                if i == 0:
                    f_letter = list_of_words[i][0]
                    list_of_lists[i + 1][0] = f_letter
                if i == len(list_of_lists) - 1:
                    f_letter = list_of_words[len(list_of_words) - 1][0]
                    list_of_lists[0][0] = f_letter
                if 0 < i < len(list_of_lists) - 1:
                    f_letter = list_of_words[i][0]
                    list_of_lists[i + 1][0] = f_letter
                i += 1

        list_of_strings = []
        for i in list_of_lists:
            list_of_strings.append("".join(i))
        sentence_out = " ".join(list_of_strings)

        return sentence_out


if __name__ == "__main__":
    obj = FirstLetterShift()
    assert obj.shift_sentence("create a function") == "freate c aunction"
    assert (
        obj.shift_sentence("it should shift the sentence")
        == "st ihould shift she tentence"
    )
    assert (
        obj.shift_sentence("the output is not very legible")
        == "lhe tutput os iot nery vegible"
    )
    assert obj.shift_sentence("edabit") == "edabit"
