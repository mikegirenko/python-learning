"""
Write a program that asks the user how many Fibonnaci numbers to generate and
then generates them. Take this opportunity to think about how you can use
functions. Make sure to ask the user to enter the number of numbers in the
sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers
in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

user_input = int(input("Enter number of numbers in a Fibonnaci sequence: "))


def generate_sequence(number):
    sequence = []
    i = 1
    if number == 0:
        sequence = []
    elif number == 1:
        sequence = [1]
    elif number == 2:
        sequence = [1, 1]
    elif number > 2:
        sequence = [1, 1]
        while i < (number - 1):
            sequence.append(sequence[i] + sequence[i - 1])
            i += 1
    return sequence


print(generate_sequence(user_input))
