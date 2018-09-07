import pygame

# timer set for no. ms
class Timer():
    """ duration :: Int
        startTime :: Int
    """

    # duration is in ms
    def __init__(self, duration):
        self.duration = duration
        self.startTime = -1

    def start(self):
        self.startTime = pygame.time.get_ticks()
    
    def getEndTime(self):
        return self.startTime + self.duration

    def isFinished(self):
        return (self.startTime != -1
            and pygame.time.get_ticks() > self.getEndTime())
    
    def timeThrough(self):
        return pygame.time.get_ticks() - self.startTime
    
    def timeLeft(self):
        return self.startTime - pygame.time.get_ticks()