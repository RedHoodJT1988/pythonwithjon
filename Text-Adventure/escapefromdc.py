# This program is a text-adventure game where your main goal is to Escape

# Weapon Classes


class Weapon:
    # defining the str function to return the name
    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A hard object made of stone, used for bludegoning."
        self.damage = 5


class Knife(Weapon):
    def __init__(self):
        self.name = "Knife"
        self.description = "A nice, small and sharp blade. Can be used for skinning as well as defense."
        self.damage = 10


class Bow(Weapon):
    def __int__(self):
        self.name = "Bow"
        self.description = "A wooden stick with nylon attached for shooting from long range."
        self.damage = 12
        self.arrow = 0


class Handgun(Weapon):
    def __init__(self):
        self.name = "Handgun"
        self.description = "A pistol. Needs bullets, but is good for defense and hunting."
        self.bullets = 0
        self.damage = 30


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
    inventory = [Rock(), 'bullets', 'stale bread', 'medpack']
    items = ["apple", "shotgun shells", "shotgun"]

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
    elif action_input in ['l', 'L']:
        print("Searching area...")
        print("Found items: ")
        print(items[2])
    else:
        print("Invalid direction! Please type a valid direction.")


play()
