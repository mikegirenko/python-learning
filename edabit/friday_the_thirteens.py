"""
Given the month and year as numbers, return whether that month contains a Friday 13th.
can use Python's datetime module.
"""
from datetime import date


class Friday13th:
    def has_friday_13(self, month, year) -> bool:
        has_friday_13th = date(year, month, 13).strftime("%A") == "Friday"

        return has_friday_13th


if __name__ == "__main__":
    friday13obj = Friday13th()

    assert friday13obj.has_friday_13(3, 2020)
    assert friday13obj.has_friday_13(10, 2017)
    assert not friday13obj.has_friday_13(1, 1985)
