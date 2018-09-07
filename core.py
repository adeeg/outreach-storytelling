# thanks to:
# https://www.pygame.org/docs/tut/ChimpLineByLine.html
# https://www.pygame.org/docs/tut/MakeGames.html

# TODO:
# emoji starting pos
# different emoji
# waiting
# different backgrounds (img? colour?)
# timer in corner
# -----------------------
# music/sounds
# effects
# -----------------------
# limits (e.g. max emoji)
# error messages
# clean up core
# proper game loop
# velocity instead of linear interp.?
import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

from internal.emoji import Emoji
from internal.scene import Scene
from internal.scene_action import SceneAction
from internal.scene_text import SceneText
from util.observer import Observer, Event

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Python Storytelling')

# emoji
emoji = Emoji()
test = pygame.sprite.RenderPlain(emoji)

# scene
scene1 = SceneAction()
e1 = Emoji()
e1.addMove(100, 0, 1000)
e1.addMove(300, 300, 2000)
e2 = Emoji()
e2.addMove(0, 100, 1000)
e2.addMove(300, 300, 2000)
scene1.addEmoji(e1)
scene1.addEmoji(e2)

# scene 2
scene2 = SceneAction()
e3 = Emoji()
e3.addMove(1000, 300, 100)
e3.addMove(0, 0, 1000)
scene2.addEmoji(e3)

# text scene
sceneT = SceneText("dog dog")

# bg
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

# clock
clock = pygame.time.Clock()

screen.blit(background, (0, 0))

scene1.background = background
sceneT.background = background
scene2.background = background

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
            self.getCurrentScene().start()
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
            self.sceneIndex += 1
            self.getCurrentScene().start()
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
g.addScene(scene1)
g.addScene(sceneT)
g.addScene(scene2)

g.start()
while not g.isFinished():
    g.loop()