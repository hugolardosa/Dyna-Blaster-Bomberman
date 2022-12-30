import pygame


from Command import InputHandler
from Game import Game

from SpriteHandler import SpriteHandler


pygame.init()
pygame.font.init()
pygame.mixer.init()

game = Game() # Initialize Game singleton

display = pygame.display.set_mode((game.scale * game.width, game.scale * game.height))

clock = pygame.time.Clock()

running = True

sprtHandler = SpriteHandler()
sprtHandler.loadSprites(game)
# music.load("Music/05_BGM1.mp3")
# music.play(-1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            InputHandler().handleInput(event, game.player, 
                                        {pygame.K_SPACE: 'action'})
        elif event.type == game.dropbomb:
            x,y = game.player.pos
            game.addBomb([x,y])
            sprtHandler.addBomb(game.bombs[-1], game)
            
        elif event.type == game.playerdead:
            game.player.takeDamage()
            print("Player Dead")
            
        elif event.type == game.nextstage:
            sprtHandler.clearSprites()
            game.loadNextStage()
            sprtHandler.loadSprites(game)
            print("Next Stage")
            
            
    display.fill("black")
    
    sprtHandler.drawSprites(display)
    
    
    state = pygame.key.get_pressed()
    if state[pygame.K_w]:
        game.player.up()
    elif state[pygame.K_s]:
        game.player.down()
    elif state[pygame.K_a]:
        game.player.left()
    elif state[pygame.K_d]:
        game.player.right()
        
    game.tick()


    pygame.display.update()
    clock.tick(30)

pygame.quit()