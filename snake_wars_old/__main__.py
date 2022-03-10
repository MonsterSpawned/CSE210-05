from snake_wars.directing.game_director import GameDirector

# This class is PURELY for stating the GameDirector class, initalizing it, and managing the bare necessities of the game.
# NOTHING ELSE!!!
class Game():
    def __init__(self):
        self.game_manager = GameDirector()
    
if __name__ == "__main__":
    game = Game()