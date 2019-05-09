import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'san_francisco_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            highs.append(high)
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            low = int(row[3])
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

plt.title('Monthly high and low temperatures - 2014\nSan Francisco, CA',
          fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
