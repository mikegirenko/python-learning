import random
import string
"""
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords,
pick a word or two from a list.
"""


def main():
    how_strong = ask_user()
    if how_strong == "Strong":
        print(generate_strong_password())
    elif how_strong == "Weak":
        print(generate_weak_password())
    elif how_strong != "Strong" or how_strong != "Weak":
        print("Choose 'Strong' or 'Weak'")


def generate_strong_password():
    letters = string.ascii_letters
    numbers = string.digits
    characters = string.punctuation
    password_length = 12
    mixed_string = ''.join(letters + numbers + characters)
    password = ''.join(random.sample(mixed_string, password_length))
    return password


def generate_weak_password():
    some_words = ["spam", "eggs", "cheese", "oil"]
    password = some_words[random.randint(0, 3)]
    return password


def ask_user():
    password_strength = input("Do you want Strong or Weak password: ")
    return password_strength


main()
