from art import tprint, DEFAULT_FONT

from snake_wars.directing.keyboard_manager import KeyboardManager
from snake_wars.directing.window_manager import WindowManager

# Manages the window and keyboard input classes (along with most of the game)
class GameDirector():
    
    def __init__(self):
        self.window_manager = WindowManager()
        self.keyboard_manager = KeyboardManager()
    
    def fancy_print_text(self, input_text):
        tprint(text=input_text, font=DEFAULT_FONT)