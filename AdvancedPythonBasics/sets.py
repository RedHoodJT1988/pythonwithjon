# my_new_set = set()
# print(type(my_new_set))

# names = {"Kyle", "Jason", "Tim"}
# print(names)

# numbers = {1, 2, 3, 4}
# print(numbers)

# print(hash("Kyle"))  # Can be used to hash passwords and other sensitive data.

# colors = {"red", "green", "blue", "blue", "red", "green", "yellow"}
# print('old', colors)

# colors.add("orange")
# print('new', colors)

# colors.discard("red")
# print("new new: ", colors)

# colors = {"red", "black", "white"}
# print("set with updated colors: ", colors)

street_fight = {"Ryu", "Blanka", "Chun-li",
                "Guile", "E. Honda", "M. Bison", "Cammy"}
favorite_fighters = {"Ryu", "Blanka", "Guile", "Ken"}

street_fight.union(favorite_fighters)
print(street_fight & favorite_fighters)
