import pygame
class Egg(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, speed):
        super().__init__()
        self.radius = radius
        self.color = (255, 255, 255)  # Yellow color
        self.rect = pygame.Rect(x - radius, y - radius, 2 * radius, 2 * radius)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
