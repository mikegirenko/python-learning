"""
Write a function that accepts the height and width (m, n) and an optional proc s and generates a list with m elements.
Each element is a string consisting of either:
The default character (hash #) repeating n times (if no proc is given).
The character passed in through the proc repeating n times.
"""


def design_rug(height, width, proc="#"):
    make_rug = []
    width_string = proc * width
    for i in range(height):
        make_rug.append(width_string)
    for string in make_rug:
        print(string)


print("rug without optional proc")
design_rug(3, 5)
print("rug with #")
design_rug(3, 5, "#")
print("rug with $")
design_rug(3, 5, "$")
print("rug with A")
design_rug(2, 2, "A")
print("bigger rug")
design_rug(5, 11, "#")
