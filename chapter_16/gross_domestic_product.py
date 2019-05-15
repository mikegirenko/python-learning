import json
from pygal_maps_world.maps import World
from pygal_maps_world.maps import COUNTRIES
from pygal.style import RotateStyle

filename = 'population_data.json'

with open(filename) as f:
    gdp_data = json.load(f)


def get_country_code(country):
    for code, name in COUNTRIES.items():
        if name == country:
            return code
    return None


gdp_all = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2010':
        country_name = gdp_dict['Country Name']
        value = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            gdp_all[code] = value


wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = 'World GDP in 2010'
wm.add('2010', gdp_all)

wm.render_to_file('gdp_world.svg')
