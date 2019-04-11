file = 'learning_python.txt'
with open(file) as file_object:
    contents = file_object.read()
    print(contents)

with open(file) as file_object:
    for line in file_object:
        print('\t', line.strip())

string = ''
with open(file) as file_object:
    lines = file_object.readlines()
for line in lines:
    string += line
print(string)

print('\t', 'File length is', len(lines), 'lines')

if 'task' in string:
    print('\t', 'File has word "Python"')

string = ''
with open(file) as file_object:
    lines = file_object.readlines()
    for line in lines:
        string += line
new_string = string.replace('Python', 'C')
print(new_string)
