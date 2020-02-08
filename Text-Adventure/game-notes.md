setting: Washington, DC
environment: War Torn, Apocalyptic
race: Elf, Wizard, Warrior, Valkrie
sex: male or female


A typical coordinate plane in math or science
(0,2)--(1,2)--(2,2)
  |      |      |
(0,1)--(1,1)--(1,2)
  |      |      |
(0,0)--(1,0)--(2,0)                    

y|
 |
 |
 |
 ------------
 x

 Game coordinate plane
(0,0)--(1,0)--(2,0)
  |      |      |
(0,1)--(1,1)--(1,2)
  |      |      |
(0,2)--(1,2)--(2,2)

x
----------
|
|
|
|
|

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


class ArmoredThug(Enemy):
    def __init__(self):
        self.name = "Armored Thug"
        self.hp = 30
        self.damage = 10


class MotorcycleGang(Enemy):
    def __init__(self):
        self.name = "Motorcycle Gang"
        self.hp = 100
        self.damage = 15


class GangLeader(Enemy):
    def __init__(self):
        self.name = "Gang Leader"
        self.hp = 120
        self.damage = 80














class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.Bandit()
            self.alive_text = "A bandit leaps out from behind a broken down car."

            self.dead_text = "Dead and broken lies the body of this bandit. "
        elif r < 0.80:
            self.enemy = enemies.ArmoredThug()
            self.alive_text = "What's this?! An armored thug has appeared from what seems like nowhere"
            self.dead_text = "A dead armored thug makes you remember the struggle you had against the tough armor you now possess."
        else:
            self.enemy = enemies.MotorcycleGang()
            self.alive_text = "You hear what you think are monsterous snarls but are actually the bellowing of the motorcycle gang that has encircled you."
            self.dead_text = "Several dead bikers lay on the ground from the aftermath of the fight that took place here."

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(
                self.enemy.damage, player.hp))