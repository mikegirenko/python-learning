"""
Create a function that takes a country's name and its area as arguments and returns the area of the country's
proportion of the total world's landmass.
"""

area_of_country_1 = (
    "Russia",
    17098242,
)  # "Russia is 11.48% of the total world's landmass"
area_of_country_2 = ("USA", 9372610)  # "USA is 6.29% of the total world's landmass"
area_of_country_3 = ("Iran", 1648195)  # "Iran is 1.11% of the total world's landmass"


def area_of_country(name, area):
    total_world_landmass = 148940000
    proportion = (area / total_world_landmass) * 100

    print(f"{name} is {round(proportion, 2)}% of the total world's landmass")


area_of_country(area_of_country_1[0], area_of_country_1[1])
area_of_country(area_of_country_2[0], area_of_country_2[1])
area_of_country(area_of_country_3[0], area_of_country_3[1])
