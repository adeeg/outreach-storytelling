from util.observer import Subject, Event
from threading import Timer

class Action(Subject):
    """ duration :: Num
        timer    :: Timer
        conc     :: Bool
    """
    def __init__(self, duration):
        super().__init__()
        self.duration = duration
        self.timer = Timer(self.duration, self.end)
    
    def start(self):
        self.timer.start()
    
    def update(self):
        pass
    
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
        super().__init__()
        self.emoji = emoji
        self.coord = coord
    
    def update(self):
        self.emoji.update()

class ActionText(Action):
    """ text :: String """
    def __init__(self, text):
        super().__init__()
        self.text = text