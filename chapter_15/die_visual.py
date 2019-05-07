import pygal
from dice import Dice

dice = Dice()

results = []
for roll_num in range(100):
    result = dice.roll()
    results.append(result)

print(results)


# Analyze results
frequencies = []
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


# Visualize the results
hist = pygal.Bar()

hist.title = 'Results of rolling the D6 dice 100 times'
labels = [i for i in range(1, 7)]
hist.x_labels = labels
hist.x_title = 'Result'
hist.y_title = 'Frequency of reslut'

hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')
