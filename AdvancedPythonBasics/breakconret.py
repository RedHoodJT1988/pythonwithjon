# Break example
names = ["Supergirl", "Batman", "Superman", "Swamp Thing", "Red Hood"]
# for name in names:
#     print(f"Hello, {name}")
#     if name == "Superman":
#         break

# Continue example
# for name in names:
#     if name != "Batman":
#         continue
#     print(f"Hello, {name}!")

# Break with continue example
# for name in names:
#     if len(name) == 4:
#         continue
#     print(f"Hello, {name}")
#     if name == "Swamp Thing":
#         break
# print("Done!")

# Break and continue working only for the current loop
# target_letter = "a"
# for name in names:
#     print(f"{name} in outer loop")
#     for char in name:
#         if char == target_letter:
#             print(f"Found {name} with letter: {target_letter}")
#             print("breaking out of inner loop")
#             break

# Break and continue in while loop example
# count = 0
# while True:
#     count += 1
#     if count == 1000:
#         print("Count reached")
#         break
# print("Game won!! Congrats!!!")


def name_length(names):
    for name in names:
        print(name)
        if name == "Red Hood":
            return "Found the special name"


name_length("Red Hood")
print("R\ne\nd\n \nH\no\no\nd")
