from util.timer import Timer
from util.observer import Subject, Event
#from app.util.timer import Timer
from util.math_helper import lerp
from util.vector2 import Vector2, fromTuple
from internal.drawable.text import Text
import pygame, copy, time

class Action(Subject):
    """ duration :: Num
        timer    :: Timer
        conc     :: Bool
    """
    def __init__(self, duration):
        super().__init__()
        self.duration = duration
        self.timer = Timer(self.duration)
        self.conc = False
    
    def start(self, scene):
        self.timer.start()
    
    def update(self, scene):
        if self.timer.isFinished(): self.end(scene)
    
    def end(self, scene):
        self.notify(self, Event.ACTION_FINISHED)

class ActionWait(Action):
    def __init__(self, duration):
        super().__init__(duration)

class ActionChangeBGCol(Action):
    """ col :: (int, int, int)
    """
    def __init__(self, duration: float, col: (int)):
        super().__init__(duration)
        self.colS = (0, 0, 0)
        self.col = col
    
    def start(self, scene):
        super().start(scene)
        self.colS = scene.getBackgroundColour()
    
    def update(self, scene):
        super().update(scene)
        colN = [0, 0, 0]
        for i in range(0, len(colN)):
            colN[i] = lerp(self.colS[i], self.col[i], self.timer.timeThrough() / self.duration)
        scene.setBackgroundColour(tuple(colN))
    
    def end(self, scene):
        super().end(scene)
        scene.setBackgroundColour(self.col)

class ActionMove(Action):
    """ emoji :: emoji
        coord :: (Num, Num)
    """
    def __init__(self, duration, emoji, coord):
        super().__init__(duration)
        self.emoji = emoji
        self.coord = coord

    def start(self, scene):
        super().start(scene)
        self.startPos = self.emoji.getPos()
        self.emoji.manip.append(self)
    
    def update(self, scene):
        super().update(scene)

        newPos = lerp(self.startPos, self.coord, self.timer.timeThrough() / self.duration)
        self.emoji.setPos(newPos)
    
    def end(self, scene):
        self.emoji.setPos(self.coord)
        super().end(scene)

class ActionText(Action):
    """ text :: String """
    def __init__(self, duration, text):
        super().__init__(duration)
        self.text = Text(text)
    
    def start(self, scene):
        self.bg = scene.background
        scene.setBackgroundColour((0, 0, 0))
        scene.addDrawable(self.text)
        for e in scene.emojis:
            e.visible = False
        super().start(scene)
    
    def update(self, scene):
        super().update(scene)
    
    def end(self, scene):
        scene.background = self.bg
        scene.drawables.remove(self.text)
        for e in scene.emojis:
            e.visible = True
        super().end(scene)

# scales an emoji by a scalar
class ActionScale(Action):
    def __init__(self, duration, emoji, scale):
        super().__init__(duration)
        self.emoji = emoji
        self.scale = scale
    
    def start(self, scene):
        super().start(scene)
        self.startImage = self.emoji.image
        self.startSize = fromTuple(self.emoji.image.get_size())
        self.endSize = self.startSize.mult(self.scale)
        self.emoji.manip.append(self)
    
    """ TODO: inflate pos? """
    def update(self, scene):
        super().update(scene)
        newSize = lerp(self.startSize, self.endSize, self.timer.timeThrough() / self.duration).operation(int)
        self.emoji.setSize(newSize)
        #self.emoji.image = pygame.transform.smoothscale(self.startImage, newSize.operation(int).toTuple())
    
    def end(self, scene):
        super().end(scene)
        self.emoji.origImage = self.emoji.image

# flips an emoji
class ActionFlip(Action):
    def __init__(self, duration, emoji, vert: bool, horz: bool):
        super().__init__(duration)
        self.emoji = emoji
        self.vert = vert
        self.horz = horz
    
    def start(self, scene):
        super().start(scene)
        self.emoji.manip.append(self)
        #self.emoji.image = pygame.transform.flip(self.emoji.image, self.vert, self.horz)
        #self.emoji.image = pygame.transform.rotate(self.emoji.image, 45)
    
    def end(self, scene):
        super().end(scene)
        self.emoji.image = pygame.transform.flip(self.emoji.image, self.vert, self.horz)

class ActionFlipHorz(ActionFlip):
    def __init__(self, duration, emoji):
        super().__init__(duration, emoji, False, True)

class ActionFlipVert(ActionFlip):
    def __init__(self, duration, emoji):
        super().__init__(duration, emoji, True, False)

# rotates an emoji by an amount
class ActionRotate(Action):
    def __init__(self, duration, emoji, angle):
        super().__init__(duration)
        self.emoji = emoji
        self.angle = angle
    
    def start(self, scene):
        super().start(scene)
        self.startRot = self.emoji.getRotation()
        self.endRot = self.startRot + self.angle
        self.emoji.manip.append(self)
        #self.startImage = copy.copy(self.emoji.image)
    
    def update(self, scene):
        super().update(scene)

        #loc = self.emoji.image.get_rect().center

        
        #print(self.emoji.getRotation())

        #loc = self.image.get_rect().center
        
        #self.image.get_rect().center = loc

        #self.emoji.image.get_rect().center = loc
        #amount = self.angle * self.timer.timeThrough() / self.duration
        #print(self.startRot + amount)
        #self.emoji.setRotation(int(self.startRot + amount))
        #amnt = self.emoji.getRotation() / self.endRot
        amnt = self.timer.perctThrough() * (self.endRot - self.startRot)
        #print(amnt)
        #diff = new - self.emoji.rot
        self.emoji.setRotation(amnt)
        #self.emoji.image = pygame.transform.rotate(self.startImage, amnt)

        #self.emoji.setRotation(newRot)
    
    def end(self, scene):
        super().end(scene)
        self.emoji.origImage = self.emoji.image
        self.emoji.setRotation(self.endRot)
        #self.emoji.setRotation(self.endRot)
        #self.emoji.image = pygame.transform.rotate(self.emoji.origImage, self.endRot)

# change the image of an emoji
# TODO: does not work properly. emoji needs to track modifications to image
class ActionChange(Action):
    def __init__(self, emoji, name: str):
        super().__init__(1000)
        self.emoji = emoji
        self.name = name
    
    def start(self, scene):
        super().start(scene)
    
    def update(self, scene):
        super().update(scene)
    
    def end(self, scene):
        super().end(scene)
        self.emoji.changeImage(self.name)
        #print("change")
        for x in self.emoji.manip:
            self.emoji.applyAction(x)

class ActionMakeVisible(Action):
    def __init__(self, emoji, visible=True):
        super().__init__(1)
        self.emoji = emoji, self.visible = visible
    
    def start(self, scene):
        super().start(scene)
    
    def update(self, scene):
        super().update(scene)
    
    def end(self, scene):
        super().end(scene)
        self.emoji.visible = self.visible