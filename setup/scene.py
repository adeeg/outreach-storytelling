class Scene:
    """ emojis :: []
    background :: Sprite
    length :: Int """

    def __init__(self, MAX_EMOJIS=25):
        self.MAX_EMOJIS = MAX_EMOJIS
        self.emojis = []
    
    def loop(self):
        return None

    def setBackground(self):
        return None
        
    def addEmoji(self, e):
        if len(self.emojis) < self.MAX_EMOJIS:
            self.emojis.append(e)
        else:
            print('Number of emojis in a scene exceeded ' + self.MAX_EMOJIS)