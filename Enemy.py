from typing import List
class Enemy:
    def __init__(self, name, staringPos, endingPos, hp, damage):
        self.pos = staringPos
        self.startingPos = staringPos
        self.endPos = endingPos
        self.name = name
        self.hp = hp
        self.damage = damage
        self.lastIndex = -1
        self.path = []
        self.calculatePath()

    def is_alive(self):
        return self.hp > 0

    def move(self):
        index = self.lastIndex + 1 if self.lastIndex < len(self.path) - 1 else 0 #TODO: GO BACK TO STARTING POS
        self.pos = self.path[index]
        self.lastIndex = index

    def calculatePath(self):
        self.path = [[7, 11], [8, 11], [9, 11], [10, 11], [11, 11] , [11, 10], [11, 9], [11, 8], [11, 7]]
        
        