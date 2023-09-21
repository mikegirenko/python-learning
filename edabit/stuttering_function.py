"""
Write a function that stutters a word as if someone is struggling to read it. The first two letters are
repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
Example: stutter("incredible") ➞ "in... in... incredible?"
"""

class Shutter:
    def stutter(self, word):
        stuttered_word = word[:2] + "... " + word[:2] + "... " + f"{word}" + "?"

        return stuttered_word


if __name__ == "__main__":
    obj = Shutter()
    print(obj.stutter("incredible"))
