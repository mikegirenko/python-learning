"""
Create a function that takes a list and string. The function should remove the letters in the string from the list,
and return the list.
"""


class RemoveTheWord:

    def remove_letters(self, list_to_clean, string_to_use) -> list:
        list_to_return = list_to_clean
        for letter in string_to_use:
            for l in list_to_return:
                if letter == l:
                    list_to_return.remove(l)

        return list_to_return


if __name__ == "__main__":
    obj = RemoveTheWord()
    print(obj.remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
    print(obj.remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))
    print(obj.remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))
