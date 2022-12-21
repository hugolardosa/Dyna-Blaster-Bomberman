from pygame import *
import pygame
from pygame.font import Font
from pygame.sprite import *
from pygame.mixer import *
from Bomb import Bomb

from Player import Player 
from Command import InputHandler
from Game import Game

from Sprites import WallSprite, BoxSprite

pygame.init()
pygame.font.init()
pygame.mixer.init()

Game() # Initialize Game singleton

display = pygame.display.set_mode((Game.getInstance().scale * Game.getInstance().width, Game.getInstance().scale * Game.getInstance().height))

clock = pygame.time.Clock()

player = Player()

running = True

wall_sprites = pygame.sprite.Group()

collision_sprites = pygame.sprite.Group()
for wall in Game.getInstance().stage.walls:
    wall_sprites.add(WallSprite(wall[0] * Game.getInstance().scale, wall[1] * Game.getInstance().scale, Game.getInstance().scale, "white"))
for box in Game.getInstance().stage.boxes:  
    collision_sprites.add(BoxSprite(box.pos[0] * Game.getInstance().scale, box.pos[1] * Game.getInstance().scale, Game.getInstance().scale, "brown"))
    
# music.load("Music/05_BGM1.mp3")
# music.play(-1)

bomb_flag = False
bomb_count = 0
dbomb = None

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
            for sp in collision_sprites:
                if (sp.x  == event.box.pos[0]* Game.getInstance().scale) and (sp.y  == event.box.pos[1] * Game.getInstance().scale):
                    collision_sprites.remove(sp)
                    break
            print(f"Box dropped - {event.box.pos}")
            
        elif event.type == Game.getInstance().playerdead:
            print("Player died")
        
           
    display.fill("black")
    player.draw(display)
    
    wall_sprites.draw(display)
    
    collision_sprites.draw(display)
    collision_sprites.update()
    
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
    clock.tick(15)

pygame.quit()