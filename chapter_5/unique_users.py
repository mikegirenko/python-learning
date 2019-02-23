current_users = ['john', 'bob', 'sam', 'tom', 'peter']
new_users = ['vincent', 'robert', 'SAM', 'tom', 'peter']

for name in new_users:
    if name.lower() in current_users:
        print(name + ' already used, please select new name')
    else:
        print(name + ' still available')
