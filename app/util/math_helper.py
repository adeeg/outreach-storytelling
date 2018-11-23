from util.vector2 import Vector2

# linear interpolation
# perct of way through start->end
def lerp(start, end, perct: float):
    diff = end - start
    thru = perct * diff
    return thru + start