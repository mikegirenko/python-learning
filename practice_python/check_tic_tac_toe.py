"""
Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the
moves were made.
Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether  anyone
has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a
diagonal.

"""
import random


class CheckTicTacToe:
    def __init__(self):
        self.board = self.populate_board()

    def populate_board(self):
        board = []
        board_size = 3
        while board_size > 0:
            row = [random.randint(0, 2) for x in range(0, 3)]
            board.append(row)
            board_size -= 1
        return board

    def print_board(self):
        i = 0
        while i < 3:
            print(self.board[i])
            i += 1

    def check_board(self):
        for i in range(0, 3):
            if (self.board[i][0] == self.board[i][1]) \
                 and (self.board[i][0] == self.board[i][2]) \
                 and (self.board[i][1] == self.board[i][2]):
                return self.board[i][0]

        for i in range(0, 3):
            if (self.board[0][i] == self.board[1][i]) \
                 and (self.board[0][i] == self.board[2][i]) \
                 and (self.board[1][i] == self.board[2][i]):
                return self.board[0][i]

        for i in range(0, 3):
            if (self.board[0][i] == self.board[1][i+1]) \
                 and (self.board[0][i] == self.board[2][i]) \
                 and (self.board[1][i+1] == self.board[2][i+2]):
                return self.board[1][i]

        return 0


if __name__ == "__main__":
    c = CheckTicTacToe()
    c.print_board()
    if c.check_board() == 0:
        print("There is no winner")
    else:
        print("The winner is Player", c.check_board())
