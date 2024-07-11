"""
The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the
alphabet
"""

import string


class AtbashCipher:

    def atbash(self, word) -> str:
        word = word.lower()
        atbash_cipher = []
        alph_list = list(string.ascii_lowercase)
        first_half = alph_list[0:13]
        second_half = alph_list[13:]

        for letter in word:
            if letter == " ":
                atbash_cipher.append(" ")
            if letter not in alph_list:
                atbash_cipher.append(letter)
            if letter in first_half:
                ind = first_half.index(letter)
                if ind == 0:
                    atbash_cipher.append(second_half[-1])
                if ind != 0:
                    atbash_cipher.append(second_half[-ind - 1])
            if letter in second_half:
                ind = second_half.index(letter)
                if ind == 0:
                    atbash_cipher.append(first_half[-1])
                if ind != 0:
                    atbash_cipher.append(first_half[-ind - 1])

        word_out = "".join(atbash_cipher)

        return word_out


if __name__ == "__main__":
    obj = AtbashCipher()
    print(obj.atbash("apple"))
    print(obj.atbash("Hello world!"))
    print(obj.atbash("Christmas is the 25th of December"))
