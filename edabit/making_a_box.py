"""
Create a function that creates a box based on dimension n.
"""


def make_box(dimension):
    if dimension == 5:
        # top horizontal row
        for i in range(0, dimension):
            print("#", end="")
        # middle columns
        spacing = " "
        print("\n#", spacing, "#")
        for i in range(0, dimension - 3):
            print("#", spacing, "#")
        # bottom horizontal row
        for i in range(0, dimension):
            print("#", end="")
    if dimension == 3:
        # top horizontal row
        for i in range(0, dimension):
            print("#", end="")
        # middle columns
        print("\n#", "#")
        for i in range(0, dimension - 3):  # -3
            print("#", spacing, "#")
        # bottom horizontal row
        for i in range(0, dimension):
            print("#", end="")
    if dimension == 2:
        # top horizontal row
        for i in range(0, dimension):
            print("#", end="")
        # middle column
        print("")
        # bottom horizontal row
        for i in range(0, dimension):
            print("#", end="")
    if dimension == 1:
        print("#")


make_box(5)
print("\n")
make_box(3)
print("\n")
make_box(2)
print("\n")
make_box(1)
