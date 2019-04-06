class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name, 'serves', self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, 'is now open')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment


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

restaurant = Restaurant('Ciccis', 'pizza')
print('We served', restaurant.number_served, 'customers')

restaurant.set_number_served(758)
print('We served', restaurant.number_served, 'customers')

restaurant.increment_number_served(100)
print('After today we served', restaurant.number_served, 'customers')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'plain']

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor.title())


ice_cream_restaurant = IceCreamStand('Little man', 'ice cream')
ice_cream_restaurant.display_flavors()
