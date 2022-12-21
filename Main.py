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

from Sprites import WallSprite, BoxSprite, EnemySprite

pygame.init()
pygame.font.init()
pygame.mixer.init()

Game() # Initialize Game singleton

display = pygame.display.set_mode((Game.getInstance().scale * Game.getInstance().width, Game.getInstance().scale * Game.getInstance().height))

clock = pygame.time.Clock()

player = Player()
enemy = Enemy("Marco", [7,11], [11, 7], 1, 1 )

running = True

wallSprites = pygame.sprite.Group()

collisionSprites = pygame.sprite.Group()
for wall in Game.getInstance().stage.walls:
    wallSprites.add(WallSprite(wall[0] * Game.getInstance().scale, wall[1] * Game.getInstance().scale, Game.getInstance().scale, "white"))
for box in Game.getInstance().stage.boxes:  
    collisionSprites.add(BoxSprite(box, Game.getInstance().scale, "brown"))

enemySprites = pygame.sprite.Group()
enemySprites.add(EnemySprite(enemy, Game.getInstance().scale, "blue"))
 
# music.load("Music/05_BGM1.mp3")
# music.play(-1)

bomb_flag = False
bomb_count = 0
dbomb = None

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
        elif event.type == Game.getInstance().dropbomb:
            if bomb_flag:
                continue
            x,y = event.pos
            bomb_flag = True
            bomb = Bomb([x,y], 40)
            
        elif event.type == Game.getInstance().boxdrop:
            Game.getInstance().stage.boxes.remove(event.box)
            for sp in collisionSprites:
                if sp.box == event.box:
                    collisionSprites.remove(sp)
                    break
            print(f"Box dropped - {event.box.pos}")
            
        elif event.type == Game.getInstance().playerdead:
            print("Player died")
        
    print(player.pos)       
    display.fill("black")
    player.draw(display)
    
    wallSprites.draw(display)
    
    collisionSprites.draw(display)
    collisionSprites.update()
    
    enemySprites.draw(display)
    enemySprites.update()
    enemy.move()
    
    state = pygame.key.get_pressed()
    if state[pygame.K_w]:
        player.up()
    elif state[pygame.K_s]:
        player.down()
    elif state[pygame.K_a]:
        player.left()
    elif state[pygame.K_d]:
        player.right()
        
    if bomb_flag:
        bomb_count += 1
        bomb.draw(display)
        if bomb_count == bomb.time:
            bomb.explode()
            bomb = None
            bomb_flag  = False
            bomb_count = 0

    pygame.display.update()
    clock.tick(30)

pygame.quit()