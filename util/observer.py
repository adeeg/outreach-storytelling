# thanks http://gameprogrammingpatterns.com/observer.html

from enum import Enum

class Event(Enum):
    FINISHED_MOVING = 1

class Observer:
    def __init__(self):
        pass
    
    # entity = who sent notification
    # event = data
    def onNotify(self, entity, event):
        pass

class Subject:
    """ observers :: [] """

    def __init__(self):
        self.observers = []
    
    # entity = who sent notification
    # event = data
    def notify(self, entity, event):
        for o in self.observers:
            o.onNotify(entity, event)
    
    def addObserver(self, o):
        self.observers.append(o)
    
    def removeObserver(self, o):
        self.observers.remove(o)