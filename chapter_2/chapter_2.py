"""
Working with variables
"""

message = 'Hello Python World!'
print(message)

message = 'Hello Python Crash Course world!'
print(message)

message_1 = 'properly named variable'
print(message_1)

s_n = 'not so properly named variable, should be student_name'
print(s_n)

# message = 'this generates error because print() has misspelled variable'
# print(mesage)

name = 'ada lovelace'
print(name.title())
print(name.lower())
print(name.upper())

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + " " + last_name
print(full_name)
print('Hello, ' + full_name.title() + '!')

print('\tPython')
print('Languages:\nPython\nC\nJava')

print('Food:\n\tSpam\n\tEggs\n\tCheese')

has_trailing_space = 'spam '
print(has_trailing_space + '.')
without_spaces = has_trailing_space.rstrip()
print(without_spaces + '.')

has_leading_and_trailing_spaces = ' eggs '
print('.' + has_leading_and_trailing_spaces + '.')
print('Without spaces:' + has_leading_and_trailing_spaces.strip() + '.')

message = "Strin'g with apostrophe"
print(message)
# message = 'Strin'g with apostrophe in single quotes'
# print(message)

sum_of_two_variables = 2 + 3
print(sum_of_two_variables)

multiplication_of_two_variables = 3 * 2
print(multiplication_of_two_variables)

order_of_operations_1 = 2 + 3 * 2
print(order_of_operations_1)

order_of_operations_2 = (2 + 3)* 2
print(order_of_operations_2)
