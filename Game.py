from Stage import Stage
from Player import Player
from Enemy import Enemy
from Box import Box
from Bomb import Bomb

import pygame 

class Game:
    
    def __init__(self):
        self._scale = 40
        self._height = 15
        self._width = 15
        self._stage = Stage("Maps/map_1.bmp")
        
        self._dropbomb = pygame.event.custom_type()
        self._boxdrop = pygame.event.custom_type()
        self._playerdead = pygame.event.custom_type()
        self._enemydead = pygame.event.custom_type()
        
        self._boxes = [Box(b[0],b[1]) for b in self._stage.boxes]
        
        self._bombs = []
        
        
        self._player = Player(self._stage.player, self._stage.walls,self._boxes,self._bombs ,self._dropbomb)
        
        self._enemies = []
        self._enemies.append(Enemy(1, [7,11] , self._player, self.stage._walls, self._boxes, self._bombs, self._enemies))
    
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
        return self._player.pos
        
    @property
    def boxdrop(self):
        return self._boxdrop

    @property
    def playerdead(self):
        return self._playerdead
    
    @property
    def bombs(self):
        return self._bombs
    
    @property
    def boxes(self):
        return self._boxes
    
    def addBomb(self, pos):
        self._bombs.append(Bomb(pos,40, 3))

    @property
    def enemies(self):
        return self._enemies
    
    @property
    def player(self):
        return self._player
    
    def tick(self):

        for enemy in self._enemies:
            enemy.tick()
            
            if self._player.pos[0] == enemy.pos[0] and self._player.pos[1] == enemy.pos[1]:
                pygame.event.post(pygame.event.Event(self._playerdead)) 
            
        for bomb in self._bombs:
            bomb.tick()
            if bomb.timePassed >= bomb.time:
                self.explosion(bomb)
                self._bombs.remove(bomb)
                
    def inRange(self, bomb, gameElement):
        bombX, bombY = bomb.pos
        
        elemX, elemY = gameElement.pos if hasattr(gameElement, "pos") else gameElement
        
        walls = self.stage.walls
        if bombX == elemX:
            for rad in range(bomb.radius + 1):
                if (bombX, bombY + rad) in walls:
                    break
                if (elemX, elemY) == (bombX, bombY + rad):
                    return True
            for rad in range(bomb.radius + 1):
                if (bombX, bombY - rad) in walls:
                    break
                if (elemX, elemY) == (bombX, bombY - rad):
                    return True
        if bombY == elemY:
            for rad in range(bomb.radius + 1):
                if (bombX - rad, bombY) in walls:
                    break
                if (elemX, elemY) == (bombX + rad, bombY ):
                    return True
            for rad in range(bomb.radius + 1):
                if (bombX - rad, bombY) in walls:
                    break
                if (elemX, elemY) == (bombX - rad, bombY):
                    return True
                
        return False

    def explosion(self,bomb):
        
        bomb.exploded = True

        if self.inRange(bomb,self._player):
            env = pygame.event.Event(self.playerdead)
            pygame.event.post(env)
        
        for box in self.boxes:
            print(box.pos)
            if self.inRange(bomb, box):
                box.setOpened()
        
        # enemies
        for enemy in self._enemies:
            if self.inRange(bomb, enemy):
                enemy.kill()
                
        
        # for box in self.boxes:
        #     if box.opened:
        #         self._boxes.remove(box)
            
        for enemy in self.enemies:
            if not enemy.isAlive:
                self._enemies.remove(enemy)
                
