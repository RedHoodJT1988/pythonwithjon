# empty_dict = {}
# print(type(empty_dict))

# numbers = {1: "one", 2: "two", 3: "three", 4: "four"}
# print(type(numbers))
# print(numbers)

# my_dict = {1: 1}
# print(my_dict)

# my_wrong_dict = {[1, 2]: 1}
# print(my_wrong_dict)

# square brackets in this instance pertain to the key in our dictionaries.
# print(numbers[2])

# print(numbers["one"])

# print(numbers.get("four")) # Don't do this with your dictionary, as it will not return the key for the value. It will return None.

# numbers[8] = "eight"
# print(numbers)

# numbers[8] = 'nine'
# print(numbers)

colors = {'r': "red", 'g': "green", 'b': "blue"}
# print(colors)
colors2 = {'o': "orange", 'y': "yellow"}
colors.update(colors2)
# print('updated colors: ', colors)
# print(colors['o'])

# Helpful dictionary methods for returning data ie keys, values and items
# prints all keys associated with the colors dictionary
print(colors.keys())
# prints all values associated with the colors dictionary
print(colors.values())
# prints all items associated with the colors dictionary
print(colors.items())
