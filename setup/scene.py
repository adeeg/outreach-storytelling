import pygame
from util.observer import Observer

class Scene(Observer):
    """     emojis :: sprite.Group
        background :: Sprite
            length :: Int """

    def __init__(self, MAX_EMOJIS=25):
        self.MAX_EMOJIS = MAX_EMOJIS
        self.emojis = pygame.sprite.Group()
        self.background = None
    
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
        flag = True
        for e in self.emojis:
            if not e.isFinished:
                flag = False
                break
        return flag
    
    def onNotify(self, entity, event):
        if event == 0:
            print("event!")