import pyray


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {
            'w': pyray.KeyboardKey.KEY_W,
            'a': pyray.KeyboardKey.KEY_A,
            's': pyray.KeyboardKey.KEY_S,
            'd': pyray.KeyboardKey.KEY_D,
            'up': pyray.KeyboardKey.KEY_UP,
            'down': pyray.KeyboardKey.KEY_DOWN,
            'left': pyray.KeyboardKey.KEY_LEFT,
            'right': pyray.KeyboardKey.KEY_RIGHT,
        }

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d or up, down, left, right)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d or up, down, left, right)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)