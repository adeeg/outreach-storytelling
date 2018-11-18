from internal.scene_action import SceneAction
from internal.action import ActionWait, ActionMove, ActionText, ActionScale
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
    newScene = SceneAction()
    newScene.setBackgroundColour(COL_RED)

    newEmoji = Emoji('laughing')
    newScene.addEmoji(newEmoji)
    newEmoji2 = Emoji('shocked')
    newScene.addEmoji(newEmoji2)

    newScene.addAction(ActionText(1000, 'This is some text!'))
    newScene.addAction(ActionMove(1000, newEmoji, Vector2(100, 150)))
    newScene.addAction(ActionScale(1000, newEmoji, 2))
    newScene.addAction(ActionWait(1000))
    newScene.addAction(ActionMove(1000, newEmoji, Vector2(200, 300)))
    newScene.addAction(ActionWait(1000))
    #newScene.addAction(ActionText(1000, 'dog'))
    #newScene.addAction(ActionMove(1500, newEmoji, Vector2(200, 300)))

    game.addScene(newScene)

# ----------------------------------------------------------------------

setup(g)
g.start()
while not g.isFinished():
    g.loop()