from game.casting.actor import Actor
from game.shared.point import Point
from game import constants


class Fighter(Actor):
    """
    A beastly air machine that can shoot rapidly.
    
    The responsibility of Fighter is to protect the earth realm.

    Attributes:
        _head (Actor): The head of Fighter that shoots
        _left_wing (Actor): The left wing of the Fighter
        _right_wing (Actor): The left wing of the Fighter
        _engine (Actor): The core of the Fighter
    """

    def __init__(self):
        """Constructs a Fighter."""
        super().__init__()
        self._head = Actor()
        self._left_wing = Actor()
        self._right_wing = Actor()
        self._engine = Actor()
        self.set_velocity(Point(0, 1 * constants.CELL_SIZE))
        self._prepare_body()

    def get_head(self):
        return self._head

    def get_left_wing(self):
        return self._left_wing

    def get_right_wing(self):
        return self._right_wing

    def get_engine(self):
        return self._engine

    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        # head
        head = Actor()
        head.set_position(Point(45, y))
        head.set_text('0')
        head.set_color(self.get_color())
        self._head = head

        # left_wing
        left_wing = Actor()
        left_wing_position = Point(self._head.get_position().get_x() - 1 * constants.CELL_SIZE,
                                   y - 1 * constants.CELL_SIZE)
        left_wing.set_position(left_wing_position)
        left_wing.set_text('>')
        left_wing.set_color(self.get_color())
        self._left_wing = left_wing

        # right_wing
        right_wing = Actor()
        right_wing_position = Point(self._head.get_position().get_x() - 1 * constants.CELL_SIZE,
                                    y + 1 * constants.CELL_SIZE)
        right_wing.set_position(right_wing_position)
        right_wing.set_text('>')
        right_wing.set_color(self.get_color())
        self._right_wing = right_wing

        # engine
        engine = Actor()
        engine_position = Point(self._head.get_position().get_x() - 1 * constants.CELL_SIZE, y)
        engine.set_position(engine_position)
        engine.set_text('8')
        engine.set_color(constants.CYAN)
        self._engine = engine

    def move_up(self):
        head_y = (self._head.get_position().get_y() - self.get_velocity().get_y()) % constants.MAX_Y
        left_wing_y = (self._left_wing.get_position().get_y() - self.get_velocity().get_y()) % constants.MAX_Y
        right_wing_y = (self._right_wing.get_position().get_y() - self.get_velocity().get_y()) % constants.MAX_Y
        engine_y = (self._engine.get_position().get_y() - self.get_velocity().get_y()) % constants.MAX_Y
        self._head.set_position(Point(self._head.get_position().get_x(), head_y))
        self._left_wing.set_position(Point(self._left_wing.get_position().get_x(), left_wing_y))
        self._right_wing.set_position(Point(self._right_wing.get_position().get_x(), right_wing_y))
        self._engine.set_position(Point(self._engine.get_position().get_x(), engine_y))

    def move_down(self):
        head_y = (self._head.get_position().get_y() + self.get_velocity().get_y()) % constants.MAX_Y
        left_wing_y = (self._left_wing.get_position().get_y() + self.get_velocity().get_y()) % constants.MAX_Y
        right_wing_y = (self._right_wing.get_position().get_y() + self.get_velocity().get_y()) % constants.MAX_Y
        engine_y = (self._engine.get_position().get_y() + self.get_velocity().get_y()) % constants.MAX_Y
        self._head.set_position(Point(self._head.get_position().get_x(), head_y))
        self._left_wing.set_position(Point(self._left_wing.get_position().get_x(), left_wing_y))
        self._right_wing.set_position(Point(self._right_wing.get_position().get_x(), right_wing_y))
        self._engine.set_position(Point(self._engine.get_position().get_x(), engine_y))


