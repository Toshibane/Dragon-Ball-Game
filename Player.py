import time, pygame, Animation, Special, Battle

class Player:
    def __init__(self, personnage, flip=True):
        self.pv = 100
        self.ki = 0
        self.pos = [0, 0]
        self.combo = []
        self.comboAttacks = 0
        self.lastAttack = 0
        self.image = pygame.image.load("Res/" + personnage + "/" + personnage + "1.png")
        self.movement = 0
        self.movementY = -4
        self.countY = 0
        self.animation = Animation.Animation(True)
        self.animation._getAll("Res/" + personnage + "/AnimNormale", 15, True)
        self.personnage = personnage
        self.flip = flip
        self.currentAnim = "AnimNormale"

    def _attack(self, nAttaque):
        self.combo.append(nAttaque)
        self.lastAttack = round(time.time()*1000)

    def _getCurrentAnim(self):
        return self.currentAnim
    def _setCurrentAnim(self, currentAnim):
        self.currentAnim = currentAnim

    def _getPV(self):
        return self.pv

    def _getKi(self):
        return self.ki

    def _setPV(self, newPV):
        self.pv = newPV

    def _getHurt(self, damages):
        self.pv -= damages
        if self.pv < 0:
            self.pv = 0
        self._setAnimation("Hurt")
        self.animation._setToFinish(True)

    def _getPos(self):
        return self.pos

    def _setPos(self, newPos):
        self.pos = newPos
        self.animation._setPos(newPos)

    def _getImage(self):
        return self.image

    def _setImage(self, dir):
        self.image = pygame.image.load(dir)

    def _getAnimation(self):
        return self.animation

    def _flip(self, flip):
        self.flip = flip

    def _isFlipped(self):
        return self.flip

    def _setAnimation(self, type, loop=False):
        if type == "Marche":
            self.animation._getAll("Res/"+self.personnage+"/AnimMarche", 15, self.flip, self.pos, loop)
            self._setCurrentAnim("Marche")
        elif type == "Saut":
            self.animation._getAll("Res/" + self.personnage + "/AnimJump", 20, self.flip, self.pos, loop)
            self._setCurrentAnim("Saut")
        elif type == "Start":
            self.animation._getAll("Res/" + self.personnage + "/AnimArrive", 15, self.flip, self.pos, loop)
            self._setCurrentAnim("Start")
        elif type == "Poing":
            self.animation._getAll("Res/" + self.personnage + "/AnimPoing", 20, self.flip, self.pos, loop)
            self._setCurrentAnim("Poing")
        elif type == "BasPoing":
            self.animation._getAll("Res/" + self.personnage + "/AnimBasPoing", 15, self.flip, self.pos, loop)
            self._setCurrentAnim("BasPoing")
        elif type == "Pied":
            self.animation._getAll("Res/" + self.personnage + "/AnimPied", 15, self.flip, self.pos, loop)
            self._setCurrentAnim("Pied")
        elif type == "BasPied":
            self.animation._getAll("Res/" + self.personnage + "/AnimBasPied", 15, self.flip, self.pos, loop)
            self._setCurrentAnim("BasPied")
        elif type == "SautPied":
            self.animation._getAll("Res/" + self.personnage + "/AnimSautPied", 15, self.flip, self.pos, loop)
            self._setCurrentAnim("SautPied")
            self.movementY = 0
        elif type == "SautPoing":
            self.animation._getAll("Res/" + self.personnage + "/AnimSautPoing", 15, self.flip, self.pos, loop)
            self._setCurrentAnim("SautPoing")
        elif type == "Hurt":
            self.animation._getAll("Res/" + self.personnage + "/AnimFrappé", 30, self.flip, self.pos, loop)
            self._setCurrentAnim("Hurt")
        elif type == "Special":
            self.animation._getAll("Res/" + self.personnage + "/AnimSpecial", 15, self.flip, self.pos, loop)

    def _changeAnimationDelay(self, delay):
        self.animation._setDelay(delay)

    def _stopAnimation(self):
        self.animation._getAll("Res/"+self.personnage+"/AnimNormale", 15, self.flip, self.pos, True)
        self._setCurrentAnim("AnimNormale")

    def _move(self, x):
        self.movement = x

    def _jump(self):
        if self.movementY == -4:
            self._setAnimation("Saut", loop=False)
            self.animation._setToFinish(True)
            self.movementY = 3

    def _drawBattle(self, screen, cible):
        Font = pygame.font.SysFont("Comic Sans MS", 20)
        fond = pygame.image.load("Res/FondCombat.jpg")
        screen.blit(fond, (0, 0))
        cible._draw(screen)
        self._draw(screen)

        lenP1 = self._getPV() * 2.5
        lenP2 = cible._getPV() * 2.5
        pygame.draw.rect(screen, (255 - lenP1, lenP1 * 255 / 250, 5), (0, 40, lenP1, 25))
        pygame.draw.rect(screen, (255 - lenP2, lenP2 * 255 / 250, 5), (600 - lenP2, 40, lenP2, 25))

        P1txt = Font.render(self.personnage, False, (0, 0, 0))
        P2txt = Font.render(cible.personnage, False, (0, 0, 0))
        screen.blit(P1txt, (10, 7))
        screen.blit(P2txt, (500, 7))

        pygame.display.update()


    def _isJumping(self):
        return self.movementY != -4

    def _attack(self, touch, cible, touches):
        self.combo.append(touch)
        curPos = self.pos
        if not self._getAnimation()._isFlipped():
            curPos[0] -= 32
        if "Bas" in touches:
            curPos[1] += 11
        self._setAnimation(touch)
        self.animation._setPos(curPos)
        if "Bas" in touches:
            curPos[1] -= 11
        if not self._isFlipped():
            curPos[0] += 32
        self.animation._setToFinish(True)
        if (not self.flip and self.pos[0] - self.animation._getFrame().get_size()[0]/2 <= cible._getPos()[0] + cible._getAnimation()._getFrame().get_size()[0]/2
            and self.pos[0] - self.animation._getFrame().get_size()[0]/2 >= cible._getPos()[0] - cible._getAnimation()._getFrame().get_size()[0]/2)\
            or (self.flip and self.pos[0] + self.animation._getFrame().get_size()[0]/2 >= cible._getPos()[0] - cible._getAnimation()._getFrame().get_size()[0]/2
            and self.pos[0] + self.animation._getFrame().get_size()[0]/2 <= cible._getPos()[0] + cible._getAnimation()._getFrame().get_size()[0]/2)\
            and self.pos[1]-self.animation._getFrame().get_size()[1] <= cible._getPos()[1]-cible._getAnimation()._getFrame().get_size()[1]:
            self.comboAttacks += 1
            self.ki += 5
            if self.ki > 100:
                self.ki = 100
            cible._getHurt(2*(2/self.comboAttacks))

    def _special(self, cible, screen):
        self.ki -= 50
        fond = pygame.image.load("Res/FondCombat.jpg")
        self.animation._getAll("Res/" + self.personnage + "/AnimSpecial", 1, self.flip, self.pos, False)
        posSpe = [self.pos[0] + self.animation._getFrame().get_size()[0]//2, 0]

        if self.personnage == "Goku":
            for i in range(7):
                self.animation._update()
                self._drawBattle(screen, cible)
                pygame.time.wait(60)
            posSpe[1] = self.pos[1] + 10
        elif self.personnage == "Gohan":
            for i in range(4):
                self.animation._update()
                self._drawBattle(screen, cible)
                pygame.time.wait(60)
            posSpe[1] = self.pos[1] + 30
        elif self.personnage == "Picolo":
            for i in range(4):
                self.animation._update()
                self._drawBattle(screen, cible)
                pygame.time.wait(60)
            posSpe[1] = self.pos[1]
        elif self.personnage == "Végéta":
            for i in range(4):
                self.animation._update()
                self._drawBattle(screen, cible)
                pygame.time.wait(60)
            posSpe[1] = self.pos[1] + self.animation._getFrame().get_size()[1]//2 - 50
        elif self.personnage == "Freezer":
            for i in range(5):
                self.animation._update()
                self._drawBattle(screen, cible)
                pygame.time.wait(60)
            posSpe[1] = self.pos[1] + self.animation._getFrame().get_size()[1]//2 - 40
        elif self.personnage == "Cell":
            for i in range(2):
                self.animation._update()
                self._drawBattle(screen, cible)
                pygame.time.wait(60)
            posSpe[1] = self.pos[1] + self.animation._getFrame().get_size()[1]//2 - 45

        direction = "Droite" if self.flip else "Gauche"
        spe = Special.Special(posSpe, self.pos, direction, self)
        for i in range(133):
            screen.blit(fond, (0, 0))
            spe._update(cible, screen)
            self._draw(screen)
            cible._draw(screen)
            pygame.time.wait(5)
            pygame.display.update()

    def _update(self, player2):
        if round(time.time()*1000) > self.lastAttack + 400:
            self.combo.clear()
            self.comboAttacks = 0
        if self.animation._isToFinish() and self.animation._isFinished():
            self._stopAnimation()
        if 0 < self.pos[0] + self.movement < 600 and \
                (not
                 (player2._getPos()[0] - player2._getAnimation()._getFrame().get_size()[0]/2 <= self.pos[0] + self.movement - self.animation._getFrame().get_size()[0]/2
                  and player2._getPos()[0] + player2._getAnimation()._getFrame().get_size()[0]/2 >= self.pos[0] + self.movement + self.animation._getFrame().get_size()[0]/2)
                 or self.movementY != -4):
            if self.movementY != 4:
                self.pos[0] += self.movement*2
            else:
                self.pos[0] += self.movement
            self.animation._setPos(self.pos)

        if self.movementY != -4:
            self.countY += 1
            self.pos[1] -= int(self.movementY*1.4)
            if self.pos[1] > 300 - self._getAnimation()._getFrame().get_size()[1]:
                self.pos[1] = 300 - self._getAnimation()._getFrame().get_size()[1]
        if self.countY == 20:
            self.countY = 0
            self.movementY -= 1
        self.animation._update()

    def _draw(self, screen):
        self.animation._draw(screen, self.flip)