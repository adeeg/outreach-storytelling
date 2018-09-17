import pygame, os
from internal.drawable.drawable import Drawable
from util.config import getConfig

class Text(Drawable):
    def __init__(self, text):
        self.text = text
        self.font = pygame.font.Font(None, 100)

        self.textSurface = self.font.render(self.text,
            1, (255, 255, 255))

    def draw(self, screen):
        self.textSurface = self.font.render(self.text,
            1, (255, 255, 255))

    def blit(self, screen, background):
        screen.blit(self.textSurface, self.getTextCenter(self.text))
    
    def getTextCenter(self, text):
        textSize = self.font.size(text)
        screen_size = getConfig('window_size')
        return ((screen_size[0] - textSize[0])/2, (screen_size[1] - textSize[1])/2)