from settings2 import *
from enum import IntEnum
from pyray import is_key_down, KeyboardKey
from camera2 import *

class Key(IntEnum):
    FORWARD = KeyboardKey.KEY_W
    BACK = KeyboardKey.KEY_S
    STR_LEFT = KeyboardKey.KEY_A
    STR_RIGHT = KeyboardKey.KEY_D

class InputHandler:
    def __init__(self, engine):
        self.camera = engine.camera

    def update(self):
        key_actions = {
            Key.FORWARD: self.camera.step_forward,
            Key.BACK: self.camera.step_back,
            Key.STR_RIGHT: self.camera.step_right,
            Key.STR_LEFT: self.camera.step_left,
        }
        for key, action in key_actions.items():
            if is_key_down(key):
                print(f"{key.name} key is down")
                action()