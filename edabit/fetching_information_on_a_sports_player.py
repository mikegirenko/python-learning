"""
Classes For Fetching Information on a Sports Player
"""


class SportsPlayer:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height} cm"

    def get_weight(self):
        return f"{self.name} weights {self.weight} kg"


if __name__ == "__main__":
    sports_player = SportsPlayer("David Jones", 25, 175, 75)
    print(sports_player.get_age())
    print(sports_player.get_height())
    print(sports_player.get_weight())
