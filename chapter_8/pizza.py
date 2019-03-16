def make_pizza(size, *toppings):
    print('\nMaking a ' + str(size) + ' inch pizza with the following '
                                      'toppings: ')
    for topping in toppings:
        print(' - ' + topping)


def make_small_pizza(*toppings):
    print('\nMaking a Small pizza with the following toppings: ')
    for topping in toppings:
        print(' - ' + topping)
