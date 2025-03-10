from settings import *

# points
P_00 = (1.0, 1.0)
P_01 = (7.0, 1.0)
P_02 = (7.0, 8.0)
P_03 = (1.0, 8.0)
#
P_04 = (5.0, 2.0)
P_05 = (4.0, 4.0)
P_06 = (5.0, 6.0)
P_07 = (6.0, 4.0)

SETTINGS = {
    'seed': 14870,
    'cam_pos': (12, CAM_HEIGHT, 12),
    'cam_target': (5, CAM_HEIGHT, 5)
}

SEGMENTS = [
    (P_04, P_05), (P_05, P_06), (P_06, P_07), (P_07, P_04),
    (P_00, P_01), (P_01, P_02), (P_02, P_03), (P_03, P_00),
]
