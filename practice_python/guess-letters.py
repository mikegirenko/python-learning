"""
Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to
guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an
infinite number of times until they get the entire word.
"""

WORD_TO_GUESS = "EVAPORATE"
word_to_show = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


def guess_a_letter():
    users_guess = input("Guess your letter: ")
    return users_guess


def populate_list_based_on_guesses(this_list):
    game_over = False
    while not game_over:
        guessed_letter = guess_a_letter()
        if guessed_letter not in this_list:
            print("Incorrect")
        for i in range(len(this_list)):
            if this_list[i] != "_":
                if guessed_letter.lower() == this_list[i].lower():
                    word_to_show[i] = guessed_letter
        print(word_to_show)
        if "_" not in word_to_show:
            print("Game over!")
            game_over = True


populate_list_based_on_guesses(WORD_TO_GUESS)
