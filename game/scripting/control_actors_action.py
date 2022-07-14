from game import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.bullet import Bullet

class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        fighter = cast.get_actors("fighter")[0]

        # fighter move up
        if self._keyboard_service.is_key_down('w'):
            fighter.move_up()

        # fighter move down
        if self._keyboard_service.is_key_down('s'):
            fighter.move_down()

        # fighter shoot
        if self._keyboard_service.is_key_down('space'):
            head = cast.get_first_actor('fighter').get_head().get_position()
            cast.add_actor('bullets', Bullet(5, head))
