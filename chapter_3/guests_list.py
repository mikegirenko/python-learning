guests_list = ['tom', 'john', 'mike', 'jerry']
print('This is my quests list', guests_list)
print('Greeting ' + guests_list[0].title() + '!')
print('Greeting ' + guests_list[1].title() + '!')
print('Greeting ' + guests_list[2].title() + '!')
print('Greeting ' + guests_list[3].title() + '!')

guest_cannot_come = 'mike'
print('\n' + guest_cannot_come.title() + ' cannot come to the dinner')
guests_list.remove(guest_cannot_come)
print('My guests list after ' + guest_cannot_come.title()
      + ' could not come is', guests_list)

new_guest = 'steve'
guests_list.insert(2, new_guest)
print('\nMy latest guests list after ' + new_guest.title()
      + ' was addedis ' + str(guests_list))

print('\nI found a much bigger diner table')
list_of_new_guests = ['jeana', 'paul', 'abby']
print('List of new guests is', list_of_new_guests)
guests_list.insert(0, list_of_new_guests[0])
guests_list.insert(2, list_of_new_guests[1])
guests_list.append(list_of_new_guests[2])
for name in guests_list:
    print('Greeting ' + name.title() + '!')
