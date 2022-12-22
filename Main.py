from pygame import *
import pygame
from pygame.font import Font
from pygame.sprite import *
from pygame.mixer import *
from Bomb import Bomb

from Player import Player
from Enemy import Enemy 
from Command import InputHandler
from Game import Game

from Sprites import WallSprite, BoxSprite, EnemySprite, BombSprite, PlayerSprite

pygame.init()
pygame.font.init()
pygame.mixer.init()

game = Game() # Initialize Game singleton

display = pygame.display.set_mode((game.scale * game.width, game.scale * game.height))

clock = pygame.time.Clock()

player = Player()


running = True

wallSprites = pygame.sprite.Group()

collisionSprites = pygame.sprite.Group()
for wall in game.stage.walls:
    wallSprites.add(WallSprite(wall[0], wall[1], game.scale, "white"))
for box in game.stage.boxes:  
    collisionSprites.add(BoxSprite(box, game.scale, "brown"))

enemySprites = pygame.sprite.Group()
enemySprites.add(EnemySprite(game.stage.enemies[0], game.scale, "blue"))
 
bombSprites = pygame.sprite.Group()

playerSprites = pygame.sprite.Group()
playerSprites.add(PlayerSprite(player, game.scale, "red"))
 
music.load("Music/05_BGM1.mp3")
music.play(-1)



inputDict = {
                pygame.K_SPACE: 'action'
            }

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            InputHandler().handleInput(event, player, 
                                        {pygame.K_SPACE: 'action'})
        elif event.type == game.dropbomb:
            x,y = player.pos
            game.bombs.append(Bomb([x,y], 40))
            bombSprites.add(BombSprite(game.bombs[-1], game.scale, "yellow"))
            
        elif event.type == game.playerdead:
            player.takeDamage()
            
      
    display.fill("olive")
    
    
    wallSprites.draw(display)
    
    collisionSprites.draw(display)
    collisionSprites.update()
    
    enemySprites.draw(display)
    enemySprites.update()
    
    bombSprites.draw(display)
    bombSprites.update()
    
    playerSprites.draw(display)
    playerSprites.update()
    
    state = pygame.key.get_pressed()
    if state[pygame.K_w]:
        player.up()
    elif state[pygame.K_s]:
        player.down()
    elif state[pygame.K_a]:
        player.left()
    elif state[pygame.K_d]:
        player.right()
        
    game.tick()


    pygame.display.update()
    clock.tick(30)

pygame.quit()