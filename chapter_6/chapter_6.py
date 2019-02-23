"""
Working with dictionaries
"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

points_earned = alien_0['points']
print('\nYou just earned ' + str(points_earned) + ' points!')

print('\nAlien is', alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print('\nUpdated alien is', alien_0)

alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points'] = 7
print('\nNew alien is', alien_1)
alien_1['color'] = 'yellow'
print('\nUpdated new alien is', alien_1)

alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('\nOriginal position is ' + str(alien_2['x_position']))
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_2['x_position'] = alien_2['x_position'] + x_increment
print('\nNew x_position is ' + str(alien_2['x_position']))

alien_3 = {'x_position': 5, 'y_position': 35, 'speed': 'fast'}
print('\nalien_3 is ' + str(alien_3))
del alien_3['speed']
print('\nUpdated alien_3 ' + str(alien_3))

favorite_languages = {
    'jen': 'python',
    'mike': 'java',
    'tom': 'c'
}
print('\nJens favorite language is ' + favorite_languages['jen'].title())

user_0 = {
    'username': 'sbotts',
    'first': 'same',
    'last': 'botts'
}

for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

for k, v in user_0.items():
    print('\n\tKey: ' + k)
    print('\tValue: ' + v)
