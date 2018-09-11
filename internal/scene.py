import pygame, os
from util.observer import Observer, Subject, Event
from util.pygame_helper import loadImg

class Scene(Observer, Subject):
    """ finished      :: Bool
        background    :: Sprite
        actions       :: [Action]
        actionIndex   :: Num
    """
    
    def __init__(self):
        super().__init__()
        self.finished = False
        self.background = None
        self.actions = []
        self.actionIndex = 0

    def start(self, screen):
        screen.blit(self.background, (0, 0))
        pygame.display.flip()
        pygame.display.update()
    
    def update(self):
        pass
    
    def draw(self, screen):
        pass
    
    def blit(self, screen):
        pass
    
    def end(self, screen):
        pass
    
    def getCurAction(self):
        return self.actions[self.actionIndex]
    
    def nextAction(self):
        self.actionIndex += 1
    
    def addAction(self, act):
        self.actions.append(act)
    
    def addActionConc(self, act):
        act.conc = True
        self.actions.append(act)
    
    def onNotify(self, entity, event):
        if event == Event.ACTION_FINISHED:
            self.nextAction()
    
    def isFinished(self):
        return self.finished
    
    def setBackgroundColour(self, colour):
        background = pygame.Surface((800, 600))
        self.background = background.convert()
        self.background.fill(colour)
    
    def setBackgroundImage(self, imgName):
        img, rect = loadImg(os.path.join('background', imgName))
        self.background = img.convert()