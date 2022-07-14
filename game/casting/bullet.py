from game.casting.actor import Actor
from game.shared.point import Point
from game import constants


class Bullet(Actor):
    """
    Dangerous metal.
    
    The responsibility of Snake is to destroy the enemy.

    Attributes:
        _magnitude (int): The amount of damage it can cause on an enemy.
    """

    def __init__(self, magnitude, head):
        super().__init__()
        self._magnitude = magnitude
        self.set_position(head)
        self.set_text('>-')
        self.set_color(constants.YELLOW)
        self.set_velocity(Point(3 * constants.CELL_SIZE, 0))

    def get_magnitude(self):
        return self._magnitude
