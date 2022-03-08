import pyray

# Manages the window and keyboard input classes
class WindowManager():
    
    def __init__(self, window_width, window_height, window_title, game_fps):
        self.open_app_window(window_width=window_width, window_height=window_height, window_title=window_title, fps=game_fps)
        
    def open_app_window(self, window_width,window_height, window_title, fps):
        pyray.init_window(window_width, window_height, window_title)
        pyray.set_target_fps(fps)
        
    def is_window_open(self):
        return not pyray.window_should_close()