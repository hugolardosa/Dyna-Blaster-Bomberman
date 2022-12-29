class Box:
    def __init__(self, x, y, powerup):
        self.pos = [x,y]
        self.opened = False
        self.powerup = None
    
    def setOpened(self):
        self.opened = True
    
    @property
    def isOpened(self):
        return self.opened
    
    
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Box):
            return False
        return self.pos == __o.pos and self.opened == __o.opened