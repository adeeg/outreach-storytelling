import pygame
from internal.scene import Scene
from util.observer import Event

class SceneAction(Scene):
    def __init__(self):
        super().__init__()
        self.emojis = pygame.sprite.Group()
        self.drawables = []
    
    def start(self, screen):
        super().start(screen)
        act = self.getCurAction()
        if act != None:
            act.start(self)
        else:
            print("Scene has no actions! Have you remembered to put '[scene_var].addAction([action_var])'?")
            self.isFinished = True
            self.notify(self, Event.SCENE_FINISHED)
    
    def update(self):
        act = self.getCurAction()
        if act != None:
            act.update(self)

    def getTextCenter(self, text):
        textSize = self.font.size(text)
        return ((640 - textSize[0])/2, (480 - textSize[1])/2)
    
    def draw(self, screen):
        #super().draw(screen)
        for e in self.emojis:
            if e.visible:
                screen.blit(e.image, e.rect)
        #self.emojis.draw(screen)
        for d in self.drawables:
            d.draw(screen)
    
    def blit(self, screen):
        super().blit(screen)
        for e in self.emojis:
            if e.visible:
                screen.blit(self.background, e.rect, e.rect)
                pass
        for d in self.drawables:
            d.blit(screen, self.background)
    
    def getCurAction(self):
        return self.actions[self.actionIndex] if self.actionIndex > -1 and self.actionIndex < len(self.actions) else None
    
    def nextAction(self):
        if self.actionIndex + 1 < len(self.actions):
            self.actionIndex += 1
            self.getCurAction().start(self)
        else:
            self.actionIndex = -1
            self.isFinished = True
            self.notify(self, Event.SCENE_FINISHED)
    
    def addAction(self, act):
        act.scene = self
        act.addObserver(self)
        self.actions.append(act)
    
    def addActionConc(self, act):
        act.conc = True
        self.addAction(act)
    
    def onNotify(self, entity, event):
        if event == Event.ACTION_FINISHED:
            self.nextAction()
        if event == Event.EMOJI_FINISHED:
            print("emoj finish")
    
    def addEmoji(self, *emoji):
        for e in emoji:
            e.addObserver(self)
        self.emojis.add(emoji)
    
    def addDrawable(self, *draw):
        self.drawables.extend(draw)