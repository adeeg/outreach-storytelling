from internal.scene_action import SceneAction
from internal.action import ActionWait, ActionMove, ActionText, ActionScale, ActionFlip, ActionRotate, ActionChange, ActionChangeBGCol
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
    """ scene1 = SceneAction()
    scene1.setBackgroundColor(COL_BLUE)
    scene1.addAction(ActionChangeBGCol(1000, COL_RED))
    emoji1 = Emoji('laughing')
    scene1.addEmoji(emoji1)
    scene1.addAction(ActionMove(1000, emoji1, Vector2(300, 200)))
    game.addScene(scene1) """

# ----------------------------------------------------------------------

setup(g)
g.start()
while not g.isFinished():
    g.loop()