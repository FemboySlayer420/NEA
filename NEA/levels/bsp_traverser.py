from settings import *
from data_types import BSPNode
from utils import *

class BSPTraversal:
    def __init__(self, engine):
        self.engine = engine
        self.root_node = engine.bsp_builder.root_node
        self.segments = engine.bsp_builder.segments

        self.cam_pos = vec2(6, 7)
        self.seg_ids_to_draw = []

    def update(self):
        self.seg_ids_to_draw.clear()
        self.traverse(self.root_node)

    def traverse(self, node: BSPNode):
        if node is None:
            return None
        
        on_front = is_on_front(self.cam_pos - node.splitter_p0, node.splitter_vec)
         #To determine which side of the splitter the camera is on by building a vector and utilise cross product
        if on_front:
            self.traverse(node.front)
            self.seg_ids_to_draw.append(node.segment_id)
            self.traverse(node.back)
        else:
            self.traverse(node.back)
            #By not appending to this list, it does not highlight the walls that are not being faced by the player
            self.traverse(node.front)