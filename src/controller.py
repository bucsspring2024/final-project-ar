import pygame
import random
import sys
from src.chicken import Chicken
from src.farmer import Farmer
from src.mainmenu import MainMenu
from src.score import Score
from src.egg import Egg
from src.endscreen import EndScreen

class Controller:
    def __init__(self):
        # Constants
        self.width, self.height = 1200, 600
        self.ground_height = 20
        self.blue = (0, 200, 255)
        self.fps = 60

        # Chicken parameters
        self.chicken_width, self.chicken_height = 75, 75
        self.chicken_x = 50
        self.chicken_y = self.height - self.ground_height - self.chicken_height
        self.chicken_jump_height = 300
        self.chicken_gravity = 2

        # Farmer parameters
        self.farmer_width, self.farmer_height = 50, 110
        self.min_farmer_gap = 200
        self.max_farmer_gap = 300
        self.farmer_speed = 5

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Chicken Run")
        self.clock = pygame.time.Clock()

        # Load images
        self.chicken_img = pygame.image.load("assets/chicken.png").convert_alpha()
        self.chicken_img = pygame.transform.scale(self.chicken_img, (self.chicken_width, self.chicken_height))

        # Main menu
        self.main_menu = MainMenu(self.width, self.height)

        # Score
        self.score = Score()

        # Chicken
        self.chicken = Chicken(self.chicken_width, self.chicken_height, self.chicken_x, self.chicken_y, self.height)

        # Farmers
        self.farmers = []

        # Eggs
        self.eggs = pygame.sprite.Group()

    def spawn_farmer(self):
        if len(self.farmers) < 2:
            if len(self.farmers) == 0 or self.farmers[-1].rect.right < self.width - random.randint(self.min_farmer_gap, self.max_farmer_gap):
                farmer = Farmer("assets/farmer.png", self.farmer_width, self.farmer_height, self.width, self.height - self.ground_height - self.farmer_height, self.farmer_speed)
                self.farmers.append(farmer)

    def spawn_eggs(self):
        if random.randint(0, 100) < 5:  
            egg = Egg(10, self.width, random.randint(50, self.height - 50), 5)  
            self.eggs.add(egg)

    def update(self):
        self.chicken.update(self.ground_height)
        for farmer in self.farmers:
            farmer.update()
        self.eggs.update()

        # Check for egg collection
        collected_eggs = pygame.sprite.spritecollide(self.chicken, self.eggs, True)
        for egg in collected_eggs:
            self.score.increase_eggs()

        # Increase score if farmer passed
        for farmer in self.farmers:
            if farmer.rect.right < 0:
                self.score.increase_score()
                self.farmers.remove(farmer)

        # Collision check
        for farmer in self.farmers:
            if pygame.Rect.colliderect(self.chicken.rect, farmer.rect):
                end_screen = EndScreen(self.width, self.height, self.score.get_score(), self.score.get_eggs())
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                self.start()  # Restart game

                    end_screen.draw(self.screen)
                    pygame.display.flip()
                    self.clock.tick(self.fps)

    def draw(self):
        self.screen.fill(self.blue)
        self.screen.blit(self.chicken.image, self.chicken.rect)
        for farmer in self.farmers:
            self.screen.blit(farmer.image, farmer.rect)
        for egg in self.eggs:
            egg.draw(self.screen)

        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(self.score.get_score()), True, (0, 0, 0))
        eggs_text = font.render("Eggs: " + str(self.score.get_eggs()), True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(eggs_text, (10, 40))

        pygame.display.flip()

    def start(self):
        while True:
            in_main_menu = True
            while in_main_menu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            in_main_menu = False

                self.main_menu.draw(self.screen)
                pygame.display.flip()
                self.clock.tick(self.fps)

            self.score = Score()  # Reset score
            self.chicken.reset(50)  # Reset chicken position
            self.farmers.clear()  # Clear existing farmers
            self.eggs.empty()  # Remove existing eggs

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.chicken.jump(self.chicken_jump_height, self.chicken_gravity)

                self.spawn_farmer()
                self.spawn_eggs()
                self.update()
                self.draw()
                self.clock.tick(self.fps)

