class Box:
    def __init__(self, x, y):
        self.pos = [x,y]
        self.opened = False
    
    def set_opened(self):
        self.opened = True
        