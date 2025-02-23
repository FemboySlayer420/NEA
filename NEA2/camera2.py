from settings2 import *

class Camera:
    def __init__(self, engine):
        self.app = engine.app
        self.engine = engine
        self.fake_up = vec3(0.0, 1.0, 0.0)
        self.m_cam: ray.Camera3D = self.get_camera()
        self.target, self.pos_3d = self.m_cam.target, self.m_cam.position
        self.pos_2d = vec2(self.pos_3d.x, self.pos_3d.z)
        self.speed = CAM_SPEED
        self.cam_step = self.forward = self.right = vec3(0)
        self.yaw = atan2(self.target.z - self.pos_3d.z, self.target.x - self.pos_3d.x)
        self.delta_yaw = 0.0

    def get_yaw(self):
        self.delta_yaw = -ray.get_mouse_delta().x * CAM_ROT_SPEED * self.app.dt
        self.yaw -= self.delta_yaw

    def set_yaw(self):
        self.update_target(glm.rotateY(self.forward, -ray.get_mouse_delta().x * CAM_ROT_SPEED * self.app.dt))

    def update_target(self, new_target_pos: vec3):
        self.target.x, self.target.z = self.pos_3d.x + new_target_pos.x, self.pos_3d.z + new_target_pos.z

    def pre_update(self):
        self.update_vectors()

    def update(self):
        self.init_cam_step()
        self.check_cam_step()
        self.update_pos_2d()
        self.set_yaw()
        self.move()

    def update_vectors(self):
        self.forward = self.get_forward()
        self.right = cross(self.forward, self.fake_up)
        print(f"Forward: {self.forward}, Right: {self.right}")

    def get_forward(self) -> glm.vec3:
        return normalize(vec3(self.target.x - self.pos_3d.x, self.target.y - self.pos_3d.y, self.target.z - self.pos_3d.z))

    def init_cam_step(self):
        self.speed = CAM_SPEED * self.app.dt
        print(f"Speed: {self.speed}")

    def move_step(self, direction: vec3, label: str):
        print(f"Moving {label}")
        self.cam_step += self.speed * direction
        print(f"New cam_step ({label}): {self.cam_step}")

    def step_forward(self): self.move_step(self.forward, "forward")
    def step_back(self): self.move_step(-self.forward, "back")
    def step_left(self): self.move_step(-self.right, "left")
    def step_right(self): self.move_step(self.right, "right")

    def check_cam_step(self):
        if all(self.cam_step.xz):
            self.cam_step *= CAM_DIAG_MOVE_CORR

    def move(self):
        print(f"Cam Step before move: {self.cam_step}")
        self.move_x(self.cam_step.x)
        self.move_z(self.cam_step.z)
        self.cam_step *= 0  

    def move_x(self, dx): self.pos_3d.x += dx; self.target.x += dx
    def move_z(self, dz): self.pos_3d.z += dz; self.target.z += dz

    def update_pos_2d(self):
        self.pos_2d.x, self.pos_2d.y = self.pos_3d.x, self.pos_3d.z

    def get_camera(self):
        return ray.Camera3D(
            self.engine.level_data.settings['cam_pos'],
            self.engine.level_data.settings['cam_target'],
            self.fake_up.to_tuple(),
            FOV_Y_DEG,
            ray.CAMERA_PERSPECTIVE
        )