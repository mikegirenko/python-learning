"""
Given a predetermined rate from a dictionary, write the function that will return the time it takes for a certain
amount of people to paint a certain amount of walls.
"""


class PaintTheWalls:

    def time(self, rate, people, walls) -> int:
        time_needed = 0
        t = rate["minutes"] / people
        time_needed = t * people

        return int(time_needed)


if __name__ == "__main__":
    obj = PaintTheWalls()
    rate = {"people": 10, "walls": 10, "minutes": 22}
    people = 14
    walls = 14
    print(
        f"It will take {obj.time(rate, people, walls)} minutes for {people} people to paint {walls} walls"
    )

    people = 10
    walls = 10
    print(
        f"It will take {obj.time(rate, people, walls)} minutes for {people} people to paint {walls} walls"
    )
