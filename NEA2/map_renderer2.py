from settings2 import *


class MapRenderer:
    def __init__(self, engine):
        self.engine = engine
        self.camera = engine.camera
        #
        #Get raw segment positions from level data
        raw_segments = [seg.pos for seg in self.engine.level_data.raw_segments]
        #Calculate the bounds of the map based on the raw segments
        self.x_min, self.y_min, self.x_max, self.y_max = self.get_bounds(raw_segments)
        #
        #Remap raw segments to fit within the map view
        self.raw_segments = self.remap_array(raw_segments)
        #
        #Remap BSP segments to fit within the map view
        self.segments = self.remap_array(
            [seg.pos for seg in self.engine.bsp_builder.segments])
        self.counter = 0.0
        #
        #Flag to determine whether to draw the map
        self.is_draw_map = False

    def draw(self):
        #Only draw the map if the flag is True
        if self.is_draw_map:
            self.draw_raw_segments()
            self.draw_segments()
            self.draw_player()
            self.counter += 0.0005

    def draw_player(self, dist=100):
        #Draw the player position and direction on the map
        x0, y0 = p0 = self.remap_vec2(self.camera.pos_2d)
        x1, y1 = p0 + self.camera.forward.xz * dist
        #
        ray.draw_line_v((x0, y0), (x1, y1), ray.WHITE)
        ray.draw_circle_v((x0, y0), 10, ray.GREEN)

    def draw_segments(self, seg_color=ray.ORANGE):
        #Draw the segments that are visible based on BSP traversal
        segment_ids = self.engine.bsp_traverser.seg_ids_to_draw
        #
        for seg_id in segment_ids:
            (x0, y0), (x1, y1) = p0, p1 = self.segments[seg_id]
            #
            ray.draw_line_v((x0, y0), (x1, y1), seg_color)
            self.draw_normal(p0, p1, seg_color)
            #
            ray.draw_circle_v((x0, y0), 3, ray.WHITE)

    def draw_normal(self, p0, p1, color, scale=12):
        #Draw the normal vector for a segment
        p10 = p1 - p0
        normal = normalize(vec2(-p10.y, p10.x))
        n0 = (p0 + p1) * 0.5
        n1 = n0 + normal * scale
        #
        ray.draw_line_v((n0.x, n0.y), (n1.x, n1.y), color)

    def draw_raw_segments(self):
        #Draw the raw segments of the map
        for p0, p1 in self.raw_segments:
            (x0, y0), (x1, y1) = p0, p1
            ray.draw_line_v((x0, y0), (x1, y1), ray.DARKGRAY)

    def remap_array(self, arr: list[tuple[vec2]]):
        #Remap an array of segment positions to fit within the map view
        return [(self.remap_vec2(p0), self.remap_vec2(p1)) for p0, p1 in arr]

    def remap_vec2(self, p: vec2):
        #Remap a single vec2 position to fit within the map view
        x = self.remap_x(p.x)
        y = self.remap_y(p.y)
        return vec2(x, y)

    def remap_x(self, x, out_min=MAP_OFFSET, out_max=MAP_WIDTH):
        #Remap the x-coordinate to fit within the map view
        return (x - self.x_min) * (out_max - out_min) / (self.x_max - self.x_min) + out_min

    def remap_y(self, y, out_min=MAP_OFFSET, out_max=MAP_HEIGHT):
        #Remap the y-coordinate to fit within the map view
        return (y - self.y_min) * (out_max - out_min) / (self.y_max - self.y_min) + out_min

    @staticmethod
    def get_bounds(segments: list[tuple[vec2]]):
        #Calculate the bounds of the map based on the segment positions
        inf = float('inf')
        x_min, y_min, x_max, y_max = inf, inf, -inf, -inf
        #
        for p0, p1 in segments:
            x_min = p0.x if p0.x < x_min else p1.x if p1.x < x_min else x_min
            x_max = p0.x if p0.x > x_max else p1.x if p1.x > x_max else x_max
            #
            y_min = p0.y if p0.y < y_min else p1.y if p1.y < y_min else y_min
            y_max = p0.y if p0.y > y_max else p1.y if p1.y > y_max else y_max
        return x_min, y_min, x_max, y_max
