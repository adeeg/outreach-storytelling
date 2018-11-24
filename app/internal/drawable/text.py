import pygame, os
from internal.drawable.drawable import Drawable
from util.config import getConfig

class Text(Drawable):
    TEXT_SPACE = 60

    def __init__(self, text):
        #self.font = pygame.font.Font(None, 100)
        self.font = pygame.font.SysFont('ubuntumono', 100)
        #print(pygame.font.get_fonts())

        self.text = text
        self.textList = self.wordWrap(text)
        self.textSurfaces = []
        for s in self.textList:
            #print(s)
            str = ' '.join(s)
            self.textSurfaces.append(self.font.render(str, 1, (255, 255, 255)))

    def draw(self, screen):
        #self.textSurface = self.font.render(self.text,
            #1, (255, 255, 255))
        pass

    def blit(self, screen, background):
        #screen.blit(self.textSurface, self.getTextCenter(self.text))
        for i, surf in enumerate(self.textSurfaces):
            screen.blit(surf, (self.getTextCenterX(' '.join(self.textList[i])), i * 60 + self.getTextCenterY(self.textList)))

    # remove one word; add to list
    # check if still too big
    # yes -> remove another word; add to list
    # no -> run again on list
    # bit of a mess but it works somehow
    def wordWrap(self, text):
        screen_width = getConfig('window_size')[0]
        if self.font.size(text)[0] > screen_width:
            words = text.split()
            result = []
            list = self.wrapTwoLines(words)
            result.append(list[0])
            while len(list[1]) > 0:
                list = self.wrapTwoLines(list[1])
                result.append(list[0])
            return result
        else:
            return [text]
    
    def wrapTwoLines(self, words):
        list = [[],[]]
        screen_width = getConfig('window_size')[0]
        while self.font.size(' '.join(words))[0] > screen_width:
            list[1].append(words[len(words) - 1])
            del words[len(words) - 1]
        list[0] = words
        list[1].reverse()
        return list
    
    def getTextCenterX(self, text):
        textSize = self.font.size(text)
        screen_size = getConfig('window_size')
        #return ((screen_size[0] - textSize[0])/2, (screen_size[1] - textSize[1])/2)
        return (screen_size[0] - textSize[0])/2
    
    def getTextCenterY(self, textList):
        screen_size = getConfig('window_size')
        return (screen_size[1] - len(textList)  * 60) / 2