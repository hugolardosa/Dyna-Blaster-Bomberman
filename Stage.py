import pygame

WALL = 16777215
PLAYER = 255
BOX = 16711680

class Stage:
    
    
    def __init__(self, filename) -> None:
        self._filename = filename
        image = pygame.image.load(self._filename)
        self.mapArray = pygame.PixelArray(image)
        self.hor_tiles=len(self.mapArray)
        self.ver_tiles=len(self.mapArray[0])

        self._walls = []
        self._boxesInitialPos = []
        self._playerInitialPos = []
        self._enemiesInitialPos = []
        
        for x in range(self.hor_tiles):
            for y in range(self.ver_tiles):
                p = self.mapArray[x][y] 
                if p == WALL:
                    self._walls.append([x,y])
                elif p == BOX:
                    self._boxesInitialPos.append([x,y])
                elif p == PLAYER:
                    self._playerInitialPos = [x,y]
    
    @property
    def player(self):
        return self._playerInitialPos
    
    @property
    def walls(self):
        return self._walls

    @property
    def boxes(self):
        return self._boxesInitialPos
    
    @property
    def enemies(self):
        return self._enemiesInitialPos
