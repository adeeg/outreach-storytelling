import os, pygame

IMG_MISSING = 'missing'

# thanks https://www.pygame.org/docs/tut/tom_games3.html#makegames-3-1
def loadImg(name):
    fullname = os.path.join('assets', name + ".png")
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image: ' + fullname + ", using test image instead")
        image = pygame.image.load(os.path.join('assets', IMG_MISSING + '.png'))
    return image, image.get_rect()