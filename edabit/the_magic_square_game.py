"""
3-by-3 grid.
player_one fills out one particular row in the grid  by putting either a 1 or a 0 in each box, such that the sum of
the numbers in that row always odd
player_two fills out one column in the grid by putting either a 1 or a 0 in each box, such that the sum of
the numbers in that column always even
"""


def magic_square_game(player_one, player_two) -> bool:
    alice_grid = [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
    values_comparison = ""
    game_result = ""

    alice_grid[player_one[0] - 1][0] = player_one[1][0]  # this is row
    alice_grid[player_one[0] - 1][1] = player_one[1][1]  # this is row
    alice_grid[player_one[0] - 1][2] = player_one[1][2]  # this is row
    alice_intersection = player_one[0]

    bob_grid = [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
    bob_grid[0][player_two[0] - 1] = player_two[1][0]  # this is column
    bob_grid[1][player_two[0] - 1] = player_two[1][1]  # this is column
    bob_grid[2][player_two[0] - 1] = player_two[1][2]  # this is column
    bob_intersection = player_two[0]

    alice_number = [alice_intersection, bob_intersection]
    alice_value = alice_grid[alice_number[0] - 1][alice_number[1] - 1]

    bob_number = [alice_intersection, bob_intersection]
    bob_value = bob_grid[bob_number[0] - 1][bob_number[1] - 1]

    if alice_value == bob_value:
        values_comparison = "same"

    alice_sum_of_numbers = 0
    for number in player_one[1]:
        alice_sum_of_numbers = alice_sum_of_numbers + int(number)

    if alice_sum_of_numbers % 2 == 0:
        alice_sum = "even"
    else:
        alice_sum = "odd"

    bob_sum_of_numbers = 0
    for number in player_two[1]:
        bob_sum_of_numbers = bob_sum_of_numbers + int(number)

    if bob_sum_of_numbers % 2 == 0:
        bob_sum = "even"
    else:
        bob_sum = "odd"

    if alice_sum == "odd" and bob_sum == "even" and values_comparison == "same":
        game_result = True
    else:
        game_result = False

    print("game result is", game_result)

    return game_result


assert not magic_square_game([2, "100"], [1, "101"])
assert magic_square_game([2, "001"], [1, "101"])
assert magic_square_game([3, "111"], [2, "011"])
assert not magic_square_game([1, "010"], [3, "101"])
