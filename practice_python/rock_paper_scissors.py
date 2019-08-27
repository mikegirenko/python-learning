"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to the
winner, and ask if the players want to start a new game)
Remember the rules:
 Rock beats scissors
 Scissors beats paper
 Paper beats rock
"""


while True:
    player_one = input("Player One, enter your play: ")
    player_two = input("Player Two, enter your play: ")
    if player_one == "rock" and player_two == 'scissors':
        print("Player One, you won")
        continue_playing = input("Want to start a new game: ")
        if continue_playing != 'yes':
            print("Thank you for playing!")
            break
    elif player_one == "scissors" and player_two == 'paper':
        print("Player One, you won")
        continue_playing = input("Want to start a new game: ")
        if continue_playing != 'yes':
            print("Thank you for playing!")
            break
    elif player_one == "paper" and player_two == 'rock':
        print("Player One, you won")
        continue_playing = input("Want to start a new game: ")
        if continue_playing != 'yes':
            print("Thank you for playing!")
            break
    else:
        if player_one not in ["rock", "paper", "scissors"] or player_two not\
                in ["rock", "paper", "scissors"]:
            print("Please enter rock, paper, or scissors")
        break
