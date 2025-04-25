from settings2 import *
from data_types2 import *

class Models:
    def __init__(self, engine):
        self.engine = engine
        self.raw_segments = engine.level_data.raw_segments
        self.wall_models: list[ray.Model] = []
        self.wall_id = 0
        self.build_wall_models()

        # Load the sword model
        self.sword_model = ray.load_model("sword.obj")
        self.sword_position = ray.Vector3(0, 0, 0)
        self.sword_rotation = ray.Vector3(0, 0, 0)

    def build_wall_models(self):
        for seg in self.raw_segments:
            if seg.back_sector_id is None:
                # solid wall
                wall = WallModel(self, seg, wall_type='solid')
                self.add_wall_model(wall, seg)
            else:
                if seg.mid_tex_id is not None:
                    # p wall mid
                    wall = WallModel(self, seg, wall_type='p_mid')
                    self.add_wall_model(wall, seg)

    def add_wall_model(self, wall_model, segment):
        self.wall_models.append(wall_model)
        segment.wall_model_id.add(self.wall_id)
        self.wall_id += 1

    def update_sword(self, camera):
        # Position the sword relative to the camera
        self.sword_position = ray.Vector3(
            camera.pos_3d.x + 0.5,
            camera.pos_3d.y - 0.5,
            camera.pos_3d.z
        )
        self.sword_rotation = ray.Vector3(
            camera.yaw,
            0,
            0
        )

    def draw_sword(self):
        ray.draw_model_ex(self.sword_model, self.sword_position, ray.Vector3(0, 1, 0), self.sword_rotation.y, ray.Vector3(1, 1, 1), ray.WHITE)

    def draw_wall_models(self):
        for wall_model in self.wall_models:
            ray.draw_model(wall_model.model, (0, 0, 0), 1.0, ray.WHITE)

class WallModel:
    def __init__(self, engine, segment, wall_type='solid'):
        self.engine = engine
        self.segment = segment
        self.wall_type = wall_type
        self.model: ray.Model = self.get_model()

    def get_model(self):
        mesh = self.get_quad_mesh()
        model = ray.load_model_from_mesh(mesh)
        return model

    def get_quad_mesh(self) -> ray.Mesh:
        triangle_count = 2
        vertex_count = 4

        # get seg coords
        (x0, z0), (x1, z1) = self.segment.pos

        # get normals
        delta = vec3(x1, 0, z1) - vec3(x0, 0, z0)
        normal = glm.normalize(vec3(-delta.z, delta.y, delta.x))
        normals = glm.array([normal] * vertex_count)

        # get vertices
        bottom, top = self.get_wall_height_data()
        v0, v1, v2, v3 = (x0, bottom, z0), (x1, bottom, z1), (x1, top, z1), (x0, top, z0)
        vertices = glm.array([vec3(v) for v in [v0, v1, v2, v3]])

        # get indices
        indices = [0, 1, 2, 0, 2, 3]
        indices = glm.array.from_numbers(glm.uint16, *indices)

        # get mesh
        mesh = ray.Mesh()
        mesh.triangleCount = triangle_count
        mesh.vertexCount = vertex_count
        mesh.vertices = ray.ffi.from_buffer("float []", vertices)
        mesh.indices = ray.ffi.from_buffer("unsigned short []", indices)
        mesh.normals = ray.ffi.from_buffer("float []", normals)

        ray.upload_mesh(mesh, False)
        return mesh
    
    def get_wall_height_data(self):
        bottom, top = 0, 4  # Default values, adjust as needed
        return bottom, top
