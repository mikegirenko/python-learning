my_pizzas = ['pepperoni', 'double cheese', 'chicken']
print('My pizzas', my_pizzas)

my_friend_pizzas = my_pizzas[:]
print("\nMy friend's pizzas", my_friend_pizzas)

my_pizzas.append('veggie')
my_friend_pizzas.append('bbq')

print('\nMy expanded pizzas list:')
for pizza in my_pizzas:
    print(pizza, end=' ')

print("\n\nMy friend's expanded pizzas list")
for pizza in my_friend_pizzas:
    print(pizza, end=' ')
