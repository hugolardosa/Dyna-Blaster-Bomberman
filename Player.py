import pygame
from Command import Command

class Player(Command):
    def __init__(self, stage, dropbomb) -> None:
        super().__init__()
        self.health = 1
        self.ticks = 0
        self.speed = 4
        self.pos = stage.player
        self.stage = stage
        self.dropbomb = dropbomb
    
    def isAlive(self):
        return self.health > 0
    
    def takeDamage(self):
        self.health -= 1    
    
    # check collision with walls and boxes
    # if no collision, move player and update Game's player position
    def up(self):
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            walls = self.stage.walls
            boxes = self.stage.boxes
            if (self.pos[0], self.pos[1] - 1) in walls or [self.pos[0], self.pos[1] - 1] in boxes:
                return
            self.pos[1] -= 1
            
            self.ticks = 0
            
    def down(self):
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            walls = self.stage.walls
            boxes = self.stage.boxes
            if (self.pos[0], self.pos[1] + 1) in walls or [self.pos[0], self.pos[1] + 1] in boxes:
                return
            self.pos[1] += 1
            
            self.ticks = 0
            
    def left(self):
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            walls = self.stage.walls
            boxes = self.stage.boxes
            if (self.pos[0]- 1, self.pos[1]) in walls or [self.pos[0]- 1, self.pos[1]] in boxes:
                return
            self.pos[0] -= 1

            self.ticks = 0
        
    def right(self):
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            walls = self.stage.walls
            boxes = self.stage.boxes
            if (self.pos[0] + 1, self.pos[1]) in walls or [self.pos[0] + 1, self.pos[1]] in boxes:
                return
            self.pos[0] += 1
            self.ticks = 0
            
    # drop bomb, send an dropbomb event to queue
    def action(self):
        env = pygame.event.Event(self.dropbomb, {"pos": self.pos})
        pygame.event.post(env)
