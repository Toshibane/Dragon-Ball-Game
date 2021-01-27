import time, pygame
from pygame.locals import *

getMillis = lambda : int(round(time.time()*1000))



pygame.init()
def getFPS():
    curFPS = 0
    clock = pygame.time.Clock()

    for i in range(1500000):
        print("FPS : " + str(clock.get_fps()))
        curFPS = clock.get_fps()
    return curFPS

def fpsLimiter(lastFrame):
    lf = lastFrame
    cf = getMillis()
    fps = (cf - lf)*1000
    print(fps)
    return cf

def afficherCombo(screen, combo):
    screen.fill((0, 0, 0))
    textFont = pygame.font.SysFont("Comic Sans MS", 150)
    text = ""
    for touch in combo:
        if text != "":
            text+=" + "
        text += str(touch)
    textObj = textFont.render(text, False, (255, 255, 255))
    textRec = textObj.get_rect()
    textRec.topleft = (0, 100)
    screen.blit(textObj, textRec)

def func():
    dernierCoup = 0
    lastFrame = 0
    combo = []
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Test")
    continuer = True
    while continuer:
        pygame.display.update()
        if dernierCoup+400 <= getMillis():
            combo.clear()
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN:
                combo.append(event.key)
                dernierCoup = getMillis()
        afficherCombo(screen,combo)
        lastFrame = fpsLimiter(lastFrame)


func()
pygame.quit()