cities = {
    'Denver': {
        'country': 'Denver',
        'population': 1000000,
        'fact': 'mile high city'
    },
    'Paris': {
        'country': 'France',
        'population': 7880000,
        'fact': 'Eifel tower'
    },
    'Lima': {
        'country': 'Peru',
        'population': 3500000,
        'fact': 'South America'
    }
}

for k, v in cities.items():
    print('The name of the city is ' + str(k))
    for k, v in v.items():
        print('\t', str(k) + ': ' + str(v))
