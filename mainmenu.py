import pygame
class Mainmenu:
# from level1 import Level1
# from levels import Levels

    def mainmenu():
        pygame.init()
        screen = pygame.display.set_mode()
        selected = None
        width, height = pygame.display.get_window_size()
        screen.fill("white")
        mainbox = pygame.draw.rect(screen, "gray", (1/2*width - 300, 1/2*height - 300, 600, 600))
        level_1box = pygame.draw.rect(screen, "blue", (1/2*width - 100, 1/2*height - 50, 240, 80))
        levelsbox = pygame.draw.rect(screen, "green", (1/2*width - 60, 1/2*height + 70, 125, 60))
        font = pygame.font.Font(None, 48)
        text = font.render("Main Menu", True, "black")
        screen.blit(text, (1/2*width - 60, 1/2*height - 200))
        option1 = font.render("play level 1", True, "black" )
        screen.blit(option1, (1/2*width - 70, 1/2*height - 30))
        option2 = font.render("levels", True, "black")
        screen.blit(option2, (1/2*width - 45, 1/2*height + 75))
        pygame.display.flip()
        
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if level_1box.collidepoint(event.pos):
                        selected = 1
                    elif levelsbox.collidepoint(event.pos):
                        selected = 2
                    
            if selected == 1:
                screen.fill("pink")
            elif selected == 2:
                screen.fill("red")
            pygame.display.flip()
            pygame.time.wait(1000)
        
    mainmenu()