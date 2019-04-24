def city_country(city, country, population=None):
    if population:
        city_country_data = \
            city.title() + ', ' + country.title() + ' - ' + 'population ' + \
            str(population)
    else:
        city_country_data = city.title() + ', ' + country.title()

    return city_country_data
