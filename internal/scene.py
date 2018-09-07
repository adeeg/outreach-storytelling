import pygame
from util.observer import Observer, Subject, Event

class Scene(Observer, Subject):
    """ background :: Sprite
        finished   :: Bool
    """
    
    def __init__(self):
        super().__init__()
        self.background = None
        self.finished = False

    def start(self):
        pass
    
    def update(self):
        pass
    
    def draw(self, screen):
        pass
    
    def blit(self, screen):
        pass
    
    def isFinished(self):
        return self.finished