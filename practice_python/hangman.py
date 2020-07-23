"""
In this exercise, we will finish building Hangman:
Only let the user guess 6 times, and tell the user how many guesses they have left (Display
"You have 4 incorrect guesses left")
Keep track of the letters the user guessed. If the user guesses a letter they already guessed,
don’t penalize them - let them guess again.

"""

MAX_INCORRECT_GUESSES = 6
WORD_TO_GUESS = "OLDMAN"
word_to_show = ["_", "_", "_", "_", "_", "_"]


class Hangman:

    def __init__(self, max_incorrect_guesses, word_to_show):
        self.max_incorrect_guesses = max_incorrect_guesses
        self.word_to_show = word_to_show

    def guess_a_letter(self):
        users_guess = input("Guess your letter: ")
        return users_guess

    def populate_list_based_on_guesses(self, this_list):
        counter = 0
        incorrect_guesses_count = 0
        game_over_flag = False
        while not game_over_flag:
            guessed_letter = self.guess_a_letter()
            if guessed_letter not in this_list:
                incorrect_guesses_count += 1
                incorrect_guesses_left = self.max_incorrect_guesses - incorrect_guesses_count
                print(f'Incorrect. You have {incorrect_guesses_left} incorrect guesses left')
                if incorrect_guesses_left == 0:
                    game_over_flag = True
                    print("Game over. You lost!")
            for i in range(len(this_list)):
                if this_list[i] != "_":
                    if guessed_letter.lower() == this_list[i].lower():
                        word_to_show[i] = guessed_letter
            print(self.word_to_show)
            if "_" not in word_to_show:
                game_over_flag = True
                print("Game over. You won!")
            counter += 1


if __name__ == '__main__':
    o = Hangman(MAX_INCORRECT_GUESSES, word_to_show)
    o.populate_list_based_on_guesses(WORD_TO_GUESS)
