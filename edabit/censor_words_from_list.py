"""
Create a function that takes a string txt and censors any word from a given list lst. The text removed must be
replaced by the given character char.
"""


class CensorWords:
    def censor_string(self, text_to_censor, words_to_censor, character_to_use):
        censored_string = []
        censored_string_to_list = text_to_censor.split(" ")
        for item in censored_string_to_list:
            if item not in words_to_censor:
                censored_string.append(item)
            if item in words_to_censor:
                replaced_text = character_to_use * len(item)
                censored_string.append(replaced_text)

        return censored_string


if __name__ == "__main__":
    censor_words_obj = CensorWords()
    print(
        censor_words_obj.censor_string("Today is a Wednesday!", ["Today", "a"], "-")
    )  # "----- is - Wednesday!"
    print(
        censor_words_obj.censor_string(
            "The cow jumped over the moon.", ["cow", "over"], "*"
        )
    )  # "The *** jumped
    # **** the moon."
    print(
        censor_words_obj.censor_string(
            "Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"
        )
    )  # "Why *** the ******* cross the ****?"
