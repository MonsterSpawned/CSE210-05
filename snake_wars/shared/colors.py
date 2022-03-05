import pyray as pr
from pyray import *
from raylib import colors

class Colors():
    pass # List all color options here.

class Color():
    
    def __init__(self, red, green, blue, alpha):
        self._r = red
        self._g = green
        self._b = blue
        self._a = alpha