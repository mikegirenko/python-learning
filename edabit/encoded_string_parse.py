import re

"""
Create a function which takes in an encoded string and returns a dictionary according to the following example:
parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}
"""


def parse_code(encoded_string):
    dict_to_return = {}
    separated_string_as_list = re.split("0+", encoded_string)

    dict_to_return["first_name"] = separated_string_as_list[0]
    dict_to_return["last_name"] = separated_string_as_list[1]
    dict_to_return["id"] = separated_string_as_list[2]

    return dict_to_return


print(parse_code("John000Doe000123"))
print(parse_code("michael0smith004331"))
print(parse_code("Thomas00LEE0000043"))
