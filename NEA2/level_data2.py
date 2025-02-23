from settings2 import *
from data_types2 import *
from test_level2 import *

class LevelData:
    def __init__(self, engine):
        self.engine = engine
        #
        self.raw_segments = [Segment(p0, p1) for (p0, p1) in SEGMENTS]
        self.settings = SETTINGS