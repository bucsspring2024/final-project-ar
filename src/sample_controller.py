import pygame
import random
import sys
from dino import Dino
from cactus import Cactus

# Constants
WIDTH, HEIGHT = 600, 200
GROUND_HEIGHT = 20
WHITE = (255, 255, 255)
FPS = 60

# Dino parameters
DINO_WIDTH, DINO_HEIGHT = 40, 40
DINO_X = 50
DINO_Y = HEIGHT - GROUND_HEIGHT - DINO_HEIGHT
DINO_JUMP_HEIGHT = 80
DINO_GRAVITY = 5

# Cactus parameters
CACTUS_WIDTH, CACTUS_HEIGHT = 20, 40
CACTUS_X = WIDTH + 50
MIN_CACTUS_GAP = 200
MAX_CACTUS_GAP = 300
CACTUS_SPEED = 5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")
clock = pygame.time.Clock()

# Load images
dino_img = pygame.image.load("assets/piggy.png").convert_alpha()
dino_img = pygame.transform.scale(dino_img, (DINO_WIDTH, DINO_HEIGHT))

# Groups
all_sprites = pygame.sprite.Group()
cactus_group = pygame.sprite.Group()
dino = Dino(DINO_WIDTH, DINO_HEIGHT, DINO_X, DINO_Y, HEIGHT)
all_sprites.add(dino)

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump(DINO_JUMP_HEIGHT, DINO_GRAVITY)

        # Spawning cactus
        if len(cactus_group) < 2:
            if len(cactus_group) == 0 or cactus_group.sprites()[-1].rect.right < WIDTH - random.randint(MIN_CACTUS_GAP, MAX_CACTUS_GAP):
                cactus = Cactus(CACTUS_WIDTH, CACTUS_HEIGHT, WIDTH, HEIGHT - GROUND_HEIGHT - CACTUS_HEIGHT, CACTUS_SPEED)
                cactus_group.add(cactus)
                all_sprites.add(cactus)

        # Update
        all_sprites.update()

        # Collision check
        if pygame.sprite.spritecollide(dino, cactus_group, False):
            pygame.quit()
            sys.exit()

        # Draw
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
