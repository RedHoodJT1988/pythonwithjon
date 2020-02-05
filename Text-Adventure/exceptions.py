# Get players data
name = input("Please enter your name: ")
age = input("Please enter your age: ")
try:
    print("You were born in {}.".format(2020 - int(age)))
except TypeError:
    print('Cannot do mathematical operation of string "31" with the number type 2020')
