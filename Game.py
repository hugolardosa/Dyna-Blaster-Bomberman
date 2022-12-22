from Stage import Stage
import pygame 

class Game:
    
    __instance = None
    
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Game.__instance == None:
            Game()
        return Game.__instance
    
    def __init__(self):
        self._scale = 40
        self._height = 15
        self._width = 15
        self._stage = Stage("Maps/map_1.bmp")
        self._playerCurrentPos = self._stage.player
        self._bombs = []
        self._dropbomb = pygame.event.custom_type()
        self._boxdrop = pygame.event.custom_type()
        self._playerdead = pygame.event.custom_type()
        self._enemydead = pygame.event.custom_type()
        
        """ Virtually private constructor. """
        if Game.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Game.__instance = self
            
    
    @property
    def scale(self):
        return self._scale
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    @property
    def stage(self):
        return self._stage
    
    @property
    def dropbomb(self):
        return self._dropbomb

    @property
    def playerCurrentPos(self):
        return self._playerCurrentPos
    
    def setPlayerCurrentPos(self, pos):
        self._playerCurrentPos = pos
        
    @property
    def boxdrop(self):
        return self._boxdrop

    @property
    def playerdead(self):
        return self._playerdead
    
    @property
    def bombs(self):
        return self._bombs
    
    def tick(self):
        for enemy in self._stage.enemies:
            enemy.tick()
            
        for bomb in self._bombs:
            bomb.tick()
            if bomb.exploded:
                self._bombs.remove(bomb)
    