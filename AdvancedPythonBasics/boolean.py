# print(4 < 6)

# print(bool(5 <= 4))

# printing boolean values with numbers
# print(bool(0))  # False
# print(bool(1))  # True
# print(bool(-1))  # True

# Evaluating empty sequences
# print(bool(""))  # False
# print(bool([]))
# print(bool({}))
# print(bool(set()))
# print(bool(()))

# Evaluating non-empty sequences
# print(bool("hello"))
# print(bool(['hi']))
# print(bool({1}))
# print(bool({5: 1}))
# print(bool((1, )))

# Printing the truthiness of 'None'
print(bool(None))

# Checking whether a value has been set
name = None
print(bool(name))

list = None
print(bool(list))

list = []
print(bool(list))
