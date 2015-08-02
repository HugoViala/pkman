
# TODO(hugo): isn't it easier to handle tuple ?
class v2:
    """ class to handle 2D vector """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def add(a,b):
    c = v2(a.x + b.x, a.y + b.y)
    return c

def times(r, v):
    c = v2(r * v.x, r * v.y)
    return c
