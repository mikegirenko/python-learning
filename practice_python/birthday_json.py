"""
In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your
program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary
defined in the program.
"""
import json

FILE_WITH_DATA = "birthdays_data.json"


class Birthdays:

    def read_file(self, file_name):
        with open(FILE_WITH_DATA, "r") as f:
            info = json.load(f)
        f.close()
        return info


if __name__ == "__main__":
    o = Birthdays()
    dict_with_data = o.read_file(FILE_WITH_DATA)

    print("Augusto Boal's date of birth is", dict_with_data['Augusto Boal'])

    for k, v in dict_with_data.items():
        print(k, 'date of birth is', v)
