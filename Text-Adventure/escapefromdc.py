# This program is a text-adventure game where your main goal is to Escape
# @TODO finish fleshing out details of program
# Author: Jonathan Reeves

from player import Player


def play():
    print("Escape From DC!")
    # Commands used to play the game
    print('''Valid Directions: 
    n or N = North
    s or S = South
    e or E = East
    w or W = West
    i or I = Inventory
    m or M = Most Powerful Weapon in Inventory
    ''')
    player = Player()

    while True:
        action_input = get_player_command()
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
            player.print_invetory()
        elif action_input in ['m', 'M']:
            player.most_powerful_weapon()
            # print(most_powerful_weapon(inventory))
        else:
            print("Invalid direction! Please type a valid direction.")


def get_player_command():
    return input("Input direction: ")


play()
