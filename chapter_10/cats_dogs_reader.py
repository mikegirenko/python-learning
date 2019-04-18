filenames = ['cats.txt', 'dogs.txt']


def file_reader(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
        # print(filename, 'does not exists')
    else:
        print(contents)


for name in filenames:
    file_reader(name)
