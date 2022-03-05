class EntityType():
    BASE = 0
    PLAYER1 = 1
    PLAYER2 = 2
    ITEM = 3
    POWER_UP = 4

class Entity():
    
    def __init__(self, name_var):
        self.ent_name = name_var
    
    def get_name(self):
        return self.ent_name