import pygame
from Command import Command
from Common import PlayerState

class Player(Command):
    def __init__(self, pos, walls, boxes, bombs, dropbomb, wallPass) -> None:
        super().__init__()
        self.health = 1
        self.ticks = 0
        self.speed = 4
        self.pos = pos
        self.walls = walls
        self.boxes = boxes
        self.bombs = bombs
        self.dropbomb = dropbomb
        self.state = PlayerState.IDLE
        self.wallPass = wallPass    
    
    def isAlive(self):
        return self.health > 0
    
    def takeDamage(self):
        self.health -= 1    
    
    def idle(self):
        self.state = PlayerState.IDLE
    
    # check collision with walls and boxes
    # if no collision, move player and update Game's player position
    def up(self):
        self.state = PlayerState.UP
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            walls = self.walls
            boxes = [b.pos for b in self.boxes if not b.isOpened]
            bombs = [b.pos for b in self.bombs]
            possible_pos = [self.pos[0], self.pos[1] - 1]
            
            if possible_pos in walls or possible_pos in bombs:
                return
                
            if not self.wallPass:
                if possible_pos in boxes:
                    return
            
            self.pos[1] -= 1
            
            self.ticks = 0
            
    def down(self):
        self.state = PlayerState.DOWN
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            walls = self.walls
            boxes = [b.pos for b in self.boxes if not b.isOpened]
            bombs =  [b.pos for b in self.bombs]
            possible_pos = [self.pos[0], self.pos[1] + 1]
            
            if possible_pos in walls or possible_pos in bombs:
                return
                
            if not self.wallPass:
                if possible_pos in boxes:
                    return
                
            self.pos[1] += 1
            
            self.ticks = 0
            
    def left(self):
        self.state = PlayerState.LEFT
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            walls = self.walls
            boxes = [b.pos for b in self.boxes if not b.isOpened]
            bombs =  [b.pos for b in self.bombs]
            possible_pos =  [self.pos[0]- 1, self.pos[1]]
            
            if possible_pos in walls or possible_pos in bombs:
                return
                
            if not self.wallPass:
                if possible_pos in boxes:
                    return
            
            self.pos[0] -= 1

            self.ticks = 0
        
    def right(self):
        self.state = PlayerState.RIGHT
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            walls = self.walls
            boxes = [b.pos for b in self.boxes if not b.isOpened]
            bombs =  [b.pos for b in self.bombs]
            possible_pos = [self.pos[0] + 1, self.pos[1]]
            
            if possible_pos in walls or possible_pos in bombs:
                return
                
            if not self.wallPass:
                if possible_pos in boxes:
                    return
            
            self.pos[0] += 1
            self.ticks = 0
            
    # drop bomb, send an dropbomb event to queue
    def action(self):
        env = pygame.event.Event(self.dropbomb, {"pos": self.pos})
        pygame.event.post(env)
