import pygame

class Special:
    def __init__(self, pos, playPos, direction, user):
        self.pos = pos  # Position boule
        self.direction = direction  # Direction boule
        self.playPos = playPos  # Position Joueur
        self.user = user  # User of the special attack

    def _update(self, cible, screen):
        if self.direction == "Droite":
            self.pos[0] += 5
            if self.pos[0] + 15 >= cible._getPos()[0] and self.pos[1] >= cible._getPos()[1] and self.pos[1] + 50 <= cible._getPos()[1] + cible._getAnimation()._getFrame().get_size()[1]:
                self._hurt(screen, cible)
        elif self.direction == "Gauche":
            self.pos[0] -= 5
            if self.pos[0] <= cible._getPos()[0] and self.pos[1] >= cible._getPos()[1] and self.pos[1] + 50 <= cible._getPos()[1] + cible._getAnimation()._getFrame().get_size()[1]:
                self._hurt(screen, cible)
        self._draw(screen)

    def _draw(self, screen):
        if self.direction == "Droite":
            r = pygame.Rect(self.playPos[0] + self.user._getAnimation()._getFrame().get_size()[0]//2, self.pos[1], self.pos[0]- (self.playPos[0] + self.user._getAnimation()._getFrame().get_size()[0]//2), 50)
            pygame.draw.rect(screen, (255, 255, 255), r)
            pygame.draw.circle(screen, (255, 255, 255), (self.pos[0], self.pos[1]+25), 25)
        else:
            r = pygame.Rect(self.pos[0], self.pos[1], self.playPos[0] - self.pos[0], 50)
            pygame.draw.rect(screen, (255, 255, 255), r)
            pygame.draw.circle(screen, (255, 255, 255), (self.pos[0], self.pos[1]+25), 25)

    def _hurt(self, screen, cible):
        cible._getHurt(0.38)
        lenP1 = self.user._getPV() * 2.5
        lenP2 = cible._getPV() * 2.5
        pygame.draw.rect(screen, (255 - lenP1, lenP1 * 255 / 250, 5), (0, 40, lenP1, 25))
        pygame.draw.rect(screen, (255 - lenP2, lenP2 * 255 / 250, 5), (600 - lenP2, 40, lenP2, 25))