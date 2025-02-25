from data_types2 import vec2
from settings2 import *

MAP_LAYOUT = [
    # Define the boundary segments
    (vec2(0, 0), vec2(32, 0)),  # Top boundary
    (vec2(32, 0), vec2(32, 32)),  # Right boundary
    (vec2(32, 32), vec2(0, 32)),  # Bottom boundary
    (vec2(0, 32), vec2(0, 0)),  # Left boundary

    # Define additional segments for the map layout
    (vec2(4.87, 3.62), vec2(4.87, 7.62)),
    (vec2(4.87, 7.62), vec2(7.87, 7.62)),
    (vec2(7.87, 7.62), vec2(7.87, 3.62)),
    (vec2(7.87, 3.62), vec2(4.87, 3.62)),
    
    # Box in the bottom-right corner
    (vec2(24.13, 3.62), vec2(24.13, 7.62)),
    (vec2(24.13, 7.62), vec2(27.13, 7.62)),
    (vec2(27.13, 7.62), vec2(27.13, 3.62)),
    (vec2(27.13, 3.62), vec2(24.13, 3.62)),

    # Box in the top-left corner
    (vec2(4.87, 24.38), vec2(4.87, 28.38)),
    (vec2(4.87, 28.38), vec2(7.87, 28.38)),
    (vec2(7.87, 28.38), vec2(7.87, 24.38)),
    (vec2(7.87, 24.38), vec2(4.87, 24.38)),

    # Box in the top-right corner
    (vec2(24.13, 24.38), vec2(24.13, 28.38)),
    (vec2(24.13, 28.38), vec2(27.13, 28.38)),
    (vec2(27.13, 28.38), vec2(27.13, 24.38)),
    (vec2(27.13, 24.38), vec2(24.13, 24.38)),
]

SETTINGS = {
    'seed': 14870,
    'cam_pos': (12, CAM_HEIGHT, 12),
    'cam_target': (5, CAM_HEIGHT, 5)
}
