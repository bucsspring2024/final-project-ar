import pygame
import sys
pygame.init()

window_width = 1200
window_height = 600
fps = 20
blue = (0, 150, 255)
green = (0, 255, 0)
add_new_flame_rate = 25
oven_img = pygame.image.load('assets/fire.png')
oven_img = pygame.transform.rotate(oven_img, 180)
oven_img_rect = oven_img.get_rect()
oven_img_rect.left = 0
fire_img = pygame.image.load('assets/fire.png')
fire_img_rect = fire_img.get_rect()
fire_img_rect.left = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont('forte', 20)

canvas = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pig')


class Topscore:
    def __init__(self):
        self.high_score = 0
    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score

topscore = Topscore()


class Dragon:
    dragon_velocity = 10

    def __init__(self):
        self.dragon_img = pygame.image.load('assets/butcher.png')
        self.dragon_img = pygame.transform.scale(self.dragon_img, (200, 200))
        self.dragon_img_rect = self.dragon_img.get_rect()
        self.dragon_img_rect.width -= 10
        self.dragon_img_rect.height -= 10
        self.dragon_img_rect.top = window_height/2
        self.dragon_img_rect.right = window_width
        self.up = True
        self.down = False

    def update(self):
        canvas.blit(self.dragon_img, self.dragon_img_rect)
        if self.dragon_img_rect.top <= oven_img_rect.bottom:
            self.up = False
            self.down = True
        elif self.dragon_img_rect.bottom >= fire_img_rect.top:
            self.up = True
            self.down = False

        if self.up:
            self.dragon_img_rect.top -= self.dragon_velocity
        elif self.down:
            self.dragon_img_rect.top += self.dragon_velocity


class Flames:
    flames_velocity = 20

    def __init__(self):
        self.flames = pygame.image.load('assets/knife.png')
        self.flames = pygame.transform.rotate(self.flames, -30)
        self.flames_img = pygame.transform.scale(self.flames, (75, 75))
        self.flames_img_rect = self.flames_img.get_rect()
        self.flames_img_rect.right = dragon.dragon_img_rect.left
        self.flames_img_rect.top = dragon.dragon_img_rect.top + 30


    def update(self):
        canvas.blit(self.flames_img, self.flames_img_rect)

        if self.flames_img_rect.left > 0:
            self.flames_img_rect.left -= self.flames_velocity


class Mario:
    velocity = 10

    def __init__(self):
        self.mario_img = pygame.image.load('assets/piggy.png')
        self.mario_img = pygame.transform.scale(self.mario_img, (100, 100))
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.left = 20
        self.mario_img_rect.top = window_height/2 - 100
        self.down = True
        self.up = False

    def update(self):
        canvas.blit(self.mario_img, self.mario_img_rect)
        if self.mario_img_rect.top <= oven_img_rect.bottom:
            game_over()
            if SCORE > self.mario_score:
                self.mario_score = SCORE
        if self.mario_img_rect.bottom >= fire_img_rect.top:
            game_over()
            if SCORE > self.mario_score:
                self.mario_score = SCORE
        if self.up:
            self.mario_img_rect.top -= 10
        if self.down:
            self.mario_img_rect.bottom += 10


def game_over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('assets/mario_dies.mp3')
    music.play()
    topscore.top_score(SCORE)
    game_over_img = pygame.image.load('assets/endimage.png')
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (window_width/2, window_height/2)
    canvas.blit(game_over_img, game_over_img_rect)
    font = pygame.font.Font(None, 48)
    text = font.render('You are a porkchop! Get Cooked!', True, 'black')
    canvas.blit(text, (window_width/2 - 275, window_height/2 - 150))
    text = font.render('Click any key to restart!', True, 'black')
    canvas.blit(text, (window_width/2 - 200, window_height/2 + 100))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                music.stop()
                game_loop()
        pygame.display.update()


def start_game():
    canvas.fill(blue)
    start_img = pygame.image.load('assets/start.png')
    start_img = pygame.transform.scale(start_img, (1200, 600))
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (window_width/2, window_height/2)
    canvas.blit(start_img, start_img_rect)
    font = pygame.font.Font(None, 72)
    text = font.render('Porkchop Run!', True, 'black')
    canvas.blit(text, (window_width/2 + 100, window_height/2))
    font2 = pygame.font.Font(None, 45)
    text1 = font2.render('Click any key to start!', True, 'black')
    canvas.blit(text1, (window_width/2 + 100, window_height/2 + 100))
    text2 = font2.render('Use the up arrow to avoid the knives, watch out for the fire on top and bottom!', True, 'black')
    canvas.blit(text2, (window_width/2 - 560, window_height/2 + 250))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()


def check_level(SCORE):
    global LEVEL
    if SCORE in range(0, 10):
        oven_img_rect.bottom = 50
        fire_img_rect.top = window_height - 50
        LEVEL = 1
    elif SCORE in range(10, 20):
        oven_img_rect.bottom = 100
        fire_img_rect.top = window_height - 100
        LEVEL = 2
    elif SCORE in range(20, 30):
        oven_img_rect.bottom = 150
        fire_img_rect.top = window_height - 150
        LEVEL = 3
    elif SCORE > 30:
        oven_img_rect.bottom = 200
        fire_img_rect.top = window_height - 200
        LEVEL = 4


def game_loop():
    while True:
        global dragon
        dragon = Dragon()
        flames = Flames()
        mario = Mario()
        add_new_flame_counter = 0
        global SCORE
        SCORE = 0
        global  HIGH_SCORE
        flames_list = []
        pygame.mixer.music.load('assets/mario_theme.mp3')
        pygame.mixer.music.play(-1, 0.0)
        while True:
            canvas.fill(blue)
            check_level(SCORE)
            dragon.update()
            add_new_flame_counter += 1

            if add_new_flame_counter == add_new_flame_rate:
                add_new_flame_counter = 0
                new_flame = Flames()
                flames_list.append(new_flame)
            for f in flames_list:
                if f.flames_img_rect.left <= 0:
                    flames_list.remove(f)
                    SCORE += 1
                f.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        mario.up = True
                        mario.down = False
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        mario.up = False
                        mario.down = True
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False

            score_font = font.render('Score:'+str(SCORE), True, green)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (200, oven_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(score_font, score_font_rect)

            level_font = font.render('Level:'+str(LEVEL), True, green)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (500, oven_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(level_font, level_font_rect)

            top_score_font = font.render('Top Score:'+str(topscore.high_score),True,green)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (800, oven_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(top_score_font, top_score_font_rect)

            canvas.blit(oven_img, oven_img_rect)
            canvas.blit(fire_img, fire_img_rect)
            mario.update()
            for f in flames_list:
                if f.flames_img_rect.colliderect(mario.mario_img_rect):
                    game_over()
                    if SCORE > mario.mario_score:
                        mario.mario_score = SCORE
            pygame.display.update()
            clock.tick(fps)


start_game()
