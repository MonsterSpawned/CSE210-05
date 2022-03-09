import pyray as pr
from pyray import *
from pyray import Color
from raylib import colors

class Colors():
    pass # TODO: List all color options here.

class BaseColor():
    
    def __init__(self, red, green, blue, alpha):
        self._r = red
        self._g = green
        self._b = blue
        self._a = alpha
        
    def get_color(self, _r, _g, _b, _a):
        return Color(_r, _b, _b, _a)