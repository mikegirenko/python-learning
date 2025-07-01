import re

"""
Very hard
First, organize the words based on the numbers they have, then delete the numbers once they are organized.
"""


class Dakti:
    def dakiti(self, chorus_in_phrases):
        chorus_of_the_song = []
        dict_of_phrases = {}
        chorus_in_phrases_as_list_no_spaces = []
        chorus_in_phrases_as_list = chorus_in_phrases.split(" ")

        for item in chorus_in_phrases_as_list:
            if item != "" and len(item) > 1:
                chorus_in_phrases_as_list_no_spaces.append(item)

        for phrase in chorus_in_phrases_as_list_no_spaces:
            this_str = "".join(filter(str.isdigit, phrase))
            for item in this_str:
                if item != "":
                    phrase_index = int(this_str)
            dict_of_phrases[phrase_index] = phrase.replace(str(phrase_index), "")
        dict_of_phrases_sorted = sorted(dict_of_phrases.items())

        for item in dict_of_phrases_sorted:
            chorus_of_the_song.append(item[1])
        chorus_of_the_song_as_str = " ".join(chorus_of_the_song)

        return chorus_of_the_song_as_str


if __name__ == "__main__":
    obj = Dakti()
    print(obj.dakiti("worl2d hell1o"))
    print(obj.dakiti("i2s th1s a3 t4est    "))
    print(obj.dakiti("yo2u cr3azy a1re ?  "))
    print(obj.dakiti("en5tere y2a bab1y y3o 4me s6e not7a cuand8o 9me-ves"))
    print(obj.dakiti("quie3res bebe4r dime1 e5s qu6e qu2e tu7 er8es m9i-bebe"))
