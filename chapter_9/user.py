class User:

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print('User name is', self.first_name.title(), self.last_name.title(),
              ', his age is', self.age, '. This user is from', self.city)

    def greet_user(self):
        print('Hello', self.first_name.title(), self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


admin = User('jim', 'burnes', '27', 'Denver')
admin.describe_user()
admin.greet_user()

admin = User('joe', 'lauzon', '33', 'San Diego')
admin.describe_user()
admin.greet_user()

admin = User('sammy', 'flowers', 21, 'Pueblo')
for i in range(1, 7):
    admin.increment_login_attempts()
print('User attempted to login ', admin.login_attempts, 'times')
admin.reset_login_attempts()
print('After reset, user attempted to login ', admin.login_attempts, 'times')
