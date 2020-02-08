class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

class Bandit(Enemy):
    def __init__(self):
        self.name = "Bandit"
        self.hp = 10
        self.damage = 2

class Armored_Thug(Enemy):
    def __init__(self):
        self.name = "Armored Thug"
        self.hp = 30
        self.damage = 10

class MotorcycleGang(Enemy):
    def __init__(self):
        self.name = "Motorcycle Gang"
        self.hp = 100
        self.damage = 20

class GangLeader(Enemy):
    def __init__(self):
        self.name = "Gang Leader"
        self.hp = 100 
        self.damage = 80
