"""
Given two .txt files that have lists of numbers in them, find the numbers that
are overlapping. One .txt file has a list of all prime numbers under 1000, and
the other .txt file has a list of happy numbers up to 1000.

"""

first_file = 'primenumbers.txt'
second_file = 'happynumbers.txt'


def main():
    first_list = convert_to_list_of_integers(read_file(first_file))
    second_list = convert_to_list_of_integers(read_file(second_file))

    print('Overlapping numbers:',
          find_overlapping_numbers(first_list, second_list))


def read_file(file_name):

    with open(file_name) as file_object:
        all_lines = file_object.readlines()
    file_object.close()
    return all_lines


def convert_to_list_of_integers(to_be_converted):
    temp = to_be_converted
    converted = []
    for item in temp:
        converted.append(int(item))
    return converted


def find_overlapping_numbers(first_list, second_list):
    overlapping_numbers = set(first_list) & set(second_list)  # Intersection
    return overlapping_numbers


if __name__ == "__main__":
    main()
