"""
In this exercise, the task is to write a function that picks a random word from a list of words from the
SOWPODS dictionary.
"""
import random
file_with_words = "sowpods.txt"


def read_file(file_name):
    with open(file_name, 'r') as file_object:
        all_records = file_object.readlines()
    file_object.close()
    return all_records


def file_to_list():
    list_of_records = list(read_file(file_with_words))
    return list_of_records


def pick_a_word():
    LIST_OF_RECORDS = file_to_list()
    random_int = random.randint(0, 100000)
    word = LIST_OF_RECORDS[random_int]
    return word


print('Random word is', pick_a_word())

