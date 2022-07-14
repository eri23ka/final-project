from game.scripting.action import Action


class DrawActorsAction(Action):

    def __init__(self, video_service):
        
        self._video_service = video_service

    def execute(self, cast, script):
       
        score = cast.get_actors("scores")[0]
        fighter = cast.get_first_actor("fighter")
        enemies = cast.get_actors("enemies")
        bullets = cast.get_actors("bullets")
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_fighter(fighter)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(bullets)
        self._video_service.draw_enemies(enemies)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
