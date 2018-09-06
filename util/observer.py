# thanks http://gameprogrammingpatterns.com/observer.html

from enum import Enum

class Event(Enum):
    EMOJI_FINISHED = 0
    SCENE_FINISHED = 1
    TIMER_FINISHED = 2

class Observer:
    def __init__(self):
        super().__init__()
    
    # entity = who sent notification
    # event = data
    def onNotify(self, entity, event):
        pass

class Subject:
    """ observers :: [] """

    def __init__(self):
        self.observers = []
        super().__init__()
    
    # entity = who sent notification
    # event = data
    def notify(self, entity, event):
        for o in self.observers:
            o.onNotify(entity, event)
    
    def addObserver(self, o):
        self.observers.append(o)
    
    def removeObserver(self, o):
        self.observers.remove(o)