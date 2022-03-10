from pyray import *
from pyray import Color

class BaseColor():
    def __init__(self, red: int, green: int, blue: int, alpha: int = 255):
        self._r = red
        self._g = green
        self._b = blue
        self._a = alpha
        
    def get_color(self, _r, _g, _b, _a):
        return Color(_r, _g, _b, _a)

class Colors():
    WHITE = BaseColor(255, 255, 255)
    RED = Color(255, 0, 0)
    YELLOW = Color(255, 255, 0)
    GREEN = Color(0, 255, 0)