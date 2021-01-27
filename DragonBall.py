import pygame, EcranTitre, PlayMenu, SelecChar, Battle, WinScreen
from pygame.locals import *

def start():
    pygame.init()  # Initiation Pygame
    pygame.display.set_caption("Dragon Ball")  # Changement nom fenêtre
    pygame.display.set_icon(pygame.image.load("Res/BouleCristal.png"))  # Changement icone fenêtre

def DragonBall():
    screen = pygame.display.set_mode((600, 600))
    continuer = True
    gameState = ["TitleScreen"]
    while continuer:
        if gameState[0] == "TitleScreen":
            screen.fill((0, 0, 0))
            gameState = EcranTitre.ecranTitre(screen)
        elif gameState[0] == "PlayMenu":
            screen.fill((0, 0, 0))
            gameState = PlayMenu.playMenu(screen)
        elif gameState[0] == "SelectChar":
            screen.fill((0, 0, 0))
            gameState = SelecChar.selectChar(screen)
        elif gameState[0] == "Battle":
            screen.fill((0, 0 , 0))
            gameState = Battle.battle(screen, gameState[1])
        elif gameState[0] == "WinScreen":
            screen.fill((0, 0, 0))
            gameState = WinScreen.WinScreen(screen, gameState[1])
        elif gameState[0] == "Quit":
            continuer = False

start()
DragonBall()
pygame.quit()
