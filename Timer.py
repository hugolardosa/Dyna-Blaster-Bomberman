from pygame.font import *

class Timer():
    def __init__(self) -> None:
        self.time = 240
        self.countTicks = 0
        self.font = SysFont("Arial", 24)
    
    def draw(self,display):
        seconds = self.time % (24 * 3600)
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60 
        imgMin = self.font.render(f"{minutes}", True, "white")
        display.blit(imgMin, (225, 20))
        imgSec = self.font.render(f"{seconds:02d}", True, "white")
        display.blit(imgSec, (255, 20))
    
    def reset_timer(self):
        self.time = 240
    
    def tick(self):
        if self.countTicks < 60:
            self.countTicks += 1
        else:
            self.time -= 1
            self.countTicks = 0
            
        # Safe Keep - if time is less than 0, reset it to 240
        if self.time < 0:
            self.time = 240
            
    def timesUp(self):
        return self.time <= 0
    