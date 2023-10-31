"""
Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?!

Given a dictionary of the stolen items and a string in lowercase representing the name of the pet (e.g. "rambo"), return:
"Rambo is gone..." if the name is on the list.
"Rambo is here!" if the name is not on the list.

Note that the first letter of the name in the return statement is capitalized.
"""

STOLEN_ITEMS_GONE = {
    "tv": 30,
    "timmy": 20,
    "stereo": 50,
}  # ➞ "Timmy is gone..."

PET_NAME = "timmy"

STOLEN_ITEMS_HERE = {
    "tv": 30,
    "stereo": 50,
}  # ➞ "Timmy is here!"

STOLEN_ITEMS_EMPTY = {}  # ➞ "Timmy is here!"


class BurglarySeries:
    def is_it_gone(self, stolen_items, pet_name) -> str:
        if pet_name in stolen_items.keys():
            cap_name = pet_name.title()
            message = f"{cap_name} is gone..."
        else:
            cap_name = pet_name.title()
            message = f"{cap_name} is here!"

        return message


if __name__ == "__main__":
    obj = BurglarySeries()
    print(obj.is_it_gone(STOLEN_ITEMS_GONE, PET_NAME))
    print(obj.is_it_gone(STOLEN_ITEMS_HERE, PET_NAME))
    print(obj.is_it_gone(STOLEN_ITEMS_EMPTY, PET_NAME))
