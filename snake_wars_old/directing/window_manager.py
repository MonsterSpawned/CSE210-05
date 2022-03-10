import pyray

# Manages the window and keyboard input classes
class WindowManager():
    
    def __init__(self, window_width: int, window_height: int, window_title: str, game_fps: int):
        self.open_app_window(window_width=window_width, window_height=window_height, window_title=window_title, fps=game_fps)
        
    def open_app_window(self, window_width,window_height, window_title, fps):
        pyray.init_window(window_width, window_height, window_title)
        pyray.set_target_fps(fps)
        
    def is_window_open(self):
        return not pyray.window_should_close()
    
    # TODO: CHANGE ALL THE BELOW CODE TO CUSTOM CODE:
    
    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()
        
    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
            
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()
        
    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)
    
    def draw_actor(self, actor, centered=False):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
            
        pyray.draw_text(text, x, y, font_size, color)
        
    def draw_actors(self, actors, centered=False):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for actor in actors:
            self.draw_actor(actor, centered)