"""
Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.
Write a function that takes in a name and returns a name tag, that should read:
If the name is not in the dictionary, return: "Hi! I'm a guest."
"""


def greeting(name):
    guest_list = {
        "Randy": "Germany",
        "Karla": "France",
        "Wendy": "Japan",
        "Norman": "England",
        "Sam": "Argentina",
    }
    for k, v in guest_list.items():
        if k == name:
            name_tag = f"Hi! I'm {k}, and I'm from {v}."
        else:
            name_tag = "Hi! I'm a guest."

    return name_tag


print(greeting("Randy"))
print(greeting("Sam"))
print(greeting("Monti"))
