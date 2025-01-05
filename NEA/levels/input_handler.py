from settings import *
from enum import IntEnum, auto
from pyray import is_key_down, is_key_pressed, KeyboardKey
from camera import *

class Key(IntEnum):
    #Defining keys for movement control
    FORWARD = KeyboardKey.KEY_W
    BACK = KeyboardKey.KEY_S
    STR_LEFT = KeyboardKey.KEY_A
    STR_RIGHT = KeyboardKey.KEY_D

class InputHandler:
    def __init__(self, engine):
        self.engine = engine
        self.camera = engine.camera

    def update(self):
        # Debugging key press detection
        if is_key_down(Key.FORWARD):
            print("Forward key is down")
            self.camera.step_forward()
        elif is_key_down(Key.BACK):
            print("Back key is down")
            self.camera.step_back()
        if is_key_down(Key.STR_RIGHT):
            print("Strafe right key is down")
            self.camera.step_right()
        elif is_key_down(Key.STR_LEFT):
            print("Strafe left key is down")
            self.camera.step_left()