class Box:
    def __init__(self, x, y, powerup=None):
        self.pos = [x,y]
        self.opened = False
        self.used = False
        self.powerup = powerup
    
    def setOpened(self):
        self.opened = True
    
    @property
    def isOpened(self):
        return self.opened
    
    def setUsed(self):
        self.used = True
    
    @property
    def isUsed(self):
        return self.used
    
    @property
    def powerUp(self):
        return self.powerup
    
    def setPowerUp(self, powerup):
        self.powerup = powerup
    
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Box):
            return False
        return self.pos == __o.pos and self.opened == __o.opened