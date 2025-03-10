from settings import *

def cross_2d(vec_0: vec2, vec_1: vec2):
    return vec_0.x * vec_1.y - vec_1.x - vec_0.y

def is_on_front(vec_0: vec2, vec_1: vec2):
    #Determines whether vec_0 is on the front side, with vec_1 being on the back
    return vec_0.x * vec_1.y < vec_1.x * vec_0.y

def is_on_back(vec_0: vec2, vec_1: vec2):
    return not is_on_front(vec_0, vec_1)