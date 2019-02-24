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
    'tom': 'c',
    'bill': 'python'
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

for name in favorite_languages.keys():
    print(name.title())

# The same as above
for name in favorite_languages:
    print('\t', name.title())

names = ['jen', 'mike']
for name in favorite_languages:
    print(name.title())
    if name in names:
        print('\tHi ' + name.title() + ' I see your favorite language is ' +
              favorite_languages[name].title() + '!')

if 'erin' not in favorite_languages.keys():
    print('\nHi Erin, what is your favorite language?')

for name in sorted(favorite_languages.keys()):
    print('\t', name.title() + ', thank you for answering!')

print('\nThe following languages were mentioned:')
for language in favorite_languages.values():
    print(language.title())

print('\nThe following unique languages were mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())
