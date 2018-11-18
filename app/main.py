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
             V
"""

def setup(game: Game):
    print("Hello World!")

    scene1 = SceneAction()
    scene1.setBackgroundColor(COL_BLUE)
    laugh = Emoji('laughing', Vector2(100, 100))
    scene1.addAction(ActionRotate(1000, laugh, 360))
    scene1.addAction(ActionFlip(1000, laugh, True, True))
    scene1.addEmoji(laugh)
    scene1.addAction(ActionScale(1000, laugh, 2))
    scene1.addAction(ActionMove(1000, laugh, Vector2(200, 200)))
    scene1.addAction(ActionScale(1000, laugh, 0.5))
    for i in range(0, 10):
        am = 2 if i % 2 == 0 else 0.5
        scene1.addAction(ActionScale(100, laugh, am))

    game.addScene(scene1)

# ----------------------------------------------------------------------

setup(g)
g.start()
while not g.isFinished():
    g.loop()