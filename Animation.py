from os import listdir
import pygame

class Animation:
    def __init__(self, loop=False):
        self.frames = []
        self.counts = []
        self.count = 0
        self.actualFrame = 0
        self.totalFrames = 0
        self.pos = []
        self.loop = loop
        self.loopFrame = -1
        self.ajout = 1
        self.toFinish = False
        self.flip = False
    def _set(self, frames, counts, pos=[0, 0]):
        self.frames = frames
        self.counts = counts
        self.count = 0
        self.actualFrame = -1
        if len(frames) > 0:
            self.actualFrame = 0
        self.pos = pos
        self.toFinish = False

    def _setPos(self, pos):
        self.pos = pos

    def _getAll(self, dir, counts, flip, pos=[0, 0], loop=True):
        self.__init__(loop)
        self.flip = flip
        for f in listdir(dir):
            self.totalFrames += 1
            if flip:
                self.frames.append(pygame.transform.flip(pygame.image.load(dir + "/" + f), True, False))
            else:
                self.frames.append(pygame.image.load(dir + "/" + f))
            self.counts.append(counts)
        self.pos = pos
        self.toFinish = False

    def _setDelay(self, delay):
        if len(delay) == 1:
            for i in range(len(self.counts)):
                self.counts[i] = delay[0]
            return 0
        elif len(delay) == len(self.counts):
            self.counts = delay[:]
            return 0
        return 1

    def _setToFinish(self, tf):
        self.toFinish = tf
    def _isToFinish(self):
        return self.toFinish
    def _isFlipped(self):
        return self.flip
    def _getFrames(self):
        return self.frames
    def _getPos(self):
        return self.pos
    def _loopIn(self, frame):
        self.loopFrame = frame
        self.loop = False

    def _update(self):
        if self.actualFrame > -1 and self.count >= self.counts[self.actualFrame]:
            self.actualFrame += self.ajout
            self.count = 0
            if self.actualFrame == len(self.frames)-1 or self.actualFrame == 0:
                if self.loop:
                    self.ajout = -self.ajout
                else:
                    if self.loopFrame == -1:
                        self.actualFrame = 0
                    else:
                        self.actualFrame = self.loopFrame
        self.count += 1

    def _draw(self, screen, flipped=False, battle=False):
        if self.actualFrame > -1:
            screen.blit(self.frames[self.actualFrame], [self.pos[0] - self._getFrame().get_size()[0]/2, self.pos[1]])

    def _getFrame(self):
        return self.frames[self.actualFrame]
    def _getActualFrame(self):
        return self.actualFrame
    def _setActualFrame(self, frame):
        self.actualFrame = frame
    def _getTotalFrames(self):
        return self.totalFrames

    def _isFinished(self):
        return len(self.frames)-2 <= self.actualFrame
