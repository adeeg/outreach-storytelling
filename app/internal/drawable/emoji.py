import pygame, os
from util.pygame_helper import loadImg
from util.timer import Timer
from util.vector2 import Vector2, fromTuple
from util.math_helper import lerp
from util.observer import Subject, Event
from internal.action import ActionMove, ActionScale, ActionFlip, ActionRotate


class Emoji(pygame.sprite.Sprite, Subject):
    IMG_PREFIX = "emoji"

    """ manip :: [Action]
    """

    def __init__(self, image="", startCoord=Vector2(0,0)):
        pygame.sprite.Sprite.__init__(self)
        Subject.__init__(self)
        super().__init__()

        self.visible = True
        self.rotation = 0
        
        self.origImage, self.rect = loadImg(os.path.join(self.IMG_PREFIX, str(image)))
        self.image = self.origImage
        self.rect.x = startCoord.x
        self.rect.y = startCoord.y
        
        self.lastPos = startCoord
        self.manip = []
    
    def changeImage(self, image: str):
        self.origImage, self.rect = loadImg(os.path.join(self.IMG_PREFIX, str(image)))
        self.image = self.origImage

    def setPos(self, coord: Vector2):
        self.rect.x = coord.x
        self.rect.y = coord.y
    
    def getPos(self) -> Vector2:
        return Vector2(self.rect.x, self.rect.y)
    
    def setRotation(self, newRot):
        #rotDiff = newRot - self.rotation
        #self.image = pygame.transform.rotate(self.origImage, rotDiff)
        self.rotation = newRot
    
    def getRotation(self):
        return self.rotation
    
    def setScale(self, scale):
        x = scale * fromTuple(self.image.get_size())
        self.image = pygame.transform.smoothscale(self.origImage, x.toTuple())
    
    def applyAction(self, act):
        if isinstance(act, ActionMove):
            self.setPos(act.coord)
        elif isinstance(act, ActionScale):
            self.setScale(act.scale)


        pass