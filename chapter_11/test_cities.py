import unittest
from city_functions import city_country


class CityCountry(unittest.TestCase):

    def test_city_country(self):
        city = 'Santiago'
        country = 'Chile'
        result = city_country(city, country)
        self.assertEqual(result, city + ', ' + country)

    def test_city_country_population(self):
        city = 'Santiago'
        country = 'Chile'
        population = 7000000
        result = city_country(city, country, population)
        self.assertEqual(
            result, city + ', ' + country + ' - ' + 'population ' + str(
                population))


unittest.main()
