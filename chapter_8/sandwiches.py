def toppings(*topping):
    print('\nYou ordered sandwich with following toppings:')
    for item in topping:
        print('\t' + str(item))


toppings('ham', 'onions', 'cheese')
toppings('just bread')
toppings('onions', 'peppers', 'sausage')
