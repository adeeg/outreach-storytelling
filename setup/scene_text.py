import pygame
from setup.scene import Scene
from setup.timer import Timer
from util.observer import Event

class SceneText(Scene):
    """ text   :: String
        textPy :: ? """

    def __init__(self, text):
        #super(SceneText, self).__init__(Scene)
        super().__init__()
        self.text = text
        self.font = pygame.font.Font(None, 50)
        self.textPy = self.font.render(self.text,
            1, (255, 255, 255))
        self.timer = Timer(1000)

    def start(self):
        self.timer.start()
    
    def update(self):
        self.checkIfFinished()
    
    def draw(self, screen):
        self.textPy = self.font.render(self.text,
            1, (255, 255, 255))
        screen.blit(self.textPy, self.textPy.get_rect())
    
    def blit(self, screen):
        screen.blit(self.background, self.textPy.get_rect(), self.textPy.get_rect())
    
    def checkIfFinished(self):
        flag = self.timer.isFinished()
        if flag: self.notify(self, Event.SCENE_FINISHED)
        return self.timer.isFinished()