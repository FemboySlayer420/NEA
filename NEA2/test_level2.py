from settings2 import *

# points
P_00 = (0.0, 0.0)
P_01 = (7.0, 0.0)
P_02 = (12.0, 0.0)
P_03 = (12.0, 6.0)
#
P_04 = (7.0, 6.0)
P_05 = (0.0, 6.0)


SECTOR_DATA = {
    0: dict(floor_h=0.0, ceil_h=3.0),
    1: dict(floor_h=0.5, ceil_h=3.0),
}

SEGMENTS_OF_SECTOR_BOUNDARIES = [

    #[(segment points), (front sector, back sector), (low texture, mid texture, high texture)]
    [(P_00, P_01), (0, 1), (1, 1, 1)],
    [(P_04, P_05), (0, 1), (1, 1, 1)],
    [(P_05, P_00), (0, 1), (1, 1, 1)],

    [(P_01, P_04), (0, 1), (1, 1, 1)],

    [(P_01, P_02), (1, 0), (1, 1, 1)],
    [(P_02, P_03), (1, 0), (1, 1, 1)],
    [(P_03, P_04), (1, 0), (1, 1, 1)],
]

SETTINGS = {
    'seed': 14870,
    'cam_pos': (12, CAM_HEIGHT, 12),
    'cam_target': (5, CAM_HEIGHT, 5)
}
