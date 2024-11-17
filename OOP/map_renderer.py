from settings import *

class MapRenderer:
    def __init__(self, engine):
        self.engine = engine
        #
        raw_segments = [seg.pos for seg in self.engine.level_data.raw_segments]
        self.x_min, self.y_min, self.x_max, self.y_max = self.get_bounds(raw_segments)

    def draw(self):
        pass

    @staticmethod
    def get_bounds(segments: list[tuple[vec2]]):
        inf = float('inf')
        x_min, y_min, x_max, y_max = inf, inf, -inf, -inf
        #
        for p0,p1 in segments:
            x_min = p0.x if p0.x < x_min else p1.x if p1.x < x_min else x_min
            x_max = p0.x if p0.x < x_max else p1.x if p1.x > x_max else x_max
            #
            y_min = p0.y if p0.y < y_min else p1.y if p1.y < y_min else y_min
            y_max = p0.y if p0.y > y_max else p1.y if p1.y > y_max else y_max
        return x_min, y_min, x_max, y_max