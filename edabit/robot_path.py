"""
Mubashir created a simple robot that is navigated by a series of North, East, South, and West [n, e, s, w] commands.
Each command moves the robot one step in the given direction. The robot is designed for only two destinations:
Destination No. 1: e, n, e, e, n
Destination No. 2: w, n, w, n, w, w, n
Create a function that takes a list of commands and returns True if the robot reaches any of the destinations,
False otherwise.
"""


def robot_path(input_path) -> bool:
    destination_one = ["e", "n", "e", "e", "n"]
    # destination_two = ["w", "n", "w", "n", "w", "w", "n"] # TODO
    destination_reached = False
    same_commands_and_counts = []
    different_commands_and_counts = []
    destination_path_counts = {
        "North": destination_one.count("n"),
        "East": destination_one.count("e"),
        "South": destination_one.count("s"),
        "West": destination_one.count("w"),
    }
    input_path_counts = {
        "North": input_path.count("n"),
        "East": input_path.count("e"),
        "South": input_path.count("s"),
        "West": input_path.count("w"),
    }

    for k, v in destination_path_counts.items():
        if input_path_counts[k] == v:
            same_commands_and_counts.append(k)
        else:
            different_commands_and_counts.append(k)

    difference = {}
    for command in different_commands_and_counts:
        d = destination_path_counts[command] - input_path_counts[command]
        difference[command] = d

    if (
        "North" in different_commands_and_counts
        and "South" in different_commands_and_counts
    ):
        if difference["North"] == difference["South"]:
            destination_reached = True
    if (
        "East" in different_commands_and_counts
        and "West" in different_commands_and_counts
    ):
        if difference["East"] == difference["West"]:
            destination_reached = True

    return destination_reached


assert robot_path(["s", "e", "e", "n", "n", "e", "n"])
assert not robot_path(["n", "e", "s", "w", "n", "e", "s", "w", "w", "s", "n", "e"])
