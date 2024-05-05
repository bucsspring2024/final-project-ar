import pygame

class EndScreen:
    def __init__(self, width, height, score, egg):
        self.width = width
        self.height = height
        self.score = score
        self.egg = egg
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Fill the screen with black color
        score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        egg_text = self.font.render("Eggs: " + str(self.egg), True, (255, 255, 255))
        retry_text = self.font.render("Nice Try! Press Space to try again!", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(self.width // 2, self.height // 3))
        egg_rect = egg_text.get_rect(center=(self.width // 2, self.height // 4))
        retry_rect = retry_text.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(score_text, score_rect)
        screen.blit(egg_text, egg_rect)
        screen.blit(retry_text, retry_rect)
