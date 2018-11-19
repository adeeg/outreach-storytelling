from internal.scene_action import SceneAction
from internal.action import ActionWait, ActionMove, ActionText, ActionScale, ActionFlip, ActionRotate
from internal.drawable.emoji import Emoji
from util.vector2 import Vector2
from util.config import COL_WHITE, COL_BLACK, COL_RED, COL_ORANGE, COL_YELLOW, COL_BLUE, COL_GREEN
from loop import Game

g = Game()

# ----------------------------------------------------------------------
""" WRITE YOUR CODE HERE
             |
             |
             V          """

def setup(game: Game):
    print("Hello World!")

# ----------------------------------------------------------------------

setup(g)
g.start()
while not g.isFinished():
    g.loop()