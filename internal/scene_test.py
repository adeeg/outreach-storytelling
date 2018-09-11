import pygame
from internal.scene import Scene
from util.observer import Event

class SceneTest(Scene):
    def __init__(self):
        super().__init__()
        self.emojis = []
    
    def update(self):
        act = self.getCurAction()
        if act != None:
            act.update()
    
    def getCurAction(self):
        return self.actions[self.actionIndex]
    
    def nextAction(self):
        self.actionIndex += 1
    
    def addAction(self, act):
        act.addObserver(self)
        self.actions.append(act)
    
    def addActionConc(self, act):
        act.conc = True
        self.actions.append(act)
    
    def onNotify(self, entity, event):
        if event == Event.ACTION_FINISHED:
            self.nextAction()
    
    def addEmoji(self, *e):
        self.emojis.append(e)