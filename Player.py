import pygame
from Command import Command
from Game import Game

class Player(Command):
    def __init__(self) -> None:
        super().__init__()
        self.health = 3
        self.pos = Game.getInstance().stage.player
        
        
    def draw(self, display):
        scale = Game.getInstance().scale
        display.fill("red", (self.pos[0] * scale, self.pos[1] * scale, scale, scale))
    
    # check collision with walls and boxes
    # if no collision, move player and update Game's player position
    def up(self):
            walls = Game.getInstance().stage.walls
            boxes = [(b.pos[0],b.pos[1]) for b in Game.getInstance().stage.boxes]
            if (self.pos[0], self.pos[1] - 1) in walls or (self.pos[0], self.pos[1] - 1) in boxes:
                return
            self.pos[1] -= 1
            Game.getInstance().setPlayerCurrentPos(self.pos)
        
    def down(self):
            walls = Game.getInstance().stage.walls
            boxes = [(b.pos[0],b.pos[1]) for b in Game.getInstance().stage.boxes]
            if (self.pos[0], self.pos[1] + 1) in walls or (self.pos[0], self.pos[1] + 1) in boxes:
                return
            self.pos[1] += 1
            Game.getInstance().setPlayerCurrentPos(self.pos)
    
    def left(self):
            walls = Game.getInstance().stage.walls
            boxes = [(b.pos[0],b.pos[1]) for b in Game.getInstance().stage.boxes]
            if (self.pos[0]- 1, self.pos[1]) in walls or (self.pos[0]- 1, self.pos[1]) in boxes:
                return
            self.pos[0] -= 1
            Game.getInstance().setPlayerCurrentPos(self.pos)
        
    def right(self):
            walls = Game.getInstance().stage.walls
            boxes = [(b.pos[0],b.pos[1]) for b in Game.getInstance().stage.boxes]
            if (self.pos[0] + 1, self.pos[1]) in walls or (self.pos[0] + 1, self.pos[1]) in boxes:
                return
            self.pos[0] += 1
            Game.getInstance().setPlayerCurrentPos(self.pos)
    
    # drop bomb, send an dropbomb event to queue
    def action(self):
        env = pygame.event.Event(Game.getInstance().dropbomb, {"pos": self.pos})
        pygame.event.post(env)
