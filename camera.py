from vec3 import Point3, Vec3
from ray import Ray
from vec3_utils import AddVectors, SubtractVectors, MultiplyVectorByConstant, DivideVectorByConstant

class Camera():
    ASPECT_RATIO = 16.0 / 9.0
    VIEWPORT_HEIGHT = 2.0
    VIEWPORT_WIDTH = ASPECT_RATIO * VIEWPORT_HEIGHT
    FOCAL_LENGTH = 1.0
    ORIGIN = Point3(0, 0, 0)
    HORIZONTAL = Vec3(VIEWPORT_WIDTH, 0, 0)
    VERTICAL = Vec3(0, VIEWPORT_HEIGHT, 0)
    LOWER_LEFT_CORNER = SubtractVectors(
        ORIGIN,
        DivideVectorByConstant(HORIZONTAL, 2)
    )
    LOWER_LEFT_CORNER = SubtractVectors(
        LOWER_LEFT_CORNER,
        DivideVectorByConstant(VERTICAL, 2)
    )
    LOWER_LEFT_CORNER = SubtractVectors(
        LOWER_LEFT_CORNER,
        Vec3(0, 0, FOCAL_LENGTH)
    )
    def get_ray(self, u, v):
        uv = MultiplyVectorByConstant(self.HORIZONTAL, u)
        vv = MultiplyVectorByConstant(self.VERTICAL, v)
        d = AddVectors(self.LOWER_LEFT_CORNER, uv)
        d = AddVectors(d, vv)
        d = SubtractVectors(d, self.ORIGIN)
        r = Ray(self.ORIGIN, d)
        return r