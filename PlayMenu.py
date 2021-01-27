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
    vsIA = textFont.render("Jouer contre l'ordinateur", False, color)
    color = WHITE
    vsIARect = vsIA.get_rect()
    vsIARect.topleft = (100, 100)

    if selection == 2:
        color = YELLOW
    retour = textFont.render("Retour", False, color)
    color = WHITE
    retourRect = retour.get_rect()
    retourRect.topleft = (100, 130)

    screen.blit(vsIA, vsIARect)
    screen.blit(retour, retourRect)

def playMenu(screen):
    selection = 1
    continuer = True
    fond = pygame.image.load("Res/FondTitle.jpg")
    boule = pygame.image.load("Res/BouleCristal.png")
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
                        return ["SelectChar"]
                    elif selection == 2:
                        return ["TitleScreen"]
                afficherMenu(selection, screen, fond)
            elif event.type == MOUSEMOTION :
                if 100 <= event.pos[0] <= 380 and 100 <= event.pos[1] <= 124:
                    selection = 1
                elif 100 <= event.pos[0] <= 244 and 130 <= event.pos[1] <= 154:
                    selection = 2
                afficherMenu(selection, screen, fond)
            elif event.type == MOUSEBUTTONDOWN:
                if selection == 1:
                    return ["SelectChar"]
                elif selection == 2:
                    return ["TitleScreen"]
        screen.blit(boule, (70, 70 + (30 * selection)))
        pygame.display.update()