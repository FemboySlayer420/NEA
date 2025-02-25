from settings2 import *
from data_types2 import *
from test_level2 import *
from map_layout import *

class LevelData:
    def __init__(self, engine):
        self.engine = engine

        self.settings = SETTINGS

        self.sectors = SECTOR_DATA
        self.sector_boundaries = SEGMENTS_OF_SECTOR_BOUNDARIES

        self.sector = {}
        self.handle_sectors()

        self.sector_segments = {sector_id: [] for sector_id in self.sector_data}

        self.raw_segments = [Segment(p0, p1) for (p0, p1) in MAP_LAYOUT]
        self.raw_segments.extend(self.create_boundary_segments())  # Add boundary segments
        self.handle_sector_boundaries()

    def handle_sectors(self):
        for sector_id, sector_data in self.sectors.items():
            sector = Sector(
                floor_h=sector_data['floor_h'],
                ceil_h=sector_data['ceil_h'],
                floor_tex=sector_data.get('floor_tex_id', 0),
                ceil_tex=sector_data.get('ceil_tex_id', 0)
            )
            self.sectors[sector_id] = sector

    def handle_sector_boundaries(self):
        for (p0, p1), sector_ids, textures in self.sector_boundaries:
            seg = self.get_segment(p0, p1, sector_ids, textures)
            self.raw_segments.append(seg)

            for sector_id in sector_ids:
                if sector_id is not None:
                    self.sector_segments[sector_id].append([p0, p1])

    def get_segment(self, p0, p1, sector_ids, tex_ids):
        seg = Segment(
            p0=p0,
            p1=p1,
            sector_id=sector_ids[0],
            back_sector_id=sector_ids[1],
            low_tex=tex_ids[0],
            mid_tex=tex_ids[1],
            high_tex=tex_ids[2]
        )
        return seg

    def create_boundary_segments(self):
        segments = []
        grid_size = 32  # Assuming a 32x32 grid
        map_width = grid_size * 1.0  # Adjust as needed
        map_height = grid_size * 1.0  # Adjust as needed

        # Define the boundary segments
        segments.append(Segment(vec2(0, 0), vec2(map_width, 0)))  # Top boundary
        segments.append(Segment(vec2(map_width, 0), vec2(map_width, map_height)))  # Right boundary
        segments.append(Segment(vec2(map_width, map_height), vec2(0, map_height)))  # Bottom boundary
        segments.append(Segment(vec2(0, map_height), vec2(0, 0)))  # Left boundary

        return segments