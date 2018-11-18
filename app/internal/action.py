

from util.timer import Timer
from util.observer import Subject, Event
#from app.util.timer import Timer
from util.math_helper import lerp
from util.vector2 import Vector2, fromTuple
from internal.drawable.text import Text
import pygame

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
        self.startSize = fromTuple(self.emoji.image.get_size())
        self.endSize = self.startSize.mult(self.scale)
        print(self.endSize)
    
    def update(self, scene):
        super().update(scene)
        newSize = lerp(self.startSize, self.endSize, self.timer.timeThrough() / self.duration)
        self.emoji.image = pygame.transform.scale(self.emoji.image, newSize.operation(int).toTuple())
        self.emoji.rect.size = newSize.operation(int).toTuple()
    
    def end(self, scene):
        super().end(scene)

# flips an emoji
class ActionFlip(Action):
    def __init__(self, duration, emoji, vert, horz):
        super().__init__(duration)
        self.emoji = emoji
        self.vert = vert
        self.horz = horz
    
    def start(self, scene):
        super().start(scene)
        #self.emoji.image = pygame.transform.flip(self.emoji.image, self.vert, self.horz)
        #self.emoji.image = pygame.transform.rotate(self.emoji.image, 45)

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
    
    def update(self, scene):
        super().update(scene)
        self.emoji.setRotation(self.emoji.getRotation() + 1)
        #amount = self.angle * self.timer.timeThrough() / self.duration
        #print(self.startRot + amount)
        #self.emoji.setRotation(int(self.startRot + amount))
    
    def end(self, scene):
        super().end(scene)
        self.emoji.setRotation(self.endRot)