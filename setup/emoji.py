import pygame
from setup.timer import Timer
from setup.vector2 import Vector2
from setup.util import lerp

class Emoji(pygame.sprite.Sprite):
    """ moves       :: []
        moveIndex   :: Int
        vel         :: (velX, velY)
        timer       :: Timer """

    def __init__(self, MAX_MOVES=25):
        self.MAX_MOVES = 25
        self.moves = []
        self.moveIndex = 0
        self.vel = (0, 0)      
        self.timer = None  

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("test.png")
        self.rect = self.image.get_rect()
        #screen = pygame.display.get_surface()

        self.addMove(0, 500, 1000)
        #self.addMove(100, 100, 100)
        #self.addMove(100, 200, 150)
        #self.addMove(-100, 200, 200)
        #self.addMove(50, 50, 100)
        #self.addMove(300, 400, 50)

        self.startNextMove()

    def getCurrentMove(self):
        return self.moves[self.moveIndex]
    
    # get difference vector
    # divide by time to get there
    def getVelForMove(self, move):
        vel = ((move[0] - self.rect.x) / move[2], (move[1] - self.rect.y) / move[2])
        return vel
    
    def startNextMove(self):
        if self.finishedMoving():
            self.vel = (0, 0)
        else:
            self.vel = self.getVelForMove(self.getCurrentMove())
            self.timer = Timer(self.getCurrentMove()[2])
            self.timer.start()
        
    # called once per frame
    def update(self, delta):
        lerp(Vector2(3, 4), Vector2(7, 15), 0)

        if not self.finishedMoving():
            if self.timer.isFinished():
                self.rect.x = self.getCurrentMove()[0]
                self.rect.y = self.getCurrentMove()[1]
                # move onto the next move
                self.incMoveIndex()
                self.startNextMove()
            
            self.addVel((self.vel[0] * delta, self.vel[1] * delta * 100))

        """ if not self.finishedMoving():
            #print(self.rect)
            move = self.getCurrentMove()
            # area to test if emoji is in
            TEST_LEN = 25
            testRect = pygame.Rect(move[0] - TEST_LEN, move[1] - TEST_LEN, move[0] + TEST_LEN, move[1] + TEST_LEN)

            if (self.rect.x < move[0] + TEST_LEN and self.rect.x > move[0] - TEST_LEN
                and self.rect.y < move[1] + TEST_LEN and self.rect.y > move[1] - TEST_LEN):
                self.vel = (0, 0)
                self.rect.x = move[0]
                self.rect.y = move[1]
                self.incMoveIndex()
                if not self.finishedMoving():
                    print(str(self.moveIndex) + " / " + str(len(self.moves)))
                    self.vel = self.getVelForMove(self.getCurrentMove()) """

            #print("-> " + str(testRect))

            # better way to do this, not using it because it wasn't work well
            #if testRect.colliderect(self.rect):
                

            

    def incMoveIndex(self):
        if self.moveIndex > len(self.moves) - 1:
            self.moveIndex = -1
        else:
            self.moveIndex += 1

    def finishedMoving(self):
        return self.moveIndex == -1

    def addVel(self, vel):
        self.rect.x += vel[0]
        self.rect.y += vel[1]

    def addMove(self, x, y, time):
        if len(self.moves) < self.MAX_MOVES:
            self.moves.append((x, y, time))
        else:
            print('Number of moves in a emoji exceeded ' + self.MAX_MOVES)
    
    def wait(self, ms):
        return None