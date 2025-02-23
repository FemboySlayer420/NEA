from settings2 import *

class Segment:
    def __init__(self, p0: tuple[float], p1: tuple[float]):
        self.pos = (vec2(p0), vec2(p1))
        self.vector = self.pos[1] - self.pos[0]

class BSPNode:
    def __init__(self):
        self.front = self.back = None
        self.splitter_p0 = self.splitter_p1 = self.splitter_vec = None
        self.segments_id = None