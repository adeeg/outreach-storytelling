# thanks to:
# https://www.pygame.org/docs/tut/ChimpLineByLine.html
# https://www.pygame.org/docs/tut/MakeGames.html

import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

from internal.emoji import Emoji
from internal.emoji_test import EmojiTest
from internal.scene import Scene
from internal.scene_action import SceneAction
from internal.scene_text import SceneText
from internal.scene_test import SceneTest
from internal.action import ActionMove, ActionText, ActionWait
from util.observer import Observer, Event
from util.vector2 import Vector2

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Python Storytelling')

# emoji
emoji = Emoji()
test = pygame.sprite.RenderPlain(emoji)

# scene
scene1 = SceneAction()
e1 = Emoji('laughing', 300, 300)
e1.addMove(100, 0, 1000)
e1.addMove(300, 300, 2000)
e2 = Emoji('angry', 0, 0)
e2.addMove(0, 100, 1000)
e2.addMove(300, 300, 2000)
scene1.addEmoji(e1)
scene1.addEmoji(e2)

# scene 2
scene2 = SceneAction()
e3 = Emoji()
e3.addMove(500, 300, 1000)
e3.addMove(0, 0, 1000)
scene2.addEmoji(e3)

# text scene
sceneT = SceneText("dog dog", 3000)

# scene 3
scene3 = SceneAction()
e4 = Emoji('laughing', 300, 300)
e4.addMove(0, 0, 1000)
e4.addMove(600, 600, 2000)
scene3.addEmoji(e4)

# bg
""" background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 0, 0)) """

# clock
clock = pygame.time.Clock()

#scene1.setBackgroundColour((255, 0, 0))
scene1.setBackgroundImage('example')
sceneT.setBackgroundColour((0, 255, 0))
scene2.setBackgroundColour((0, 0, 255))
scene3.setBackgroundColour((0, 0, 0))

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
#g.addScene(scene1)
#g.addScene(sceneT)
#g.addScene(scene2)
#g.addScene(scene3)

sceneT = SceneTest()
sceneT.setBackgroundColour((255, 255, 255))

#eT1 = Emoji('laughing')
eT1 = EmojiTest('laughing')
sceneT.addEmoji(eT1)

sceneT.addAction(ActionWait(1000))
sceneT.addAction(ActionMove(1000, eT1, Vector2(200, 200)))
sceneT.addAction(ActionWait(250))
sceneT.addAction(ActionMove(1500, eT1, Vector2(200, 450)))

g.addScene(sceneT)

g.start()
while not g.isFinished():
    g.loop()