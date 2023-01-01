class Bomb:
    def __init__(self, pos, time, radius) -> None:
        self.pos = pos
        self.time = time
        self.radius = radius
        self.damage = 1
        self.ticks = 0
        self.exploded = False
        

   
    def tick(self):
        if self.ticks < self.time:
            self.ticks += 1  
            
    