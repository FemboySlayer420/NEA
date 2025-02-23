from settings2 import *
from data_types2 import BSPNode
from utils2 import *

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
        if not node:
            return
        
        on_front = is_on_front(self.cam_pos - node.splitter_p0, node.splitter_vec)
        
        #Traverse the front first if the camera is on the front side
        if on_front:
            self.traverse(node.front)
            self.seg_ids_to_draw.append(node.segment_id)  #Only add visible walls
            self.traverse(node.back)
        else:
            self.traverse(node.back)
            self.traverse(node.front)