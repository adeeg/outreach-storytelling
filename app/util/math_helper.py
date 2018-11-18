# linear interpolation
# perct of way through start->end
def lerp(start, end, perct):
    diff = end.sub(start)
    thru = diff.mult(perct)
    return thru.add(start)