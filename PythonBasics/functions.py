# def greeting():
#     print("Hello from Python!")


# greeting()


# my_variable = "Hello"
# print(my_variable)

# a = input("Please enter a number: ")
# b = input("Please enter a second number: ")

# if int(b) % int(a) == 0:
#     print(True)
# else:
#     print(False)

def is_factor():
    a = input("Please enter a number: ")
    b = input("Please enter a second number: ")

    if int(b) % int(a) == 0:
        print(True)
    else:
        print(False)


is_factor()


def factors(b):
    for i in range(1, b + 1):
        if b % i == 0:
            print(i)


# if __name__ == '__main__':
#     b = input("Your Number Please")
#     b = float(b)
#     if b > 0 and b.is_integer():
#         factors(int(b))
#     else:
#         print("Please enter a positive number")
