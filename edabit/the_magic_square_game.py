"""
3-by-3 grid.
player_one fills out one particular row in the grid  by putting either a 1 or a 0 in each box, such that the sum of
the numbers in that row always odd
player_two fills out one column in the grid by putting either a 1 or a 0 in each box, such that the sum of
the numbers in that column always even
"""

#  TODO Finish "they’ve each written down the same number in the one square where their row and column intersect."


def magic_square_game(player_one, player_two):
    grid = [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
    game_result = ""

    grid[player_one[0]-1][0] = player_one[1][0]
    grid[player_one[0]-1][1] = player_one[1][1]
    grid[player_one[0]-1][2] = player_one[1][2]
    for row in grid:
        print(row)
    print(grid)
    print("* " * 7)
    grid[0][player_two[0]-1] = player_two[1][0]
    grid[1][player_two[0]-1] = player_two[1][1]
    grid[2][player_two[0]-1] = player_two[1][2]
    for row in grid:
        print(row)
    print(grid)

    alice_numbers = 0
    for number in player_one[1]:
        alice_numbers = alice_numbers + int(number)
    print(alice_numbers)
    if alice_numbers % 2 == 0:
        alice_sum = "even"
    else:
        alice_sum = "odd"
    print(alice_sum)

    bob_numbers = 0
    for number in player_two[1]:
        bob_numbers = bob_numbers + int(number)
    print(bob_numbers)
    if bob_numbers % 2 == 0:
        bob_sum = "even"
    else:
        bob_sum = "odd"
    print(bob_sum)

    if alice_sum == "odd" and bob_sum == "even":
        game_result = True

    print(game_result)


magic_square_game([2, "100"], [1, "101"])
magic_square_game([2, "001"], [1, "101"])
magic_square_game([3, "111"], [2, "011"])
