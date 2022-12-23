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
        self._boxes = []
        self._player = []
        
        for x in range(self.hor_tiles):
            for y in range(self.ver_tiles):
                p = self.mapArray[x][y] 
                if p == WALL:
                    self._walls.append((x,y))
                elif p == BOX:
                    self._boxes.append([x,y])
                elif p == PLAYER:
                    self._player = [x,y]
    
    @property
    def player(self):
        return self._player
    
    @property
    def walls(self):
        return self._walls

    @property
    def boxes(self):
        return self._boxes


    def getGameMatrix(self):
        matrix = [[1 for x in range(self.ver_tiles)] for y in range(self.hor_tiles)]
        for w in self._walls:
            matrix[w[1]][w[0]] = 0
        for b in self._boxes:
            matrix[b[1]][b[0]] = 0
        return matrix