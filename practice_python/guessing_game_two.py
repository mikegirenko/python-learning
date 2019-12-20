"""
In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it. This time,
we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number. At the 
end of this exchange, your program should print out how many guesses it took to get your number. As the writer of 
this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply 
start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing 
strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then 
increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy!
"""


class GuessingGame:
    def __init__(self):
        self.program_guess = 50
        self.number_of_guesses = 0

    def guess_a_number(self):
        print("User, guess a number between 0 and 100")
        while True:
            print(f"User, I think your number is {self.program_guess}?")
            user_response = input("User response is ")
            if user_response == "Correct":
                self.number_of_guesses += 1
                break
            elif user_response == "Too high":
                self.program_guess -= 1
                self.number_of_guesses += 1
            elif user_response == "Too low":
                self.program_guess += 1
                self.number_of_guesses += 1
        print(f"User, your number is {self.program_guess}. "
              f"It took {self.number_of_guesses} guess(es) to find it")


if __name__ == '__main__':
    lets_play = GuessingGame()
    lets_play.guess_a_number()
