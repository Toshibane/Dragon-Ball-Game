import Animation, pygame
from pygame.locals import *
# 0 - Goku    1 - Gohan    2 - Picolo   3 - Végéta   4 - Freezer   5 - Cell
def WinScreen(screen, characters):
    clock = pygame.time.Clock()
    fond = pygame.image.load("Res/FondCombat.jpg")
    animWin = Animation.Animation(False)
    animWin._getAll("Res/"+characters[0]+"/AnimGagné", 15, False, [220, 340])

    if characters[0] == "Goku":
        animWin._loopIn(6)
    elif characters[0] == "Gohan":
        animWin._loopIn(7)
    elif characters[0] == "Picolo":
        animWin._loopIn(7)
    elif characters[0] == "Végéta":
        animWin._loopIn(6)
    elif characters[0] == "Freezer":
        animWin._loopIn(3)
    elif characters[0] == "Cell":
        animWin._loopIn(7)

    animPer = Animation.Animation(False)
    animPer._getAll("Res/"+characters[1]+"/AnimPerdu", 15, False, [400, 280])

    if characters[1] == "Goku":
        animPer._loopIn(2)
    elif characters[1] == "Gohan":
        animPer._loopIn(4)
    elif characters[1] == "Picolo":
        animPer._loopIn(3)
    elif characters[1] == "Végéta":
        animPer._loopIn(7)
    elif characters[1] == "Freezer":
        animPer._loopIn(2)
    elif characters[1] == "Cell":
        animPer._loopIn(2)

    continuer = True
    clock.tick()
    while continuer:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                return ["Quit"]
            elif event.type == KEYDOWN:
                return ["TitleScreen"]
        screen.blit(fond, (0, 0))
        animWin._update()
        animWin._draw(screen)
        animPer._update()
        animPer._draw(screen)
        pygame.display.update()
        w = clock.tick()
        pygame.time.wait(15-w)