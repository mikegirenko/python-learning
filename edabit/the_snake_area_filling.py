"""
Create a function that takes the side n of the game screen and returns the number of times the snake can eat before
it runs out of space in the game screen.
"""


class Snake:
    def snakefill(self, side):
        number_of_times = 1
        while number_of_times < side:
            number_of_times = number_of_times * 2

        return number_of_times


if __name__ == "__main__":
    snake_object = Snake()
    assert snake_object.snakefill(3) == 3
    assert snake_object.snakefill(6) == 5
    assert snake_object.snakefill(24) == 9
