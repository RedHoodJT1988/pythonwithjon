# Handle actions made by the player
print("Escape from DC")
action_input = input("Please choose a direction from the following\ns= south, n=north, w=west, e=east: ")
if action_input == 'n':
    print("Go North!")
elif action_input == 's':
    print("Go South!")
elif action_input == 'e':
    print("Go East!")
elif action_input == 'w':
    print("Go West!")
else:
    print("Invalid action! Please type a valid action.")