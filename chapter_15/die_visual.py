from dice import Dice

dice = Dice()

results = []
for roll_num in range(100):
    result = dice.roll()
    results.append(result)

print(results)
