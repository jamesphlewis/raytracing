import math
from vec3 import Point3, Vec3
from ray import Ray
from vec3_utils import AddVectors, SubtractVectors, MultiplyVectorByConstant, DivideVectorByConstant, UnitVector, Cross, RandomInUnitDisk

class Camera():
    FOCAL_LENGTH = 1.0

    def __init__(self, lookfrom, lookat, vup, fov, aspect_ratio, aperture, focus_dist):
        self.ASPECT_RATIO = aspect_ratio
        self.THETA = math.radians(fov)
        self.H = math.tan(self.THETA / 2)
        self.VIEWPORT_HEIGHT = 2.0 * self.H
        self.VIEWPORT_WIDTH = self.ASPECT_RATIO * self.VIEWPORT_HEIGHT
        self.W = UnitVector(SubtractVectors(lookfrom, lookat))
        self.U = UnitVector(Cross(vup, self.W))
        self.V = Cross(self.W, self.U)
        self.ORIGIN = lookfrom
        self.HORIZONTAL = MultiplyVectorByConstant(
            MultiplyVectorByConstant(
                self.U,
                self.VIEWPORT_WIDTH),
            focus_dist
        )
        self.VERTICAL = MultiplyVectorByConstant(
            MultiplyVectorByConstant(
                self.V,
                self.VIEWPORT_WIDTH),
            focus_dist
        )
        self.LOWER_LEFT_CORNER = SubtractVectors(
            self.ORIGIN,
            DivideVectorByConstant(self.HORIZONTAL, 2)
        )
        self.LOWER_LEFT_CORNER = SubtractVectors(
            self.LOWER_LEFT_CORNER,
            DivideVectorByConstant(self.VERTICAL, 2)
        )
        self.LOWER_LEFT_CORNER = SubtractVectors(
            self.LOWER_LEFT_CORNER,
            MultiplyVectorByConstant(
                self.W,
                focus_dist
            )
        )
        self.LENS_RADIUS = aperture / 2

    def get_ray(self, s, t):
        rd = MultiplyVectorByConstant(RandomInUnitDisk(), self.LENS_RADIUS)
        offset = AddVectors(
            MultiplyVectorByConstant(self.U, rd.x()),
            MultiplyVectorByConstant(self.V, rd.y())
        )
        sv = MultiplyVectorByConstant(self.HORIZONTAL, s)
        tv = MultiplyVectorByConstant(self.VERTICAL, t)
        d = AddVectors(self.LOWER_LEFT_CORNER, sv)
        d = AddVectors(d, tv)
        d = SubtractVectors(d, self.ORIGIN)
        d = SubtractVectors(d, offset)
        return Ray(
            AddVectors(self.ORIGIN, offset),
            d
        )