class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, 'serves', self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, 'is now open')


new_restaurant = Restaurant('Modos Pizza', 'pizza')

print('Name is', new_restaurant.restaurant_name)
print('Cuisine is', new_restaurant.cuisine_type)

new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

mexican_restaurant = Restaurant('Casa', 'mexican')
mexican_restaurant.describe_restaurant()

italian_restaurant = Restaurant('Bonos', 'italian')
italian_restaurant.describe_restaurant()

french_restaurant = Restaurant('Paris', 'french')
french_restaurant.describe_restaurant()