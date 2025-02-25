from settings2 import *
import glm

vec2 = glm.vec2

class Sector:
    def __init__(self, floor_h=None, ceil_h=None, floor_tex=None, ceil_tex=None):
        self.floor_h: float = floor_h #Height of the floor
        self.ceil_h: float = ceil_h #Height of the ceiling
        self.floor_tex: int = floor_tex #Texture of the floor
        self.ceil_tex: int = ceil_tex #Texture of the ceiling
        

class Segment:
    def __init__(self, p0, p1, sector_id=None, back_sector_id=None, low_tex=None, mid_tex=None, high_tex=None):
        self.pos = (vec2(p0), vec2(p1))
        self.vector = self.pos[1] - self.pos[0]

        self.sector_id: int = sector_id
        self.back_sector_id: int = back_sector_id


        self.low_tex: int = low_tex
        self.mid_tex: int = mid_tex
        self.high_tex: int = high_tex

        self.wall_model_id: set[int] = set()

class BSPNode:
    def __init__(self):
        self.front = self.back = None
        self.splitter_p0 = self.splitter_p1 = self.splitter_vec = None
        self.segments_id = None