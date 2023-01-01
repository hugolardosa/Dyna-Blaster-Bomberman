import pygame
from spritesheet import SpriteSheet
from Common import PowerUps, PlayerState


class HeaderSprite(pygame.sprite.Sprite):
    def __init__(self, size) -> None:
        super().__init__()
        SPRITESHEET = SpriteSheet("Sprite/sprites.png")
        self.x = 0
        self.y = 0
        self.size = size
        
        banner_img_rect = (0, 148, 256, 25)
        self.banner_image = SPRITESHEET.image_at(banner_img_rect)
        self.banner_image = pygame.transform.scale(self.banner_image, (15*size, 2*size))
        
        self.image : pygame.Surface = pygame.Surface([15 * size, 2 * size])
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")
        
        self.image.blit(
            self.banner_image,
            (self.size * self.x, self.size * self.y),
        )
        

class GrassSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        SPRITESHEET = SpriteSheet("Sprite/sprites.png")
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        grass_image_rect = (367, 110, 16, 16)
        self.grass_image = SPRITESHEET.image_at(grass_image_rect)
        self.grass_image = pygame.transform.scale(self.grass_image, (size, size))
        
        self.image : pygame.Surface = pygame.Surface([size * size, size * size])
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")

        # Render Food
        self.image.blit(
            self.grass_image,
            (self.size * self.x, self.size * self.y),
        )


class WallSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        SPRITESHEET = SpriteSheet("Sprite/sprites.png")
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        wall_image_rect = (415, 110, 16, 16)
        self.wall_image = SPRITESHEET.image_at(wall_image_rect)
        self.wall_image = pygame.transform.scale(self.wall_image, (size, size))
        
        up_wall_image_rect = (447, 110, 16, 16)
        self.up_wall_image = SPRITESHEET.image_at(up_wall_image_rect)
        self.up_wall_image = pygame.transform.scale(self.up_wall_image, (size, size))
        
        down_wall_image_rect = (588, 110, 16, 16)
        self.down_wall_image = SPRITESHEET.image_at(down_wall_image_rect)
        self.down_wall_image = pygame.transform.scale(self.down_wall_image, (size, size))
        
        left_wall_image_rect = (623, 110, 16, 16)
        self.left_wall_image = SPRITESHEET.image_at(left_wall_image_rect)
        self.left_wall_image = pygame.transform.scale(self.left_wall_image, (size, size))
        
        right_wall_image_rect = (495, 110, 16, 16)
        self.right_wall_image = SPRITESHEET.image_at(right_wall_image_rect)
        self.right_wall_image = pygame.transform.scale(self.right_wall_image, (size, size))
        
        self.image : pygame.Surface = pygame.Surface([size * size, size * size])
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")
        if self.x == 0:
            self.image.blit(
                self.left_wall_image,
                (self.size * self.x, self.size * self.y),
            )
        elif self.x == 14:
            self.image.blit(
                self.right_wall_image,
                (self.size * self.x, self.size * self.y),
            )
        elif self.y == 2:
            self.image.blit(
                self.up_wall_image,
                (self.size * self.x, self.size * self.y),
            )
        elif self.y == 14:
            self.image.blit(
                self.down_wall_image,
                (self.size * self.x, self.size * self.y),
            )
        else:
            self.image.blit(
                self.wall_image,
                (self.size * self.x, self.size * self.y),
            )

class BoxSprite(pygame.sprite.Sprite):
    def __init__(self, box, size, color):
        super().__init__()
        SPRITESHEET = SpriteSheet("Sprite/sprites.png")
        self.box = box
        self.size = size
        
        # Box Item Image
        box_image_rect = (399, 110, 16, 16)
        self.box_image = SPRITESHEET.image_at(box_image_rect)
        self.box_image = pygame.transform.scale(self.box_image, (size, size))

        # Create a dictionary of powerUps
        self.powerUpDict = {
            PowerUps.NextLevel: (240, 48, 16, 16),
            PowerUps.SpeedUp: (48, 48, 16, 16),
            PowerUps.SpeedDown: (112, 48, 16, 16),
            PowerUps.FireUp: (0, 48, 16, 16),
            PowerUps.FireDown: (64, 48, 16, 16),
            PowerUps.Wallpass: (80, 48, 16, 16)
        }
        
        for key, value in self.powerUpDict.items():
            self.powerUpDict[key] = SPRITESHEET.image_at(value, -1)
            self.powerUpDict[key] = pygame.transform.scale(self.powerUpDict[key], (size, size))
        
        self.image : pygame.Surface = pygame.Surface([size * size, size * size])
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")

        # Render Food
        self.image.blit(
            self.box_image,
            (self.size * self.box.pos[0], self.size * self.box.pos[1]),
        )
        
        if self.box.opened:
            if self.box.powerUp is None:
                self.kill()
            elif self.box.powerUp is not None:
                
                self.image.fill("white")
                self.image.set_colorkey("white")
                
                self.image.blit(
                    self.powerUpDict[self.box.powerUp],
                    (self.size * self.box.pos[0], self.size * self.box.pos[1]),
                )
        if self.box.used:
            self.kill()
    
class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, enemy, size, color):
        super().__init__()
        super().__init__()
        SPRITESHEET = SpriteSheet("Sprite/sprites.png")
        self.enemy = enemy
        self.size = size
        
        self.enemyWalk = [(426, 215, 15, 18), (442, 215, 15, 18), (458, 215, 15, 18)]
        for i in range(len(self.enemyWalk)):
            self.enemyWalk[i] = SPRITESHEET.image_at(self.enemyWalk[i],-1)
            self.enemyWalk[i] = pygame.transform.scale(self.enemyWalk[i], (size, size))
        
        self.enemyDeath = [(474, 215, 15, 18), (490, 215, 15, 18), (379, 215, 15, 18), (394, 215, 15, 18), (410, 215, 15, 18)]
        for i in range(len(self.enemyDeath)):
            self.enemyDeath[i] = SPRITESHEET.image_at(self.enemyDeath[i],-1)
            self.enemyDeath[i] = pygame.transform.scale(self.enemyDeath[i], (size, size))
            
        self.image : pygame.Surface = pygame.Surface([size * size, size * size])
        self.rect = self.image.get_rect()
        
        self.count = 0
        
        self.update()
   
    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")
        
        if not self.enemy.isAlive:
            intTick = self.enemy.ticks % 5
            self.image.fill("white")
            self.image.set_colorkey("white")
            self.image.blit(
                self.enemyDeath[intTick],
                (self.size * self.enemy.pos[0], self.size * self.enemy.pos[1]),
            )
            self.count+= 1
            
            if self.count == 5:
                self.kill()
            
        else:
            # Render Food
            self.image.blit(
                self.enemyWalk[int((self.enemy.ticks / 3) % 3)],
                (self.size * self.enemy.pos[0], self.size * self.enemy.pos[1]),
            )

class BombSprite(pygame.sprite.Sprite):
    def __init__(self, bomb, size, color):
        super().__init__()
        SPRITESHEET = SpriteSheet("Sprite/sprites.png")
        self.bomb = bomb
        self.size = size
        
    
        self.bombLife = [(470, 0, 16, 16), (486, 0, 16, 16), (502, 0, 16, 16)]
        for i in range(len(self.bombLife)):
            self.bombLife[i] = SPRITESHEET.image_at(self.bombLife[i],-1)
            self.bombLife[i] = pygame.transform.scale(self.bombLife[i], (size, size))
        
        self.explode_rect = (406, 32, 16, 16)
        self.explode = SPRITESHEET.image_at(self.explode_rect,-1)
        self.explode = pygame.transform.scale(self.explode, (size, size))
        
        self.image : pygame.Surface = pygame.Surface([size * size, size * size])
        self.rect = self.image.get_rect()
        self.ticks = 0
        self.update()
        
    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")

        # Render Food
        self.image.blit(
            self.bombLife[int(self.ticks / 3 )% 3],
            (self.size * self.bomb.pos[0], self.size * self.bomb.pos[1]),
        )
        
        if self.bomb.exploded:
            for i in range(self.bomb.radius):
                self.image.blit(
                    self.explode,
                    (self.size * (self.bomb.pos[0]+i), self.size * self.bomb.pos[1]),
                )
                self.image.blit(
                    self.explode,
                    (self.size * (self.bomb.pos[0]-i), self.size * self.bomb.pos[1]),
                )
                self.image.blit(
                    self.explode,
                    (self.size * self.bomb.pos[0], self.size * (self.bomb.pos[1]+i)),
                )
                self.image.blit(
                    self.explode,
                    (self.size * self.bomb.pos[0], self.size * (self.bomb.pos[1]-i)),
                )
            
            if self.ticks % 2 == 0:
                self.kill()
        
        self.ticks += 1
class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, player, size, color):
        super().__init__()
        super().__init__()
        SPRITESHEET = SpriteSheet("Sprite/sprites.png")
        self.player = player
        self.size = size
        
        self.playerUp = [(242,0,18,22),(268,0,18,22)]
        self.playerDown = [(28,0,18,22),(50,0,18,22)]
        self.playerLeft = [(169,0,18,22),(193,0,18,22)]
        self.playerRight = [(98,0,18,22),(121,0,18,22)]
        for i in range(2):
            self.playerUp[i] = SPRITESHEET.image_at(self.playerUp[i],-1)
            self.playerUp[i] = pygame.transform.scale(self.playerUp[i], (size, size))
            self.playerDown[i] = SPRITESHEET.image_at(self.playerDown[i],-1)
            self.playerDown[i] = pygame.transform.scale(self.playerDown[i], (size, size))
            self.playerLeft[i] = SPRITESHEET.image_at(self.playerLeft[i],-1)
            self.playerLeft[i] = pygame.transform.scale(self.playerLeft[i], (size, size))
            self.playerRight[i] = SPRITESHEET.image_at(self.playerRight[i],-1)
            self.playerRight[i] = pygame.transform.scale(self.playerRight[i], (size, size))
    
        
        self.playerIdle_rect = (3,0,18,22)
        self.playerIdle = SPRITESHEET.image_at(self.playerIdle_rect,-1)
        self.playerIdle = pygame.transform.scale(self.playerIdle, (size, size))
        
        
        self.image : pygame.Surface = pygame.Surface([size * size, size * size])
        self.rect = self.image.get_rect()
        self.update()
   
    def update(self):
        if not self.player.isAlive:
            self.kill()
            
        self.image.fill("white")
        self.image.set_colorkey("white")
        if self.player.state == PlayerState.UP:
            self.image.blit(
                self.playerUp[int((self.player.ticks / 2) % 2)],
                (self.size * self.player.pos[0], self.size * self.player.pos[1]),
            )
        elif self.player.state == PlayerState.LEFT:
            self.image.blit(
                self.playerLeft[int((self.player.ticks / 2) % 2)],
                (self.size * self.player.pos[0], self.size * self.player.pos[1]),
            )
        elif self.player.state == PlayerState.DOWN:
            self.image.blit(
                self.playerDown[int((self.player.ticks / 2) % 2)],
                (self.size * self.player.pos[0], self.size * self.player.pos[1]),
            )
        elif self.player.state == PlayerState.RIGHT:
            self.image.blit(
                self.playerRight[int((self.player.ticks / 2) % 2)],
                (self.size * self.player.pos[0], self.size * self.player.pos[1]),
            )
        else:
            self.image.blit(
                self.playerIdle,
                (self.size * self.player.pos[0], self.size * self.player.pos[1]),
            )
