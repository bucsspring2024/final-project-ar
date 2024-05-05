import pygame

class MainMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.title_font = pygame.font.Font(None, 64)
        self.option_font = pygame.font.Font(None, 36)

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Fill the screen with black color
        title_text = self.title_font.render("Chicken Run!", True, (255, 255, 255))
        option_text = self.option_font.render("Press Space to start! Collect your eggs and avoid farmers!", True, (255, 255, 255))
        instruction_text = self.option_font.render("Tip: Jump super close to the farmers but don't let them hit you!", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.width // 2, self.height // 3))
        option_rect = option_text.get_rect(center=(self.width // 2, self.height // 2))
        instruction_rect = instruction_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
        screen.blit(title_text, title_rect)
        screen.blit(option_text, option_rect)
        screen.blit(instruction_text, instruction_rect)
