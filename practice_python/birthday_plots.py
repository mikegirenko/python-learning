"""
In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in
"""
# using matplotlib instead of bokeh

import matplotlib.pyplot as plt
from practice_python import birthday_months
FILE_WITH_DATA = "birthdays_data.json"


o = birthday_months.BirthdayMonths()
counts = o.count_months(FILE_WITH_DATA)

labels = counts.keys()
men_means = counts.values()
width = 0.35

fig, ax = plt.subplots()

ax.bar(labels, men_means, width)

ax.set_ylabel('Birthdays')
ax.set_title('Which months the scientists have birthdays in')
ax.legend()

plt.show()
