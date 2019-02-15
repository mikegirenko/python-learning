"""
Working with lists
"""

food = ['spam', 'eggs', 'cheese']
print('Whole list is ', food)
print('First element of this list is ' + food[0])
print('Last element of this list is ' + food[-1])

motorcycles = ['honda', 'yamaha', 'suzuki']
print('Original list is', motorcycles)

motorcycles[0] = 'harley'
print('Updated list is', motorcycles)

motorcycles.append('ducati')
print('List after one element added is', motorcycles)

motorcycles.insert(0, 'bmw')
print('List after one element was inserted is', motorcycles)

del motorcycles[0]
print('List after first element was deleted is', motorcycles)

popped_motorcycle = motorcycles.pop()
print('List after item was popped (which removes last item)', motorcycles)
print('Popped item is ' + popped_motorcycle)

first_popped_motorcycle = motorcycles.pop(0)
print('List after first item was popped)', motorcycles)
print('First popped item is ' + first_popped_motorcycle)

item_to_remove = 'suzuki'
motorcycles.remove(item_to_remove)
print('List after ' + item_to_remove + ' was removed', motorcycles)
print('Removed item is ' + item_to_remove)
