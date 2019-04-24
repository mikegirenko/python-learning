class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_amount=None):
        if raise_amount:
            self.salary = int(self.salary) + int(raise_amount)
        else:
            self.salary = self.salary + 5000
        return self.salary
