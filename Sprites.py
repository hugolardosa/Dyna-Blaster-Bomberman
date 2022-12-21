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