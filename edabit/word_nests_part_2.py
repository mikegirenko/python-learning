"""
Very hard
Given a starting word and a final word nest, return True if the word nest is valid. Return False otherwise.
"""

class WordNests:
    def valid_word_nest(self, word_in, word_out) -> bool:
        is_valid = False
        print("word_in:", word_in)
        midpoint = 0
        #  A word nest is created by taking a starting word, and generating a new string by placing the word inside
        #  itself
        midpoint = len(word_in) // 2
        l, r = word_in[:midpoint], word_in[midpoint:]
        print("first midpoint:", l, r)
        first_string = l + "(" + word_in + ")" + r
        print("first_string:", first_string, " : expected: incre(incredible)dible" )

        midpoint = 0
        midpoint = len(first_string) // 2
        l, r = first_string[:midpoint], first_string[midpoint:]
        print("second midpoint:", l, r)
        second_string = l + "(" + word_in + ")" + r
        print("second_string:", second_string, " : expected: increin(incredible)credibledible")

        str_list = first_string.split(word_in)
        word_out = "".join(str_list)
        print("word out: ", word_out)

        return is_valid


if __name__ == "__main__":
    obj = WordNests()
    obj.valid_word_nest("incredible", "incredible")
    # obj.valid_word_nest("deep", "deep")
    # obj.valid_word_nest("novel", "novel")
