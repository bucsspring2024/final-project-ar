import pygame

class Chicken(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, screen_height):
        super().__init__()
        self.image = pygame.image.load("assets/chicken.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vel_y = 0
        self.is_jump = False
        self.screen_height = screen_height

    def jump(self, jump_height, gravity):
        if not self.is_jump:
            self.vel_y = -jump_height
            self.is_jump = True

    def update(self, ground_height):
        self.vel_y += ground_height
        self.rect.y += self.vel_y
        if self.rect.bottom >= self.screen_height - ground_height:
            self.rect.bottom = self.screen_height - ground_height
            self.vel_y = 0
            self.is_jump = False

    def reset(self, ground_height):
        self.rect.x = 50
        self.rect.y = self.screen_height - ground_height - self.rect.height