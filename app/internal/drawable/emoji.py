import pygame, os, copy
from util.pygame_helper import loadImg
from util.timer import Timer
from util.vector2 import Vector2, fromTuple
from util.math_helper import lerp
from util.observer import Subject, Event
from internal.action import ActionMove, ActionScale, ActionFlip, ActionFlipHorz, ActionRotate

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
        #self.image = copy.copy(self.origImage)
        self.image = self.origImage
        self.rect.x = startCoord.x
        self.rect.y = startCoord.y
        
        self.lastPos = startCoord
        self.manip = []
    
    def changeImage(self, image: str):
        #y = self.origImage
        self.origImage, self.rect = loadImg(os.path.join(self.IMG_PREFIX, str(image)))
        self.image = self.origImage
        #self.image = copy.copy(self.origImage)
        #self.image = self.origImage

    def setPos(self, coord: Vector2):
        self.rect.x = coord.x
        self.rect.y = coord.y
    
    def getPos(self) -> Vector2:
        return Vector2(self.rect.x, self.rect.y)
    
    def setRotation(self, newRot):
        #rotDiff = newRot - self.rotation
        #self.image = pygame.transform.rotate(self.origImage, rotDiff)
        self.rotation = newRot
        self.image = pygame.transform.rotate(self.origImage, newRot)
    
    def getRotation(self):
        return self.rotation
    
    def setScale(self, scale):
        x = scale * fromTuple(self.image.get_size())
        self.image = pygame.transform.smoothscale(self.origImage, x.operation(int).toTuple())
    
    def setSize(self, size):
        self.image = pygame.transform.smoothscale(self.origImage, size.operation(int).toTuple())
    
    def flip(self, vert, horz):
        self.origImage = pygame.transform.flip(self.image, vert, horz)
    
    def applyAction(self, act):
        if isinstance(act, ActionMove):
            self.setPos(act.coord)
            #print("move")
        elif isinstance(act, ActionScale):
            self.setScale(act.scale)
            #print("scale")
        elif isinstance(act, ActionRotate):
            self.setRotation(act.endRot - act.startRot)
            #print("rot")
        elif isinstance(act, ActionFlip):
            self.flip(act.vert, act.horz)
            #print("flip")