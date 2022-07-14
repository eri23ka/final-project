from game import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):

    def __init__(self):
      
        self._is_game_over = False

    def execute(self, cast, script):
       
        if not self._is_game_over:
            self._handle_bullet_enemy_collision(cast)
            self._handle_invasion(cast)
            self._handle_bullet_miss(cast)
            self._handle_game_over(cast)

    def _handle_bullet_enemy_collision(self, cast):
       
        bullets = cast.get_actors('bullets')
        enemies = cast.get_actors('enemies')
        score = cast.get_first_actor('scores')
        for bullet in bullets:
            for enemy in enemies:
                if bullet.get_position().equals(enemy.get_core().get_position()):
                    score.add_points(20 if enemy.get_is_advanced() else 5)
                    enemy.reset()

    def _handle_bullet_miss(self, cast):
        bullets = cast.get_actors('bullets')

        for bullet in bullets:
            if bullet.get_position().get_x() > constants.MAX_X:
                cast.remove_actor('bullets', bullet)

    def _handle_invasion(self, cast):

        enemies = cast.get_actors('enemies')

        for enemy in enemies:
            if enemy.get_right_top().get_position().get_x() < 0:
                self._is_game_over = True

    def _handle_game_over(self, cast):

        if self._is_game_over:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            message = Actor()
            message.set_text("Your score is " + str(cast.get_first_actor('scores').get_points()))
            score_position = Point(position.get_x(), position.get_y() + 1 * constants.CELL_SIZE)
            message.set_position(score_position)
            cast.add_actor("messages", message)

            cast.get_first_actor('fighter').set_color(constants.WHITE)