import pygame

class Scene:
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