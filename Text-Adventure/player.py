import items


class Player:
    def __init__(self):
        self.inventory = [
            items.Handgun(),
            items.Knife(),
            'Cash(5)',
            'medpack'
        ]

    def print_invetory(self):
        print("Inventory: ")
        for item in self.inventory:
            printf("*" + str(item))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon is your {}".format(best_weapon))

    # Create a function to check the damage value of each item in the players inventory
    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        print(best_weapon)
