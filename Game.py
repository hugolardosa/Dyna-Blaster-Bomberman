from Stage import Stage
from Player import Player
from Enemy import Enemy
from Box import Box
from Bomb import Bomb
from Common import PowerUps


import pygame 

import random

import logging

class Game:
    
    def __init__(self):
        self.level = 1
        self._scale = 40
        self._height = 15
        self._width = 15
        
        self._stage = Stage(f"Maps/map_{self.level}.bmp")
        self._stagepowerUps = {
            1 : [PowerUps.NextLevel, PowerUps.FireUp],
            2 : [PowerUps.SpeedUp, PowerUps.NextLevel, PowerUps.FireUp],
            
        }
        
        self._dropbomb = pygame.event.custom_type()
        self._boxdrop = pygame.event.custom_type()
        self._playerdead = pygame.event.custom_type()
        self._enemydead = pygame.event.custom_type()
        self._nextstage = pygame.event.custom_type()
        
        self._wallPass = False
        self._bombRadius = 2
        self._bombs = []
        
        self._loadStage()
        
    
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
    def nextstage(self):
        return self._nextstage
    
    @property
    def bombs(self):
        return self._bombs
    
    @property
    def boxes(self):
        return self._boxes
    
    def addBomb(self, pos):
        self._bombs.append(Bomb(pos,40, self._bombRadius))

    @property
    def enemies(self):
        return self._enemies
    
    @property
    def player(self):
        return self._player
    
    def tick(self):
        self._checkPlayerBox()
                
        for enemy in self._enemies:
            enemy.tick()
            
            if self._player.pos[0] == enemy.pos[0] and self._player.pos[1] == enemy.pos[1] and enemy.isAlive:
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
            if self.inRange(bomb, box):
                box.setOpened()
        
        # enemies
        for enemy in self._enemies:
            if self.inRange(bomb, enemy):
                enemy.kill()
                
    def _checkPlayerBox(self):
        boxes = [b for b in self._boxes if b.isOpened and b.powerUp != None and not b.isUsed]
        
        if self.player.pos in [b.pos for b in boxes]:
            for box in boxes:
                if self.player.pos == box.pos:
                    if box.powerUp is PowerUps.NextLevel:
                        logging.info(f"Player is in box with powerup {box.powerUp}")
                        if all([not e.isAlive for e in self._enemies]):
                            pygame.event.post(pygame.event.Event(self._nextstage))
                            box.setUsed()
                    elif box.powerUp is PowerUps.FireUp:
                        self._bombRadius += 1 if self._bombRadius < 5 else 5
                        box.setUsed()
                    elif box.powerUp is PowerUps.FireDown:
                        self._bombRadius -= 1 if self._bombRadius > 3 else 2
                        box.setUsed()
                    elif box.powerUp is PowerUps.SpeedUp:
                        self._player.speed -= 1 if self._player.speed > 1 else 0
                        box.setUsed()
                    elif box.powerUp is PowerUps.SpeedDown:
                        self._player.speed += 1 if self._player.speed < 5 else 4
                        box.setUsed()
                        
    def _setPowerUps(self):
        numPowerUps = len(self._stagepowerUps[self.level])
        boxes = random.choices(self._boxes, k=numPowerUps)
        for b in range(numPowerUps):
            boxes[b].setPowerUp(self._stagepowerUps[self.level][b])
            
    def loadNextStage(self):
        self.level += 1
        self._stage = Stage(f"Maps/map_{self.level}.bmp")
        self._loadStage()
    
    def _loadStage(self):
        self._boxes = [Box(b[0],b[1]) for b in self._stage.boxes]
        self._setPowerUps()
        
        self._player = Player(self._stage.player, self._stage.walls,self._boxes,self._bombs ,self._dropbomb,self._wallPass)
        
        self._enemies = []
        i = 0
        print(self._stage.enemies)
        for pos in self._stage.enemies:
            self._enemies.append(Enemy(i, pos , self._player, self.stage._walls, self._boxes, self._bombs, self._enemies,self._wallPass))
            i += 1
            
        print(self._enemies)