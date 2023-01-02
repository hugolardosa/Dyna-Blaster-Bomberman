from Stage import Stage
from Player import Player
from Enemy import Enemy
from Box import Box
from Bomb import Bomb
from Common import PowerUps
from ScoreBoard import ScoreBoard
from Timer import Timer


import pygame 

import random

class Game:
    
    def __init__(self):
        self.level = 1
        self._scale = 35
        self._height = 15
        self._width = 15
        
        self._stage = Stage(f"Maps/map_{self.level}.bmp")
        self._stagepowerUps = {
            1 : [PowerUps.NextLevel, PowerUps.FireUp],
            2 : [PowerUps.NextLevel, PowerUps.SpeedUp, PowerUps.FireUp],
            3 : [PowerUps.NextLevel, PowerUps.SpeedUp, PowerUps.FireUp, PowerUps.FireDown],
            4 : [PowerUps.NextLevel, PowerUps.SpeedUp, PowerUps.FireUp, PowerUps.FireDown, PowerUps.Wallpass],
        }
        
        for i in range(5, 12):
            self._stagepowerUps[i] = [PowerUps.NextLevel, PowerUps.SpeedUp, PowerUps.FireUp, PowerUps.FireDown, PowerUps.Wallpass]
        
        self._dropbomb = pygame.event.custom_type()
        self._boxdrop = pygame.event.custom_type()
        self._playerdead = pygame.event.custom_type()
        self._enemydead = pygame.event.custom_type()
        self._nextstage = pygame.event.custom_type()
        self._exploding = pygame.event.custom_type()
        self._gamewon = pygame.event.custom_type()
        
        self._scoreboard = ScoreBoard()
        self._timer = Timer()
        
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
    def gamewon(self):
        return self._gamewon
    
    @property
    def exploding(self):
        return self._exploding
    
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
    
    @property
    def scoreboard(self):
        return self._scoreboard
    
    @property
    def timer(self):
        return self._timer
    
    def tick(self):
        self._checkPlayerBox()
        self._timer.tick()
        
        if self._timer.timesUp():
            pygame.event.post(pygame.event.Event(self._playerdead))
        
        for enemy in self._enemies:
            enemy.tick()
            
            if self._player.pos[0] == enemy.pos[0] and self._player.pos[1] == enemy.pos[1] and enemy.isAlive:
                pygame.event.post(pygame.event.Event(self._playerdead)) 
            
        for bomb in self._bombs:
            bomb.tick()
            if bomb.ticks >= bomb.time:
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
        
        pygame.event.post(pygame.event.Event(self._exploding))
        
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
                        if all([not e.isAlive for e in self._enemies]):
                            pygame.event.post(pygame.event.Event(self._nextstage))
                            box.setUsed()
                    elif box.powerUp is PowerUps.FireUp:
                        if self._bombRadius < 5:  self._bombRadius += 1
                        box.setUsed()
                    elif box.powerUp is PowerUps.FireDown:
                        if self._bombRadius > 3: self._bombRadius -= 1 
                        box.setUsed()
                    elif box.powerUp is PowerUps.SpeedUp:
                        if self._player.speed > 1: self._player.speed -= 1
                        box.setUsed()
                    elif box.powerUp is PowerUps.SpeedDown:
                        if self._player.speed < 5: self._player.speed += 1
                        box.setUsed()
                    elif box.powerUp is PowerUps.Wallpass:
                        self._wallPass = True
                        self.player.wallPass = True
                        for e in self._enemies:
                            e.wallPass = True
                        box.setUsed()
                        
    def _setPowerUps(self):
        numPowerUps = len(self._stagepowerUps[self.level])
        indexes = random.sample(range(0, len(self._boxes)), numPowerUps)

        p = 0
        for i in indexes:
            self._boxes[i].setPowerUp(self._stagepowerUps[self.level][p])
            p += 1
            
    def loadNextStage(self):
        if self.level == 11:
            env = pygame.event.Event(self.gamewon)
            pygame.event.post(env)
            return
        self.level += 1
        self._stage = Stage(f"Maps/map_{self.level}.bmp")
        self._loadStage()
    
    def _loadStage(self):
        self._boxes = [Box(b[0],b[1]) for b in self._stage.boxes]
        self._setPowerUps()
        
        self._player = Player(self._stage.player, self._stage.walls,self._boxes,self._bombs ,self._dropbomb,self._wallPass)
        
        self._enemies = []
        i = 0
        for pos in self._stage.enemies:
            e = Enemy(i, pos , self._player, self.stage._walls, self._boxes, self._bombs, self._enemies,self._wallPass)
            e.add_observer(self._scoreboard)
            self._enemies.append(e)
            i += 1
            