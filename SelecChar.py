import pygame, Animation
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (242, 226, 0)

# IMAGES :
# 0 - Goku    1 - Gohan    2 - Picolo   3 - Végéta   4 - Freezer   5 - Cell

def loadImages(images):
    images[0].append(pygame.transform.scale(pygame.image.load("Res/Goku/GokuIcon.jpg"), (150, 150)))
    images[0].append((pygame.image.load("Res/Goku/Goku1.png")))

    images[1].append(pygame.transform.scale(pygame.image.load("Res/Gohan/GohanIcon.jpg"), (150, 150)))
    images[1].append((pygame.image.load("Res/Gohan/Gohan1.png")))

    images[2].append(pygame.transform.scale(pygame.image.load("Res/Picolo/PicoloIcon.jpg"), (150, 150)))
    images[2].append((pygame.image.load("Res/Picolo/Picolo1.png")))

    images[3].append(pygame.transform.scale(pygame.image.load("Res/Végéta/VégétaIcon.jpg"), (150, 150)))
    images[3].append((pygame.image.load("Res/Végéta/Végéta1.png")))

    images[4].append(pygame.transform.scale(pygame.image.load("Res/Freezer/FreezerIcon.jpg"), (150, 150)))
    images[4].append((pygame.image.load("Res/Freezer/Freezer1.png")))

    images[5].append(pygame.transform.scale(pygame.image.load("Res/Cell/CellIcon.jpg"), (150, 150)))
    images[5].append((pygame.image.load("Res/Cell/Cell1.png")))

def afficherMenu(selection, screen, images):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, YELLOW, (154*(selection[0]-1) + 70, 154 * (selection[1]-1) + 248, 154, 154))

    screen.blit(images[0][0], (72, 250))
    screen.blit(images[1][0], (226, 250))
    screen.blit(images[2][0], (380, 250))

    screen.blit(images[3][0], (72, 404))
    screen.blit(images[4][0], (226, 404))
    screen.blit(images[5][0], (380, 404))

def selectChar(screen):
    selection = [1, 1]
    continuer = True
    images = [[] for i in range(6)]
    characters = [0, -1, 1]
    listPerso = ["Goku", "Gohan", "Picolo", "Végéta", "Freezer", "Cell"]
    loadImages(images)
    animP1 = Animation.Animation(True)
    animP1._getAll("Res/Goku/AnimNormale", 60, True, [60, 80])
    animP1._setPos([120, 248 - animP1._getFrame().get_size()[1]])
    fontObj = pygame.font.SysFont("Comic Sans MS", 24)

    animP2 = Animation.Animation()
    animP2._set([], [])

    afficherMenu(selection, screen, images)
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                return ["Quit"]
            elif event.type == KEYDOWN :
                if event.key == K_UP:
                    if selection[1] > 1:
                        selection[1] -= 1
                    else:
                        selection[0] = 1
                    if characters[2] == 1:
                        animP1._getAll("Res/" + listPerso[(selection[1]-1)*3 + selection[0] -1] + "/AnimNormale", 60, True)
                        animP1._setPos([120, 248 - animP1._getFrame().get_size()[1]])
                    else:
                        animP2._getAll(
                            "Res/" + listPerso[(selection[1] - 1) * 3 + selection[0] - 1] + "/AnimNormale", 60,
                            False)
                        animP2._setPos([550, 248 - animP2._getFrame().get_size()[1]])
                elif event.key == K_DOWN :
                    if selection[1] < 2:
                        selection[1] += 1
                    else:
                        selection[0] = 3
                    if characters[2] == 1:
                        animP1._getAll("Res/" + listPerso[(selection[1]-1)*3 + selection[0] -1] + "/AnimNormale", 60, True)
                        animP1._setPos([120, 248 - animP1._getFrame().get_size()[1]])
                    else:
                        animP2._getAll(
                            "Res/" + listPerso[(selection[1] - 1) * 3 + selection[0] - 1] + "/AnimNormale", 60,
                            False)
                        animP2._setPos([550, 248 - animP2._getFrame().get_size()[1]])
                elif event.key == K_LEFT:
                    if selection[0] > 1:
                        selection[0] -= 1
                        if characters[2] == 1:
                            animP1._getAll(
                                "Res/" + listPerso[(selection[1] - 1) * 3 + selection[0] - 1] + "/AnimNormale", 60,
                                True)
                            animP1._setPos([120, 248 - animP1._getFrame().get_size()[1]])
                        else:
                            animP2._getAll(
                                "Res/" + listPerso[(selection[1] - 1) * 3 + selection[0] - 1] + "/AnimNormale", 60,
                                False)
                            animP2._setPos([550, 248 - animP2._getFrame().get_size()[1]])
                elif event.key == K_RIGHT:
                    if selection[0] < 3:
                        selection[0] += 1
                        if characters[2] == 1:
                            animP1._getAll(
                                "Res/" + listPerso[(selection[1] - 1) * 3 + selection[0] - 1] + "/AnimNormale", 60,
                                True)
                            animP1._setPos([120, 248 - animP1._getFrame().get_size()[1]])
                        else:
                            animP2._getAll(
                                "Res/" + listPerso[(selection[1] - 1) * 3 + selection[0] - 1] + "/AnimNormale", 60,
                                False)
                            animP2._setPos([550, 248 - animP2._getFrame().get_size()[1]])
                elif event.key == K_RETURN or K_KP_ENTER:
                    if characters[2] < 2:
                        characters[2] += 1
                        animP2._getAll(
                            "Res/" + listPerso[(selection[1] - 1) * 3 + selection[0] - 1] + "/AnimNormale", 60,
                            False)
                        animP2._setPos([550, 248 - animP2._getFrame().get_size()[1]])
                    elif characters[2] == 2:
                        retChars = [listPerso[characters[0]], listPerso[characters[1]]]
                        return ["Battle", retChars]
                if characters[2] <= 1:
                    characters[0] = ((selection[1]-1)*3)+selection[0]-1
                elif characters[2] == 2:
                    characters[1] = ((selection[1]-1)*3)+selection[0]-1

        afficherMenu(selection, screen, images)

        P1Txt = fontObj.render(listPerso[characters[0]], False, (255, 255, 255))
        screen.blit(P1Txt, (10, 0))
        animP1._update()
        animP1._draw(screen)
        if characters[2] > 1:
            P2Txt = fontObj.render(listPerso[characters[1]], False, (255, 255, 255))
            screen.blit(P2Txt, (500, 0))
        animP2._update()
        animP2._draw(screen)
        pygame.display.update()