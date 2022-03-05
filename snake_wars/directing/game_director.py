from art import tprint, DEFAULT_FONT

# Manages the window and keyboard input classes (along with most of the game)
class GameDirector():
    
    def __init__(self):
        pass
    
    def fancy_print_text(self, input_text):
        tprint(text=input_text, font=DEFAULT_FONT)