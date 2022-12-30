import pygame
from pygame.mixer import music, Sound

from Command import InputHandler
from Game import Game

from SpriteHandler import SpriteHandler
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

game = Game() # Initialize Game singleton

display = pygame.display.set_mode((game.scale * game.width, game.scale * game.height))

clock = pygame.time.Clock()

running = True

sprtHandler = SpriteHandler()
sprtHandler.loadSprites(game)
music.load("Music/05_BGM1.mp3")
music.play(-1)



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
            Sound("Music/oh-no.mp3").play()
            print("Player Dead")
            
        elif event.type == game.nextstage:
            music.stop()
            Sound("Music/10_Stage Clear.mp3").play()
            sprtHandler.clearSprites()
            game.loadNextStage()
            sprtHandler.loadSprites(game)
            print("Next Stage")
            music.load(random.choice(["Music/05_BGM1.mp3", "Music/06_BGM2.mp3", "Music/07_BGM3.mp3"]))
            music.play(-1)
        elif event.type == game.exploding:
            Sound("Music/explosion.mp3").play()
            print("Bomb Exploding")
            
    display.fill("black")
    
    sprtHandler.drawSprites(display)
    
    
    state = pygame.key.get_pressed()
    if state[pygame.K_UP]:
        game.player.up()
    elif state[pygame.K_DOWN]:
        game.player.down()
    elif state[pygame.K_LEFT]:
        game.player.left()
    elif state[pygame.K_RIGHT]:
        game.player.right()

        
    game.tick()


    pygame.display.update()
    clock.tick(60)

pygame.quit()