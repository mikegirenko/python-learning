"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. If the number is a multiple
of 4, print out a different message.
"""

number = int(input("Enter a number: "))

if number % 2 == 0 and number % 4 != 0:
    print(number, "is even")
elif number % 2 != 0:
    print(number, "is odd")
elif number % 4 == 0:
    print(number, "is a multiple of 4")
