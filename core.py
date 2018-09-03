# thanks to:
# https://www.pygame.org/docs/tut/ChimpLineByLine.html
# https://www.pygame.org/docs/tut/MakeGames.html
import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

from setup.emoji import Emoji

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Python Storytelling')

emoji = Emoji()
test = pygame.sprite.RenderPlain(emoji)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

screen.blit(background, (0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    

    emoji.update()

    screen.blit(background, emoji.rect, emoji.rect)
    test.draw(screen)
    pygame.display.flip()