import pygame, os
from util.pygame_helper import loadImg
from util.timer import Timer
from util.vector2 import Vector2
from util.math import lerp
from util.observer import Subject, Event

class EmojiTest(pygame.sprite.Sprite, Subject):
    IMG_PREFIX = "emoji"

    def __init__(self, image="", startCoord=Vector2(0,0)):
        pygame.sprite.Sprite.__init__(self)
        Subject.__init__(self)
        super().__init__()

        self.image, self.rect = loadImg(os.path.join(self.IMG_PREFIX, str(image)))
        self.rect.x = startCoord.x
        self.rect.y = startCoord.y

        self.lastPos = startCoord
    
    def setPos(self, coord):
        self.rect.x = coord.x
        self.rect.y = coord.y
    
    def getPos(self):
        return Vector2(self.rect.x, self.rect.y)