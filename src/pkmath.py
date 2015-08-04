# NOTE(hugo): to improve Python3 compatibility
# and to have a floating division
from __future__ import division
import math

# TODO(hugo): isn't it easier to handle tuple ?
class v2:
    """ class to handle 2D vector """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def add(a, b):
    c = v2(a.x + b.x, a.y + b.y)
    return c

def times(r, v):
    c = v2(r * v.x, r * v.y)
    return c

def norm(v):
    return math.sqrt(v.x * v.x + v.y * v.y)

# TODO(hugo): isn't faster to do norm(v) == 0.0 ?
def isNull(v):
    return v.x == 0.0 and v.y == 0.0

# TODO(hugo): check if this actually works
def normalize(v):
    if not isNull(v):
        n = norm(v)
        return times(1 / n, v)
    else:
        return v
