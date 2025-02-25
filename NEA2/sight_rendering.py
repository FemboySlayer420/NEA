from settings2 import *
from models import Models


class ViewRenderer:
    def __init__(self, engine):
        self.engine = engine
        #
        self.segments = engine.bsp_builder.segments
        self.camera = engine.camera
        self.segment_ids_to_draw = self.engine.bsp_traverser.seg_ids_to_draw
        #
        self.models = Models(engine)
        self.wall_models = self.models.wall_models
        #
        self.wall_ids_to_draw = set()
        #
        self.screen_tint = ray.WHITE

    def update(self):
        self.wall_ids_to_draw.clear()

        for seg_id in self.segment_ids_to_draw:
            #Wall indexing is found through searching the bsp tree
            seg = self.segments[seg_id]
            self.wall_ids_to_draw |= seg.wall_model_id

    def draw(self):
        #Draw walls using their indexes as obtained in the previous function
        for wall_id in self.wall_ids_to_draw:
            ray.draw_model(self.wall_models[wall_id], VEC3_ZERO, 1.0, self.screen_tint)

    def update_screen_tint(self):
        self.screen_tint = (
            ray.GRAY if self.engine.map_renderer.is_draw_map else ray.WHITE
        )
