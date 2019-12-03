# For Loop in Python

fighters = ["Cyclops", "Cable", "Ryu"]
# for fighter in fighters:
#     print(f"The fighter is {fighter}!")

# Using the built-in range() method
# for num in range(6):
#     print(f"The number is: {num}")

# Using the step parameter
# for num in range(4, 12, 3):
#     print(f"The number is: {num}")

# for index, item in enumerate(fighters):
#     print(f"Item: {item} at index: {index}.")

hex_colors = {
    "Red": "#FFF",
    "Green": "#0F0",
    "Blue": "#00F"
}
# Wrong way to loop through the dictionary
for color in hex_colors:
    print(f"The value of color is actually: {color}")

for color, hex_value in hex_colors.items():
    print(f"The color {color}, the hex value is: {hex_value}")
