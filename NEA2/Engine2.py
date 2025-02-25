from settings2 import *
from level_data2 import LevelData
from map_renderer2 import MapRenderer
from bsp import BSPTreeBuilder
from bsp_travel import BSPTraversal
from camera2 import Camera
from inputs import InputHandler
from sight_rendering import ViewRenderer
from models import Models 

class Engine:
    def __init__(self, app):
        self.app = app
        self.level_data = LevelData(self)
        self.bsp_builder = BSPTreeBuilder(self)
        self.camera = Camera(self)
        self.input_handler = InputHandler(self)
        self.bsp_traverser = BSPTraversal(self)
        self.map_renderer = MapRenderer(self)
        self.sight_renderer = ViewRenderer(self)
        self.models = Models(self)  # Initialize Models

    def update(self):
        self.input_handler.update()  # Process input first
        self.camera.pre_update()  # Prepare the camera for updates (like resetting cam_step)
        self.camera.update()  # Update the camera position and direction
        self.bsp_traverser.update()  # Update BSP traversal after camera and input updates
        self.sight_renderer.update()

    def draw_2d(self):
        self.map_renderer.draw()  # Draw the map if the flag is set
        ray.draw_fps(10, 10)

    def draw_3d(self):
        ray.begin_mode_3d(self.camera.m_cam)
        ray.draw_grid(32, 1.0)
        self.draw_wall_models()  # Draw wall models
        ray.end_mode_3d()

    def draw_wall_models(self):
        for model in self.models.wall_models:
            ray.draw_model(model, (0, 0, 0), 1.0, ray.WHITE)

    def draw(self):
        ray.begin_drawing()
        ray.clear_background(ray.BLACK)
        self.draw_3d()
        self.draw_2d()
        ray.end_drawing()