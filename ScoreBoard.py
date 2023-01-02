from pygame.font import *
from observer import Observer

class ScoreBoard(Observer):
    def __init__(self) -> None:
        self.score = 0
        self.font = SysFont("Arial", 24)
       
    def on_notify(self):
        self.score += 100
    
    def draw(self,display):
        img = self.font.render(f"{self.score}", True, "white")
        display.blit(img, (50, 20))
        