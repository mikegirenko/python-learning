from collections import OrderedDict

glossary = OrderedDict()

glossary['function'] = 'a named block of code which designed to do one ' \
                       'specific job'
glossary['variable'] = 'place in the memory which holds a value'
glossary['library'] = 'a module'
glossary['list'] = 'an ordered sequences of values'
glossary['integer'] = 'a whole number'

for key, value in glossary.items():
    print('\n' + key + ' : ' + value)
