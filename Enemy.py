from typing import List
class Enemy:
    def __init__(self, name, staringPos, endingPos, hp, damage):
        self.pos = staringPos
        self.speed = 10
        self.startingPos = staringPos
        self.endPos = endingPos
        self.name = name
        self.alive = True
        self.ticks = 0
        self.damage = damage
        self.lastIndex = -1
        self.path = []
        self.calculatePath()

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
        index = self.lastIndex + 1 if self.lastIndex < len(self.path) - 1 else 0 #TODO: GO BACK TO STARTING POS
        self.pos = self.path[index]
        self.lastIndex = index

    def calculatePath(self):
        self.path = [[7, 11], [8, 11], [9, 11], [10, 11], [11, 11] , [11, 10], [11, 9], [11, 8], [11, 7]]
        
        