class User():

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


user_1 = User('jim', 'burnes', '27', 'Denver')
user_1.describe_user()
user_1.greet_user()

user_2 = User('joe', 'lauzon', '33', 'San Diego')
user_2.describe_user()
user_2.greet_user()

user_3 = User('sammy', 'flowers', '21', 'Pueblo')
for i in range(1, 7):
    user_3.increment_login_attempts()
print('User attempted to login ', user_3.login_attempts, 'times')
user_3.reset_login_attempts()
print('After reset, user attempted to login ', user_3.login_attempts, 'times')


class Privileges():

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Admin has the below privileges:')
        for privilege in self.privileges:
            print('\t', privilege)


class Admin(User):

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()


admin_1 = Admin('pat', 'simms', '29', 'Laguna Beach')
print(admin_1.privileges.show_privileges())
