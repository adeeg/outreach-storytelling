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

        self.addMove(0, 200, 100)
        print(self.getVelForMove(self.getCurrentMove()))
        self.vel = self.getVelForMove(self.getCurrentMove())
        self.addMove(50, 50, 100)
        self.addMove(300, 400, 100)

    def getCurrentMove(self):
        return self.moves[self.moveIndex]
    
    # get difference vector
    # divide by time to get there
    def getVelForMove(self, move):
        vel = ((move[0] - self.rect.x) / move[2], (move[1] - self.rect.y) / move[2])
        return vel

    # called once per frame
    def update(self, delta):
        if not self.finishedMoving():
            #print(self.rect)
            move = self.getCurrentMove()
            # area to test if emoji is in
            TEST_LEN = 2
            testRect = pygame.Rect(max(0, move[0] - TEST_LEN), move[1] - TEST_LEN, move[0] + TEST_LEN, move[1] + TEST_LEN)

            #print("-> " + str(testRect))

            if testRect.colliderect(self.rect):
                self.vel = (0, 0)
                self.rect.x = move[0]
                self.rect.y = move[1]
                self.incMoveIndex()
                if not self.finishedMoving():
                    print(str(self.moveIndex) + " / " + str(len(self.moves)))
                    self.vel = self.getVelForMove(self.getCurrentMove())

            self.addVel(self.vel * delta)

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