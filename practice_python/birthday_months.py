"""
In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this
exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many
scientists have a birthday in each month.

"""
from collections import Counter
from practice_python import birthday_json

FILE_WITH_DATA = "birthdays_data.json"
months_string = []

o = birthday_json.Birthdays()
dict_with_data = o.read_file(FILE_WITH_DATA)

for v in dict_with_data.values():
    months_string.append(v[:3])

print(Counter(months_string))
