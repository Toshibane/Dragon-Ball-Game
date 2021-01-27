import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (242, 226, 0)

def afficherMenu(selection, screen, fond):
    screen.blit(fond, (0, 0))
    textFont = pygame.font.SysFont("Comic Sans MS", 24)
    color = WHITE
    if selection == 1:
        color = YELLOW
    Jouer = textFont.render("JOUER", False, color)
    JouerRect = Jouer.get_rect()
    JouerRect.topleft = (100, 100)
    color = WHITE

    if selection == 2:
        color = YELLOW
    Quit = textFont.render("QUITTER", False, color)
    QuitRect = Quit.get_rect()
    QuitRect.topleft = (100, 130)
    color = WHITE

    screen.blit(Jouer, JouerRect)
    screen.blit(Quit, QuitRect)

def ecranTitre(screen):
    selection = 1
    fond = pygame.image.load("Res/FondTitle.jpg")
    boule = pygame.image.load("Res/BouleCristal.png")
    continuer = True
    afficherMenu(selection, screen, fond)

    while continuer:

        for event in pygame.event.get():
            if event.type == QUIT:
                return ["Quit"]
            elif event.type == KEYDOWN :
                if event.key == K_UP:
                    if selection > 1:
                        selection -= 1
                elif event.key == K_DOWN :
                    if selection < 2:
                        selection += 1
                elif event.key == K_RETURN or K_KP_ENTER:
                    if selection == 1:
                        return ["PlayMenu"]
                    elif selection == 2:
                        return ["Quit"]
                afficherMenu(selection, screen, fond)
            elif event.type == MOUSEMOTION :
                if 100 <= event.pos[0] <= 244 and 100 <= event.pos[1] <= 124:
                    selection = 1
                elif 100 <= event.pos[0] <= 244 and 130 <= event.pos[1] <= 154:
                    selection = 2
                afficherMenu(selection, screen, fond)
            elif event.type == MOUSEBUTTONDOWN:
                if selection == 1:
                    return ["PlayMenu"]
                elif selection == 2:
                    return ["Quit"]
        screen.blit(boule, (70, 70+(30*selection)))
        pygame.display.update()
