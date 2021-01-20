from vec3 import Color, Point3
from vec3_utils import AddVectors, SubtractVectors, MultiplyVectorByConstant, UnitVector
from sphere import RandomInUnitSphere
from hittable import HitFromList

class Ray():
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def at(self, t):
        return AddVectors(self.origin, MultiplyVectorByConstant(self.direction, t))

INFINITY = 10000000000

def RayColor(ray, hittables):
    hit, rec = HitFromList(ray, 0, INFINITY, hittables)
    if hit:
        target = AddVectors(rec.point, rec.normal)
        target = AddVectors(target, RandomInUnitSphere())
        r = Ray(rec.point, SubtractVectors(target, rec.point))
        return MultiplyVectorByConstant(RayColor(r, hittables), 0.5)

    unit_direction = UnitVector(ray.direction)
    t = 0.5 * (unit_direction.y() + 1.0)
    it = (1.0 - t)
    return AddVectors(
        MultiplyVectorByConstant(Color(1.0, 1.0, 1.0), it),
        MultiplyVectorByConstant(Color(0.5, 0.7, 1.0), t))