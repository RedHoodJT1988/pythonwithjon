# Lists

# Creation of list
my_list = ['Ken', 'Ryu', 'Chun-li']

my_list_of_numbers = [1, 2, 3]

# list_of_lists = [['Guile', 'Blanka', 'M. Bison'],
#                  ['Vega', 'E. Honda', 'Saget']]

# print(my_list)

# Updating a list
inventory = ['sword', 'healing potion', 'mana potion', 'long sword']
print(inventory)

# inventory[2] = 'poison'

# print(inventory)

# Counting items in the list
# print(inventory.count('sword'))

# remove item from list
# inventory.pop(3)
# print(inventory)

# Adding an item to the list
ring = 'ring of healing'
inventory.insert(0, ring)
print(inventory)

# Extending a list
list_to_extend = ['dagger', 'dungeon key', 'map']
inventory.extend(list_to_extend)
print(inventory)
