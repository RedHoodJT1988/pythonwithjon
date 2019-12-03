# Example of if statements
# if 4 < 3:
#     print("Hello world")

# Using the not keyword to convert b varialbe to True from False
# b = False
# if not b:
#     print("Converting False to True!")

# Using truthiness to print messages, if a is set to a truthy value then print message
# message = "Hey"
# a = 0
# if a:
#     print("a:", message)

# b = -1
# if b:
#     print("b", message)

# c = []
# if c:
#     print("c", message)

# d = [1, 2, 3, 4]
# if d:
#     print("d", message)

# If statements in functions example
# def modify_username(name):
#     if len(name) < 10:
#         print(name.upper())
#     else:
#         print(name.lower())

# modify_username("Princess Zelda")


# Nesting if statements within a function
# def number_info(num):
#     if num > 0:
#         print("Greater than zero")
#         if num > 10:
#             print("Also greater than ten")


# number_info(3)
# number_info(20)

# If, elif and else example
def awesome_Fighter(fighter):
    if fighter == "Ryu":
        print("He's the best!")
    elif fighter == "Guile":
        print("He's kinda cool")
    elif fighter == "Cammy":
        print("Wow Cammy!")
    else:
        print("They are not even close to cool")


awesome_Fighter("Ryu")  # Prints: "He's the best!"
awesome_Fighter("Cammy")  # Prints: "Wow Cammy!"
awesome_Fighter("Guile")  # Prints: "He's kinda cool"
awesome_Fighter("m. Bison")  # Prints: "They are not even close to cool"
