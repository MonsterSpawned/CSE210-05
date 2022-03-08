import pyray

from snake_wars.shared.point import Point

# Manages the window and keyboard input classes
class KeyboardManager():
    
    def __init__(self, cell_size: int = 1):
        self._cell_size = cell_size
        
    def get_direction(self, player_num):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0
        if player_num == 1:   
            if pyray.is_key_down(pyray.KeyboardKey.KEY_LEFT):
                dx = -1
                
            if pyray.is_key_down(pyray.KeyboardKey.KEY_RIGHT):
                dx = 1
            
            if pyray.is_key_down(pyray.KeyboardKey.KEY_UP):
                dy = -1
            
            if pyray.is_key_down(pyray.KeyboardKey.KEY_DOWN):
                dy = 1

            direction = Point(dx, dy)
            direction = direction.scale(self._cell_size)
            
            return direction
        elif player_num == 2:   
            if pyray.is_key_down(pyray.KeyboardKey.KEY_A):
                dx = -1
            
            if pyray.is_key_down(pyray.KeyboardKey.KEY_D):
                dx = 1
            
            if pyray.is_key_down(pyray.KeyboardKey.KEY_W):
                dy = -1
            
            if pyray.is_key_down(pyray.KeyboardKey.KEY_S):
                dy = 1

            direction = Point(dx, dy)
            direction = direction.scale(self._cell_size)
            
            return direction