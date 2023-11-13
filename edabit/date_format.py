"""
Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
"""


def date_format(date_to_reformat) -> str:
    year = date_to_reformat[6:]
    day = date_to_reformat[3] + date_to_reformat[4]
    month = date_to_reformat[:2]

    reformatted_date = year + day + month
    return reformatted_date


assert date_format("11/12/2019") == "20191211"
assert date_format("12/31/2019") == "20193112"
assert date_format("01/15/2019") == "20191501"
