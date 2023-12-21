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
    #      destination_two = ["w", "n", "w", "n", "w", "w", "n"] # TODO
    destination_reached = False
    same_commands_and_counts = []
    different_commands_and_counts = []
    destination_path_counts = {"North": destination_one.count("n"), "East": destination_one.count("e"),
                               "South": destination_one.count("s"), "West": destination_one.count("w")}
    input_path_counts = {"North": input_path.count("n"), "East": input_path.count("e"),
                         "South": input_path.count("s"), "West": input_path.count("w")}
    print("destination_path: ", destination_path_counts)
    print("input_path      : ", input_path_counts)
    for k, v in destination_path_counts.items():
        if input_path_counts[k] == v:
            same_commands_and_counts.append(k)
        else:
            different_commands_and_counts.append(k)
    print("same commands and counts - ignore", same_commands_and_counts)
    print("different commands and counts - action on them", different_commands_and_counts)
    dest_diff = {}
    for command in different_commands_and_counts:
        d = destination_path_counts[command] - input_path_counts[command]
        dest_diff[command] = d
    print("dest_diff", dest_diff)
    # offset each other
    if "North" in different_commands_and_counts:
        if dest_diff["North"] == dest_diff["South"]:
            destination_reached = True
    if "South" in different_commands_and_counts:
        if dest_diff["South"] == dest_diff["North"]:
            destination_reached = True
    if "East" in different_commands_and_counts:
        if dest_diff["East"] == dest_diff["West"]:
            destination_reached = True
    if "West" in different_commands_and_counts:
        if dest_diff["West"] == dest_diff["East"]:
            destination_reached = True

    return destination_reached

# print(robot_path(["s", "e", "e", "n", "n", "e", "n"]))  # passes
robot_path(["n", "e", "s", "w", "n", "e", "s", "w", "w", "s", "n", "e"])


"""
{'North': 2, 'South': 0}
{'North': 3, 'South': 1}
determine which North is larger, then by how much
then see if opposite South offsets it 
"""

"""
        if (destination_path_counts[command] - input_path_counts[command] == 1)\
                or (input_path_counts[command] - destination_path_counts[command] == 1):
"""