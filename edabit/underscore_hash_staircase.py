"""
Very Hard
Create a function that will build a staircase using the underscore _ and hash # symbols
"""


class UnderscoreHashStaircase:
    def staircase(self, steps):
        print("  new staircase  ")
        if steps > 0:
            i = 1
            while i <= steps:
                und_count = "_" * (steps - i)
                hash_count = "#" * i
                print(und_count + hash_count)
                i += 1
        if steps < 0:
            i = abs(steps)
            while i > 0:
                hash_count = "#" * i
                und_count = "_" * (abs(steps) - i)
                print(und_count + hash_count)
                i -= 1


if __name__ == "__main__":
    obj = UnderscoreHashStaircase()
    obj.staircase(3)
    obj.staircase(7)
    obj.staircase(2)
    obj.staircase(-8)
