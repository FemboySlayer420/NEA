from levels.settings import *
from levels.data_types import Segment, BSPNode
from levels.utils import cross_2d
from copy import copy

class BSPTreeBuilder:
    def __init__(self, engine):
        self.engine = engine
        self.raw_segments = engine.level_data.raw_segments
        #
        self.root_node = BSPNode()
        #
        self.build_tree(self.root_node, self.raw_segments)

    def split_space(self, node: BSPNode, input_segments: list[Segment]):
        splitter_seg = input_segments[0]
        splitter_pos = splitter_seg.pos
        splitter_vec = splitter_seg.vector

        node.splitter_vec = splitter_vec
        node.splitter_p0 = splitter_pos[0]
        node.splitter_p1 = splitter_pos[1]

        front_segs, back_segs = [], []

        for segment in input_segments[1:]:
            #
            segment_start = segment.pos[0]
            segment_end = segment.pos[1]
            segment_vector = segment.vector

            numerator = cross_2d((segment_start - splitter_pos[0]), splitter_vec)
            denominator = cross_2d(splitter_vec, segment_vector)

            denom_is_0 = abs(denominator) < EPS
            num_is_0 = abs(numerator) < EPS

            if denom_is_0 and num_is_0:
                front_segs.append(segment)
                continue

            if not denom_is_0:
                intersection = numerator/denominator
                if 0.0 < intersection < 1.0:
                    intersection_point = segment_start + intersection * segment_vector

                r_segment = copy(segment)
                r_segment.pos = segment_start, intersection_point
                r_segment.vector = r_segment.pos[1] - r_segment.pos[0]

                if numerator > 0:
                    l_segment, r_segment = r_segment, l_segment
                
                front_segs.append(r_segment)
                back_segs.append(l_segment)
                continue

    def build_tree(self, node: BSPNode, input_segments: list[Segment]):
        if not input_segments:
            return None
        #
        front_segs, back_segs = self.split_space(node, input_segments)

        if back_segs:
            node.back = BSPNode()
            self.build_tree(node.back, back_segs)

        if front_segs:
            node.front = BSPNode()
            self.build_tree(node.front, front_segs)