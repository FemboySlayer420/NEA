from settings import *

class Segment:
    def __init__(self, p0: tuple[float], p1: tuple[float]):
        #
        self.pos: tuple[vec2] = vec2(p0), vec2(p1)
        self.vector: vec2 = self.pos[1] - self.pos[0]

class BSPNode:
    def __init__(self):
        #
        self.front: BSPNode = None
        self.back: BSPNode = None
        #
        self.splitter_p0: vec2 = None
        self.splitter_p1: vec2 = None
        self.splitter_vec: vec2 = None
        #
        self.segments_id: int = None