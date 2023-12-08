"""
Given a dictionary with at least one key/value pair, convert all the values to numbers.
"""


def convert_to_number(dict_to_convert) -> dict:
    dict_out = {}
    for k, v in dict_to_convert.items():
        dict_out[k] = int(v)

    return dict_out


print(convert_to_number({"piano": "200"}))
print(convert_to_number({"piano": "200", "tv": "300"}))
print(convert_to_number({"piano": "200", "tv": "300", "stereo": "400"}))
