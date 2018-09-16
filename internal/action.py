from util.observer import Subject, Event
from util.timer import Timer
from util.math import lerp
from internal.text import Text
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