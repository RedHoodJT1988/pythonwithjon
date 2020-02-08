import enemies
import random


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.Bandit()
            self.alive_text = "A bandit leaps out from behind a broken down car."

            self.dead_text = "Dead and broken lies the body of this bandit. "
        elif r < 0.80:
            self.enemy = enemies.Armored_Thug()
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


class VictoryTile(MapTile):
    def intro_text(self):
        return """
        There's a helicopter in the distance...
        ... you hear the blades whipping the air!
        Victory is yours!
        """


world_map = [
    [None, VictoryTile(1, 0), None],
    [None, EnemyTile(1, 1), None],
    [EnemyTile(0, 2), StartTile(1, 2), EnemyTile(2, 2)],
    [None, EnemyTile(1, 3), None]
]


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
