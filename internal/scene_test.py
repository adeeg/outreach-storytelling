import pygame
from internal.scene import Scene
from util.observer import Event

class SceneTest(Scene):
    def __init__(self):
        super().__init__()
        self.emojis = pygame.sprite.Group()
    
    def start(self, screen):
        super().start(screen)
        act = self.getCurAction()
        if act != None:
            act.start()
    
    def update(self):
        act = self.getCurAction()
        if act != None:
            act.update()
    
    def draw(self, screen):
        self.emojis.draw(screen)
    
    def blit(self, screen):
        for e in self.emojis:
            screen.blit(self.background, e.rect, e.rect)
    
    def getCurAction(self):
        return self.actions[self.actionIndex] if self.actionIndex > -1 and self.actionIndex < len(self.actions) else None
    
    def nextAction(self):
        if self.actionIndex + 1 < len(self.actions):
            self.actionIndex += 1
            self.getCurAction().start()
        else:
            self.actionIndex = -1
            self.isFinished = True
            self.notify(self, Event.SCENE_FINISHED)
    
    def addAction(self, act):
        act.addObserver(self)
        self.actions.append(act)
    
    def addActionConc(self, act):
        act.conc = True
        self.actions.append(act)
    
    def onNotify(self, entity, event):
        if event == Event.ACTION_FINISHED:
            self.nextAction()
        if event == Event.EMOJI_FINISHED:
            print("emoj finish")
    
    def addEmoji(self, *e):
        for emoj in e:
            emoj.addObserver(self)
        self.emojis.add(e)