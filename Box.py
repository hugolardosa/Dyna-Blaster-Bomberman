class Box:
    def __init__(self, x, y):
        self.pos = [x,y]
        self.opened = False
    
    def set_opened(self):
        self.opened = True
    
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Box):
            return False
        return self.pos == __o.pos and self.opened == __o.opened