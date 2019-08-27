import random
"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
guess the number, then tell them whether they guessed too low, too high, or
exactly right. (Hint: remember to use the user input lessons from the very
first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, 
print this out.
"""

counter = 0

while True:

    number_to_guess = random.randint(1, 9)
    print("Number to guess", number_to_guess)
    users_guess = input("Guess the number between 1 and 9. Enter 'exit' to "
                        "end the game. ")

    counter += 1
    if users_guess == "exit":
        break
    elif number_to_guess == int(users_guess):
        print("You guess is right!")
    elif number_to_guess > int(users_guess):
        print("Your guess is too low")
    elif number_to_guess < int(users_guess):
        print("Your guess is too high")

print("You tried", counter, "times")
