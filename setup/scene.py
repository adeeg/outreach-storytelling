import pygame
from util.observer import Observer, Subject, Event

class Scene(Observer, Subject):
    """ emojis     :: sprite.Group
        background :: Sprite
        length     :: Int
        finished   :: Bool """

    def __init__(self, MAX_EMOJIS=25):
        #Subject.__init__(self)
        #super(Scene, self).__init__()
        super().__init__()
        self.MAX_EMOJIS = MAX_EMOJIS
        self.emojis = pygame.sprite.Group()
        self.background = None
        self.finished = False

    def start(self):
        pass
    
    def loop(self):
        return None

    def setBackground(self, bg):
        self.background = bg
    
    def addEmoji(self, e):
        e.addObserver(self)
        self.emojis.add(e)
        """ if len(self.emojis) < self.MAX_EMOJIS:
            self.emojis.append(e)
        else:
            print('Number of emojis in a scene exceeded ' + self.MAX_EMOJIS) """
    
    def draw(self, screen):
        self.emojis.draw(screen)
    
    def update(self):
        self.emojis.update()
    
    def blit(self, screen):
        for e in self.emojis:
            screen.blit(self.background, e.rect, e.rect)
    
    def isFinished(self):
        return self.finished
    
    def onNotify(self, entity, event):
        # when one emoji is finished
        if event == Event.EMOJI_FINISHED:
            self.checkIfFinished()
    
    # checks all emojis to see if finished
    # sets finished to true if so
    # and notifies game
    def checkIfFinished(self):
        for e in self.emojis:
            if not e.isFinished():
                self.finished = False
                break
            self.finished = True
            self.notify(self, Event.SCENE_FINISHED)
        