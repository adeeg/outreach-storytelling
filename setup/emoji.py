import pygame

class Emoji(pygame.sprite.Sprite):
    """ moves       :: []
        moveIndex   :: Int
        vel         :: (velX, velY) """

    def __init__(self, MAX_MOVES=25):
        self.MAX_MOVES = 25
        self.moves = []
        self.moveIndex = 0
        self.vel = (0, 0)
        

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("test.png")
        self.rect = self.image.get_rect()
        #screen = pygame.display.get_surface()

        self.addMove(0, 2, 1)
        print(self.getVelForMove(self.getCurrentMove()))
        self.addMove(3, 1, 1)

    def getCurrentMove(self):
        return self.moves[self.moveIndex]
    
    # get difference vector
    # divide by time to get there
    def getVelForMove(self, move):
        vel = ((move[0] - self.rect.x) / move[2], (move[1] - self.rect.y) / move[2])
        return vel

    def update(self):
        # called once per frame
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

    def addMove(self, x, y, time):
        if len(self.moves) < self.MAX_MOVES:
            self.moves.append((x, y, time))
        else:
            print('Number of moves in a emoji exceeded ' + self.MAX_MOVES)
    
    def wait(self, ms):
        return None