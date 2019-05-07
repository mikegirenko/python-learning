import pygal

from dice import Dice

dice_1 = Dice(num_sides=8)
dice_2 = Dice(num_sides=8)

results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1000 times."
labels = [x for x in range(2, 17)]
hist.x_labels = labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('two_d8_dice_visual.svg')
