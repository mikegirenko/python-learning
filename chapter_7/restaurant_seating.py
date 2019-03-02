group_size = input('Hi there, how many people are in your group? ')
if int(group_size) > 8:
    print('You have ' + group_size + ' and you will need to wait for your '
                                     'table')
else:
    print('You only have ' + group_size + '? Good, the table is ready for '
                                          'you!')
