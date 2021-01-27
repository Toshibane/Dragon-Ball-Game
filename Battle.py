import pygame, Player, random
from pygame.locals import *

def start(screen, player1, player2, fond):
    player1._setAnimation("Start")
    player1._changeAnimationDelay([24])
    player2._setAnimation("Start")
    player2._changeAnimationDelay([24])
    j1F, j2F = False, False
    clock = pygame.time.Clock()
    clock.tick()
    while not (j1F and j2F):
        if not j1F:
            if player1._getAnimation()._isFinished():
                player1._stopAnimation()
                j1F = True
        if not j2F:
            if player2._getAnimation()._isFinished():
                player2._stopAnimation()
                j2F = True
        screen.blit(fond, (0, 0))
        player1._update(player2)
        player1._draw(screen)
        player2._update(player1)
        player2._draw(screen)
        pygame.display.update()

        w = clock.tick()

        pygame.time.wait(10-w)


def input(event, player, player2, touches, p, screen):
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            player._move(-1)
            if player._getCurrentAnim() != "Saut" and player._getCurrentAnim() != "Hurt":
                player._setAnimation("Marche")
            touches[p].append("Left")
        elif event.key == K_RIGHT:
            player._move(1)
            if player._getCurrentAnim() != "Saut" and player._getCurrentAnim() != "Hurt":
                player._setAnimation("Marche")
            touches[p].append("Right")
        elif event.key == K_UP:
            player._jump()
        elif event.key == K_DOWN:
            touches[p].append("Bas")
        elif event.key == K_a:
            if (player._isFlipped() and "Right" in touches[p] or not player._isFlipped() and "Left" in touches[p]) and "Bas" in touches[p] and player._getKi() >= 50:
                player._special(player2, screen)
            elif "Bas" in touches[p]:
                player._attack("BasPoing", player2, touches[p])
            elif player._isJumping():
                player._attack("SautPoing", player2, touches[p])
            else:
                player._attack("Poing", player2, touches[p])
        elif event.key == K_s:
            if "Bas" in touches[p]:
                player._attack("BasPied", player2, touches[p])
            elif player._isJumping():
                player._attack("SautPied", player2, touches[p])
            else:
                player._attack("Pied", player2, touches[p])
    elif event.type == KEYUP:
        if event.key == K_LEFT or event.key == K_RIGHT:
            player._move(0)
            if player._getCurrentAnim() != "Saut" and player._getCurrentAnim() != "Hurt":
                player._stopAnimation()
            if event.key == K_LEFT:
                touches[p].remove("Left")
            else:
                touches[p].remove("Right")
        elif event.key == K_DOWN:
            touches[p].remove("Bas")
    return event

def drawBackground(screen, fond):
    screen.blit(fond, (0, 0))

def drawPlayers(screen, player1, player2, fond):
    drawBackground(screen, fond)
    player1._update(player2)
    player1._draw(screen)
    player2._update(player1)
    player2._draw(screen)
    if player1._getPos()[0] > player2._getPos()[0]:
        player1._flip(False)
        player2._flip(True)
    else:
        player1._flip(True)
        player2._flip(False)

def displayLife(screen, player1, player2):
    lenP1 = player1._getPV() * 2.5
    lenP2 = player2._getPV() * 2.5
    pygame.draw.rect(screen, (255-lenP1, lenP1*255/250, 5), (0, 40, lenP1, 25))
    pygame.draw.rect(screen, (255-lenP2, lenP2*255/250, 5), (600 - lenP2, 40, lenP2, 25))

def displayKi(screen, player1, player2):
    Font = pygame.font.SysFont("Comic Sans MS", 20)

    ki1 = Font.render(str(player1._getKi()) + "%", False, (0, 0, 0))
    ki2 = Font.render(str(player2._getKi()) + "%", False, (0, 0, 0))
    screen.blit(ki1, (50, 500))
    screen.blit(ki2, (500, 500))

def IAP2(player, player2, touches, times, screen):
    # Faire une vraie ia
    times += 1
    if player2._getCurrentAnim() == "Hurt":
        times = 0
    if times == 33:
        if player2._getPos()[0] - player2._getAnimation()._getFrame().get_size()[0]/2 > player._getPos()[0]+player._getAnimation()._getFrame().get_size()[0]/2:
            if 'Left' not in touches[1]:
                e = pygame.event.Event(KEYDOWN, {"key": K_LEFT})
                input(e, player2, player, touches, 1, screen)
        elif player2._getPos()[0]+ player2._getAnimation()._getFrame().get_size()[0]/2 < player._getPos()[0] - player._getAnimation()._getFrame().get_size()[0]/2:
            if 'Right' not in touches[1]:
                e = pygame.event.Event(KEYDOWN, {"key": K_RIGHT})
                input(e, player2, player, touches, 1, screen)
        else:
            if 'Left' in touches[1]:
                e = pygame.event.Event(KEYUP, {"key": K_LEFT})
                input(e, player2, player, touches, 1, screen)
            if 'Right' in touches[1]:
                e = pygame.event.Event(KEYUP, {"key": K_RIGHT})
                input(e, player2, player, touches, 1, screen)
            if random.randint(0, 1) == 1:
                e = pygame.event.Event(KEYDOWN, {"key": K_a})
                input(e, player2, player, touches, 1, screen)
            else:
                e = pygame.event.Event(KEYDOWN, {"key": K_s})
                input(e, player2, player, touches, 1, screen)
        times = 0
    return times


def battle(screen, characters):
    touches = [[], []]
    clock = pygame.time.Clock()
    fond = pygame.image.load("Res/FondCombat.jpg")
    Font = pygame.font.SysFont("Comic Sans MS", 20)

    Joueur1 = Player.Player(characters[0])
    Joueur2 = Player.Player(characters[1], False)
    Joueur1._setPos([30, 300-Joueur1._getAnimation()._getFrame().get_size()[1]])
    Joueur2._setPos([570, 300-Joueur2._getAnimation()._getFrame().get_size()[1]])
    start(screen, Joueur1, Joueur2, fond)
    continuer = True
    compteurIA = 0
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                return ["Quit"]
            else:
                i = input(event, Joueur1, Joueur2, touches, 0, screen)
        compteurIA = IAP2(Joueur1, Joueur2, touches, compteurIA, screen)
        drawPlayers(screen, Joueur1, Joueur2, fond)
        displayLife(screen, Joueur1, Joueur2)
        displayKi(screen, Joueur1, Joueur2)
        if Joueur1._getPV() <= 0:
            return ["WinScreen", [Joueur2.personnage, Joueur1.personnage]]
        elif Joueur2._getPV() <= 0:
            return ["WinScreen", [Joueur1.personnage, Joueur2.personnage]]
        P1txt = Font.render(Joueur1.personnage, False, (0, 0, 0))
        P2txt = Font.render(Joueur2.personnage, False, (0, 0, 0))
        screen.blit(P1txt, (10, 7))
        screen.blit(P2txt, (500, 7))
        pygame.display.update()
        w = clock.tick()
        pygame.time.wait(15-w)
