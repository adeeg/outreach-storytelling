# thanks to:
# https://www.pygame.org/docs/tut/ChimpLineByLine.html
# https://www.pygame.org/docs/tut/MakeGames.html

import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

from internal.scene_action import SceneAction
from internal.action import ActionWait, ActionMove, ActionText, ActionScale
from internal.drawable.emoji import Emoji
from util.observer import Observer, Event
from util.timer import Timer
from util.vector2 import Vector2
from util.config import getConfig

pygame.init()
screen = pygame.display.set_mode(tuple(getConfig('window_size')))
pygame.display.set_caption('Python Storytelling')

class Game(Observer):
    """ begun      :: Bool
        scenes     :: [Scene]
        sceneIndex :: Int
    """
    def __init__(self):
        self.begun = False
        self.scenes = []
        self.sceneIndex = 0

    def start(self):
        if not self.begun:
            self.getCurrentScene().start(screen)
            self.begun = True

    def loop(self):
        if self.begun:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            scene = self.getCurrentScene()
            if scene != None:
                scene.blit(screen)
                scene.update()
                scene.draw(screen)
                pygame.display.flip()
    
    def getCurrentScene(self):
        return None if self.sceneIndex == -1 else self.scenes[self.sceneIndex]

    def addScene(self, scene):
        scene.addObserver(self)
        self.scenes.append(scene)

    def nextScene(self):
        if self.sceneIndex < len(self.scenes) - 1:
            self.getCurrentScene().end(screen)
            self.sceneIndex += 1
            self.getCurrentScene().start(screen)
        else:
            self.sceneIndex = -1
    
    def isFinished(self):
        return self.sceneIndex == -1
    
    def onNotify(self, entity, event):
        scene = self.getCurrentScene()
        if scene != None and scene == entity:
            if  event == Event.SCENE_FINISHED:
                print("scene finished!")
                self.nextScene()

g = Game()

newScene = SceneAction()
newScene.setBackgroundColour((255, 255, 255))

newEmoji = Emoji('laughing')
newScene.addEmoji(newEmoji)
newEmoji2 = Emoji('shocked')
newScene.addEmoji(newEmoji2)

newScene.addAction(ActionText(5000, 'This is some text!'))
newScene.addAction(ActionMove(1000, newEmoji, Vector2(100, 150)))
newScene.addAction(ActionScale(1000, newEmoji, 2))
newScene.addAction(ActionWait(1000))
newScene.addAction(ActionMove(1000, newEmoji, Vector2(200, 300)))
newScene.addAction(ActionWait(1000))
#newScene.addAction(ActionText(1000, 'dog'))
#newScene.addAction(ActionMove(1500, newEmoji, Vector2(200, 300)))

g.addScene(newScene)

g.start()
while not g.isFinished():
    g.loop()