from settings import *

class Camera:  # Allows control over camera movement
    def __init__(self, engine):
        self.app = engine.app
        self.engine = engine
        self.fake_up = vec3(0.0, 1.0, 0.0)
        self.m_cam: ray.Camera3D = self.get_camera()
        self.target: ray.Vector3 = self.m_cam.target
        self.pos_3d: ray.Vector3 = self.m_cam.position
        self.pos_2d: glm.vec2 = vec2(self.pos_3d.x, self.pos_3d.z)
        self.speed = CAM_SPEED
        self.cam_step = vec3(0)
        self.forward = vec3(0)
        self.right = vec3(0)
        self.yaw = atan2(self.target.z - self.pos_3d.z, self.target.x - self.pos_3d.x)
        self.delta_yaw = 0.0

    def get_yaw(self):  # Yaw refers to the movements of the camera in a rotary sense
        self.delta_yaw = -ray.get_mouse_delta().x * CAM_ROT_SPEED * self.app.dt
        self.yaw -= self.delta_yaw

    def set_yaw(self):
        delta_yaw = -ray.get_mouse_delta().x * CAM_ROT_SPEED * self.app.dt
        new_target_pos = glm.rotateY(self.forward, delta_yaw)
        self.update_target(new_target_pos)

    def update_target(self, new_target_pos: vec3):
        self.target.x = self.pos_3d.x + new_target_pos.x
        self.target.z = self.pos_3d.z + new_target_pos.z

    def pre_update(self):
        self.update_vectors()

    def update(self):
        self.init_cam_step()  # Move init_cam_step to the start of update
        self.check_cam_step()
        self.update_pos_2d()
        self.set_yaw()
        self.move()

    def update_vectors(self):  # Forward vector is the normalized difference between the camera position and target position
        self.forward = self.get_forward()
        self.right = cross(self.forward, self.fake_up)
        print(f"Forward: {self.forward}, Right: {self.right}")

    def get_forward(self) -> glm.vec3:
        return normalize(vec3(
            self.target.x - self.pos_3d.x,
            self.target.y - self.pos_3d.y,
            self.target.z - self.pos_3d.z,
        ))

    def init_cam_step(self):
        self.speed = CAM_SPEED * self.app.dt
        print(f"Speed: {self.speed}")

    def step_forward(self):
        print("Moving forward")
        self.cam_step += self.speed * self.forward
        print(f"New cam_step (forward): {self.cam_step}")

    def step_back(self):
        print("Moving back")
        self.cam_step += -self.speed * self.forward
        print(f"New cam_step (back): {self.cam_step}")

    def step_left(self):
        print("Moving left")
        self.cam_step += -self.speed * self.right
        print(f"New cam_step (left): {self.cam_step}")

    def step_right(self):
        print("Moving right")
        self.cam_step += self.speed * self.right
        print(f"New cam_step (right): {self.cam_step}")

    def check_cam_step(self):
        dx, dz = self.cam_step.xz
        if dx and dz:
            self.cam_step *= CAM_DIAG_MOVE_CORR

    def move(self):
        dx, dz = self.cam_step.xz
        print(f"Cam Step before move: {self.cam_step}")
        self.move_x(dx)
        self.move_z(dz)
        self.cam_step *= 0  # Reset cam_step after applying movement

    def move_x(self, dx):
        self.pos_3d.x += dx
        self.target.x += dx

    def move_z(self, dz):
        self.pos_3d.z += dz
        self.target.z += dz

    def update_pos_2d(self):
        # 2D position on xz plane
        self.pos_2d[0] = self.pos_3d.x
        self.pos_2d[1] = self.pos_3d.z

    def get_camera(self):  # This tells where the camera is facing, and the position it's in as stated in the test_level file
        cam = ray.Camera3D(
            self.engine.level_data.settings['cam_pos'],
            self.engine.level_data.settings['cam_target'],
            self.fake_up.to_tuple(),
            FOV_Y_DEG,
            ray.CAMERA_PERSPECTIVE
        )
        return cam
