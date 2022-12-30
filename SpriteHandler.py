import pygame
from Sprites import WallSprite, BoxSprite, EnemySprite, BombSprite, PlayerSprite

class SpriteHandler:
    def __init__(self) -> None:
        self.wallSprites = pygame.sprite.Group()
        self.collisionSprites = pygame.sprite.Group()
        self.bombSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()
    
    def loadSprites(self, game):  
        for wall in game.stage.walls:
            self.wallSprites.add(WallSprite(wall[0], wall[1], game.scale, "white"))
        for box in game.boxes: 
            self.collisionSprites.add(BoxSprite(box, game.scale, "brown"))

        for enemy in game.enemies:
            self.enemySprites.add(EnemySprite(enemy, game.scale, "blue"))
        
        self.playerSprites.add(PlayerSprite(game.player, game.scale, "red"))
 
    def addBomb(self, bomb, game):
        self.bombSprites.add(BombSprite(bomb, game.scale, "yellow"))
        
    def clearSprites(self):
        self.wallSprites.empty()
        self.collisionSprites.empty()
        self.bombSprites.empty()
        self.playerSprites.empty()
        self.enemySprites.empty()

    def drawSprites(self, display):    
        self.wallSprites.draw(display)
        
        self.collisionSprites.draw(display)
        self.collisionSprites.update()
        
        self.enemySprites.draw(display)
        self.enemySprites.update()
        
        self.bombSprites.draw(display)
        self.bombSprites.update()
        
        self.playerSprites.draw(display)
        self.playerSprites.update()