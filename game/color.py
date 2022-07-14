class Color:
    def __init__(self, red, violet, skyblue, magenta, brown, alpha = 255):
        self._red = red
        self._violet = violet
        self._skyblue = skyblue
        self._magenta = magenta
        self._brown = brown

        self.alpha = alpha
    
    def to_tuple(self):

        return (self._red, self._violet, self._red, self._skyblue, self._magenta, self._brown, self._alpha)