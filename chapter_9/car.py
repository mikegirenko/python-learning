class Car():

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def car_info(self):
        print('Make is ' + self.make.title() + ' and model is ' +
              self.model.title())


car = Car('toyota', 'camry')
print(car.car_info())


class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        self.range = 0

    def get_range(self):
        if self.battery_size == 70:
            self.range = 240
        elif self.battery_size == 85:
            self.range = 270
        print('The range is ' + str(self.range))

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
        else:
            print('Your battery is fully charged')


battery = Battery()
print(battery.get_range())


class ElectricCar(Car):

    def __init__(self, make, model):
        super().__init__(make, model)
        self.battery = Battery()


electric_car = ElectricCar('nissan', 'leaf')
electric_car.car_info()
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()
