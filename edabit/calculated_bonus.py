"""
Write a function to read the billable days of an employee and return the bonus he/she has obtained in that quarter.
"""


class CalculatedBonus:
    def __init__(self, billable_days):
        self.billable_days = billable_days

    def bonus(self) -> int:
        calculated_bonus = 0
        if self.billable_days <= 32:
            calculated_bonus = 0
        if 33 <= self.billable_days <= 40:
            calculated_bonus = (self.billable_days - 32) * 325
        if 41 <= self.billable_days <= 48:
            calculated_bonus = (8 * 325) + ((self.billable_days - 40) * 550)
        if 48 < self.billable_days:
            calculated_bonus = (8 * 325) + (8 * 550) + ((self.billable_days - 48) * 600)

        return calculated_bonus


if __name__ == "__main__":
    days = 15
    calc_bonus_obj = CalculatedBonus(days)
    assert calc_bonus_obj.bonus() == 0

    days = 37
    calc_bonus_obj = CalculatedBonus(days)
    assert calc_bonus_obj.bonus() == 1625

    days = 45
    calc_bonus_obj = CalculatedBonus(days)
    assert calc_bonus_obj.bonus() == 5350

    days = 50
    calc_bonus_obj = CalculatedBonus(days)
    assert calc_bonus_obj.bonus() == 8200
