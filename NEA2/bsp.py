from settings2 import *
from data_types2 import Segment, BSPNode
from utils2 import cross_2d
from copy import copy
import random

class BSPTreeBuilder:
    def __init__(self, engine):
        self.engine = engine
        self.raw_segments = engine.level_data.raw_segments
        self.root_node = BSPNode()
        self.segments = []  
        self.seg_id = 0

        seed = self.engine.level_data.settings['seed']
        random.seed(seed)
        random.shuffle(self.raw_segments)

        self.num_front = self.num_back = self.num_splits = 0
        self.build_tree(self.root_node, self.raw_segments)

        print(f'num front: {self.num_front}, num back: {self.num_back}, num splits: {self.num_splits}')

    def find_best(self, start_seed=0, end_seed=20_000, weight_factor=3):
        best_seed, best_score = -1, float('inf')

        for seed in range(start_seed, end_seed):
            random.seed(seed)
            random.shuffle(self.raw_segments)

            self.root_node = BSPNode()
            self.segments = []
            self.seg_id = 0
            self.num_front = self.num_back = self.num_splits = 0

            self.build_tree(self.root_node, self.raw_segments)
            score = abs(self.num_back - self.num_front) + weight_factor * self.num_splits

            if score < best_score:
                best_seed, best_score = seed, score

        print(f'best_seed = {best_seed}, score = {best_score}')
        return best_seed

    def split_space(self, node: BSPNode, input_segments: list[Segment]):
        splitter_seg = input_segments[0]
        node.splitter_p0, node.splitter_p1 = splitter_seg.pos
        node.splitter_vec = splitter_seg.vector

        front_segs, back_segs = [], []

        for segment in input_segments[1:]:
            start, end, vector = segment.pos[0], segment.pos[1], segment.vector

            numerator = cross_2d(start - node.splitter_p0, node.splitter_vec)
            denominator = cross_2d(node.splitter_vec, vector)

            denom_is_0, num_is_0 = abs(denominator) < EPS, abs(numerator) < EPS

            if denom_is_0 and num_is_0:
                front_segs.append(segment)
                continue

            if not denom_is_0:
                intersection = numerator / denominator

                if 0.0 < intersection < 1.0:
                    self.num_splits += 1
                    intersection_point = start + intersection * vector

                    r_segment, l_segment = copy(segment), copy(segment)
                    r_segment.pos, l_segment.pos = (start, intersection_point), (intersection_point, end)
                    r_segment.vector, l_segment.vector = r_segment.pos[1] - r_segment.pos[0], l_segment.pos[1] - l_segment.pos[0]

                    if numerator > 0:
                        l_segment, r_segment = r_segment, l_segment

                    front_segs.append(r_segment)
                    back_segs.append(l_segment)
                    continue

            if numerator < 0 or (num_is_0 and denominator > 0):
                front_segs.append(segment)
            elif numerator > 0 or (num_is_0 and denominator < 0):
                back_segs.append(segment)

        self.add_segment(splitter_seg, node)
        return front_segs, back_segs

    def add_segment(self, splitter_seg: Segment, node: BSPNode):
        self.segments.append(splitter_seg)
        node.segment_id = self.seg_id
        self.seg_id += 1

    def build_tree(self, node: BSPNode, input_segments: list[Segment]):
        if not input_segments:
            return

        front_segs, back_segs = self.split_space(node, input_segments)

        if back_segs:
            self.num_back += 1
            node.back = BSPNode()
            self.build_tree(node.back, back_segs)

        if front_segs:
            self.num_front += 1
            node.front = BSPNode()
            self.build_tree(node.front, front_segs)
