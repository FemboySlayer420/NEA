#game settings
import pyray as ray
import glm
from glm import vec2, vec3, ivec2, normalize, cross, dot, atan2, sin, cos, length

#resolution
RES = WIN_WIDTH, WIN_HEIGHT = (1600, 900)

MAP_OFFSET = 50
MAP_WIDTH, MAP_HEIGHT = WIN_WIDTH - MAP_OFFSET, WIN_HEIGHT - MAP_OFFSET

EPS = 1e-4

#Camera
CAM_HEIGHT = 0.6
CAM_SPEED = 6.2
CAM_ROT_SPEED = 1
CAM_DIAG_MOVE_CORR = 1 / pow(2, 0.5)

#Vertical camera value
FOV_Y_DEG = 50

VEC3_ZERO = ray.Vector3(0, 0, 0)
VEC2_ZERO = ray.Vector2(0, 0, 0)