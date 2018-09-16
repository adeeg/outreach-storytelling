import pygame, os
from internal.drawable import Drawable

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
        return ((640 - textSize[0])/2, (480 - textSize[1])/2)