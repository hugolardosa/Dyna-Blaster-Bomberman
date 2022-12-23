from typing import List

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class Enemy:
    def __init__(self, name, staringPos, endingPos, stage, playerCurrentPos):
        self.pos = staringPos
        self.speed = 10
        self.stage = stage
        self.startingPos = staringPos
        self.endPos = endingPos
        self.name = name
        self.alive = True
        self.ticks = 0
        self.damage = 1
        self.lastIndex = -1
        self.path = []
        self.intelligent = False
        self.playerCurrentPos = playerCurrentPos
        self.calculatePath()
        print(self.path)

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
        if self.pos != self.path[-1]:
            index = self.lastIndex + 1
            self.pos = self.path[index]
            self.lastIndex = index
        else:
            self.lastIndex = -1
            self.calculatePath()
            
        
            
             
    # A Star Pathfinding 
    def calculatePath(self):
        # Get Corrent Game grid
        matrix = self.stage.getGameMatrix()

        grid = Grid(matrix=matrix)
        
        if self.pos == self.startingPos:
            # Get starting and ending positions
            start = grid.node(self.startingPos[0], self.startingPos[1])
            end = grid.node(self.endPos[0], self.endPos[1]) if not self.intelligent else grid.node(self.playerCurrentPos[0], self.playerCurrentPos[1])
            
        else:
            start = grid.node(self.endPos[0], self.endPos[1]) if not self.intelligent else grid.node(self.playerCurrentPos[0], self.playerCurrentPos[1])
            end = grid.node(self.startingPos[0], self.startingPos[1])
            
        finder = AStarFinder()
        
        path, runs = finder.find_path(start, end, grid)
        
        self.path = path