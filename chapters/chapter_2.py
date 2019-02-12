message = 'Hello Python World!'
print(message)

message = 'Hello Python Crash Course world!'
print(message)

message_1 = 'good variable'
print(message_1)

s_n = 'bad variable, should be student_name'
print(s_n)

# message = 'this generates error'
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

has_trailing_spase = 'spam '
print(has_trailing_spase + '.')
without_spaces = has_trailing_spase.rstrip()
print(without_spaces + '.')

has_leading_and_trailing_spaces = ' eggs '
print('.' + has_leading_and_trailing_spaces + '.')
print('Without spaces:' + has_leading_and_trailing_spaces.strip() + '.')

message = "Strin'g with apostrophe"
print(message)
# message = 'Strin'g with apostrophe in single quotes'
# print(message)
