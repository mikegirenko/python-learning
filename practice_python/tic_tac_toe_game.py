"""
The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in
this exercise is to use the functions from those previous exercises all together in the same program to make a
two-player game that you can play with a friend. There are a lot of choices you will have to make when completing
this exercise, so you can go as far or as little as you want with it.

Here are a few things to keep in mind:
You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
If there are no more moves left, don’t ask for the next player’s move!
"""


class PlayTicTacToeGame:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def print_board(self):
        if self.board is not None:
            for row in self.board:
                print(row)

    def game_over(self):
        for row in self.board:
            if row == ["X", "X", "X"] or row == ["0", "0", "0"]:
                print('Game Over!')
                return True

    def get_user_input(self):
        iteration = 1
        while not self.game_over():
            user_input = ""
            if iteration % 2 != 0:
                user_input = input(f"Player 1, enter coordinate in 'row,column' format: ")
            if iteration % 2 == 0:
                user_input = input(f"Player 2, enter coordinate in 'row,column' format: ")
            temp = user_input.split(',')
            row = int(temp[0])
            column = int(temp[1])
            if self.board[row][column] == " ":
                if iteration % 2 != 0:
                    self.board[row][column] = 'X'
                else:
                    self.board[row][column] = 'O'
                self.print_board()
            else:
                print('This cell already populated')
            iteration += 1
        return self.board


if __name__ == '__main__':
    object_play = PlayTicTacToeGame()
    object_play.get_user_input()
