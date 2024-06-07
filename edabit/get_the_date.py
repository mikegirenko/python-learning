import datetime

"""
Write a function that, given a date (in the format MM/DD/YYYY), returns the day of the week as a string
"""


def get_day(date) -> str:
    week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]
    date_split = date.split("/")
    year = int(date_split[2])
    month = int(date_split[0])
    day = int(date_split[1])

    int_day = datetime.date(year=year, month=month, day=day).weekday()
    if int_day == 6:
        day = week[int_day - 6]
    else:
        day = week[int_day + 1]

    return day


assert get_day("12/07/2016") == "Wednesday"
assert get_day("09/04/2016") == "Sunday"
assert get_day("12/08/2011") == "Thursday"
