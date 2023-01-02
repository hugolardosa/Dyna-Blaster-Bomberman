import pygame
from pygame.mixer import music, Sound

from Command import InputHandler
from Game import Game

from SpriteHandler import SpriteHandler
import random

from GameScreen import renderGameWonScreen, renderGameLostScreen

pygame.init()
pygame.font.init()
pygame.mixer.init()

game = Game() # Initialize Game singleton

display = pygame.display.set_mode((game.scale * game.width, game.scale * game.height))
pygame.display.set_caption('Dyna Blaster')
clock = pygame.time.Clock()

running = True

sprtHandler = SpriteHandler()
sprtHandler.loadSprites(game)
music.load("Music/05_BGM1.mp3")
music.play(-1)

gameWon = False
gameLost = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if gameWon:
                running = False
            if gameLost:
                if event.key == pygame.K_RETURN:
                    running = False
                else:
                    gameLost = False
                    music.load(random.choice(["Music/05_BGM1.mp3", "Music/06_BGM2.mp3", "Music/07_BGM3.mp3"]))
                    music.play(-1)
            InputHandler().handleInput(event, game.player, 
                                        {pygame.K_SPACE: 'action'})
        elif event.type == game.dropbomb:
            x,y = game.player.pos
            game.addBomb([x,y])
            sprtHandler.addBomb(game.bombs[-1], game)
            
        elif event.type == game.playerdead:
            music.stop()
            Sound("Music/oh-no.mp3").play()
            music.load("Music/16_Game Over.mp3")
            music.play()
            gameLost = True
            
        elif event.type == game.nextstage:
            print("Next Stage")
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
        elif event.type == game.gamewon:
            gameWon = True
            music.stop()
            Sound("Music/18_VS Victory.mp3").play()
    
    if gameWon:
        renderGameWonScreen(display)
        pygame.display.update()
        continue
    
    if gameLost:
        renderGameLostScreen(display)
        pygame.display.update()
        continue
    
    
        
    display.fill("black")
    
    sprtHandler.drawSprites(display)
    game.scoreboard.draw(display)
    game.timer.draw(display)
    
    state = pygame.key.get_pressed()
    if state[pygame.K_UP]:
        game.player.up()
    elif state[pygame.K_DOWN]:
        game.player.down()
    elif state[pygame.K_LEFT]:
        game.player.left()
    elif state[pygame.K_RIGHT]:
        game.player.right()
    else:
        game.player.idle()
        
    game.tick()


    pygame.display.update()
    clock.tick(60)

pygame.quit()