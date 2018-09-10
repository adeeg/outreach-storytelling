import pygame
from internal.scene import Scene
from util.timer import Timer
from util.observer import Event

# scene which displays text for no. seconds
class SceneText(Scene):
    """ text   :: String
        textSurface :: ?
    """

    def __init__(self, text, ms=1000):
        super().__init__()
        self.text = text
        self.font = pygame.font.Font(None, 100)

        self.textSurface = self.font.render(self.text,
            1, (255, 255, 255))
        self.timer = Timer(ms)

    def start(self, screen):
        super().start(screen)
        self.timer.start()
    
    def update(self):
        self.checkIfFinished()
    
    def draw(self, screen):
        self.textSurface = self.font.render(self.text,
            1, (255, 255, 255))
    
    def blit(self, screen):
        screen.blit(self.textSurface, self.getTextCenter(self.text))
    
    def end(self, screen):
        pass
    
    def checkIfFinished(self):
        flag = self.timer.isFinished()
        if flag: self.notify(self, Event.SCENE_FINISHED)
        return self.timer.isFinished()
    
    def getTextCenter(self, text):
        textSize = self.font.size(text)
        return ((640 - textSize[0])/2, (480 - textSize[1])/2)