import pygame
from Command import Command
from Game import Game

class Player(Command):
    def __init__(self) -> None:
        super().__init__()
        self.health = 1
        self.ticks = 0
        self.speed = 5
        self.pos = Game.getInstance().stage.player
    
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
            walls = Game.getInstance().stage.walls
            boxes = [(b.pos[0],b.pos[1]) for b in Game.getInstance().stage.boxes]
            if (self.pos[0], self.pos[1] - 1) in walls or (self.pos[0], self.pos[1] - 1) in boxes:
                return
            self.pos[1] -= 1
            Game.getInstance().setPlayerCurrentPos(self.pos)
            self.ticks = 0
            
    def down(self):
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            walls = Game.getInstance().stage.walls
            boxes = [(b.pos[0],b.pos[1]) for b in Game.getInstance().stage.boxes]
            if (self.pos[0], self.pos[1] + 1) in walls or (self.pos[0], self.pos[1] + 1) in boxes:
                return
            self.pos[1] += 1
            Game.getInstance().setPlayerCurrentPos(self.pos)
            self.ticks = 0
            
    def left(self):
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            walls = Game.getInstance().stage.walls
            boxes = [(b.pos[0],b.pos[1]) for b in Game.getInstance().stage.boxes]
            if (self.pos[0]- 1, self.pos[1]) in walls or (self.pos[0]- 1, self.pos[1]) in boxes:
                return
            self.pos[0] -= 1
            Game.getInstance().setPlayerCurrentPos(self.pos)
            self.ticks = 0
        
    def right(self):
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            walls = Game.getInstance().stage.walls
            boxes = [(b.pos[0],b.pos[1]) for b in Game.getInstance().stage.boxes]
            if (self.pos[0] + 1, self.pos[1]) in walls or (self.pos[0] + 1, self.pos[1]) in boxes:
                return
            self.pos[0] += 1
            Game.getInstance().setPlayerCurrentPos(self.pos)
            self.ticks = 0
            
    # drop bomb, send an dropbomb event to queue
    def action(self):
        env = pygame.event.Event(Game.getInstance().dropbomb, {"pos": self.pos})
        pygame.event.post(env)
