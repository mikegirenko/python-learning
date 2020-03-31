"""
Ask user to enter coordinate in 'row,column' format.
Player 1 (the first player to move) is X and player 2 (the second player) is O.
If a player tries to put a piece in a game position where there already is another piece, do not allow the piece to
go there.
Bonus:
For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are
full. In a bonus version, keep track of how many squares are full and automatically stop asking for moves
when there are no more valid moves.
"""


class PlayTicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def print_board(self):
        if self.board is not None:
            for row in self.board:
                print(row)

    def get_user_input(self):
        entries = 1
        while entries < 6:
            if entries % 2 != 0:
                user_input = input("First Player, enter coordinate in 'row,column' format: ")
                temp = user_input.split(',')
                row = int(temp[0])
                column = int(temp[1])
                if self.board[row][column] == " ":
                    self.board[row][column] = 'X'
                else:
                    print('This cell already populated')
            if entries % 2 == 0:
                user_input = input("Second Player, enter coordinate in 'row,column' format: ")
                temp = user_input.split(',')
                row = int(temp[0])
                column = int(temp[1])
                if self.board[row][column] == " ":
                    self.board[row][column] = '0'
                else:
                    print('This cell already populated')
            entries += 1
        return self.board


if __name__ == '__main__':
    object_play = PlayTicTacToe()
    object_play.get_user_input()
    object_play.print_board()
