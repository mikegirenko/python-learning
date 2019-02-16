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
      + ' was added is ' + str(guests_list))

print('\nI found a much bigger diner table')
list_of_new_guests = ['jeana', 'paul', 'abby']
print('List of new guests is', list_of_new_guests)
guests_list.insert(0, list_of_new_guests[0])
guests_list.insert(2, list_of_new_guests[1])
guests_list.append(list_of_new_guests[2])
for name in guests_list:
    print('Greeting ' + name.title() + '!')
print('My current guests list is', guests_list)

print('\nI can only invite 2 guests')

popped_guest = guests_list.pop(0)
print('Sorry ' + popped_guest.title() + ' I cannot invite you')

popped_guest = guests_list.pop(0)
print('Sorry ' + popped_guest.title() + ' I cannot invite you')

popped_guest = guests_list.pop(0)
print('Sorry ' + popped_guest.title() + ' I cannot invite you')

popped_guest = guests_list.pop(0)
print('Sorry ' + popped_guest.title() + ' I cannot invite you')

popped_guest = guests_list.pop(0)
print('Sorry ' + popped_guest.title() + ' I cannot invite you')

for name in guests_list:
    print(name.title() + ' you are still invited')

print('Current list is', guests_list)

del guests_list[0]
del guests_list[0]

print('My list at the end is', guests_list)
