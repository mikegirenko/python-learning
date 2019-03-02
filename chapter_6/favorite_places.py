favorite_places = {
    'mike': {
        'place': 'mesa verde'
    },
    'tom': {
        'place': 'garden of the gods'
    },
    'bob': {
        'place': 'winter part'
    }
}

for k, v in favorite_places.items():
    print('Hi ' + str(k).title() + '. What is your favorite place? It is '
          + str(v['place']).title())
