import datetime

"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they 
will turn 100 years old.
"""

user_input_name = input("Enter your name: ")
user_input_age = input("Enter your age: ")

print("Hi", user_input_name.title(), "your age now is", user_input_age)


def calculate_year(age):
    now = datetime.datetime.now()
    current_year = now.year
    year_when_turning_100 = current_year + (100 - int(age))
    return year_when_turning_100


print("You will turn 100 years old in", calculate_year(user_input_age))
