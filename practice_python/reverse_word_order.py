"""
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except
with the words in backwards order. For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.

"""


def user_input():
    user_string = input("Enter some words: ")
    return user_string


def reverse_string(string_to_reverse):
    temp_string = str(string_to_reverse).split()
    new_string = str(temp_string[::-1])
    return new_string


print(reverse_string(user_input()))
