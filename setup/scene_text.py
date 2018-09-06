from setup.scene import Scene
import pygame

class SceneText(Scene):
    """ text   :: String
        textPy :: ? """

    def __init__(self, text):
        Scene.__init__(self)
        self.text = text
        self.font = pygame.font.Font(None, 50)
        self.textPy = self.font.render(self.text,
            1, (255, 255, 255))
    
    def draw(self, screen):
        self.textPy = self.font.render(self.text,
            1, (255, 255, 255))
        screen.blit(self.textPy, self.textPy.get_rect())
    
    def blit(self, screen):
        screen.blit(self.background, self.textPy.get_rect(), self.textPy.get_rect())