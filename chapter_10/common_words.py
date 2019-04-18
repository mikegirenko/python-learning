filename = 'book.txt'
contents = ''
search_string = 'gutenberg'
words_count = 0

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(filename, 'not found')
else:
    words_count = contents.lower().count(search_string)
    print(words_count)
