import pygame
from internal.scene import Scene
from util.observer import Event

# scene which displays moving emojis
class SceneAction(Scene):
    """ emojis :: Group
    """

    def __init__(self):
        super().__init__()
        self.emojis = pygame.sprite.Group()

    def start(self):
        for e in self.emojis:
            e.start()
    
    def update(self):
        self.emojis.update()

    def draw(self, screen):
        self.emojis.draw(screen)
    
    def blit(self, screen):
        for e in self.emojis:
            screen.blit(self.background, e.rect, e.rect)

    def addEmoji(self, e):
        e.addObserver(self)
        self.emojis.add(e)
        
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