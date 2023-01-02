from pygame.font import *

def renderGameWonScreen(display):
    display.fill("black")
    
    font1 = Font("Fonts/BOMBERMA.TTF", 50)
    won = font1.render(f"Game Won!", True, "yellow")
    display.blit(won, (20, 20))
    
    font2 = Font("Fonts/BOMBERMA.TTF", 20)
    key = font2.render(f"Press any key to exit", True, "white")
    display.blit(key, (20, 90))
    
def renderGameLostScreen(display):
    display.fill("black")
    
    font1 = Font("Fonts/BOMBERMA.TTF", 50)
    lost = font1.render(f"Game Lost!", True, "yellow")
    display.blit(lost, (20, 20))
    
    font2 = Font("Fonts/BOMBERMA.TTF", 20)
    
    key = font2.render(f"Press enter to exit", True, "white")
    display.blit(key, (20, 90))
    
    key = font2.render(f"Press any other key to continue", True, "white")
    display.blit(key, (20, 140))