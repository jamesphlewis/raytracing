from vec3 import Color, Point3
from vec3_utils import AddVectors, SubtractVectors, MultiplyVectors, MultiplyVectorByConstant, UnitVector
from sphere import RandomInHemisphere
from hittable import HitFromList

class Ray():
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def at(self, t):
        return AddVectors(self.origin, MultiplyVectorByConstant(self.direction, t))

INFINITY = 10000000000

def RayColor(ray, hittables, depth=50):
    hit, rec = HitFromList(ray, 0.000001, INFINITY, hittables)
    if depth <= 0:
        return Color(0, 0, 0)
    if hit:
        if getattr(rec, 'material', None) is not None:
            attenuate, attenuation, scattered = rec.material.scatter(ray, rec)
            if attenuate:
                return MultiplyVectors(attenuation, RayColor(scattered, hittables, depth-1))
            return color(0, 0, 0)

    unit_direction = UnitVector(ray.direction)
    t = 0.5 * (unit_direction.y() + 1.0)
    it = (1.0 - t)
    return AddVectors(
        MultiplyVectorByConstant(Color(1.0, 1.0, 1.0), it),
        MultiplyVectorByConstant(Color(0.5, 0.7, 1.0), t))
