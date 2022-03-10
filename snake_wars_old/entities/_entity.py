from tkinter import CURRENT


class EntityType():
    
    CURRENT_TYPE = -1
    
    BASE = 0
    PLAYER1 = 1
    PLAYER2 = 2
    ITEM = 3
    POWER_UP = 4
    
    UNKNOWN = 9
    
    def __init__(self, type: int):
        if type == 0:
            self.CURRENT_TYPE = self.BASE
        elif type == 1:
            self.CURRENT_TYPE = self.PLAYER1
        elif type == 2:
            self.CURRENT_TYPE = self.PLAYER2
        elif type == 3:
            self.CURRENT_TYPE = self.ITEM
        elif type == 4:
            self.CURRENT_TYPE = self.POWER_UP
        else:
            self.CURRENT_TYPE = self.UNKNOWN

class Entity():
    
    def __init__(self, name_var, ent_type: EntityType):
        self.ent_name = name_var
        # if self.ent_type == EntityType(EntityType.PLAYER1) or self.ent_type == EntityType(EntityType.PLAYER2):
            
                
    
    def get_name(self):
        return self.ent_name