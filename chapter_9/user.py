class User:

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print('User name is', self.first_name.title(), self.last_name.title(),
              ', his age is', self.age, '. This user is from', self.city)

    def greet_user(self):
        print('Hello', self.first_name.title(), self.last_name.title())


admin = User('jim', 'burnes', '27', 'Denver')
admin.describe_user()
admin.greet_user()

admin = User('joe', 'lauzon', '33', 'San Diego')
admin.describe_user()
admin.greet_user()
