from snake.casting.entity import Entity

class ItemEntity(Entity):
    
    def __init__(self, name_var):
        super().__init__(name_var)
        self.ent_name = "Item"