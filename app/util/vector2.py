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
    
    def __add__(self, other):
        return self.add(other)
    
    def __sub__(self, other):
        return self.sub(other)
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __mul__(self, other):
        self.__rmul__(other)
    
    def __rmul__(self, other):
        return Vector2(self.x * other, self.y * other)
    
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