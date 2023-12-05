"""
Write a function that inverts the keys and values of a dictionary.
"""


def invert_keys_values(dict_to_invert) -> dict:
    output_dict = {}
    for k, v in dict_to_invert.items():
        output_dict[v] = k

    return output_dict


print(invert_keys_values({"z": "q", "w": "f"}))
print(invert_keys_values({"a": 1, "b": 2, "c": 3}))
print(invert_keys_values({"zebra": "koala", "horse": "camel"}))
