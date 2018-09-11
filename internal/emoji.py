import pygame, os
from util.pygame_helper import loadImg
from util.timer import Timer
from util.vector2 import Vector2
from util.math import lerp
from util.observer import Subject, Event

# sprite which you can add movements to
# which happen when sprite is started
class Emoji(pygame.sprite.Sprite, Subject):
    IMG_PREFIX = "emoji"

    """ moves       :: []
        moveIndex   :: Int
        startPos    :: Vector2
        timer       :: Timer
    """

    def __init__(self, image="", x=0, y=0, MAX_MOVES=25):
        self.MAX_MOVES = 25
        
        self.moves = []
        self.moveIndex = 0
        self.timer = None

        pygame.sprite.Sprite.__init__(self)
        Subject.__init__(self)
        super().__init__()

        self.image, self.rect = loadImg(os.path.join(self.IMG_PREFIX, str(image)))
        self.rect.x = x
        self.rect.y = y
    
    def start(self):
        self.startNextMove()
        
    # called once per frame
    def update(self):
        move = self.getCurrentMove()
        if len(self.moves) == 0:
            self.setFinished()

        if not self.isFinished():
            # move % dist through dep. on time through timer
            if not self.timer.isFinished():
                timeThrough = self.timer.timeThrough()
                newPos = lerp(self.startPos, self.getCurMovePos(), timeThrough / self.getCurrentMove()[2])
                self.rect.x = newPos.x
                self.rect.y = newPos.y

                if self.timer.isFinished():
                    self.rect.x = self.getCurrentMove()[0]
                    self.rect.y = self.getCurrentMove()[1]
                    # move onto the next move
                    #self.incMoveIndex()
                    #self.startNextMove()

    def getCurrentMove(self):
        return self.moves[self.moveIndex] if len(self.moves) != 0 else None

    def getCurMovePos(self):
        move = self.getCurrentMove()
        return Vector2(move[0], move[1])
    
    def getCurMoveTime(self):
        move = self.getCurrentMove()
        return move[2]
    
    def startNextMove(self):
        if len(self.moves) != 0:
            if self.isFinished():
                finalPos = self.getCurMovePos()
                self.rect.x = finalPos.x
                self.rect.y = finalPos.y
            else:
                self.startPos = Vector2(self.rect.x, self.rect.y)
                self.timer = Timer(self.getCurMoveTime())
                self.timer.start()

    def addMove(self, x, y, time):
        if len(self.moves) < self.MAX_MOVES:
            self.moves.append((x, y, time))
        else:
            print('Number of moves in a emoji exceeded ' + self.MAX_MOVES)

    # honestly no idea why it's -2 and not -1
    def incMoveIndex(self):
        if self.moveIndex > len(self.moves) - 2:
            self.setFinished()
        else:
            self.moveIndex += 1

    def isFinished(self):
        return self.moveIndex == -1
    
    def setFinished(self):
        self.moveIndex = -1
        self.notify(self, Event.EMOJI_FINISHED)
    
    # stay in place for a while
    def wait(self, ms):
        self.addMove(self.rect.x, self.rect.y, ms)