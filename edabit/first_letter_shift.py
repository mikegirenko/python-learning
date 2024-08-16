"""
Very Hard
Given a sentence, create a function which shifts the first letter of each word to the next word in the sentence
(shifting right).
"""


class FirstLetterShift:
    def shift_sentence(self, sentence_in) -> str:
        sentence_out = ""
        list_of_words = sentence_in.split(" ")
        print(list_of_words)
        i = 0
        while i < len(list_of_words):
            f_letter = list_of_words[i][i]
            list_of_words[i + 1][i] = f_letter
            print(list_of_words)

        return sentence_out


if __name__ == "__main__":
    obj = FirstLetterShift()
    print(obj.shift_sentence("create a function"))
