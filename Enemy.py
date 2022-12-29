from typing import List
from Common import Direction

# from pathfinding.core.grid import Grid
# from pathfinding.finder.a_star import AStarFinder

class Enemy:
    def __init__(self, id, staringPos, player, walls, boxes, bombs, enemies):
        self.pos = staringPos
        self.speed = 10
        
        self.startingPos = staringPos
        self.id = id
        self.alive = True
        self.ticks = 0
        #self.damage = 1
        #self.lastIndex = -1

        # self.path = []
        
        self.player = player
        self.walls = walls
        self.boxes = boxes
        self.bombs = bombs
        self.enemies = enemies
        
        self.intelligent = False
        
        self.lastPos = [0,0]
        self.direction = Direction.RIGHT
        self.directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]

    def kill(self):
        self.alive = False
    
    @property
    def isAlive(self):
        return self.alive

    def tick(self):
        if self.ticks < self.speed:
            self.ticks += 1
        else:
            self.ticks = 0
            self.move()
            
    def move(self):
        self.getNextPos()
    
    def getNextPos(self):
        
        walls = self.walls
        boxes = [b.pos for b in self.boxes if not b.isOpened]
        bombs =  [b.pos for b in self.bombs]
        enemies = [e.pos for e in self.enemies if e.id != self.id]
        
        
        new_pos = [self.pos[0], self.pos[1]]
        
        if self.direction == Direction.RIGHT:
            possiblePos = [self.pos[0]+1, self.pos[1]]
            if possiblePos not in walls and possiblePos not in boxes and possiblePos not in bombs and possiblePos not in enemies:
                new_pos[0] += 1
            else:
                self.direction = self.directions[(self.direction.value + 1) % len(self.directions)]
        elif self.direction == Direction.LEFT:
            possiblePos = [self.pos[0]-1, self.pos[1]]
            if possiblePos not in walls and possiblePos not in boxes and possiblePos not in bombs and possiblePos not in enemies:
                new_pos[0] -= 1
            else:
                self.direction = self.directions[(self.direction.value + 1) % len(self.directions)]
        elif self.direction == Direction.UP:
            possiblePos = [self.pos[0], self.pos[1]-1]
            if possiblePos not in walls and possiblePos not in boxes and possiblePos not in bombs and possiblePos not in enemies:
                new_pos[1]-=1
            else:
                self.direction = self.directions[(self.direction.value + 1) % len(self.directions)]
        elif self.direction == Direction.DOWN:
            possiblePos = [self.pos[0], self.pos[1]+1]
            if possiblePos not in walls and possiblePos not in boxes and possiblePos not in bombs and possiblePos not in enemies:
                new_pos[1] += 1
            else:
                self.direction = self.directions[(self.direction.value + 1) % len(self.directions)] 
            
        self.lastPos = self.pos
        self.pos = new_pos
        
            
             
    # # A Star Pathfinding 
    # def calculatePath(self):
    #     # Get Corrent Game grid
    #     matrix = self.stage.getGameMatrix()

    #     grid = Grid(matrix=matrix)
        
    #     if self.pos == self.startingPos:
    #         # Get starting and ending positions
    #         start = grid.node(self.startingPos[0], self.startingPos[1])
    #         end = grid.node(self.endPos[0], self.endPos[1]) if not self.intelligent else grid.node(self.playerCurrentPos[0], self.playerCurrentPos[1])
            
    #     else:
    #         start = grid.node(self.endPos[0], self.endPos[1]) if not self.intelligent else grid.node(self.playerCurrentPos[0], self.playerCurrentPos[1])
    #         end = grid.node(self.startingPos[0], self.startingPos[1])
            
    #     finder = AStarFinder()
        
    #     path, runs = finder.find_path(start, end, grid)
        
    #     self.path = path