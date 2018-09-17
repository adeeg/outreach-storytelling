def fromTuple(tupl):
    return Vector2(tupl[0], tupl[1])

class Vector2():
    """ x :: Num
        y :: Num
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Vector2[" + str(self.x) + ", " + str(self.y) + "]"
    
    def add(self, vec):
        return Vector2(self.x + vec.x, self.y + vec.y)
    
    def sub(self, vec):
        return Vector2(self.x - vec.x, self.y - vec.y)
    
    def mult(self, scal):
        return Vector2(self.x * scal, self.y * scal)
    
    def toTuple(self):
        return (self.x, self.y)

    def operation(self, op):
        return Vector2(op(self.x), op(self.y))