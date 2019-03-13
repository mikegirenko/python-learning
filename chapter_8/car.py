def make_car(manufacturer, model, **other_info):
    car_info = {}
    car_info['manufacturer'] = manufacturer.title()
    car_info['model'] = model.title()
    for k, v in other_info.items():
        car_info[k] = v
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
