
from art import tprint, DEFAULT_FONT
class Game():
    def __init__(self):
        pass
    
    def fancy_print_text(self, input_text):
        tprint(text=input_text, font=DEFAULT_FONT)
    
if __name__ == "__main__":
    game = Game()