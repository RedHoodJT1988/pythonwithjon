# This program is a text-adventure game where your main goal is to Escape


def get_player_command():
    return input("Input direction: ")


def play():
    # Prints the name of the game to the player
    print("Escape From DC!")
    # Prints useful commands to play the game
    print('''Valid Directions: 
    n or N = North
    s or S = South
    e or E = East
    w or W = West
    i or I = Inventory
    ''')
    # Initialize and set variables
    action_input = get_player_command()
    inventory = ['Handgun', 'bullets', 'stale bread', 'medpack']

    # Handle player commands
    if action_input in ['n', 'N']:
        print("Go North!")
    elif action_input in ['s', 'S']:
        print("Go South!")
    elif action_input in ['e', 'E']:
        print("Go East!")
    elif action_input in ['w', 'W']:
        print("Go West!")
    elif action_input in ['i', 'I']:
        print("Inventory: ")
        print(inventory)
    else:
        print("Invalid direction! Please type a valid direction.")


play()
