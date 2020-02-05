# Weapon Classes
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

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
    def __init__(self):
        self.name = "Bow"
        self.description = "A wooden stick with nylon attached for shooting from a distance."
        self.arrows = 0
        self.damage = 20


class Handgun(Weapon):
    def __init__(self):
        self.name = "Handgun"
        self.description = "A pistol. Needs bullets, but is good for defense and hunting."
        self.bullets = 0
        self.damage = 30
