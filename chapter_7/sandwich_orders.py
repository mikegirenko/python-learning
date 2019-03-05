sandwich_orders = ['tuna', 'blt', 'veggie', 'meat', 'italian', 'spam']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made you ' + current_sandwich.title() + ' sandwich')
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print('\t' + sandwich.title() + ' sandwich was made')

expanded_orders_list = ['pastrami', 'blt', 'veggie', 'pastrami',
                        'italian', 'spam', 'pastrami', 'meat']
finished_sandwiches = []
print('\nSorry, we are out of pastrami!')
while expanded_orders_list:
    current_sandwich = expanded_orders_list.pop()
    if current_sandwich != 'pastrami':
        finished_sandwiches.append(current_sandwich)
print('Here is sandwich list without pastrami sandwich:')
for item in finished_sandwiches:
    print('\t', item.title() + ' sandwich')
