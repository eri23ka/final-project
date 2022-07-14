import random
from game.casting.actor import Actor
from game.shared.point import Point
from game import constants


class Enemy(Actor):
    """
    A beastly air machine that can shoot rapidly.

    The responsibility of Fighter is to protect the earth realm.

    Attributes:
        _core (Actor): The core of the enemy, its destruction means enemy is destroyed
        _left_top (Actor): part of the enemy
        _left_bottom (Actor): part of the enemy
        _right_top (Actor): part of the enemy
        _right_bottom (Actor): part of the enemy
        _movement (str): movement of enemy, could be in any direction for regular enemy but any directions for
         advanced enemy.
    """

    def __init__(self, advanced):
        """Constructs a Fighter."""
        super().__init__()
        self._core = Actor()
        self._left_top = Actor()
        self._left_bottom = Actor()
        self._right_top = Actor()
        self._right_bottom = Actor()
        self._is_advanced = advanced
        self._movement = 'up' if random.randint(0, 8) > 4 else 'down'
        self._prepare_body()
        self.set_velocity(Point(1, 0))

    def get_core(self):
        return self._core

    def get_left_top(self):
        return self._left_top

    def get_left_bottom(self):
        return self._left_bottom

    def get_right_top(self):
        return self._right_top

    def get_right_bottom(self):
        return self._right_bottom

    def get_is_advanced(self):
        return self._is_advanced

    def _prepare_body(self):
        y = random.randint(1, constants.ROWS - 1)

        self.set_color(constants.RED) if self._is_advanced else self.set_color(constants.PURPLE)
        x = int(constants.MAX_X)

        # right_top
        right_top = Actor()
        right_top_position = Point(x - 15 * constants.CELL_SIZE, y * constants.CELL_SIZE)
        right_top.set_position(right_top_position)
        right_top.set_text('<')
        right_top.set_color(self.get_color())
        self._right_top = right_top

        # left_top
        left_top = Actor()
        left_top_position = Point(right_top_position.get_x() - 2 * constants.CELL_SIZE, right_top_position.get_y())
        left_top.set_position(left_top_position)
        left_top.set_text('<')
        left_top.set_color(self.get_color())
        self._left_top = left_top

        # core
        core = Actor()
        core.set_position(Point(right_top_position.get_x() - 1 * constants.CELL_SIZE,
                                right_top_position.get_y() + 1 * constants.CELL_SIZE))
        core.set_text('8' if self._is_advanced else '0')
        core.set_color(self.get_color())
        self._core = core

        # right_bottom
        right_bottom = Actor()
        right_bottom_position = Point(right_top_position.get_x(),
                                      right_top_position.get_y() + 2 * constants.CELL_SIZE)
        right_bottom.set_position(right_bottom_position)
        right_bottom.set_text('<')
        right_bottom.set_color(self.get_color())
        self._right_bottom = right_bottom

        # left_bottom
        left_bottom = Actor()
        left_bottom_position = Point(right_top_position.get_x() - 2 * constants.CELL_SIZE,
                                     right_top_position.get_y() + 2 * constants.CELL_SIZE)
        left_bottom.set_position(left_bottom_position)
        left_bottom.set_text('<')
        left_bottom.set_color(self.get_color())
        self._left_bottom = left_bottom

    def _move(self, part, y):
        if self._is_advanced:
            if self._movement == 'up':
                part.set_position(Point((part.get_position().get_x() - self._velocity.get_x() - constants.CELL_SIZE) % constants.MAX_X, (part.get_position().get_y() - y) % constants.MAX_Y))
            else:
                part.set_position(Point((part.get_position().get_x() - self._velocity.get_x() - constants.CELL_SIZE) % constants.MAX_X, (part.get_position().get_y() + y) % constants.MAX_Y))
        else:
            x = (part.get_position().get_x() - self._velocity.get_x())
            part.set_position(Point(x, part.get_position().get_y()))

    def move_next(self):
        y = random.randint(1, constants.ROWS - 1)
        self._move(self._right_top, y)
        self._move(self._left_top, y)
        self._move(self._core, y)
        self._move(self._right_bottom, y)
        self._move(self._left_bottom, y)

    def reset(self):
        y = random.randint(1, constants.ROWS - 1)

        self.set_color(constants.RED) if self._is_advanced else self.set_color(constants.PURPLE)
        x = int(constants.MAX_X)

        # right_top
        right_top = Actor()
        right_top_position = Point(x - 15 * constants.CELL_SIZE, y * constants.CELL_SIZE)
        right_top.set_position(right_top_position)
        right_top.set_text('<')
        right_top.set_color(self.get_color())
        self._right_top = right_top

        # left_top
        left_top = Actor()
        left_top_position = Point(right_top_position.get_x() - 2 * constants.CELL_SIZE, right_top_position.get_y())
        left_top.set_position(left_top_position)
        left_top.set_text('<')
        left_top.set_color(self.get_color())
        self._left_top = left_top

        # core
        core = Actor()
        core.set_position(Point(right_top_position.get_x() - 1 * constants.CELL_SIZE,
                                right_top_position.get_y() + 1 * constants.CELL_SIZE))
        core.set_text('8' if self._is_advanced else '0')
        core.set_color(self.get_color())
        self._core = core

        # right_bottom
        right_bottom = Actor()
        right_bottom_position = Point(right_top_position.get_x(),
                                      right_top_position.get_y() + 2 * constants.CELL_SIZE)
        right_bottom.set_position(right_bottom_position)
        right_bottom.set_text('<')
        right_bottom.set_color(self.get_color())
        self._right_bottom = right_bottom

        # left_bottom
        left_bottom = Actor()
        left_bottom_position = Point(right_top_position.get_x() - 2 * constants.CELL_SIZE,
                                     right_top_position.get_y() + 2 * constants.CELL_SIZE)
        left_bottom.set_position(left_bottom_position)
        left_bottom.set_text('<')
        left_bottom.set_color(self.get_color())
        self._left_bottom = left_bottom
