from util.observer import Subject, Event
from util.timer import Timer
from util.math import lerp

class Action(Subject):
    """ duration :: Num
        timer    :: Timer
        conc     :: Bool
    """
    def __init__(self, duration):
        super().__init__()
        self.duration = duration
        self.timer = Timer(self.duration)
    
    def start(self):
        self.timer.start()
    
    def update(self):
        if self.timer.isFinished(): self.end()
    
    def end(self):
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

    def start(self):
        super().start()
        self.startPos = self.emoji.getPos()
    
    def update(self):
        super().update()

        newPos = lerp(self.startPos, self.coord, self.timer.timeThrough() / self.duration)
        self.emoji.setPos(newPos)
    
    def end(self):
        self.emoji.setPos(self.coord)
        super().end()

class ActionText(Action):
    """ text :: String """
    def __init__(self, text):
        super().__init__()
        self.text = text
    
    def start(self):
        self.textSurface = self.font.render(self.text,
            1, (255, 255, 255))
        super().start()
    
    def update(self):
        super().update()
    
    def end(self):
        super().end()