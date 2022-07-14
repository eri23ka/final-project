import pyray
from game.shared.point import Point

class KeyboardService:
  
    def __init__(self):
       
        self._keys = {'w': pyray.KEY_W, 's': pyray.KEY_S, 'space': pyray.KEY_SPACE}

    def is_key_up(self, key):
       
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):

        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)