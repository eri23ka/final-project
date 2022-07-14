from game import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.bullet import Bullet


class ControlActorsAction(Action):
    
    def __init__(self, keyboard_service):
        
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        
    def execute(self, cast, script):
       
        fighter = cast.get_actors("fighter")[0]
        
        # up 
        if self._keyboard_service.is_key_down('w'):
            self.move_up()
            
        # down 
        if self._keyboard_service.is_key_down('s'):
            self.move_down()

        #shoot
        if self._keyboard_service.is_key_down('space'):
            head = cast.get_first_actor('fighter').get_head().get_position()
            cast.add_actor('bullets', Bullet(5, head))