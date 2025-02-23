from settings2 import *

def cross_2d(v0: vec2, v1: vec2):
    return v0.x * v1.y - v1.x * v0.y

def is_on_front(v0: vec2, v1: vec2):
    return cross_2d(v0, v1) < 0

def is_on_back(v0: vec2, v1: vec2):
    return not is_on_front(v0, v1)