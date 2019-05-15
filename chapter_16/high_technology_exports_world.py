import csv
from pygal_maps_world.maps import World
from pygal_maps_world.maps import COUNTRIES
from pygal.style import RotateStyle


def get_country_code(country):
    for code, name in COUNTRIES.items():
        if name == country:
            return code
    return None


filename = 'high_tech_exports.csv'

with open(filename) as f:
    reader = csv.reader(f)

    exports_by_country = {}
    for row in reader:
        if row[-4]:
            if row[-4] != '2016':
                exports_by_country[row[0]] = int(float(row[-4]))


data_to_plot = {}
for k, v in exports_by_country.items():
    code = get_country_code(k)
    data_to_plot[code] = v

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = 'High Technology Exports in the world in 2015'
wm.add('2015', data_to_plot)

wm.render_to_file('high_tech_exports.svg')
