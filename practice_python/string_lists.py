"""
Ask the user for a string and print out whether this string is a palindrome
or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

user_input = input("Please enter a string: ")

reversed_string = "".join(reversed(user_input))

if user_input.lower() == reversed_string.lower():
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")
