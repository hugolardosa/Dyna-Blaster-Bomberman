import pygame
import time 


class Bomb:
    def __init__(self, pos, time) -> None:
        self.pos = pos
        self.time = time
        self.radius = 5
        self.damage = 1
        self.timePassed = 0
        self.exploded = False
        

   
    def tick(self):
        if self.timePassed < self.time:
            self.timePassed += 1  
            
    