# thanks to:
# https://www.pygame.org/docs/tut/ChimpLineByLine.html
# https://www.pygame.org/docs/tut/MakeGames.html
import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

from setup.emoji import Emoji
from setup.scene import Scene
from setup.scene_text import SceneText

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Python Storytelling')

# emoji
emoji = Emoji()
test = pygame.sprite.RenderPlain(emoji)

# scene
scene1 = Scene()
e1 = Emoji()
e1.addMove(100, 0, 1000)
e1.addMove(300, 300, 2000)
e2 = Emoji()
e2.addMove(0, 100, 1000)
e2.addMove(300, 300, 2000)
scene1.addEmoji(e1)
scene1.addEmoji(e2)

# text scene
sceneT = SceneText("dog dog")

# bg
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

# clock
clock = pygame.time.Clock()

# time
font = pygame.font.Font(None, 50)
text = font.render("Hello World", 1, (255, 255, 255))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
print(textpos)

screen.blit(background, (0, 0))

scene1.setBackground(background)
sceneT.setBackground(background)

c = 0
while 1:
    c += 1
    
    delta = 1 / clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.blit(background, text.get_rect(), text.get_rect())
    sceneT.blit(screen)
    #screen.blit(background, emoji.rect, emoji.rect)
    scene1.blit(screen)
    

    #emoji.update(delta)
    scene1.update()

    """ text = font.render(str(pygame.time.get_ticks() / 1000) + ": "
        + str(emoji.rect.x) + ","  + str(emoji.rect.y) + " | "
        + str(emoji.vel[0] * delta) + "," + str(emoji.vel[1] * delta),
        1, (255, 255, 255))
    screen.blit(text, text.get_rect()) """

    sceneT.draw(screen)
    #screen.blit(background, emoji.rect, emoji.rect)
    #screen.blit(background, scene1.emojis)
    #scene1.blit(screen)
    
    #test.draw(screen)
    scene1.draw(screen)

    pygame.display.flip()

def play(scene):
    return None