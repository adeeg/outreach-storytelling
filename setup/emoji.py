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
        self.begun = False
        self.vel = (0, 0)      
        self.timer = None  

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/test.png")
        self.rect = self.image.get_rect()
        #screen = pygame.display.get_surface()

        """ self.addMove(0, 500, 1000)
        self.addMove(100, 100, 1000)
        self.addMove(100, 200, 1500)
        self.addMove(-100, 200, 2000)
        self.addMove(50, 50, 1000)
        self.addMove(300, 400, 500) """

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
            self.startPos = Vector2(self.rect.x, self.rect.y)
            self.vel = self.getVelForMove(self.getCurrentMove())
            self.timer = Timer(self.getCurrentMove()[2])
            self.timer.start()

    def getNextMovePos(self):
        move = self.getCurrentMove()
        return Vector2(move[0], move[1])
        
    # called once per frame
    def update(self):
        if not self.begun:
            self.startNextMove()
            self.begun = True
        
        if not self.finishedMoving():
            # move % dist through dep. on time through timer
            timeThrough = self.timer.timeThrough()
            newPos = lerp(self.startPos, self.getNextMovePos(), timeThrough / self.getCurrentMove()[2])
            print(newPos)
            self.rect.x = newPos.x
            self.rect.y = newPos.y

            if self.timer.isFinished():
                self.rect.x = self.getCurrentMove()[0]
                self.rect.y = self.getCurrentMove()[1]
                # move onto the next move
                self.incMoveIndex()
                self.startNextMove()
            
            #self.addVel((self.vel[0] * delta, self.vel[1] * delta * 100))

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
                

            
    # honestly no idea why it's -2 and not -1
    def incMoveIndex(self):
        if self.moveIndex > len(self.moves) - 2:
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