from game.casting.cast import Cast
from game.casting.fighter import Fighter
from game.casting.enemy import Enemy
from game.casting.score import Score
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("fighter", Fighter())
    cast.add_actor("enemies", Enemy(True))
    cast.add_actor("enemies", Enemy(True))
    cast.add_actor("enemies", Enemy(False))
    cast.add_actor("enemies", Enemy(False))
    cast.add_actor("enemies", Enemy(False))
    cast.add_actor("enemies", Enemy(False))
    cast.add_actor("scores", Score())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()
    
    
