class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0
    
    def walk(self):
        walls = Game.getInstance().stage.walls
        boxes = Game.getInstance().stage.boxes
        
        