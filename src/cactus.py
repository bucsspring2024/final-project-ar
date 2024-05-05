import pygame
class Cactus(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
