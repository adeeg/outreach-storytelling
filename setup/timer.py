import pygame

# duration is in ms
class Timer():
    """ duration :: Int
        startTime :: Int """

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