import pygame

class WallSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.width = size
        self.height = size
        self.x = x
        self.y = y
        
    def draw(self, display):
        display.fill(self.color, (self.x, self.y, self.width, self.height))
        
    def update(self):
        pass

class BoxSprite(pygame.sprite.Sprite):
    def __init__(self, box, size, color):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = box.pos[0] * size
        self.rect.y = box.pos[1] * size
        self.color = color
        self.width = size
        self.height = size
        self.x = box.pos[0]
        self.y = box.pos[1]
        self.box = box
        
    def draw(self, display):
        display.fill(self.color, (self.x, self.y, self.width, self.height))
        
    def update(self):
        pass
    
class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, enemy, size, color):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = enemy.pos[0] * size
        self.rect.y = enemy.pos[1] * size
        self.color = color
        self.width = size
        self.height = size
        self.x = enemy.pos[0] * size
        self.y = enemy.pos[1] * size
        self.enemy = enemy
        
    def draw(self, display):
        display.fill(self.color, (self.x, self.y, self.width, self.height))
        
    def update(self):
        self.rect.x = self.enemy.pos[0] * self.width
        self.rect.y = self.enemy.pos[1] * self.width
        self.x = self.enemy.pos[0] * self.width
        self.y = self.enemy.pos[1] * self.width
