import pygame
from spritesheet import SpriteSheet
from Common import PowerUps


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
        
        self.image = pygame.Surface([size * size, size * size])
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
        
        self.image = pygame.Surface([size * size, size * size])
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")

        # Render Food
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
        
        self.image = pygame.Surface([size * size, size * size])
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
        
        enemy_image_rect = (426, 215, 15, 18)
        self.enemy_image = SPRITESHEET.image_at(enemy_image_rect, -1)
        self.enemy_image = pygame.transform.scale(self.enemy_image, (size, size))

        self.image = pygame.Surface([size * size, size * size])
        self.rect = self.image.get_rect()
        self.update()
   
    def update(self):
        if not self.enemy.isAlive:
            self.kill()
        self.image.fill("white")
        self.image.set_colorkey("white")

        # Render Food
        self.image.blit(
            self.enemy_image,
            (self.size * self.enemy.pos[0], self.size * self.enemy.pos[1]),
        )

class BombSprite(pygame.sprite.Sprite):
    def __init__(self, bomb, size, color):
        super().__init__()
        SPRITESHEET = SpriteSheet("Sprite/sprites.png")
        self.bomb = bomb
        self.size = size
        
        bomb_image_rect = (470, 0, 16, 16)
        self.bomb_image = SPRITESHEET.image_at(bomb_image_rect, -1)
        self.bomb_image = pygame.transform.scale(self.bomb_image, (size, size))

        self.image = pygame.Surface([size * size, size * size])
        self.rect = self.image.get_rect()
        self.update()
        
    def draw(self, display):
        display.fill(self.color, (self.x, self.y, self.width, self.height))
        
    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")

        # Render Food
        self.image.blit(
            self.bomb_image,
            (self.size * self.bomb.pos[0], self.size * self.bomb.pos[1]),
        )
        
        if self.bomb.exploded:
            self.kill()
            
class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, player, size, color):
        super().__init__()
        super().__init__()
        SPRITESHEET = SpriteSheet("Sprite/sprites.png")
        self.player = player
        self.size = size
        
        player_image_rect = (0, 0, 19, 19)
        self.player_image = SPRITESHEET.image_at(player_image_rect, -1)
        self.player_image = pygame.transform.scale(self.player_image, (size, size))

        self.image = pygame.Surface([size * size, size * size])
        self.rect = self.image.get_rect()
        self.update()
   
    def update(self):
        if not self.player.isAlive:
            self.kill()
        self.image.fill("white")
        self.image.set_colorkey("white")

        # Render Food
        self.image.blit(
            self.player_image,
            (self.size * self.player.pos[0], self.size * self.player.pos[1]),
        )

