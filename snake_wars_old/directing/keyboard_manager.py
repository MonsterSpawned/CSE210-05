import pyray

# Manages the window and keyboard input classes
class KeyboardManager():
    
    def __init__(self):
        self._keys = {
            # Player 1's keys:
            'w': pyray.KeyboardKey.KEY_W,
            'a': pyray.KeyboardKey.KEY_A,
            's': pyray.KeyboardKey.KEY_S,
            'd': pyray.KeyboardKey.KEY_D,
            # PLayer 2's keys:
            'down': pyray.KeyboardKey.KEY_DOWN,
            'up': pyray.KeyboardKey.KEY_UP,
            'left': pyray.KeyboardKey.KEY_LEFT,
            'right': pyray.KeyboardKey.KEY_RIGHT,
        }
    
    def is_key_up(self, key):
        # Run this code when the player releases a key:
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        # Run this code when the player presses a key (or holds it):
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)