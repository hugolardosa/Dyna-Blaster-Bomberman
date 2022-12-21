import pygame
import time 

from Game import Game


class Bomb:
    def __init__(self,pos,time) -> None:
        self.pos = pos
        self.time = time
        self.radius = 5
        self.damage = 1
        self.exploded = False
    
    def draw(self,display):
        scale = Game.getInstance().scale
        display.fill("orange", (self.pos[0] * scale, self.pos[1] * scale, scale, scale))
    
    def inRange(self, gameElement):
        bombX, bombY = self.pos
        
        elemX, elemY = gameElement.pos if hasattr(gameElement, "pos") else gameElement
        
        walls = Game.getInstance().stage.walls
        if bombX == elemX:
            for rad in range(self.radius + 1):
                if (bombX, bombY + rad) in walls:
                    break
                if (elemX, elemY) == (bombX, bombY + rad):
                    return True
            for rad in range(self.radius + 1):
                if (bombX, bombY - rad) in walls:
                    break
                if (elemX, elemY) == (bombX, bombY - rad):
                    return True
        if bombY == elemY:
            for rad in range(self.radius + 1):
                if (bombX - rad, bombY) in walls:
                    break
                if (elemX, elemY) == (bombX + rad, bombY ):
                    return True
            for rad in range(self.radius + 1):
                if (bombX - rad, bombY) in walls:
                    break
                if (elemX, elemY) == (bombX - rad, bombY):
                    return True
                
        return False
        
        
    def explode(self):
        player = Game.getInstance().playerCurrentPos
        
        self.exploded = True
        
        if self.inRange(player):
            env = pygame.event.Event(Game.getInstance().playerdead)
            pygame.event.post(env)
        
        for box in Game.getInstance().stage.boxes:
            if self.inRange(box):
                env = pygame.event.Event(Game.getInstance().boxdrop, {"box": box})
                pygame.event.post(env)
        
        # enemies
        
        # bomb