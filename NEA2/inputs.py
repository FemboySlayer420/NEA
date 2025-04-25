from settings2 import *
from enum import IntEnum, auto
from pyray import is_key_down, is_key_pressed, is_mouse_button_pressed, KeyboardKey, MOUSE_BUTTON_LEFT


class Key(IntEnum):
    #
    FORWARD = KeyboardKey.KEY_W
    BACK = KeyboardKey.KEY_S
    STRAFE_LEFT = KeyboardKey.KEY_A
    STRAFE_RIGHT = KeyboardKey.KEY_D
    MAP = KeyboardKey.KEY_M


class InputHandler:
    def __init__(self, engine):
        self.engine = engine
        self.camera = engine.camera

    def update(self):
        #player control
        if is_key_down(Key.FORWARD):
            self.camera.step_forward()
        elif is_key_down(Key.BACK):
            self.camera.step_back()
        if is_key_down(Key.STRAFE_RIGHT):
            self.camera.step_right()
        elif is_key_down(Key.STRAFE_LEFT):
            self.camera.step_left()

        if is_key_pressed(Key.MAP):
            self.engine.map_renderer.is_draw_map = not self.engine.map_renderer.is_draw_map
            self.engine.sight_renderer.update_screen_tint()

        if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            self.attack()

    def attack(self):
        # Implement attack logic here
        print("Attack with sword!")
        # Check for collisions with enemies and apply damage