import pygal

from dice import Dice

dice_1 = Dice()
dice_2 = Dice()
dice_3 = Dice()

results = []
for roll_number in range(1000):
    result = dice_1.roll() + dice_2.roll() + dice_3.roll()
    results.append(result)

frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Results of rolling three D6 dice 1000 times'
labels = [x for x in range(3, 19)]
hist.x_labels = labels
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('three_d6_dice_visual.svg')
