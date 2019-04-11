from random import randint


class Die:
    def __init__(self, sides=6):
        self. sides = sides

    def roll_die(self):
        print('\t', randint(1, self.sides))


print('Printing 6 sided roll:')
six_sided_roll = Die()
for i in range(1, 11):
    six_sided_roll.roll_die()

print('Printing 10 sided roll:')
ten_sided_roll = Die(10)
i = 1
while i <= 10:
    ten_sided_roll.roll_die()
    i += 1

print('Printing 20 sided roll:')
twenty_sided_roll = Die(20)
i = 1
while True:
    if i == 11:
        break
    else:
        twenty_sided_roll.roll_die()
    i += 1
