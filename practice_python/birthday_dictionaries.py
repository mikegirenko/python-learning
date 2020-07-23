"""
For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based
on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the
user to enter a name, and return the birthday of that person back to them.
"""

MY_RECORD = {'Mike': '09/20/1999', 'Sammy': '01/01/2009'}


class PrintBirthday:

    def __init__(self, record):
        self.record = record

    def get_name(self):
        name = input("Enter your friend's name: ")
        return name

    def print_record(self):
        returned_name = self.get_name()
        for name, age in self.record.items():
            if returned_name not in self.record.keys():
                print(returned_name, 'not found')
            if name == returned_name:
                print(name, "'s", 'birthday is', self.record[name])


if __name__ == '__main__':
    o = PrintBirthday(MY_RECORD)
    o.print_record()
